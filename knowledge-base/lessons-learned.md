# Lessons Learned

## TICK-15 — Voice-agent SEO blueprint (2026-07-14)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/how-to-build-ai-voice-agent-2026.md` — a zero-budget voice-agent
  build guide (STT→LLM→TTS loop on n8n; free/open stack table; 5-step build).
  Fills a genuine funnel gap: no voice/phone content existed in the blog before.
  Cross-links 13 existing articles and funnels to the monetization-kit +
  ai-content-machine-blueprint products. Reused the established blog front-matter
  schema for generator compatibility. Updated tasks.md + this log. No secrets touched.
- **Lesson:** Scan existing slugs for a *missing medium/format axis*, not just a
  missing comparison axis. Voice/phone was a whole underserved channel next to the
  text-support, lead-gen, and faceless-video content — a practical "build it" guide
  in that channel is high-value, low-competition, and extends the same funnel.

## TICK-13 — Framework-comparison SEO + prompt-library sync (2026-07-14)

**What was done (agent-executable, zero human gate):**
- Authored `revenue/blog/langgraph-vs-autogen-vs-crewai-vs-n8n-2026.md` — an
  evergreen framework-comparison piece (LangGraph vs AutoGen vs CrewAI vs n8n)
  reusing the proven tool-comparison angle of the n8n article, with a
  side-by-side table and cross-links into the existing funnel. Fills the
  "which framework do I pick" top/mid-funnel gap.
