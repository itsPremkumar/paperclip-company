# PREM AUTONOMOUS CO — REVENUE TRACKING DASHBOARD

**Owner:** Hermes CMO / Hermes Engineer · **Status:** live (tracking artifact)
**Cadence:** updated weekly (every Monday) · **Last updated:** 2026-07-14 (M4 projection + burn reconciliation added; PRE-89 milestone)
**Window tracked:** Month 1 (30-day) projection, from launch 2026-07-12 — **+ Month-2 projection, burn analysis & runway (PRE-73)** — **+ Month-3 projection, burn analysis & revenue tracking (PRE-75)** — **+ Month-4 projection, burn analysis & reconciliation (PRE-89)**
**Source of truth for targets:** `revenue/30-day-zero-cost-launch-plan.md` + `revenue/monetization-brief-revenue-engine-v1.md`
**Burn/runway source of truth:** live Paperclip API telemetry (`/companies/{id}/budgets/overview`, `/costs/summary`) pulled 2026-07-14T14:07Z (this milestone) and 2026-07-13T06:25Z (M3 baseline)

> This is a manual tracking doc. Each metric below has a **Target** (from strategy docs) and an
> **Actual** (entered weekly from real dashboards). Do NOT estimate — pull real numbers from the
> sources listed in "Where the numbers come from" and append a row to the Weekly Log.

---

## 1. Month 1 Projection (headline KPIs)

Targets are straight from the launch plan's 30-day KPIs and the monetization brief.

| Metric | Month-1 Target | Actual (Week 0) | Source |
|--------|---------------:|----------------:|--------|
| Calculator / landing visitors | 500 | 0 (not launched) | site analytics |
| Leads captured | 40 | 0 | email/CRM capture |
| Fit calls booked | 12 | 0 | calendar |
| Paid subscribers (starter/team) | 5 | 0 | Gumroad/Stripe |
| Build proposals sent | 3 | 0 | CRM |
| **MRR (month-end)** | **$245** | **$0** | billing |
| Burn / ad spend | $0 | $0 | finance |
| Articles published | 3+ | 3 | see §4 |
| Fiverr gigs live | TBD | 0 | see §5 |

> Note: the monetization brief's conservative month-1 line is **5 starter subscribers = $245/mo**.
> The launch plan's 30-day KPI block matches this. These are the same target stated two ways.

---

## 1b. Month-2 Projection, Burn Analysis & Runway (PRE-73)

> Added 2026-07-13. Targets come straight from `monetization-brief-revenue-engine-v1.md` §6
> (the published 90-day conservative plan). Actuals are pulled from **live Paperclip telemetry**
> (`/companies/3056c999-.../budgets/overview`, `/costs/summary`) as of 2026-07-13T04:39Z.
> Burn reflects the autonomous-company operating cost (model inference via OpenRouter), which is
> the only spend the system tracks today. Human-owned ad/tooling spend stays $0 by policy.

### 1b.1 Month-2 revenue projection (target vs. actual, to be filled weekly)

Month 2 window: 2026-08-12 → 2026-09-12 (30 days after the 2026-07-12 launch).
The strategy doc's conservative month-2 line is **15 subscribers + 1 build = ~$1,240/mo**.

| Metric | Month-1 target | Month-2 target | Month-2 actual (W0 baseline) | Source |
|--------|---------------:|---------------:|-----------------------------:|--------|
| Paid subscribers (starter/team) | 5 | 15 | 0 | Gumroad/Stripe |
| Build proposals closed | 0 | 1 | 0 | CRM |
| **MRR (month-2 end)** | **$245** | **~$1,240** | **$0** | billing |
| One-time build revenue | $0 | ~$990–$4,900 | $0 | billing |
| Affiliate/recurring add-ons | — | (reseller later) | $0 | dashboards |

> At the $49 starter price, 15 subscribers = $735/mo; the brief's ~$1,240/mo assumes a mix of
> starter/team tiers plus the one build. Track the blended figure weekly and reconcile to the brief.

### 1b.2 Burn analysis (live)

Pulled 2026-07-13T04:39Z from the Paperclip budgets/costs endpoints (company scope, calendar-month UTC window 2026-07-01 → 2026-08-01).

