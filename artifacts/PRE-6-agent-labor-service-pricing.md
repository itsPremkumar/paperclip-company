# PRE-6 — Agent-Labor Service Definition + Pricing Tiers

**Company:** Prem Autonomous Co (autonomous AI-agent company)
**Parent:** PRE-3 Zero-Investment Monetization Plan (next-step #2)
**Constraint:** Marginal cost ≈ $0 (agent compute + founder time only; no paid APIs, no ad spend, no hired labor)
**Prepared by:** Hermes Engineer (agent 9eed5712) · Run fc50ab48 (updated by run 98457eae)
**Owner for go-live decisions:** Founder (Premkumar M)

---

## 1. The Service: "Agent Labor" (productized)

**One-line pitch:** Hire an autonomous AI engineering team that ships real work — code, content, media, research, and automation — on a flat monthly retainer or per-task basis, at a fraction of a human contractor's cost.

### 1.1 What we actually sell
We do NOT sell "access to an AI." We sell **completed, reviewed deliverables**. The unit of value is a shipped work product, not tokens or hours.

Concrete, repeatable deliverable types (each has ~0 marginal cost — agent compute only):

| Deliverable | Example | Typical turnaround |
|---|---|---|
| Code task | Bug fix, small feature, script, refactor, test suite | 1–3 days |
| Automation | Web scraper, data pipeline, cron/report bot, integration glue | 2–5 days |
| Generated media | Narrated explainer/short-form video via AVG pipeline | 1–2 days |
| Content | Technical blog post, docs, README, landing copy | 1 day |
| Research | Market/competitor scan, tech due-diligence brief | 1–2 days |

### 1.2 Why the margin is ~100%
- Agent compute is the only recurring input; everything runs on free/OSS tooling the company already owns (Paperclip runtime, Automated-Video-Generator, free stock/CC0 media, Edge-TTS).
- No inventory, no per-seat SaaS, no cloud render bills at the volumes a free tier covers.
- Founder time is the scarce resource — so pricing and tier limits are set to protect founder review capacity, not compute.

### 1.3 Positioning vs. alternatives
- vs. a freelancer: cheaper, faster first draft, no scheduling friction, always-on.
- vs. a raw LLM subscription: we deliver finished, reviewed output — the buyer doesn't prompt-engineer or QA.
- vs. an agency: no minimums, no onboarding fees, transparent flat pricing.

---

## 2. Pricing Tiers (free-tier-friendly)

Design principles:
1. **Free tier is a real, useful product** — it's the top of the funnel and the living demo, not a crippled teaser.
2. **Price on founder-review capacity**, not compute. Limits = number of deliverables the founder can realistically review per period.
3. **Land-and-expand:** free → single paid task → monthly retainer.
4. All prices are launch anchors; the founder confirms the floor (see §4).

### Tier 0 — Free / Community ($0)
- **1 small deliverable per month** (e.g., one bug fix, one short script, one 30–60s video, or one blog post).
- Public-friendly: output may be showcased publicly (portfolio/lead-gen) unless the requester opts out.
- Community support only (async, best-effort).
- **Purpose:** proof-of-work funnel + samples for PRE-7. Converts to paid on the 2nd request.

### Tier 1 — Starter (pay-per-task, ~$15–40 / task)
- **One-off deliverables, no subscription.** Buyer picks from the §1.1 catalog.
- Price banded by scope: micro ($15) / standard ($25) / complex ($40).
- 1 revision round included.
- Private by default.
- **Purpose:** lowest-friction first purchase; captures buyers not ready for a retainer.

### Tier 2 — Retainer / Pro (~$99 / month)
- **Up to 8 deliverables per month** (rolls the per-task catalog into a flat rate; effective ~$12/deliverable).
- Priority queue, 2 revision rounds each.
- Private by default, light SLA (first draft within 3 business days).
- **Purpose:** predictable recurring revenue; the core offer.

### Tier 3 — Team / Scale (~$299 / month)
- **Up to 30 deliverables per month** across mixed types (effective ~$10/deliverable).
- Dedicated intake channel, fastest queue priority, 3 revision rounds.
- Optional monthly roadmap/standup summary.
- **Purpose:** power users / small businesses treating the agent as an outsourced team. Upper bound is set by founder review throughput — raise only when review is further automated.

### Add-ons (any tier)
- Rush (same-day, where feasible): +50% of task price.
- Public showcase opt-out on free/Starter: small flat fee or auto-included in Pro+.

---

## 3. Unit Economics (illustrative, per month)

| Tier | Price | Deliverables | Marginal cost | Gross margin |
|---|---|---|---|---|
| Free | $0 | 1 | ~$0 (compute) | funnel / lead-gen |
| Starter | $25 avg | 1 | ~$0 | ~100% |
| Pro | $99 | up to 8 | ~$0 | ~100% |
| Scale | $299 | up to 30 | ~$0 | ~100% |

The real constraint is **founder review hours**, not cash cost. Tier caps exist so quality/liveness stays high while free tiers are outgrown.

---

## 4. Founder Pricing Gates — Status

> Updated after CEO review of the concrete go-live pricing (PRE-26). The conceptual tier framework in §2 remains the umbrella; the **approved go-live pricing is the 6-packaged-team model** in `revenue/public-pricing-sheet.md` + `revenue/service-catalog-6-agent-teams.md`.

1. **Floor price — RESOLVED (CEO).** The approved public range is **$129–$499/mo + $990 custom** (Content Machine $149 → Autonomous Team $499), sitting inside the COMPANY_PLAN $49–$499 band. The §2 "Agent Labor" $15 Starter micro-floor is a *lower experimental band*, not the go-live floor. Do not publish the $15 floor as the public offer.
2. **Free-tier public showcase — OPEN.** Still needs founder call: auto-showcase free-tier output publicly (opt-out) for lead-gen, or keep free output private by default. (Guardrail context: PRE-8 outreach relies on samples.)
3. **Primary channel at launch — RESOLVED (CEO).** Lead with the 6 packaged teams published via the PRE-5 showcase repo / LinkedIn, not the per-task Starter framing.
4. **Deliverable catalog scope — RESOLVED (CEO).** Launch with the 6 packaged agent teams (Content Machine, Ops Autopilot, Lead Engine, Support Agent, Founder's CoS, Build-It Custom) rather than the broader five-type §1.1 catalog.

**Remaining human gate (NOT auto-crossed by any agent):** Final publication of any pricing to a public site is a **founder (Prem) decision** — a commercial commitment. Agents may draft and stage pricing pages, then stop and request founder publish approval. Publications must NOT be auto-published.

---

## 5. Recommended Next Steps (delegatable)
- Publish tier table on the showcase repo / LinkedIn (PRE-5).
- Use the free tier to seed the first 3 sample videos (PRE-7).
- Reference this price list in free-board outreach (PRE-8).

---

## 6. Compliance Guardrails Applied (recovered from cancelled PRE-26)

Two doc fixes were required by CEO review before the pricing page goes live. They were recovered and applied to `revenue/public-pricing-sheet.md` (PRE-26 was cancelled, so this executor re-applied them):

1. **Reseller reference fixed.** Line 22 now references the real published doc `revenue/reseller-&-affiliate-program.md` (was a broken `partnerships.md` link). 25% recurring commission is within the plan's allowed 20–30%.
2. **Founder-owned payment note added.** The Payment section now carries: *"Payment is processed via founder-managed Stripe / Razorpay accounts. Agents draft invoices and pricing only — no agent collects or holds funds. Publication of this pricing to any public site is a founder (Prem) decision; do not auto-publish."*

These satisfy 2 of the 3 PRE-26 acceptance criteria. The third (draft staged but not publicly published) is enforced by process: nothing was published; only workspace files were edited.
