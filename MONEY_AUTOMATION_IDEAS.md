# 💰 Money-Earning Automation Idea Bank
*Derived from `itsPremkumar/ai-company` blueprint (100+ free OSS tools). Researched & validated 2026-07-13.*

> Principle: every pipeline below uses ONLY free / open-source / self-hostable tools from the
> `ai-company` blueprint. Compute (VPS/GPU) is the only bill. Income = sell outcomes, not "AI".

---

## 📊 Validated Market Signals (from live research, 2026)
| Signal | Source | Implication |
|--------|--------|-------------|
| n8n freelancers earn **$800–$2,500/project** + **$99–$149/mo retainer** | affstudio.org | Retainer model = recurring income |
| Solo w/ 5 retainers + 2 projects → **$3k–$5k/mo** in 6–12 mo | affstudio.org | Achievable solo target |
| Fiverr AI gigs grew **340% YoY** (Q1 2026) | betonai.net | Hottest category right now |
| Email-automation gig: **$350–$800** price, **$3–$8** AI cost = **95–99% margin** | betonai.net | Insane leverage |
| Workflow automation market: **$23.77B (2025) → $37.45B (2030)** | affstudio.org | Expanding TAM |
| **76%** of businesses want automation but lack in-house skills | affstudio.org | Huge demand gap |

---

## 🔧 The 12 Automation Pipelines

### 1. 🤖 Fiverr/Upwork AI-Automation Gig Factory  ⭐ TOP PICK
- **Tools:** n8n (automation) + OpenHands/Hermes (build) + your 31 ClawHub skills
- **Flow:** Scan Fiverr/Upwork for "automate X" requests → auto-generate the n8n workflow → deliver as done-for-you gig → upsell $99/mo maintenance retainer
- **Income:** $200–$2,000/gig, 95–99% margin. Target 5 retainers = $500/mo recurring + projects
- **Why now:** 340% YoY growth, race-to-bottom hasn't hit AI automations yet

### 2. 📧 Cold-Email Outreach Agency (Done-For-You)
- **Tools:** Mautic (email) + Listmonk (newsletters) + Postal (mail server) + n8n (sequencing)
- **Flow:** Client gives list → n8n enriches via API → Mautic sends sequences → track opens → report
- **Income:** $350–$800 setup + $99–$149/mo management per client
- **Margin:** Email infra self-hosted = near-zero cost

### 3. 📄 Proposal/Contract Generator Service
- **Tools:** DocAssemble (legal docs) + Hermes (drafting) + your `doc-extractor` skill
- **Flow:** Client fills form → DocAssemble generates contract/proposal → PDF delivered
- **Income:** $50–$300/doc, $5 AI cost. Sell as Fiverr gig "I will generate your legal contract"
- **Tools in blueprint:** `departments/15-hr-legal.md` → DocAssemble, Documenso