| Burn metric | Value | Notes |
|-------------|------:|-------|
| Recognized revenue (M-T-D) | **$0.00** | No revenue events recorded; pre-revenue stage |
| Gross burn (M-T-D) | **$70.00** (7,000¢) | 100% OpenRouter model inference (tencent/hy3:free), attributed to Hermes CMO |
| Monthly budget cap | **$500.00** (50,000¢) | hard-stop policy, calendar-month UTC |
| Budget remaining | **$430.00** (43,000¢) | 14% of cap used; 0 active incidents |
| Net burn (M-T-D) | **$70.00 / mo** | = gross burn (revenue is $0) |
| Burn rate (month-to-date run-rate) | **$6.02 / day** (~$183 / mo) | principled figure: $70 ÷ 11.6 days elapsed — **use this for planning** |
| Burn rate (process-uptime burst) | **$35.53 / hr** (~$852 / day) | artifact of a fresh process started 2026-07-12T13:10Z; **do NOT use for runway** |

> Two rates are shown deliberately. The month-to-date run-rate ($6.02/day) reflects real elapsed
> calendar time and is the planning figure. The process-uptime rate is a burst artifact (all spend
> landed in a ~2h window after the process booted) and overstates burn ~14x.

### 1b.3 Runway update

Runway has two valid definitions; only one is computable from system data today.

- **Runway to budget cap (computable): ~71 days** at the M-T-D pace of $6.02/day against the
  $430 remaining. Comfortably covers the 19.4 days left in the current billing window, so the
  $500 cap will **not** be breached this month. Even at the burst rate it would take ~0.5 day to
  hit the cap — but that rate is not expected to persist.
- **Runway to insolvency (NOT yet computable): undefined.** True runway = cash balance ÷ net burn.
  The company record has `cashBalanceCents: null` and no funding figure is stored anywhere in the
  system. **Gap to close (owner: founder/Prem):** supply a single `cash_balance` input (and any
  committed funding) before "runway in months" can be stated. Until then, runway is reported only
  relative to the budget cap.

### 1b.4 Net position & 2-month picture

| Snapshot | Value |
|----------|------:|
| Cumulative burn (launch → 2026-07-13) | $70.00 |
| Cumulative revenue (launch → 2026-07-13) | $0.00 |
| Net cash impact (launch → now) | **–$70.00** |
| Month-2 revenue target (added MRR) | +$1,240/mo |
| Projected burn if M-T-D pace holds | ~$183/mo |
| Projected net for Month 2 (if targets hit) | **≈ +$1,057** (first net-positive month) |

> Note: the only tracked cost is autonomous agent inference. Human-owned acquisition spend stays $0
> by policy (organic/product-led). If Prem later funds paid acquisition, that must be added to gross
> burn and the budget cap revisited.

---

## 1c. Month-3 Projection, Burn Analysis & Revenue Tracking (PRE-75)

> Added 2026-07-13. Targets come straight from `monetization-brief-revenue-engine-v1.md` §6
> (the published 90-day conservative plan): **Month 3 = 35 subs + 2 builds + 1 reseller ≈ $3,200/mo.**
> Actuals are pulled from **live Paperclip telemetry** (`/companies/3056c999-.../budgets/overview`,
> `/costs/summary`) as of 2026-07-13T06:25Z, plus the new revenue ledger
> (`/companies/{id}/revenue`, `/companies/{id}/revenue/summary`) which was **wired in for this
> milestone** (see §1c.3 — the route existed but was never mounted in `server/src/app.ts`).

### 1c.1 Month-3 revenue projection (target vs. actual, to be filled weekly)

Month 3 window: 2026-09-11 → 2026-10-11 (60 days after launch). The strategy doc's conservative
month-3 line is **35 subscribers + 2 builds + 1 reseller ≈ $3,200/mo**.

| Metric | Month-1 target | Month-2 target | Month-3 target | Month-3 actual (W0 baseline) | Source |
|--------|---------------:|---------------:|---------------:|-----------------------------:|--------|
| Paid subscribers (starter/team) | 5 | 15 | **35** | 0 | Gumroad/Stripe |
| Build proposals closed | 0 | 1 | **2** | 0 | CRM |
| Reseller / affiliate deals | — | (reseller later) | **1** | 0 | dashboards |
| **MRR (month-3 end)** | **$245** | **~$1,240** | **~$3,200** | **$0** | billing |
| One-time build revenue | $0 | ~$990–$4,900 | ~$1,980–$9,800 | $0 | billing |
| Affiliate/recurring add-ons | — | (reseller later) | ~$0–$640 | $0 | dashboards |

> At the $49 starter price, 35 subscribers = $1,715/mo. The brief's ~$3,200/mo assumes a starter/team
> mix plus 2 builds and the first reseller's recurring cut. Track the blended figure weekly and
> reconcile to the brief.

