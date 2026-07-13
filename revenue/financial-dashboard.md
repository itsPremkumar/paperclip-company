# PREM AUTONOMOUS CO — REVENUE TRACKING DASHBOARD

**Owner:** Hermes CMO / Hermes Engineer · **Status:** live (tracking artifact)
**Cadence:** updated weekly (every Monday) · **Last updated:** 2026-07-13 (Week 0 / baseline)
**Window tracked:** Month 1 (30-day) projection, from launch 2026-07-12
**Source of truth for targets:** `revenue/30-day-zero-cost-launch-plan.md` + `revenue/monetization-brief-revenue-engine-v1.md`

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
| 2026-07-13 (W0) | 2 | $0 | 0 | 3 | untracked | 0 | 0 | baseline; launch 2026-07-12 |
| | | | | | | | | |

---

*This dashboard is the single source of truth for PRE-59. Edit it directly each week; no code changes needed.
Do not auto-publish founder-owned pricing/payment pages — that remains a Prem (founder) decision.*
