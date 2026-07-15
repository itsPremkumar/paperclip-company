# Lessons Learned

## TICK-27 — Low-RAM self-protect tick + skill hardening (2026-07-15)
- **What was done (agent-executable, zero human gate):** Free physical RAM measured
  `258736 KB` (~252 MB) via `wmic OS Get FreePhysicalMemory`, which is below the
  `FREE_RAM_WARN_MB = 300` gate. Per `skills/automation/low-ram-self-protect.md` the
  tick deferred all heavy work (no SEO generation, no build, no generators) and ran
  only a lightweight self-improve pass: hardened that same skill with a copy-paste
  bash parser (`/Value` flag + `tr -d '\r'` to strip wmic's CRLF, integer compare
  against `307200 KiB`) so the documented check matches what `autonomy-loop.py::
  free_ram_mb` actually runs. Updated tasks.md + this log. No secrets, no money
  movement, no model inference.
- **Lesson:** The RAM gate is doing its job — it caught a sub-300 MB tick and kept the
  loop on cheap, safe text edits instead of thrashing the 6 GB host. Two reusable
  gotchas worth pinning in the skill: (1) `wmic` default output is padded tabular
  text that's painful to parse; the `/Value` form (`FreePhysicalMemory=NNN`) is one
  clean line. (2) `wmic` emits CRLF, so the trailing `\r` must be stripped or the
  bash integer comparison silently misbehaves. Encoding the exact loop snippet in
  the skill closes the gap between "documented policy" and "code that runs".

## TICK-26 — AI writing-assistant comparison SEO (Jasper vs Copy.ai vs Writesonic vs Rytr) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/jasper-vs-copy-ai-vs-writesonic-vs-rytr-2026.md` — an AI-writing-assistant
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict + side-by-side
  table + 12 contextual cross-links + product funnel). Targets the missing *text/content-creation
  writing tool* axis, which is distinct from the already-covered image (Midjourney), video
  (Runway), voice (ElevenLabs), and slides (Gamma) media generators — the corpus owned the *media*
  layers but not the *prose* layer those mediums all script. Splits the decision cleanly into
  *long-form brand marketing* (Jasper) vs *short-form copy workflows* (Copy.ai) vs *SEO article
  production + chatbots* (Writesonic) vs *cheapest budget writing* (Rytr), reinforcing the
  faceless-content + content-repurposing + package-prompts + course-product funnel. Updated
  tasks.md + this log. No secrets, no money movement.
- **Lesson:** The comparison pattern keeps finding unsaturated, high-intent axes — "AI writing
  assistant" is a top-tier 2026 search lane that the media-generator quartet (image/video/voice/
  slides) had implicitly circled but never owned, so it compounds the funnel instead of sitting as
  an island. The brand-long-form-vs-short-form-workflows-vs-SEO-articles-vs-budget split maps onto
  four distinct operator jobs, which makes the cross-links (content-repurposing, faceless-channel,
  image/video/voice/slides comparisons, package-prompts, zero-cost-products, stack, lead-gen,
  how-to-run-ai-company, monetization) and the product funnel land harder than a flat feature
  list. Harvesting the *prose* axis that the media family scripts is higher-leverage than opening a
  brand-new category because it reuses link equity already in the repo.

## TICK-25 — AI presentation-maker comparison SEO (Gamma vs Beautiful.ai vs Tome vs SlidesAI) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/gamma-vs-beautiful-ai-vs-tome-vs-slidesai-2026.md` — an AI-deck-builder
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict + side-by-side
  table + 12 contextual cross-links + product funnel). Targets the missing *presentation/slides*
  axis adjacent to the already-covered image (Midjourney), video (Runway), and voice (ElevenLabs)
  generator axes — extending the image→video→voice→slides content-creation-medium quartet.
  Splits the decision cleanly into *one-click generation* (Gamma) vs *design-polish auto-layout*
  (Beautiful.ai) vs *narrative media-rich storytelling* (Tome) vs *cheapest bulk text-to-decks*
  (SlidesAI), reinforcing the faceless-content + content-repurposing + course-product funnel.
  Updated tasks.md + this log. No secrets, no money movement.
- **Lesson:** The comparison pattern keeps finding adjacent unsaturated axes — slides are the
  natural "container" that holds the image/video/voice mediums the corpus already owns, so this
  completes a four-medium content-family narrative and lets the whole set cross-link into one
  "build a faceless content machine" story. The generation-vs-polish-vs-storytelling-vs-bulk split
  maps onto four distinct operator jobs, which makes the cross-links (content-repurposing,
  faceless-channel, image/video/voice comparisons, package-prompts, zero-cost-products, stack,
  lead-gen, how-to-run-ai-company, monetization) and the product funnel land harder than a flat
  feature list. Compounding the content-medium quartet is higher-leverage than opening a brand-new
  axis because it harvests link equity already in the repo.