### 1c.2 Burn analysis (live)

Pulled 2026-07-13T06:25Z from the Paperclip budgets endpoint (company scope, calendar-month UTC
window 2026-07-01 → 2026-08-01). **Identical to the M2 baseline** — no spend has occurred since
the 2026-07-12 process boot; the only tracked cost remains autonomous model inference (OpenRouter).

| Burn metric | Value | Notes |
|-------------|------:|-------|
| Recognized revenue (M-T-D) | **$0.00** | No revenue events recorded; pre-revenue stage |
| Gross burn (M-T-D) | **$70.00** (7,000¢) | 100% OpenRouter model inference (tencent/hy3:free), attributed to Hermes CMO |
| Monthly budget cap | **$500.00** (50,000¢) | hard-stop policy, calendar-month UTC |
| Budget remaining | **$430.00** (43,000¢) | 14% of cap used; 0 active incidents |
| Net burn (M-T-D) | **$70.00 / mo** | = gross burn (revenue is $0) |
| Burn rate (month-to-date run-rate) | **$6.02 / day** (~$183 / mo) | principled figure: $70 ÷ 11.6 days elapsed — **use this for planning** |
| Burn rate (process-uptime burst) | **$35.53 / hr** (~$852 / day) | artifact of a fresh process started 2026-07-12T13:10Z; **do NOT use for runway** |

> Trajectory of burn rate across milestones (single telemetry source, no new spend):
> - M1/M2 baseline (2026-07-13T04:39Z): $70 MTD, $6.02/day run-rate.
> - M3 baseline (2026-07-13T06:25Z): **unchanged** — $70 MTD, $6.02/day. The agent fleet is holding
>   a flat, sub-cap burn; the $500/mo cap is safe with $430 remaining and no ad spend by policy.

### 1c.3 Revenue tracking — actual payouts (Gumroad / GitHub Sponsors / Medium Partner)

This is the new tracking layer for M3. A revenue ledger route existed in `server/src/routes/revenue.ts`
but was **never mounted** — revenue could not be recorded or read via the API. PRE-75 wired it into
`server/src/app.ts` (`api.use(revenueRoutes(db))`) so actual payouts can now be tracked.

**Live pull (2026-07-13T06:25Z):**

```
GET /companies/3056c999-.../revenue/summary  →  entryCount: 0, byCurrency: {}, totalGross: 0, currency: "USD"
```

| Payout channel | Credentials / account | Status | Recorded (USD) | Source of truth |
|----------------|----------------------|--------|---------------:|-----------------|
| Gumroad | founder-owned (PRE-52, human gate) | 2 free products live; 0 paid sales | $0 | `revenue` ledger + Gumroad dashboard |
| GitHub Sponsors | `github.com/sponsors/itsPremkumar` (PRE-57, human gate) | not enabled | $0 | `revenue` ledger + Sponsors dashboard |
| Medium Partner Program | not enrolled | not started | $0 | `revenue` ledger + Medium dashboard |

> **Recording workflow (from now on):** when a real payout lands, POST to
> `POST /companies/{id}/revenue` with `{source:"gumroad"|"github_sponsors"|"medium", gross:<cents/usd>, currency:"USD", memo}`.
> The dashboard's weekly log (§8) and this table are then reconciled against the ledger `summary`.

### 1c.4 Net position & 3-month picture

| Snapshot | Value |
|----------|------:|
| Cumulative burn (launch → 2026-07-13) | $70.00 |
| Cumulative revenue (launch → 2026-07-13) | $0.00 |
| Net cash impact (launch → now) | **–$70.00** |
| Month-3 revenue target (added MRR + builds + reseller) | +$3,200/mo |
| Projected burn if M-T-D pace holds | ~$183/mo |
| Projected net for Month 3 (if targets hit) | **≈ +$3,017** (deeply net-positive month) |
| Breakeven point | burn ($183/mo) is covered once ≈ 4 subscribers (@$49) are retained — reached the moment M2's 15-subscriber target is touched |

> The only tracked cost is autonomous agent inference; human-owned acquisition spend stays $0 by
> policy. The dominant risk to the M3 target is **not burn** — it is the founder gates on Gumroad
> (PRE-52) and GitHub Sponsors (PRE-57) that keep the paid storefronts from going live. Unblock those
> and the revenue engine can publish + track autonomously.

---

## 1d. Month-4 Projection, Burn Analysis & Reconciliation ("Revenue dashboard M4" issue)

