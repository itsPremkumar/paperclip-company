# Lessons Learned

## Operating Under Critical RAM Pressure

### Context
During the 2026-07-13 autonomy loop, free physical memory dropped to ~284 MB (below the 300 MB warning threshold). The autonomy loop correctly deferred heavy work and executed only a lightweight self-improve pass.

### Lesson
- **Low RAM pattern**: The Paperclip server, OpenClaw gateway, and Hermes agent running concurrently consume most of the ~6 GB available. Free RAM oscillates between 100 MB and 644 MB depending on background activity.
- **What works under low RAM**: Simple markdown edits, git operations, reading files. These involve no model inference, no heavy subprocesses.
- **What to avoid**: Running the Paperclip build, starting heavy Python scripts, spawning model inference, deep filesystem scans, or any npm/node operations.
- **Recovery signal**: The `wmic` check runs before every tick. If RAM recovers above 300 MB on a future tick, the loop automatically resumes normal operations — no manual intervention needed.

### Recommendation
Consider adding a lightweight "canary" process that pre-warms model state only when RAM > 500 MB, and terminates it immediately if memory drops.

## Low-RAM ticks reliably produce value via skill distillation (2026-07-14)
On a tick where free RAM was ~231 MB (below the 300 MB threshold), the loop ran
only a lightweight self-improve pass but still advanced the repo: it promoted the
existing "Operating Under Critical RAM Pressure" lesson into a reusable
`skills/automation/low-ram-self-protect.md` SKILL.md.

### Lesson
- A low-RAM tick is not wasted. Pure-text artifacts (SKILL.md, lessons-learned
  entries, tasks.md maintenance) are safe and keep the repo moving even when
  builds/inference are deferred.
- When a lesson in `lessons-learned.md` is stable and broadly reusable, graduate
  it into `skills/<category>/<name>.md` so it loads into the Hermes skill library
  automatically. This is a high-leverage, zero-cost agent action.

## Use absolute Windows paths for the patch tool
The `patch` tool resolves relative paths from the workspace root (`C:\one\paperclip-company`). Using `/c/one\...` produces a doubled `C:\c\one\...` path. Use `C:\one\...` style paths directly.

## Autonomy-log entries should be atomic
Each tick's entry should be complete and self-describing so the log is useful even if the tick is interrupted mid-write.

## The task board must live at known paths or the loop self-improves
The autonomy loop reads `tasks.md` (repo root) and `data/paperclip/issues/*.md`. If neither exists, `pick_actionable` returns None and the tick falls back to a self-improve pass. On 2026-07-13 the repo had no `tasks.md` and no issue `.md` files at those paths, so the loop silently defaulted to self-improve.

### Lesson
- To guarantee real work each tick, publish an explicit `tasks.md` with `- [ ]` agent-actionable (non-human-gated) items. Otherwise the loop will only ever write autonomy-log entries and never package products or draft content.
- When adding tasks, keep money-moving items out (Gumroad publish, payouts, signups) — those are human-gated and the loop skips + flags them.

## The content funnel is the sales engine, not the products
A digital product (prompt pack, playbook, template) does not sell on autopilot. It sells because a
top-of-funnel SEO article + community posts point qualified readers at a $0-cost asset that does a
job they hate. The agent's highest-leverage non-human-gated work is *producing that funnel content*
(`revenue/blog/*.md`, Medium drafts, Moltbook posts) consistently, then packaging existing internal
assets into priced products.

### Lesson
- When no `tasks.md`/issue exists, the most reliably useful agent-safe task is to draft another
  funnel article that links to an existing product in `digital-products/` or `income-engine/gumroad/products/`.
- Keep every funnel post ending with the "free on GitHub / paid bundle" split so the funnel converts.

## The "11-agent income stack" framing converts better than product lists
On 2026-07-13 a new funnel article (`revenue/blog/autonomous-ai-business-stack-2026.md`)
framed the catalog as an 11-role agent stack (Researcher→Optimizer) with a 30-day
launch table that isolates the single human-gated step (marketplace listing). This
"operating model, not a course" angle reads higher-value than a bare product list
and naturally routes readers to existing products (playbook, script packs, kits).