## TICK-24 — AI meeting-assistant comparison SEO (Otter.ai vs Fireflies.ai vs Fathom vs tl;dv) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/otter-vs-fireflies-vs-fathom-vs-tldv-2026.md` — an AI-meeting-notetaker
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict + side-by-side
  table + 12 contextual cross-links + product funnel). Targets the missing *sales/support capture*
  axis (B2B call-recording) adjacent to the lead-gen, customer-support, solopreneur-automation, and
  n8n automation articles — the funnel's *input* layer that the comparison corpus had not yet owned.
  Splits the decision cleanly into *best capture/search* (Otter) vs *CRM/pipeline handoff* (Fireflies)
  vs *free-first solo capture* (Fathom) vs *async video highlights* (tl;dv), reinforcing the
  lead-gen + support + content-repurposing funnel. Updated tasks.md + this log. No secrets, no money
  movement.
- **Lesson:** The comparison pattern keeps finding unsaturated, high-intent B2B axes — "AI meeting
  notetaker" is a strong 2026 search lane that maps directly onto the existing sales-call and
  support-call funnels (the *capture* half of lead-gen and customer-support), so it compounds the
  funnel instead of sitting as an island. The capture-vs-handoff-vs-free-vs-highlight split maps onto
  four distinct operator jobs, which makes the cross-links (7-workflows, lead-gen, support, n8n,
  content-repurposing, faceless-content) and the product funnel land harder than a flat feature list.

## TICK-23 — AI voice-generator comparison SEO (ElevenLabs vs Cartesia vs PlayHT vs OpenAI TTS) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/elevenlabs-vs-cartesia-vs-playht-vs-openai-tts-2026.md` — an AI-voice-generator
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict + side-by-side
  table + 11 contextual cross-links + product funnel). Targets the missing *voice/speech* axis
  next to the already-covered image (Midjourney) and video (Runway) generator axes, completing the
  image→video→voice content-creation-medium trio. Splits the decision cleanly into *hero realism*
  (ElevenLabs) vs *real-time latency* (Cartesia) vs *multilingual bulk* (PlayHT) vs *cheapest
  simple API* (OpenAI TTS), reinforcing the faceless-content + voice-agent funnel and pairing
  directly with `how-to-build-ai-voice-agent-2026`. Updated tasks.md + this log. No secrets, no
  money movement.
- **Lesson:** The comparison pattern keeps finding adjacent unsaturated axes — voice is a natural
  neighbor of the faceless-content funnel (the audio those channels actually ship), and the
  realism-vs-latency-vs-bulk-vs-cheap split maps onto four distinct business jobs, which makes the
  cross-links and product funnel land harder than a flat feature list. Completing the
  image→video→voice trio also lets the corpus cross-link the three content mediums into one
  "build a faceless content machine" narrative, compounding link equity across the whole family.

## TICK-22 — AI app-builder comparison SEO (Bolt vs Lovable vs v0 vs Replit) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/bolt-vs-lovable-vs-v0-vs-replit-2026.md` — an AI-app-builder
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict +
  side-by-side pricing table + 11 contextual cross-links + product funnel). Targets a
  *distinct builder axis* (prompt-to-app generators) that sits adjacent to, but separate
  from, the already-covered coding-assistant axis (pair-programmers, not full-app
  generators). Frames the four as speed-vs-control trade-offs (spark / product lane /
  front-end face / workshop) and routes to monetization-kit, zero-to-10k-ai-agents, and
  the AI-content-machine blueprint. Updated tasks.md + this log. No secrets, no money
  movement.
- **Lesson:** The comparison pattern keeps finding unsaturated axes — "AI app builders"
  is a high-intent 2026 lane the corpus did not yet own, and it is cleanly distinguishable
  from coding assistants (generate-an-app vs help-me-code), so it compounds the funnel
  without cannibalizing the existing adjacent article. The spark→product-lane→workshop
  analogy (Bolt / Lovable / Replit) plus v0-as-"face" gives readers a decision shortcut
  that maps onto real business jobs, which is what makes the cross-links and product
  funnel land.

## TICK-21 — Video-generator comparison SEO (Runway vs Pika vs Synthesia vs HeyGen) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/runway-vs-pika-vs-synthesia-vs-heygen-2026.md` — an AI-video-generator
  comparison SEO piece reusing the proven "X vs Y vs Z" pattern (30-second verdict +
  side-by-side table + 11 cross-links + product funnel). Targets the missing *video/motion*
  axis next to the already-covered tool, framework, model, channel, visual, vector-DB, and
  coding-assistant axes. Splits the decision cleanly into *b-roll/motion* (Runway, Pika) vs
  *talking-head avatar* (Synthesia, HeyGen), reinforcing the faceless-content + content-machine
  funnel. Updated tasks.md + this log. No secrets, no money movement.
- **Lesson:** The comparison pattern keeps finding adjacent unsaturated axes — video is a
  natural neighbor of the faceless-content funnel (the asset those channels actually ship), and
  the b-roll-vs-avatar split maps onto two distinct business jobs (footage vs presenter), which
  makes the cross-links and product funnel land harder than a flat feature list. Avatar tools
  (Synthesia/HeyGen) also let the corpus recommend a camera-free path, extending the zero-budget
  thesis beyond just self-hostable open-weight software.