> Added 2026-07-14. The monetization brief (`revenue/monetization-brief-revenue-engine-v1.md` §6)
> gives explicit conservative targets through **Month 3** only (35 subs + 2 builds + 1 reseller ≈
> $3,200/mo). Month 4 has no published figure, so it is **derived** here from the brief's own
> trajectory — *not invented* — using a transparent, stated method. Live telemetry was re-pulled
> for this milestone (2026-07-14T14:07Z) and reconciled against the M3 baseline (issue
> "Revenue dashboard M3").

### 1d.1 Deriving the M4 target (method + result)

The brief's month-over-month subscriber ramp is **5 → 15 → 35**. The incremental adds are
+10 (M1→M2) then +20 (M2→M3) — a ~2x step each month. Two defensible continuations:

- **Linear-of-increments (lower bound):** hold the last increment (+20) → **55 subs**.
- **Geometric-of-increments (upper bound):** double the last increment (+40) → **75 subs**.
- **Blended M4 planning figure:** **~60 subscribers** (midpoint, conservative vs the geometric case).

Carrying the brief's revenue mix forward (starter/team blend that produced ~$3,200 at 35 subs,
plus builds + reseller recurring cut), M4 target is built as:

| Component | M4 planning figure | Rationale |
|-----------|-------------------:|-----------|
| Subscribers (blended) | 60 | midpoint of 55–75 derived ramp |
| Added MRR from subs | +~$2,400 vs M3 (~$5,600/mo gross) | $3,200 ÷ 35 × 60 ≈ $5,486; reseller + 2nd build tail adds ~$115 |
| One-time builds closed (cumulative) | 3 | +1 build in M4 (M3 was 2) |
| Reseller / affiliate deals | 2 | +1 reseller (M3 was 1) → adds ~$640/mo recurring |
| **M4 target MRR (month-end)** | **≈ $5,600/mo** | conservative blend of the two ramp methods |
| Cumulative build revenue (M1–M4) | ~$2,970–$14,700 | 3 builds × $990–$4,900 |

> This is explicitly a **projection**, not a committed target. It is flagged as the agent-derived
> M4 line so the founder can ratify or revise it. If Prem prefers the brief's geometric method,
> the upper bound is ~$7,400/mo at 75 subs; if linear, ~$5,100/mo at 55 subs.

### 1d.2 Month-4 revenue projection (target vs. actual, to be filled weekly)

Month 4 window: 2026-10-11 → 2026-11-11 (90 days after launch). Note the brief's 90-day target
window closes *inside* M4; M4 is therefore the "steady-state maturity" month.

| Metric | M1 | M2 | M3 | M4 target (derived) | M4 actual (W0 baseline) | Source |
|--------|---:|---:|---:|---------------------:|-------------------------:|--------|
| Paid subscribers (starter/team) | 5 | 15 | 35 | **~60** | 0 | Gumroad/Stripe |
| Builds closed (cumulative) | 0 | 1 | 2 | **3** | 0 | CRM |
| Reseller / affiliate deals | — | (later) | 1 | **2** | 0 | dashboards |
| **MRR (month-end)** | $245 | ~$1,240 | ~$3,200 | **≈ $5,600** | $0 | billing |
| Cumulative build revenue | $0 | ~$990–$4,900 | ~$1,980–$9,800 | ~$2,970–$14,700 | $0 | billing |
| Affiliate/recurring add-ons | — | — | ~$0–$640 | ~$640 | $0 | dashboards |

### 1d.3 Burn analysis (live — re-pull 2026-07-14T14:07Z)

Reconciled against the M3 baseline (2026-07-13T06:25Z). Same single telemetry source, same
billing window (2026-07-01 → 2026-08-01 UTC).

| Burn metric | M3 baseline (07-13) | M4 pull (07-14) | Δ | Notes |
|-------------|--------------------:|----------------:|--:|-------|
| Recognized revenue (M-T-D) | $0.00 | **$0.00** | — | still pre-revenue |
| Gross burn (M-T-D) | $70.00 (7,000¢) | **$70.00 (7,000¢)** | $0 | 100% OpenRouter inference (tencent/hy3:free) |
| Monthly budget cap | $500.00 | $500.00 | — | hard-stop, calendar-month UTC |
| Budget remaining | $430.00 | **$430.00** | $0 | 14% of cap used |
| Net burn (M-T-D) | $70.00 | **$70.00** | — | = gross burn (revenue $0) |
| Burn rate (M-T-D run-rate) | $6.02/day (~$183/mo) | **$6.02/day** | — | $70 ÷ 11.6 days elapsed; planning figure |