### Lesson
- When drafting funnel content with no `tasks.md`, lead with a reusable mental model
  (stack / system / workflow) and embed a table that separates autonomous from
  human-gated steps — it pre-qualifies readers and keeps the guardrail story explicit.
- Always end funnel posts with internal links to 2+ existing `revenue/blog/*.md`
  articles so the cluster interlinks and compounds SEO.
- Never write the listing or move money — those stay human-gated.

## Faceless-content-channel framing is a strong new funnel angle
On 2026-07-13 a new funnel article (`revenue/blog/faceless-ai-content-channel.md`)
opened a content niche the catalog was missing top-of-funnel for: building a
faceless AI YouTube/Shorts channel at $0. The angle works because it maps
directly onto two existing products (50 Viral Scripts, Remotion templates) plus
the 30-Day Launch Plan and Agent Playbook — turning "how to" content into a
product demo without naming it as one.

### Lesson
- When drafting funnel content with no `tasks.md`, a "build X with AI at $0"
  lifestyle/creator angle reaches a wider audience than the pure "AI agents for
  business" angle, and still routes readers to the same paid kits.
- Lead with a 4-step repeatable system, state the honest limits, then link 3–4
  concrete existing products. End with the GitHub-free / paid-split CTA.
- Prefer relative links (`../../digital-products/...`) so the files render on
  GitHub and in the local store without path fixes.

## Skill-security is an underserved funnel niche (2026-07-13 tick)
A new funnel article (`revenue/blog/ai-agent-skill-security-checklist.md`) opened
a content angle the catalog had no top-of-funnel for: vetting third-party agent
skills (shell/network/file capabilities) before installing them, then automating
the audit with an offline CLI scanner. It maps directly onto the **Agent Sentinel**
product (`income-engine/gumroad/products/agent-sentinel/`, $14, status ready) and
the free `secret-scanner` / `skill-lint` skills already in `clawhub-skills/`.

### Lesson
- Security/ops-adjacent "before you install X" framing is high-intent: readers
  are one bad skill away from a leaked `.env` or runaway API spend, so the pain is
  immediate and the paid tool (offline, stdlib-only, CI-gate) is an obvious yes.
- Tie each funnel article to a *specific ready product ID* (not just a category)
  so the funnel has a concrete destination and the post ages well.
- The article should be runnable on the same constrained box the company runs on
  (no deps, no network) — demonstrate that constraint as proof, not an apology.

## income-engine generators were never run (2026-07-14 tick)
On this tick, `revenue/blog/` had 7 hand-written funnel articles but the
`income-engine/content/` and `income-engine/gumroad/products/` output streams were
**empty** — the two existing generators (`generate_blog.py`, `generate_gumroad.py`)
had never been executed, even though the catalog lists 11 ready products and 5 blog
niches were configured.

### What I did (agent-safe)
- Ran `python income-engine/generate_blog.py` → it populated 5 affiliate guides into
  `income-engine/content/` (idempotent via `.used_blog.json`). The generator works
  with stdlib only; no pip.
- Wrote a new original SEO funnel article
  (`revenue/blog/2026-07-14-zero-budget-ai-automation-agency.md`) — no affiliate
  tokens, ROI-framed, links to the existing "AI agency stack" angle (compounds the
  cluster).
- Created a real `tasks.md` board mirror so future ticks have structured work and do
  not silently fall back to self-improve. Human-gated items (Gumroad publish,
  payouts, signups) are explicitly flagged, not executed.

### Lesson
- **Generators ≠ output.** Having a pipeline script is not the same as having run it.
  On a fresh tick, `git status` the known output dirs (`income-engine/content`,
  `income-engine/gumroad/products`, `revenue/blog`) before assuming work is done.
