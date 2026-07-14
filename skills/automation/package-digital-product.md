---
name: package-digital-product
category: automation
description: >-
  Repeatable skill for turning existing scattered content (articles, docs,
  threads, notes) into a sellable zero-cost digital product — Markdown + CSV +
  JSON assets wrapped with a README and license, registered in the catalog.
state: active
---

# Package a Digital Product From Existing Content

## When to use
You already have value sitting in repo docs, blog drafts, or notes, and want a
shippable product without authoring anything new. The autonomy loop ran this
eight times in one session (cold-outreach-pack, ai-pricing-templates-pack,
zero-cost-launch-plan, agent-ops-playbook, remotion-templates, monetization-kit,
job-board-guide, dev-prompts-pack) — it is the highest-leverage, lowest-risk
revenue task an agent can do solo.

## Inputs
- Source content already in the repo (a blog article, a README, a notes file).
- `product-catalog.json` (the registry of catalog products).
- `income-engine/gumroad/products/` as the output location.

## Steps
1. **Pick a source.** Find one existing asset with clear, standalone value
   (e.g. an outreach article → cold-outreach-pack).
2. **Carve the product.** Split the source into consumable units: a main
   `README.md`, plus supporting files (`.csv`, `.json`, `.yaml`, `.md`).
   Don't invent net-new content — reorganize and polish what exists.
3. **Author the bonuses only if promised.** If the catalog entry advertises
   bonus templates (AGENTS.md, .env.example, configs), write those — they are
   the differentiator. Keep them minimal and correct.
4. **Add a README + LICENSE.** The README explains what's included, who it's
   for, and how to use it. License = the commercial terms.
5. **Drop it in** `income-engine/gumroad/products/<product-slug>/`.
6. **Register it** in `product-catalog.json` (slug, title, price tier, status).
7. **Scan for secrets** before any commit — never ship `.env`, keys, or
   credentials inside a product bundle.

## Guardrails
- Agent writes the asset and the catalog entry. The **Gumroad publish** and any
  price approval stay HUMAN-GATED (Constitution S0) — the loop never lists or
  moves money.
- Keep bundles text-only and tiny; no binary blobs, no external fetches.
- If a promised bonus can't be produced correctly, drop the promise rather than
  ship a broken template.

## Why this matters
It converts sunk content cost into a priced asset at ~$0 marginal effort, and
it's fully reversible (just another folder + a JSON line). It's the safest
revenue-producing action an autonomous agent can take, which is exactly why the
loop leans on it between heavier ticks.

## See also
- `skills/automation/low-ram-self-protect.md` (when to defer heavy packaging)
- `revenue/blog/zero-cost-digital-products-that-sell.md` (the product thesis)