### 4. 🎬 Video-Generation Product (YOUR EDGE)
- **Tools:** Your `Automated-Video-Generator` (Remotion+Edge-TTS) + CogVideoX + your `ascii-video` skill
- **Flow:** Input: product URL / script → auto-generate promo video → deliver MP4
- **Income:** $100–$500/video. Sell on Fiverr "AI product video" + Gumroad templates
- **Blueprint ref:** `departments/18-video-generation.md` (your project is Product #1)

### 5. 🔍 Lead-Enrichment Micro-SaaS
- **Tools:** n8n + Firecrawl/Crawl4AI (crawling) + your `maps-cli`/`polymarket-cli` patterns
- **Flow:** User pastes company list → n8n enriches (web scrape + contact find) → CSV back
- **Income:** $0.10–$0.50/lead, or $29–$99/mo SaaS tier. Self-host = zero marginal cost
- **Blueprint ref:** `departments/05b-web-crawling.md`

### 6. 💬 AI Customer-Support Bot Deployer
- **Tools:** Chatwoot (helpdesk) + Hermes/OpenClaw (brain) + your `agent-sentinel`
- **Flow:** Client's FAQs → train bot → deploy on Chatwoot → monitor with agent-sentinel
- **Income:** $500–$1,500 setup + $99–$299/mo managed support
- **Blueprint ref:** `departments/13-customer-support.md`

### 7. 📊 Social-Content Auto-Poster (Agency)
- **Tools:** n8n + Mautic + your `youtube-content` + `gif-search` + `ascii-art-creator` skills
- **Flow:** Client topic → generate 30 days of posts (text+video+gif) → auto-schedule across platforms
- **Income:** $300–$800/mo per client for "done-for-you content"
- **Blueprint ref:** `departments/11-marketing.md`

### 8. 🧠 RAG Knowledge-Base Builder for SMBs
- **Tools:** Mem0 + pgvector + Graphiti + Docling (your `doc-extractor`) + Open WebUI
- **Flow:** Client dumps docs → build private RAG → embed in their site/support
- **Income:** $1,000–$3,000 project + $99–$199/mo hosting
- **Blueprint ref:** `departments/00-core-intelligence.md`, `22-self-evolving-core.md`

### 9. 🧪 Automated SEO/Audit Reporter
- **Tools:** your `codebase-inspection` + `secret-scanner` + `skill-lint` + n8n scheduler
- **Flow:** Subscribe URL → weekly scan (security/SEO/code quality) → PDF report via Stirling-PDF
- **Income:** $49–$199/mo per site. Pure recurring.
- **Blueprint ref:** `departments/09-qa-security.md` + Stirling-PDF (84.9k★)

### 10. 🌐 Niche Affiliate Site Farm (Autopilot)
- **Tools:** n8n + Agent-Reach (research) + Hermes (write) + your `web-research` + Medusa (ecom)
- **Flow:** Pick niche → Agent-Reach researches → Hermes drafts 50 articles → auto-publish → affiliate links
- **Income:** $200–$2,000/mo per matured site (ad + affiliate). Build 5–10.
- **Blueprint ref:** `departments/21-ecommerce.md`, `20-gap-fillers.md`

### 11. 🔄 Invoice/Bookkeeping Automation for Freelancers
- **Tools:** ERPNext (accounting) + n8n + InvoicePlane
- **Flow:** Freelancer connects bank/Stripe → n8n categorizes → ERPNext invoices → reminders
- **Income:** $29–$79/mo SaaS or $200 setup. Recurring.
- **Blueprint ref:** `departments/16-finance.md`

### 12. 🛡️ Security/Compliance Scanner as a Service
- **Tools:** your `secret-scanner` + Wazuh + Grafana + n8n
- **Flow:** Scan client repo/infra → Wazuh monitors → dashboard + alert → monthly report
- **Income:** $99–$499/mo per client. High-value, sticky.
- **Blueprint ref:** `departments/08-devops-cloud.md`, `09-qa-security.md`

---

## 🏆 Ranking (solo, $0 budget, fastest to first $)

| Rank | Pipeline | First $ in | Ceiling/mo | Effort | Recurring? |
|------|----------|-----------|-----------|--------|-----------|
| 1 | Fiverr AI-Automation Gig Factory | 1–2 wk | $3k–$12k | Low | Hybrid |
| 2 | Cold-Email Outreach Agency | 2–3 wk | $2k–$8k | Low | Yes |
| 3 | Video-Generation (your edge) | 1 wk | $1k–$5k | Med | Hybrid |
| 4 | AI Support Bot Deployer | 3–4 wk | $2k–$6k | Med | Yes |
| 5 | SEO/Audit Reporter | 1 wk | $500–$3k | Low | Yes |
| 6 | Lead-Enrichment Micro-SaaS | 4–6 wk | $1k–$10k | Med | Yes |
| 7 | RAG KB Builder | 3–4 wk | $2k–$8k | High | Yes |
| 8 | Social Content Auto-Poster | 2 wk | $1k–$4k | Med | Yes |
| 9 | Affiliate Site Farm | 2–3 mo | $1k–$10k | Med | Yes |
| 10 | Invoice Automation | 3 wk | $500–$3k | Med | Yes |
| 11 | Security Scanner SaaS | 4–6 wk | $1k–$15k | High | Yes |
| 12 | Proposal Generator | 1 wk | $500–$2k | Low | Hybrid |

---

## 🚀 Recommended 90-Day Launch (using what we already built)
- **Week 1–2:** Stand up Pipeline #1 (Fiverr gigs) using n8n + your 31 ClawHub skills. List 5 gigs.
- **Week 3–4:** Add Pipeline #3 (video gen — your Automated-Video-Generator) + #5 (SEO reporter).
- **Week 5–8:** Convert early clients to retainers ($99–$149/mo) → recurring base.
- **Week 9–12:** Launch Pipeline #9 (RAG KB) for highest-paying clients; automate delivery with the autonomy loop.

## 🔗 Synergy with existing repos
- `Hermes-Full-Autonomous-Company` = the engine (100 skills + 31 ClawHub tools + autonomy loop)
- `ai-company` = the blueprint/strategy
- This file = the **money map** connecting tools → income

> All tools free. Only cost = VPS (~$35–$75/mo). Margins 95%+. Start with Pipeline #1.