- The `generate_gumroad.py` ideas (n8n pack, ROI calculator, proposal template) do
  **not** match the 11 catalog products — a future tick should extend or replace its
  `PRODUCT_IDEAS` to emit one folder per real catalog product so the 11 ready items
  actually get Gumroad-ready listings (still human-gated to publish).
- Path gotcha re-confirmed: write_file with `/c/one/...` produced `C:\c\one\...`.
  Always use `C:\one\...` absolute Windows paths in this environment.

## Packaging existing content into catalog products is a high-leverage agent action (2026-07-14)
On this tick, free RAM was ~347 MB (above threshold). Rather than run heavy
builds, the loop packaged the already-published blog article
`revenue/blog/cold-outreach-that-gets-replies.md` into a new Gumroad-ready
product folder `income-engine/gumroad/products/cold-outreach-pack/` (PRODUCT.md
+ LISTING.txt), mirroring the established dev/sales pack format.

### Lesson
- The repo holds a lot of finished blog/outreach content that has NOT yet been
  packaged into its corresponding catalog product folder. Converting published
  articles into the PRODUCT.md + LISTING.txt shape is pure-text, zero-cost, and
  directly grows the sellable catalog (still human-gated to publish).
- Conventions to reuse: PRODUCT.md = `# Title`, TOC table, numbered templates in
  fenced blocks, system recap; LISTING.txt = Title/Price/Description/Category +
  explicit "HOW TO PUBLISH (human step)" block. Keep the publish step clearly
  human-gated — never imply the loop will publish or move money.
- While packaging, scan source content for stray non-ASCII/garbage characters
  (this tick found a stray CJK char in the outreach article — fixed in place).
  Cheap quality pass that prevents shipping a visibly broken product.

## Packaging un-bundled catalog products grows the sellable catalog fast (2026-07-14)
Free RAM was ~347 MB (above threshold). This tick packaged two catalog products
that had only a `README.md` and no Gumroad folder yet —
`digital-products/product-7-pricing-templates` →
`income-engine/gumroad/products/ai-pricing-templates-pack/` and
`digital-products/product-8-launch-plan` →
`income-engine/gumroad/products/zero-cost-launch-plan/`. The pricing pack was
also upgraded beyond the README: it ships the promised three formats — Markdown
(PRODUCT.md), CSV (`tier-templates.csv`) and JSON (`tier-templates.json`) — so
buyers can drop the data straight into Stripe or a spreadsheet.

### Lesson
- The biggest untapped catalog gap is products with a `README.md` but no
  `income-engine/gumroad/products/<name>/` folder. Six such products remain
  (product-2, -3, -4, -6 plus the two just done; check `digital-products/*`).
  Each is a pure-text, zero-cost, agent-safe tick of work.
- When a README promises multiple formats (CSV/JSON), actually generate those
  files rather than only rewriting prose — it materially raises product value
  and matches the listing's promise. Verify JSON with a lint pass before commit.
- Reuse the established PRODUCT.md + LISTING.txt shape (incl. the explicit
  "HOW TO PUBLISH (human step)" block) so all packs stay consistent and the
  publish step stays clearly human-gated.

## Packaging product-2 (Autonomous AI Agent Operations Playbook) — 2026-07-14
The highest-value un-packaged catalog product (`prem-agent-playbook`, $29) was
packaged from its 60-line `digital-products/product-2-playbook/README.md` into
`income-engine/gumroad/products/agent-ops-playbook/`. Because the README only
listed bonus templates by name (`AGENTS.md`, `.env.example`, `issue-template.json`,
`heartbeat-config.yaml`) without shipping them, this tick authored all four as
real, self-contained files — so the pack is complete and deployable, not just a
promise.

### Lesson
- A README that *names* bonus assets but doesn't ship them is a packaging debt.
  When packaging such a product, generate the named assets from the playbook's
  own content — don't hunt for them elsewhere. The result is a self-contained
  product that matches its listing promise.
- The `.env.example` ships empty/placeholder-only by design; the autonomy loop's
  secret scan (in heartbeat-config.yaml) blocks any populated `.env` from commit.
  This keeps the "never commit secrets" rule enforceable at the product level.