> **Reconciliation result:** burn is **flat** across M2→M3→M4 pulls — no new spend has occurred
> since the 2026-07-12 process boot. The $500/mo cap is safe (14% used, $430 remaining). The
> process-uptime burst artifact ($35.53/hr) remains excluded from runway math. The fleet is holding
> a sub-cap, zero-ad-spend burn by policy.

### 1d.4 Reconciliation vs. actual income-engine inventory

The income-engine (`money/INCOME_DASHBOARD.md`, regenerated 2026-07-14) reports a *separate*
addressable inventory: **74 ready-to-sell packages across 18 pipelines**, combined one-time value
$47,841, realistic 90-day target **$3,000–$8,000/mo**. Reconciling the two views:

| Lens | Figure | Status | Gap / note |
|------|-------:|--------|------------|
| Service-subscription model (brief) — M4 MRR target | ≈ $5,600/mo | projection | gated on Gumroad/Sponsors founder publish |
| Income-engine package inventory — 90-day realistic | $3,000–$8,000/mo | projection | gated on Fiverr/Upwork founder account setup |
| Digital-product catalog (product-catalog.json) | 12 products, 9 zips built | ready | 0 published (founder Gumroad gate) |
| **Actual realized revenue (live ledger)** | **$0.00** | confirmed | matches both models' pre-revenue state |

> **Key reconciliation insight:** both revenue models show strong *probability-weighted* upside
> ($3k–$8k/mo) but **$0 realized**, and the blocker is identical in both: the founder-owned publish
> gates (Gumroad PRE-52, GitHub Sponsors PRE-57, Fiverr PRE-58, Medium PRE-54). Burn is not the
> risk — distribution is. Unblock the founder gates and both engines begin recording real payouts
> against this ledger.

### 1d.5 Net position & 4-month picture

| Snapshot | Value |
|----------|------:|
| Cumulative burn (launch → 2026-07-14) | $70.00 |
| Cumulative revenue (launch → 2026-07-14) | $0.00 |
| Net cash impact (launch → now) | **–$70.00** |
| Month-4 revenue target (added MRR + builds + reseller) | +$5,600/mo |
| Projected burn if M-T-D pace holds | ~$183/mo |
| Projected net for Month 4 (if targets hit) | **≈ +$5,417** (deeply net-positive; covers 31x the burn) |
| Breakeven status | already covered at ~4 retained subscribers; M4 target is ~15x breakeven |

---

## 2. Products Published

Real inventory as of 2026-07-13 (from `digital-products/product-catalog.json` and
`income-engine/gumroad/.used_products.json`).

**Cataloged & ready:** 10 digital products.
**Gumroad published (live):** 2.
**Gumroad listings drafted (not yet published):** 5 more.

| # | Product | Price (USD) | Catalog status | Gumroad status |
|---|---------|------------:|----------------|----------------|
| 1 | 50 Viral Short-Form Video Scripts | 12 | ready | drafted |
| 2 | Autonomous AI Agent Operations Playbook | 29 | ready | drafted |
| 3 | Remotion Short-Form Video Template Pack | 19 | ready | drafted |
| 4 | AI-Powered Business Monetization Kit | 29 | ready | drafted |
| 5 | Cold Outreach & Lead Generation Pack | 15 | ready | drafted |
| 6 | Free Job Board Outreach Mastery Guide | 12 | ready | drafted |
| 7 | AI Agent Service Catalog + Pricing Templates | 19 | ready | drafted |
| 8 | 30-Day Zero-Cost Business Launch Plan | 9 | ready | drafted |
| 9 | AI Agent Capability Manifest Toolkit | 14 | ready | drafted |
| 10 | 150 Developer Productivity Prompts | 14 | ready | drafted |
| — | ai-agent-roi-calculator (lead magnet / product) | 0/free | — | **published** |
| — | n8n-starter-workflow-pack | — | — | **published** |

**Total published products:** 2 · **Total cataloged:** 10 · **Bundle price:** $109 (35% saving vs $167 separately).

---

## 3. Sales by Product (revenue)

Baseline = 0. Fill in weekly from Gumroad + Stripe dashboards.

