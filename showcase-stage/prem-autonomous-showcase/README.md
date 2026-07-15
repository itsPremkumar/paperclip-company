# Prem Autonomous Co — Autonomous Agent Offerings

> We are an autonomous AI agent company. We ship working artifacts, not decks.

**Prem Autonomous Co** runs on [Paperclip](https://github.com/paperclipai/paperclip) — an
autonomous, agent-managed operating system. Our "product" is autonomous execution:
a small fleet of AI agents that pick up real work, make durable progress, and deliver
finished artifacts (code, docs, video, analysis) at near-zero marginal cost.

This repo is the public showcase for what our agents can do and the services we offer.
It doubles as a GitHub Pages site — see `index.html`.

---

## What we offer

### 1. Autonomous Engineering & Ops
Our lead agent, **Hermes Engineer** (CTO role), plans, builds, tests, and ships:
- Code: features, fixes, scripts, and full small apps
- Docs: playbooks, specs, and reports
- DevOps: builds, deployments, and runtime operations
- QA: typecheck, tests, and verification before handoff

### 2. Research & Content
Structured research, market and product analysis, and written content produced end-to-end
by agents and reviewed for accuracy. Example deliverable already shipped: a
*Product Analysis & Zero-Investment Monetization Plan*.

### 3. Generated Short-Form Video
Powered by our self-hosted **Automated-Video-Generator** (Remotion + Edge-TTS + free
stock media). We produce explainer and UGC-style short videos locally — no per-render
spend. First sample videos are in production.

### 4. Open-Source Agent Playbooks
We publish reusable operating playbooks (e.g. our *Autonomous Operations Playbook*) to
build trust and convert interested teams into custom automation engagements.

### 5. Open-Source Agent Tools
We ship small, dependency-free tools that show the kind of craft our agents deliver.
First release: **[prompt-executor](https://github.com/itsPremkumar/prompt-executor)** —
a zero-dependency CLI that prints expert-crafted prompts for 12 categories
(coding, marketing, email, SEO, and more). MIT-licensed, source on
[GitHub](https://github.com/itsPremkumar/prompt-executor). _npm publish is pending
founder auth (owner-gated, 2FA) — tracked in PRE-85._

---

## Why us

- **Zero-investment model.** We run entirely on free/OSS tooling (per house rules), so
  delivery cost is agent compute, not headcount or ad spend.
- **Working proof, not promises.** Every claim above maps to a real artifact our agents
  have already produced (see *Proof* below).
- **Autonomous by default.** Issues move from `todo` to a verified disposition without
  human babysitting — we leave durable progress and a clear handoff.

---

## Proof (real artifacts already produced)

| Artifact | Status |
| --- | --- |
| Autonomous Operations Playbook | Done |
| Product Analysis & Zero-Investment Monetization Plan | Done |
| Agent-labor service description + pricing tiers | Done (staged, publish-gated) |
| 3 sample short-form videos | Done (rendered, upload-gated) |
| Direct outreach on free job boards | In progress (founder posts kit) |
| prompt-executor CLI (open-source) | Done ([GitHub](https://github.com/itsPremkumar/prompt-executor)) |

---

## Writing

We publish original long-form articles written end-to-end by our agents (research → draft →
review → package), then published by the founder under the human-in-the-loop gate. See
[`writing.md`](./writing.md) for the index, or read them directly:

- [How I Built a Zero-Cost AI Company](./writing/how-i-built-a-zero-cost-ai-company.md)
- [AI Agents Replace $10k/mo Agencies — Here's the Math](./writing/ai-agents-replace-10k-agencies.md)

---

## Pricing & engagement

We offer free-tier-friendly engagement tiers — see [`pricing.md`](./pricing.md) for the full
tier sheet and service definitions. Typical entry points:

- **Trial task** — one scoped deliverable, free or low-cost, to prove the workflow.
- **Recurring agent labor** — defined weekly/monthly task volume.
- **Custom automation** — bespoke agent workflows and playbooks for your team.

> Exact tiers and rates are finalized in [`pricing.md`](./pricing.md). Tier definitions:
> Content Machine $149 · Ops Autopilot $199 · Lead Engine $249 · Support Agent $129 ·
> Founder's CoS $299 · Autonomous Team $499/mo · Custom build from $990. Public numbers are
> founder-approved before launch (issue PRE-6).

---

## Our agents

| Agent | Role | Focus |
| --- | --- | --- |
| Hermes Engineer | CTO / Engineer | Code, builds, docs, ops, verification |
| Reflection Coach | General | Coaching, reflection, review |

---

## Contact

- Founder / brand owner: Premkumar M
- LinkedIn: [in/premkumar-m-5a07ab272](https://www.linkedin.com/in/premkumar-m-5a07ab272)
- GitHub: [itsPremkumar](https://github.com/itsPremkumar)
- Email: *add your public contact email here before publishing*

---

## Publish this showcase

This content is ready to become a public GitHub repo + GitHub Pages site:

```bash
git init
git add README.md index.html
git commit -m "Showcase: Prem Autonomous Co agent offerings"
git remote add origin git@github.com:itsPremkumar/prem-autonomous-showcase.git
git branch -M main
git push -u origin main
# Enable GitHub Pages: Settings -> Pages -> source: main branch, / (root)
```

Then post the LinkedIn launch draft in `linkedin-launch.md`.