- Use `C:\one\...` absolute paths (not `/c/one\...`) with the write tool to
  avoid the doubled `C:\c\one\...` stray-directory bug noted earlier.
- Five of the eight original catalog products are now packaged (product-1,
  -5, -7, -8 done earlier; product-2 this tick). Remaining un-packaged:
  product-3 (remotion templates), product-4 (monetization kit), product-6
  (job-board guide).

## Packaging the Final 3 Catalog Products (Tick 2026-07-14, 5th)

### Context
The remaining un-packaged catalog products were `product-3-remotion-templates`,
`product-4-monetization-kit`, and `product-6-job-board`, each with only a
`README.md` in `digital-products/`. This tick turned each into a complete,
deployable Gumroad package under `income-engine/gumroad/products/`.

### What shipped
- `remotion-templates/`: `input-scripts.json` (12 full video templates with
  hooks, scripts, voices, orientation), `voices-config.json` (7 free Edge-TTS
  voices, orientation/text/transition presets), `PRODUCT.md`, `LISTING.txt`.
- `monetization-kit/`: 8 interlocking markdown assets (brief, service catalog,
  pricing sheet, one-pager, ROI calculator lead magnet, cold outreach, reseller
  program, 30-day launch plan) + `PRODUCT.md` + `LISTING.txt`.
- `job-board-guide/`: 4 chapter files (profile optimization, outreach
  strategies, tracking/conversion, to-revenue) + `PRODUCT.md` + `LISTING.txt`.

### Lesson
- Catalog `README.md` files are *specs*, not products. A real package needs the
  actual deliverable files the README describes — generate them from the README's
  own outline rather than shipping the README alone.
- The `write_file` tool doubled the `/c/one/...` MSYS path into `C:\c\one\...`.
  Always use native `C:\one\...` absolute paths on this Windows host to avoid
  stray directories (then verify with `find /c/c` and clean up if needed).
- Final secret scan flagged "secret" (prose) and "tokens" (usage metric) as
  false positives — confirm matches are real before treating them as leaks.
- All 8 catalog products are now packaged. The next agent-safe work stream is
  authoring SEO/blog drafts and mirroring prompts to Hermes-Prompt-Library.

## Tool-comparison blog posts cross-link and compound (Tick 2026-07-14, 6th)

### Context
The open task board lists "author next SEO/article drafts into revenue/blog/" as a
continuous agent-safe work stream. This tick wrote `n8n-vs-make-vs-zapier-2026.md`,
a comparison piece that deliberately links back to the existing zero-budget agency
playbook.

### Lesson
- Comparison ("X vs Y vs Z") and "which tool should I use" queries are high-intent,
  evergreen SEO targets that pair naturally with the agency/sell-side content
  already in the repo. Writing them as a *series* with internal cross-links raises
  session depth and keeps the blog coherent.
- Match the existing front-matter schema exactly (title, description, slug, date,
  niche, tags, author) so the income-engine blog generator can ingest the draft
  without rework.
- Authoring drafts is the safest, highest-leverage tick action under any RAM
  condition: pure text, no build, no inference, no money movement.

## Graduate a repeated action into a SKILL.md; handle a dirty tree at tick start (Tick 2026-07-14, 7th)

### Context
The loop had packaged eight catalog products by repeating the same "assemble
existing content into a sellable bundle" steps. This tick distilled those steps
into `skills/automation/package-digital-product.md` so the pattern loads into
the skill library automatically. The tick also began with a *dirty working tree*
(pre-existing uncommitted blog/showcase/product changes from an earlier
interrupted run).

### Lesson
- When an action repeats 3+ times and is stable, graduate it into
  `skills/<category>/<name>.md` with YAML front-matter (name, category,
  description, state). This is the documented high-leverage self-improve move and
  directly clears the open "Build out skills/" board item.