## TICK-20 — Image-generator comparison SEO (Midjourney vs DALL·E 3 vs Stable Diffusion vs Flux) (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/midjourney-vs-dalle-vs-stable-diffusion-vs-flux-2026.md` — an
  AI-image-generator comparison SEO piece reusing the proven "X vs Y vs Z" pattern
  (20-second verdict + side-by-side table + 11 cross-links + product funnel). Targets
  the missing *visual/content-creation* axis next to the already-covered tool,
  framework, model, channel, vector-DB, and coding-assistant axes. Ties directly into
  the existing faceless-content and content-repurposing articles. Updated tasks.md +
  this log. No secrets, no money movement.
- **Lesson:** The comparison pattern keeps finding new unsaturated axes
  (visual generation is a natural neighbor of the faceless-content funnel) — scanning
  existing slugs for the next open axis remains the lowest-risk, highest-compounding
  autonomous tick. Self-hostable open-weight options (Stable Diffusion, Flux) also let
  the corpus recommend a $0-marginal-cost path, reinforcing the zero-budget thesis.

## TICK-17 — Channel-comparison SEO (Faceless YouTube vs TikTok vs Newsletter) (2026-07-14)
- **What was done (agent-executable, zero human gate):** Authored
  `revenue/blog/faceless-youtube-vs-tiktok-vs-newsletter-2026.md` — a
  medium/channel-comparison SEO piece reusing the proven "X vs Y vs Z" pattern
  (30-second verdict + side-by-side table + cross-links to 9 existing articles +
  product funnel). Targets an *unsaturated channel axis* (faceless YouTube vs
  TikTok vs newsletter) next to the already-covered tool/framework/model axes.
  Also flushed the prior tick's uncommitted generator WIP (real-estate raw
  source content + cold-email-templates-ai-agencies gumroad product) that had
  been left staged but never committed. Updated tasks.md + this log. No secrets.
- **Lesson:** The comparison pattern extends beyond tools/frameworks/models to
  *channels/media* — picking the next unsaturated axis (vertical, medium, or
  model) keeps the corpus compounding without inventing a brand-new format.
  Always flush accumulated uncommitted WIP at commit time so a tick's partial
  generator output doesn't drift from the recorded task board.

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

## TICK-17 — Faceless channel-comparison SEO + WIP flush (2026-07-14)
- **What was done (agent-executable, zero human gate):** Authored
  `faceless-youtube-vs-tiktok-vs-newsletter-2026.md` — a medium/channel-comparison SEO
  piece (Faceless YouTube vs TikTok vs Newsletter) filling the *channel* axis gap left by
  the tool/framework/model comparisons. Side-by-side table + 30-second verdict + 9
  cross-links; funneled to ai-content-machine-blueprint + zero-to-10k-ai-agents. Also
  flushed the prior tick's uncommitted generator WIP (real-estate raw content + cold-email
  Gumroad product). No secrets.
- **Lesson:** the channel/medium axis is a fourth evergreen comparison family alongside
  tool/framework/model; rotate through all four to keep coverage broad without inventing
  new angles.

## TICK-18 — Vector-DB comparison SEO (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `pinecone-vs-chroma-vs-qdrant-vs-weaviate-2026.md` — a vector-database (infra/storage)
  comparison, the fifth comparison axis after tool/framework/model/channel. 30-second
  verdict, side-by-side table, 11 cross-links, funnel to ai-agent-monetization +
  zero-to-10k-ai-agents. Backfilled the missing TICK-17 lessons entry (board claimed it,
  log missed it). No secrets touched; scanned working tree and confirmed no secrets before
  commit.
- **Lesson:** scanning existing slugs for a *missing axis* (now: tool → framework → model
  → channel → infra) keeps the comparison series compounding and low-risk. The vector-DB
  axis is self-host-friendly, so it reinforces the zero-budget thesis better than a pure
  SaaS comparison.

## TICK-19 — AI-coding-assistant comparison SEO (2026-07-15)
- **What was done (agent-executable, zero human gate):** Authored
  `cursor-vs-windsurf-vs-copilot-vs-claude-code-2026.md` — an AI-coding-tool comparison
  (Cursor vs Windsurf vs GitHub Copilot vs Claude Code), the sixth comparison axis and a
  *developer-tool* family that serves the builder audience directly (GUI-assist vs
  terminal-agent split). 30-second verdict, side-by-side table, 11 cross-links, funnel to
  monetization-kit + zero-to-10k-ai-agents via the monetization blueprint. Updated tasks.md
  + this log. Scanned working tree; no secrets.
- **Lesson:** the comparison series can keep expanding into *role-specific tool families*
  (here: coding assistants) without leaving the proven "X vs Y vs Z" format — the axis is
  "what job does the reader have," not just "what category." Splitting the verdict on
  workflow shape (GUI assist vs terminal agent) is a crisp, decision-useful cut that also
  reinforces the zero-budget, one-person-company thesis.