| Product | Units sold | Revenue (USD) | Notes |
|---------|-----------:|--------------:|-------|
| 50 Viral Short-Form Video Scripts | 0 | 0 | not live |
| Autonomous AI Agent Operations Playbook | 0 | 0 | not live |
| Remotion Short-Form Video Template Pack | 0 | 0 | not live |
| AI-Powered Business Monetization Kit | 0 | 0 | not live |
| Cold Outreach & Lead Generation Pack | 0 | 0 | not live |
| Free Job Board Outreach Mastery Guide | 0 | 0 | not live |
| AI Agent Service Catalog + Pricing Templates | 0 | 0 | not live |
| 30-Day Zero-Cost Business Launch Plan | 0 | 0 | not live |
| AI Agent Capability Manifest Toolkit | 0 | 0 | not live |
| n8n-starter-workflow-pack | 0 | 0 | live, no sales yet |
| ai-agent-roi-calculator | 0 | 0 | live, free lead magnet |
| **Total** | **0** | **$0** | — |

**Subscription MRR (service catalog plans):** $0 (no subscribers yet — see §1 paid-subscriber target).

---

## 4. Articles Published & Views

Real articles on disk as of 2026-07-13:

| # | Article | Location | Views | Source |
|---|---------|----------|------:|--------|
| 1 | Best AI Agents for Small Business Automation | `income-engine/content/` | 0 (untracked) | blog |
| 2 | No-Code Automation Tools: n8n, Make, Zapier | `income-engine/content/` | 0 (untracked) | blog |
| 3 | How to Run an AI Company at Zero Budget | `revenue/blog/` | 0 (untracked) | blog |

**Articles published:** 3 · **Total views:** not yet tracked (no analytics connected to the site).
> Action: connect site analytics (GitHub Pages / Vercel / Plausible) and record weekly view counts here.

---

## 5. Fiverr Gigs Live

**Gigs live:** 0 — no Fiverr assets exist anywhere in the repo (no `fiverr` references found).
**Plan:** this is a future channel. Create gigs once the first 2–3 digital products have proof of sale.
Track the count here each week once gigs go live.

| Gig title | Price (USD) | Status | Orders |
|-----------|------------:|--------|-------:|

---

## 6. Leads Generated

**Leads captured:** 0 — the ROI calculator lead magnet exists (`income-engine/gumroad/products/ai-agent-roi-calculator`)
but is not yet wired to an email-capture + CRM, so no leads are recorded.

| Week | Leads (calculator) | Outreach replies | Fit calls booked | Converted to paid |
|------|-------------------:|-----------------:|-----------------:|------------------:|
| W0   | 0 | 0 | 0 | 0 |

---

## 7. Where the numbers come from (pull weekly)

- **Product publish status:** `digital-products/product-catalog.json` + `income-engine/gumroad/.used_products.json`.
- **Sales / revenue / MRR:** Gumroad dashboard + Stripe/Razorpay (founder-managed accounts).
- **Article views:** site analytics (connect if missing).
- **Fiverr gigs / orders:** Fiverr seller dashboard.
- **Leads:** email-capture backend + CRM behind the ROI calculator.

---

## 8. Weekly Log

Append a row every Monday. Keep the latest on top.

| Week of | Products live | MRR | Units sold | Articles | Views | Fiverr gigs | Leads | Notes |
|---------|--------------:|----:|-----------:|---------:|------:|------------:|------:|-------|
| 2026-07-14 (M4 baseline) | 2 | $0 | 0 | 3 | untracked | 0 | 0 | "Revenue dashboard M4": M4 projection + burn reconciliation added; re-pulled live telemetry (burn flat $70/$500); derived M4 target ≈ $5,600/mo; reconciled vs income-engine 74-pkg inventory |
| 2026-07-13 (W0) | 2 | $0 | 0 | 3 | untracked | 0 | 0 | baseline; launch 2026-07-12 |
| 2026-07-13 (W1) | 0 | $0 | 0 | 0 | untracked | 0 | 0 | cataloged 11 products incl. agent-sentinel bundle (#11) |
| 2026-07-13 (M3 baseline) | 2 | $0 | 0 | 3 | untracked | 0 | 0 | PRE-75: M3 projection + burn added; revenue ledger route wired into API (app.ts) |

---

*This dashboard is the single source of truth for PRE-59 (Month-1), PRE-73 (Month-2 projection,
burn analysis & runway), PRE-75 (Month-3 projection, burn analysis & revenue tracking), and
"Revenue dashboard M4" (Month-4 projection, burn analysis & reconciliation). Edit it
directly each week; no code changes needed.
Do not auto-publish founder-owned pricing/payment pages — that remains a Prem (founder) decision.*
