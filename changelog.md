# Changelog

## 2026-07-15 — Autonomy tick: appointment scheduling/booking automation SEO (TICK-34)
- Authored `income-engine/content/ai-agents-for-appointment-scheduling-and-booking-automation.md`, a new high-intent local-service SEO article (after-hours lead capture + no-show reduction angle), distinct from the existing voice-agent and small-business pieces.
- Added `TICK-34` entry to `knowledge-base/lessons-learned.md`.
- Lightweight self-improve pass only: free RAM was ~256 MB (below the 300 MB threshold), so no server build or heavy pipeline was run.
- Secret hygiene: staged only the new article + logs, NOT a blanket `git add -A`; machine dumps (`company-report.md`, `issues.json`) and secret-bearing `start-pc-now.sh` / `_analyze.py` left unstaged.

## 2026-07-15 — Autonomy tick: no-code AI agent builder SEO comparison (TICK-31)
- Authored `revenue/blog/dify-vs-flowise-vs-langflow-vs-botpress-2026.md`, the
  missing *no-code AI agent builder* comparison axis (Dify, Flowise, Langflow,
  Botpress) following the `seo-comparison-article` SKILL schema (slug == filename,
  30-second verdict, 6-dim table, 11 cross-links, product funnel, no price/checkout).
- Added `TICK-31` entry to `knowledge-base/lessons-learned.md` and an autonomy-log
  row in `knowledge-base/autonomy-log.md`.
- Secret hygiene: `start-pc-now.sh` (untracked) embeds `BETTER_AUTH_SECRET` and
  reads `OPENROUTER_API_KEY` from a local `.env`; deliberately excluded from the
  commit (staged only article + logs, not a blanket `git add -A`).

## 2026-07-13 — Repository bootstrap + prompt consolidation (v2.0)
- Created `Hermes-Full-Autonomous-Company` as the single source of truth on GitHub.
- Pushed the real, running company from `/c/one/paperclip-company`: 8 digital products, income engine, finance ledger, `hermes-paperclip-adapter` source, COMPANY_PLAN, status snapshot.
- Consolidated six overlapping prompt drafts into **`CONSTITUTION.md` (Master Operating Prompt v2.0)**:
  - Adopted the reality-matched structure of `hermes-master-operating-prompt.md` (Paperclip + OpenClaw + budget caps + human-in-the-loop).
  - Dropped fictional stack assumptions (n8n, Mem0, CrewAI, AutoGen, standalone OmniRouter) that don't run here.
  - Removed dependence on unverified "Claude Fable 5 leaked prompts"; mandated officially-published prompt guidance instead.
  - Added explicit low-RAM / memory-discipline section (this machine is memory-starved).
  - Kept the good parts: GitHub-as-truth, tool validation, End-Goal Loops, self-improvement loop, decision framework.
- Archived the five superseded drafts in `prompts/archive/` (v0.1–v0.5, v1.0).
- Added `tools/approved.md` and `tools/rejected.md` documenting what actually runs vs. what was considered.
- Added this changelog and README index.

## Prior (local-only, pre-GitHub)
- Paperclip company stood up with 7 agents; 8 digital products generated via income engine; finance ledger + burn guard implemented (all local at `/c/one/paperclip-company`, not yet on GitHub until this commit).