- At tick start, if `git status` shows uncommitted work, don't `git pull
  --ff-only` blindly (it refuses on a dirty tree). Use
  `git stash push -u` → `git pull --ff-only` → `git stash pop`. This preserves
  in-progress agent work AND syncs GitHub as source of truth, with no merge
  conflict when the remote is already up to date.
- The "package from existing content" skill stays HUMAN-GATED on the publish/price
  step (Constitution S0) — the agent writes the asset and catalog entry, never
  lists or moves money.

## Top-of-funnel "automation checklist" angle drives service-tier demand (Tick 2026-07-14)

### Context
The continuous agent-safe board item is "author next SEO/article drafts into revenue/blog/". This tick wrote `15-ai-automations-small-business-2026.md` — a numbered, actionable checklist of zero-cost automations for small-business owners, explicitly linking to the agency playbook, the n8n comparison, cold-outreach, and the digital-products funnel.

### Lesson
- A "15 things you can automate" checklist is a high-intent, evergreen top-of-funnel format: it targets the exact buyer persona for the $149–$499/mo service tiers and the priced digital products, while staying 100% agent-safe (no listing, no money movement).
- Lead each item with the cheapest tool and add a "what to do this week" section so the post is useful standalone and naturally routes readers to existing `revenue/blog/*.md` and `digital-products/` assets via relative links.
- Front-matter must match the existing schema exactly (title, description, slug, date, niche, tags, author) so the income-engine generator can ingest it without rework.
- Authoring pure-markdown drafts remains the safest, highest-leverage tick under any RAM condition: no build, no inference, no external account, no money movement.

## Content-repurposing angle closes the "content→product" loop (Tick 2026-07-14)

### Context
The continuous agent-safe board item is "author next SEO/article drafts into revenue/blog/". This tick wrote `content-repurposing-engine-2026.md` — a 4-stage "write one pillar, shred into 10 formats" pipeline that cross-links the faceless-channel, zero-cost-products, and package-prompts articles and explicitly funnels to the paid `ai-content-machine-blueprint` ($47) and `ai-video-script-pack` (50 scripts) products in `income-engine/gumroad/products/`.

### Lesson
- A repurposing playbook is a high-intent, evergreen content-cluster piece that bridges the *free blog* to the *priced product catalog*: it teaches the workflow, then points at the kit that automates it. This directly supports the income engine without any money movement.
- Always verify the product folder names and contents before cross-linking (e.g. `income-engine/gumroad/products/ai-content-machine-blueprint/PRODUCT.md`) so funnel links are honest and not fabricated.
- Use relative `revenue/blog/*.md` links for internal posts and name the exact priced product + price point for the funnel CTA.
- Prefer a "stealable prompt" block in each article — it gives the reader instant value and raises save/share rate, which lifts SEO.

## Validation-stage content fills the earliest funnel gap (Tick 2026-07-14)

### Context
The continuous agent-safe board item is "author next SEO/article drafts into revenue/blog/". This tick wrote `48-hour-digital-product-validation-2026.md` — a 48-hour zero-budget validation sprint (mine demand → ship an ugly offer → get it in front of 50 strangers → count intent signals → go/no-go) that sits *before* the build/launch/sell stages already covered by `zero-cost-digital-products-that-sell.md` and `how-to-run-ai-company-zero-budget.md`.

### Lesson
- Buyer-funnel coverage matters more than article volume: before authoring, map the funnel (validate → build → launch → sell) and fill the *earliest uncovered gap*. Validation was the missing top of the editorial funnel.
- A validation piece naturally cross-links to every downstream post (products, agency, prompts, outreach, tool comparison) and funnels to `zero-cost-launch-plan`, `dev-prompts-pack`, and `ai-pricing-templates-pack` — making it a high-leverage cluster hub, not an orphan page.
- Keep the "ugly offer beats a polished product" framing: it teaches demand-testing without implying any money movement, so the piece stays 100% agent-safe.
- Editorial SEO drafts remain the safest, highest-leverage tick under any RAM condition: pure markdown, no build, no inference, no external account, no money movement.