- Cloned `Hermes-Prompt-Library` to satisfy the open "mirror top prompts" task.
  Found the library is already the canonical mirror and is *ahead* of the
  company repo (master prompt v3.0 vs the company's v2.0). Synced v3.0 into
  `prompts/` so the company repo tracks the latest — no redundant push needed.
- Updated tasks.md (tick-13 + mirror marked done) + this log. No secrets touched.

**Lessons:**
1. The "comparison article" pattern is repeatable and low-risk: pick any
   two-to-four competing tools/frameworks in the niche, give a 30-second verdict,
   a side-by-side table, and cross-links. It compounds SEO and fills funnel gaps.
2. "Mirror to a sibling repo" can already be satisfied: verify the target repo
   state before cloning/pushing. Here the library was already ahead, so the
   valuable action was syncing the company repo *up* to v3.0 rather than pushing
   v2.0 over it. Avoid pushing stale versions onto a canonical mirror.

## TICK-12 — Author AI-agent-monetization SEO blueprint (2026-07-14)

**What was done (agent-executable, zero human gate):**
- Authored `revenue/blog/ai-agent-monetization-2026.md` — a bottom-of-funnel
  monetization blueprint (6 ranked models: productize output, AaaS, white-label,
  prompt packs, faceless content, lead-gen/affiliate arbitrage) filling the
  "how do I actually make money" gap in the content funnel. Cross-links 11
  existing articles and funnels to the monetization-kit + zero-to-10k-ai-agents
  products.
- Reused the established blog front-matter schema for generator compatibility.
- Updated tasks.md (new tick-12 entry) + this lessons log. No secrets touched.

**Lessons:**
1. The content funnel now spans top (15 automations, agency) → mid (lead-gen,
   support, content repurposing, validation) → bottom (monetization, package
   prompts, zero-cost products). The loop can keep extending each spoke with
   evergreen, cross-linked articles — low-risk, compounding SEO work.
2. Bottom-of-funnel articles that explicitly name and funnel to paid products are
   the highest-leverage agent work: they turn existing free content into a path
   to the (human-gated) store, with no money movement required from the loop.

## TICK-11 — Author AI customer-support zero-budget SEO blueprint (2026-07-14)

**What was done (agent-executable, zero human gate):**
- Authored `revenue/blog/ai-customer-support-zero-budget-2026.md` — a
  self-hosted help-desk blueprint (triage→draft→route on n8n) filling the
  post-sale support gap in the content funnel. Cross-links 6 existing articles.
- Reused the established blog front-matter schema (title/description/slug/date/
  niche/tags/author) for generator compatibility.
- Updated tasks.md (new tick entry) + this lessons log. No secrets touched.

**Lessons:**
1. Content funnel still has clear post-sale gaps (support, retention) the loop
   can keep filling with evergreen, cross-linked articles — low-risk, continuous
   agent work that compounds SEO value.
2. Matching the existing front-matter schema is what lets the income-engine blog
   generator pick the file up without manual edits; consistency beats novelty.


## PRE-85 — Publish prompt-executor CLI to GitHub + npm (2026-07-14)

**What was done (agent-executable, zero human gate):**
- Verified the package builds and the test suite passes locally: `node test/prompt-executor.test.js` → **8/8 OK**.
- The public repo `github.com/itsPremkumar/prompt-executor` already existed with a
  configured `origin`; committed the publish-ready README + a `PUBLISH.md` handoff
  doc and pushed (`57e654f..a147fbc` on `master`).
- README now links to the Prem Autonomous Co showcase (PRE-5) and documents the
  post-publish `npm install -g prompt-executor` flow.

**What is blocked (by design — Constitution S0, human-in-the-loop):**
- `npm publish` requires the **founder's npm account + 2FA/OTP**. `npm whoami` in
  this environment returns `E401 Unauthorized` → no token present. This is an
  owner/money-movement action, so the agent stops and documents the exact
  handoff commands in `PUBLISH.md` instead of attempting it.

**Lessons:**
1. Product source repos (separate GitHub repos) are fully agent-publishable:
   verify build/test, commit, and `git push` work end-to-end with cached git creds.
2. npm publish is *not* agent-executable without the owner's token/2FA — treat it
   as a hard human gate and leave a precise, copy-paste runbook rather than blocking silently.
3. The product folder is double-tracked (its own `.git` + tracked in the main
   company repo). Keep the standalone repo as the publish source of truth; the
   main-repo copy is just a mirror. Avoid editing both from one commit.
4. `gh` CLI is **not installed** here; repo creation would need the GitHub API +
   a token, so prefer pushing to an already-created repo.

### Tick 2026-07-14 (14th) — LLM comparison article
- **Lesson:** The content funnel had tool comparisons (n8n vs Make vs Zapier) and
  framework comparisons (LangGraph vs AutoGen vs CrewAI vs n8n) but **no LLM
  model comparison**. Evergreen "which model wins for X" pieces are high-volume,
  low-competition SEO and pair naturally with the orchestration comparisons.
- Added `chatgpt-vs-claude-vs-gemini-vs-llama-2026.md` with a side-by-side superpower
  table + a 4-line decision shortcut (Claude=agents, ChatGPT=ecosystem, Gemini=context/
  scale, Llama=privacy/fixed cost). Cross-linked 9 existing articles and funneled to
  the zero-to-10k-ai-agents product.
- **Reuse:** when picking the next article, scan existing slugs for a missing
  comparison axis (model vs tool vs framework vs vertical) before inventing a new angle.

## TICK-16 — Evergreen comparison-SEO skill (2026-07-14)
- **What was done (agent-executable, zero human gate):** Graduated the repeated
  "X vs Y vs Z" comparison-article pattern into a reusable SKILL.md at
  `skills/content/seo-comparison-article/SKILL.md`. It encodes the full method
  distilled from TICK-13/14/15: scan existing blog slugs for an unsatisfied
  comparison axis (tool / framework / model / vertical / medium), reuse the
  canonical front-matter schema verbatim (title/description/slug/date/niche/
  tags/author), ship a 30-second verdict + side-by-side table, cross-link 6–13
  existing articles, and funnel to a (human-gated) paid product. Directly
  satisfies the open "Build out skills/" task. Updated tasks.md + this log.
  No secrets touched.
- **Lesson:** A pattern the loop repeats 3+ times is worth promoting to a skill.
  Capturing it as SKILL.md makes the next tick a fill-in-the-blanks job and keeps
  the front-matter schema (the thing that silently breaks the blog generator) from
  drifting. Prefer "extend the funnel via cross-links + product funnel" over
  inventing new angles — consistency compounds SEO.
