---
name: low-ram-self-protect
category: automation
description: >-
  Self-protection policy for running the Paperclip + Hermes + OpenClaw autonomy
  loop on a memory-constrained Windows host. When free physical RAM drops below
  a threshold, defer heavy work and run only a lightweight self-improve pass.
state: active
---

# Low-RAM Self-Protection (autonomy loop)

## When to use
Every autonomy tick, before doing real work, check free RAM. The Paperclip
server, OpenClaw gateway, and Hermes agent run concurrently on a ~6 GB Windows
host and free physical memory routinely oscillates between ~100 MB and ~644 MB.

## Trigger threshold
- Free RAM **< 300 MB** → lightweight pass only.
- Free RAM **>= 300 MB** → resume normal operations (no manual intervention).

## How to measure (Windows / git-bash)
```bash
wmic OS Get FreePhysicalMemory /Value
```
The value is in **KB**. `236580` = ~231 MB. Parse and compare in KB to avoid
float rounding. Copy-paste check used by the loop (`autonomy-loop.py::free_ram_mb`):
```bash
free_kb=$(wmic OS Get FreePhysicalMemory /Value 2>/dev/null \
          | grep -i '=' | cut -d= -f2 | tr -d '\r' | tr -d ' ')
if [ "${free_kb:-0}" -lt 307200 ]; then   # 300 MiB = 307200 KiB
  echo "LOW RAM ($((${free_kb:-0}/1024)) MB) — lightweight pass only"
else
  echo "OK ($((${free_kb:-0}/1024)) MB)"
fi
```
Note the `/Value` flag yields `FreePhysicalMemory=NNN` (one line, no header
padding), which is far easier to parse than the default tabular output. Always
`tr -d '\r'` — `wmic` emits CRLF on Windows and the trailing CR breaks integer
comparison in bash.

## Lightweight pass (safe under low RAM)
- Markdown edits to `knowledge-base/`, `skills/`, `tasks.md` (pure text, no model
  inference).
- Reading files, `git pull --ff-only`, `git add/commit/push` of small text diffs.
- Adding a SKILL.md or lessons-learned entry distilled from an existing log.

## Avoid under low RAM
- Paperclip build / `tsc` / npm / node operations.
- Starting heavy Python generators (`generate_v2_docs.py`, `*_generator.py`).
- Spawning model inference, deep `search_files` scans, large asset fetches.

## Recovery signal
The `wmic` check runs at the top of every tick. When RAM recovers above 300 MB
the loop automatically resumes normal work — no flag file or manual action needed.

## Lightweight pass menu (pick one, zero-inference)
When the low-RAM branch fires, choose ONE or more of these — all are pure-markdown
and safe under < 300 MB free:

1. **Harden an existing SKILL.md.** Add a missing step, a concrete command, or a
   gotcha surfaced in a prior tick. Prefer skills the loop already consumes
   (`skills/automation/`, `skills/content/`).
2. **Add a lessons-learned entry** (`knowledge-base/lessons-learned.md`) capturing
   the tick's RAM reading, the branch taken, and the exact action performed.
3. **Extend the SEO Coverage-Matrix backlog** in
   `skills/content/seo-comparison-article/SKILL.md` with the *next* candidate axis
   (research only — authoring the article is the normal-RAM job).
4. **Tidy the task board** (`tasks.md`): mark done items, re-flag human-gated items,
   or add a one-line lightweight-tick note. Pure text edits.

Never, under low RAM, run generators, the Paperclip build, `tsc`, npm/node, or
model inference — those are the deferred heavy jobs.

## Tick record template
Log a low-RAM tick with just enough detail to keep the next tick consistent:
```
TICK-NN (low-RAM): Free RAM = <N> KB (~<M> MB) < 300 MB gate -> lightweight pass.
Action: <skill hardened / lesson added / backlog extended>. Staged only safe files;
no `git add -A`. No model inference, no money movement.
```

## Why this matters
On a 6 GB host running three live services, a full build or model spawn under
< 300 MB free will thrash or OOM-kill the loop. Deferring to a cheap
self-improve pass keeps the repo advancing (docs/skills) while protecting
stability. The content funnel and product packaging work resumes safely once
memory frees up.
