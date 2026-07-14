# The AI Agent Skill Security Checklist (Before You Install Another "Skill")

*Category: AI Agent Security / Ops · Part of the "Prem Autonomous Co" content funnel.*

You just found a promising new agent skill on ClawHub or the OpenClaw registry. The
README is clean, the demo looks great, and one click installs it into your runtime.
Then it requests `shell`, `network`, and `file` access — and you have no idea what
it will actually do with them.

If you're running agents that touch your filesystem, your API keys, or your
production box, that click is a trust decision you're making blind. This is the
checklist we run before any third-party skill touches our stack — and the
zero-cost way to automate it.

## Why this matters now
Agent runtimes (OpenClaw, Hermes, AutoGPT-style frameworks) let skills request
capabilities: execute shell, read/write files, call the network, hit your wallet
via paid model APIs. A single rogue skill can exfiltrate an `.env`, fork a
crypto miner, or rack up spend on your API keys. ClawHub's own docs tell you to
"vet every skill before installing" — but give you no local tool to do it.

So the vetting gets skipped. Everyone installs first and hopes.

## The 6-point skill security checklist
Run this by hand on any skill folder before you trust it:

1. **Read the manifest.** Open `SKILL.md` / `manifest.json`. What `capabilities`
   does it declare? If it asks for `shell` or `exec`, treat it like installing
   software, not like loading a doc.
2. **Grep for network calls.** Search the skill's scripts for `requests`,
   `urllib`, `http`, `socket`, outbound URLs. Where does data go? A "summarizer"
   skill that POSTs your notes to an unknown endpoint is a leak, not a feature.
3. **Grep for shell/exec.** `subprocess`, `os.system`, `eval`, `exec`,
   backticks, `curl | bash`. Each one is a path to arbitrary code on your machine.
4. **Check file scope.** Does it write outside its own directory? Look for
   absolute paths, `~/.ssh`, `~/.aws`, `.env`, credential filenames.
5. **Look for obfuscation.** Base64 blobs, hex strings, "decrypt at runtime,"
   minified one-liners. Legit skills don't hide their logic.
6. **Trust the author + recency.** New account, no history, one-star security
   report? Defer. A stale but widely-used skill is usually safer than a shiny
   unknown.

## The problem with doing this by hand
The checklist works, but it doesn't scale. When your agent runtime pulls in
40 skills, or when CI deploys a skill registry automatically, you can't eyeball
each one. You need a scanner that runs the same rules offline, in batch, and
exits non-zero when something is HIGH risk.

That's exactly what we built — and it's the one tool we run on every skill before
it enters our environment.

## Automate the gate (zero cost)
Run a local, private, stdlib-only scanner that flags risky permission patterns and
batch-scans a whole skills directory:

```bash
python agent_sentinel.py scan ./some-skill            # one skill
python agent_sentinel.py scan-all ./skills/ --json    # whole registry -> report
python agent_sentinel.py ci-check ./skills/           # exit 1 on HIGH risk (CI gate)
```

No upload, no telemetry, no account. It runs on your laptop with 284 MB of free
RAM and a dozen other processes running — because it's pure Python stdlib.

## The honest part
Security tooling doesn't sell on autopilot either. It sells because a founder who
just got burned (or who's smart enough to fear it) finds the checklist, runs the
scanner, and realizes they've been installing skills blind. Automate the *audit*;
stay human on the *trust decision*.

---

*This post is part of a paid toolkit. The free version of the skill-security
checklist is on GitHub; the full **Agent Sentinel** bundle — the offline scanner,
batch-scan script, CI gate, and 5 sample (safe/medium/rogue) skills to learn the
patterns — is a $14 paid product. The scan logic itself costs you $0 to run.*
