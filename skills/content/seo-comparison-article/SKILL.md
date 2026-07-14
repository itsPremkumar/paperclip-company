---
name: seo-comparison-article
category: content
description: >-
  Repeatable skill for authoring evergreen "X vs Y vs Z" comparison articles
  into revenue/blog/ that the income-engine blog generator picks up
  automatically. Scan existing slugs for a missing comparison axis, reuse the
  canonical front-matter schema, then ship a 30-second verdict + side-by-side
  table + cross-links + product funnel. Zero human gate, no money movement.
state: active
---

# Author an Evergreen Comparison SEO Article

## When to use
You want continuous, low-risk, compounding SEO work that fills the content
funnel between heavier ticks. The autonomy loop has run this pattern nine times
(n8n vs Make vs Zapier, LangGraph vs AutoGen vs CrewAI vs n8n, ChatGPT vs Claude
vs Gemini vs Llama, and others). It is the safest agent-executable content task:
it needs no model inference, no money, and no human approval.

## Inputs
- `revenue/blog/*.md` — the existing article corpus (the source of truth for
  what axes are already covered).
- The canonical front-matter schema (below) — the blog generator reads it to
  render the post, so matching it exactly is what makes the file publishable
  without manual edits.
- A list of paid products to funnel to (see `income-engine/gumroad/products/`
  and the catalog): e.g. `monetization-kit`, `zero-to-10k-ai-agents`,
  `ai-content-machine-blueprint`.

## Steps
1. **Scan for a missing comparison axis.** List existing slugs and group them by
   axis type. The loop has covered three axis families so far:
   - *Tools*: `n8n-vs-make-vs-zapier-2026`
   - *Frameworks*: `langgraph-vs-autogen-vs-crewai-vs-n8n-2026`
   - *Models*: `chatgpt-vs-claude-vs-gemini-vs-llama-2026`
   Pick an UNSATISFIED axis — e.g. a *vertical* ("AI agents for real estate vs
   healthcare vs e-commerce"), a *medium/channel* ("faceless YouTube vs TikTok
   vs newsletter"), or a next tool/framework/model quartet. Prefer the gap with
   the highest search volume and lowest existing competition in the corpus.
2. **Reuse the canonical front-matter block verbatim** (YAML between `---`
   fences). Required keys, in order:
   ```yaml
   ---
   title: "X vs Y vs Z: <question> in 2026"
   description: "<no-hype one-liner with the contenders and the payoff>"
   slug: x-vs-y-vs-z-2026
   date: "2026-07-14"
   niche: "<contender family + audience>"
   tags: ["x", "y", "z", "automation", "comparison"]
   author: "Prem Autonomous Co — Hermes Agent Team"
   ---
   ```
   The `slug` MUST equal the filename stem or the generator mis-links it.
3. **Open with a 30-second verdict.** 2–4 bullets, one per contender:
   "Pick X if … ; Pick Y if … ; Pick Z if …". This is the snippet search
   engines and LLMs lift for AEO/GEO answers.
4. **Add a side-by-side comparison table** (markdown `|` table) across the
   dimensions buyers actually care about: price/free tier, self-hosting, ease,
   best-fit use case, lock-in risk. Keep it skimmable.
5. **Cross-link 6–13 existing articles** using relative `./slug.md` links in
   prose. Each link should be contextually motivated ("this pairs with our
   <topic> guide"), not a footer dump. Cross-links are what compound the
   funnel — never ship a standalone island.
6. **Funnel to at least one paid product** near the end ("if you want the
   done-for-you version, see <product>"). Name the product; do not embed buy
   links or price (publish/payout is human-gated).
7. **Save as** `revenue/blog/<slug>.md` and verify the file name == `slug`.
8. **Scan for secrets** before any commit (see guardrails).

## Guardrails
- Agent writes the article only. **Gumroad publish, pricing, and payouts stay
  HUMAN-GATED** (Constitution S0) — the loop never lists or moves money, and
  must never embed a checkout/price link in the body.
- Keep the front-matter schema EXACTLY as specified; a drifted key breaks the
  generator's parser and the post goes unpublished silently.
- No secrets, API keys, `.env`, or credentials ever belong in a blog article.
- Prefer extending the funnel (cross-links + product funnel) over inventing a
  brand-new angle — consistency beats novelty for SEO.

## Why this matters
Comparison queries ("X vs Y") are high-intent, high-volume, and low-competition
relative to broad "how to" content. Because the loop already owns a deep,
cross-linked corpus, each new comparison article inherits link equity and routes
readers toward (human-gated) products. It is pure text, costs zero to produce,
and is fully reversible — the ideal autonomous-tick task.

## See also
- `skills/automation/package-digital-product.md` (turn the funnel into priced assets)
- `revenue/blog/n8n-vs-make-vs-zapier-2026.md` (reference implementation)
- `revenue/blog/chatgpt-vs-claude-vs-gemini-vs-llama-2026.md` (model-axis example)
- `knowledge-base/lessons-learned.md` (TICK-13/TICK-14/TICK-15 derivations)
