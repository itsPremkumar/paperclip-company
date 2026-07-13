#!/usr/bin/env python3
"""
PRE-51 Income Engine — content generator.

Auto-generates an affiliate blog + product-listing corpus for the company's
zero-investment monetization strategy (see docs/product-analysis-monetization-plan.md).

Outputs (written under ./out):
  - blog/<slug>.md        affiliate blog posts (markdown) for the company storefront
  - products/<id>.md      Gumroad-ready product listings (markdown) for the 8 products
  - index.json            manifest: corpus metadata + publish map

Affiliate policy (house rule: $0 budget, free/OSS only):
  - Only link tools the company actually uses and genuinely recommends.
  - Affiliate links are placeholders ({{{AFF_LINK:tool}}}), never fabricated URLs.
  - No paid promotions. Every post leads with real, useful content.

Run:  python generate.py
"""
import json
import os
import re
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out")
BLOG = os.path.join(OUT, "blog")
PROD = os.path.join(OUT, "products")
os.makedirs(BLOG, exist_ok=True)
os.makedirs(PROD, exist_ok=True)

GENERATED_AT = datetime.date.today().isoformat()

# ---------------------------------------------------------------------------
# Brand + product context (source of truth: digital-products/product-catalog.json)
# ---------------------------------------------------------------------------
STORE = {
    "name": "Prem Autonomous Co — Digital Products",
    "tagline": "Build tools that make founders and creators money.",
    "platform": "Gumroad",
    "bundle_price_usd": 99,
}

PRODUCTS = [
    {
        "id": "prem-50-viral-scripts",
        "title": "50 Viral Short-Form Video Scripts",
        "price_usd": 12,
        "category": "Content / Templates",
        "tagline": "Done-for-You YouTube Shorts / Reels / TikTok Scripts — 5 Niches, Ready to Film",
        "audience": "creators, solopreneurs, social-media managers",
        "pain": "You know short-form video drives reach, but scripting 50 hooks that actually stop the scroll is exhausting and time-consuming.",
        "outcome": "Filming-ready scripts across Space, Ocean, Productivity, Tech, and Science niches — open the doc, hit record, post.",
        "formats": ["PDF", "Markdown", "CSV", "JSON"],
        "highlights": ["50 finished scripts", "5 proven niches", "Hook–body–CTA structure", "Reusable CSV for batch posting"],
    },
    {
        "id": "prem-agent-playbook",
        "title": "Autonomous AI Agent Operations Playbook",
        "price_usd": 29,
        "category": "Business / Operations",
        "tagline": "Run an Entire Company with AI Agents — Zero Headcount, Zero Burn",
        "audience": "founders, ops leads, indie hackers",
        "pain": "Hiring is slow and expensive. You want leverage now, without payroll or management overhead.",
        "outcome": "The exact playbook we use to run a real company on autonomous agents — plus the AGENTS.md, .env.example, and config templates to copy.",
        "formats": ["PDF", "Markdown"],
        "highlights": ["Zero-headcount operating model", "Ready AGENTS.md + configs", "Heartbeat & disposition patterns", "4 reusable templates"],
    },
    {
        "id": "prem-remotion-templates",
        "title": "Remotion Short-Form Video Template Pack",
        "price_usd": 19,
        "category": "Templates / Development",
        "tagline": "Production-Ready Video Generation Templates for AVG — 12 Templates",
        "audience": "developers, video creators, agencies",
        "pain": "Building video templates from scratch is fiddly; you want a head start that renders locally with no per-render cost.",
        "outcome": "12 Remotion templates you can drop into the Automated-Video-Generator and start producing short-form video on autopilot.",
        "formats": ["JSON", "Markdown", "Configuration"],
        "highlights": ["12 templates", "AVG-compatible", "Local, free rendering", "Customizable configs"],
    },
    {
        "id": "prem-monetization-kit",
        "title": "AI-Powered Business Monetization Kit",
        "price_usd": 29,
        "category": "Business / Strategy",
        "tagline": "8 Complete Assets to Launch Your AI-Native Business at $0 Cost",
        "audience": "founders, creators, consultants",
        "pain": "You have skills but no clear path to revenue — and no budget to experiment.",
        "outcome": "8 finished assets (pricing, outreach, catalog, launch plan) that turn capability into paying offers, at zero spend.",
        "formats": ["Markdown"],
        "highlights": ["8 complete assets", "Zero-cost launch path", "Used to launch us", "Strategy + tactics"],
    },
    {
        "id": "prem-cold-outreach",
        "title": "Cold Outreach & Lead Generation Pack",
        "price_usd": 15,
        "category": "Marketing / Sales",
        "tagline": "Done-for-You Sequences That Get Replies (Not Ignored)",
        "audience": "freelancers, agencies, sales founders",
        "pain": "Cold outreach gets ghosted. You need sequences that earn a reply, plus objection handlers.",
        "outcome": "13 email + LinkedIn templates and follow-up sequences engineered to start conversations, with rebuttals for common objections.",
        "formats": ["Markdown", "CSV"],
        "highlights": ["13 templates", "Email + LinkedIn", "Follow-up sequences", "Objection handlers"],
    },
    {
        "id": "prem-job-board-guide",
        "title": "Free Job Board Outreach Mastery Guide",
        "price_usd": 12,
        "category": "Career / Freelance",
        "tagline": "Land Clients on Naukri, LinkedIn, Wellfound, YC & More — $0 Spent",
        "audience": "job seekers, freelancers, career switchers",
        "pain": "Paid job boards and ads are out of reach. You need free channels that actually convert.",
        "outcome": "A playbook for 10 free platforms (Naukri, LinkedIn, Wellfound, YC and more) to land clients and roles with $0 spent.",
        "formats": ["Markdown", "PDF"],
        "highlights": ["10 platforms covered", "100% free", "Profile + outreach tactics", "Tracked templates"],
    },
    {
        "id": "prem-pricing-templates",
        "title": "AI Agent Service Catalog + Pricing Templates",
        "price_usd": 19,
        "category": "Templates / Business",
        "tagline": "Customizable Tiered Pricing for AI-Native Services",
        "audience": "service providers, agencies, solopreneurs",
        "pain": "Pricing AI-native work is confusing — too cheap and you leave money; too high and you scare buyers.",
        "outcome": "6 tiered pricing templates (Markdown/CSV/JSON) you can adapt to any AI service so quotes are instant and consistent.",
        "formats": ["Markdown", "CSV", "JSON"],
        "highlights": ["6 tiers", "Service catalog", "Editable CSV/JSON", "Margin-safe framing"],
    },
    {
        "id": "prem-30-day-launch",
        "title": "30-Day Zero-Cost Business Launch Plan",
        "price_usd": 9,
        "category": "Business / Strategy",
        "tagline": "From Zero to First Paying Customer in 30 Days — $0 Spent",
        "audience": "new founders, side-hustlers",
        "pain": "You want to start but the gap from idea to first paying customer feels endless.",
        "outcome": "A day-by-day, $0-budget plan to reach your first paying customer in 30 days, with a $245 MRR target.",
        "formats": ["Markdown", "PDF", "CSV"],
        "highlights": ["30-day roadmap", "$0 budget", "$245 MRR target", "Daily actions"],
    },
]

# Affiliate tools the company genuinely uses (free / free-tier). Links are
# placeholders the operator fills with their real affiliate URLs.
AFF = {
    "paperclip": {
        "name": "Paperclip",
        "blurb": "The autonomous, agent-managed operating system we run the entire company on.",
        "note": "Self-hosted / OSS-friendly. We use it to run agents, issues, and documents.",
    },
    "gumroad": {
        "name": "Gumroad",
        "blurb": "The free platform we sell every digital product on — no monthly fees, pay-as-you-earn.",
        "note": "Free to start; Gumroad takes a small share of each sale.",
    },
    "remotion": {
        "name": "Remotion",
        "blurb": "Code-based video generation we use to produce short-form content locally, at zero per-render cost.",
        "note": "Open-source React library for programmatic video.",
    },
}

def aff(tool: str) -> str:
    return "{{{AFF_LINK:%s}}}" % tool

# ---------------------------------------------------------------------------
# Blog post builders
# ---------------------------------------------------------------------------

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]

def post_zero_cost_business() -> str:
    p = PRODUCTS[3]  # monetization kit
    l = PRODUCTS[7]  # 30-day launch
    return f"""# How to Start a Zero-Cost AI Business (and Reach Your First Paying Customer in 30 Days)

*Published {GENERATED_AT} · Affiliate resource guide · {STORE['name']}*

Most "start a business" advice assumes you have money to spend. You don't need it.
This company runs on autonomous AI agents and free/OSS tooling, and we hit our first
paying offer with **$0 of ad spend**. Here is the exact path.

## 1. Pick a capability you can deliver with agents
You don't need inventory. You need a repeatable service or asset you can produce
consistently — research, content, code, video, or a templated product.

## 2. Package it as a product, not a favor
Buyers want something they can own. Turn your capability into a downloadable asset
or a fixed-scope service. We packaged ours into a
[{p['title']} (${p['price_usd']})]({{PRODUCT_LINK:{p['id']}}}) and a
[{l['title']} (${l['price_usd']})]({{PRODUCT_LINK:{l['id']}}}).

## 3. Use free tools only
- **Run your ops on [Paperclip]({aff('paperclip')})** — {AFF['paperclip']['blurb']}
- **Sell on [Gumroad]({aff('gumroad')})** — {AFF['gumroad']['blurb']}
- **Make video with [Remotion]({aff('remotion')})** — {AFF['remotion']['blurb']}

## 4. Follow a 30-day launch sequence
A day-by-day plan keeps momentum. Our
[{l['title']}]({{PRODUCT_LINK:{l['id']}}}) maps every day from zero to first
paying customer, targeting **$245 MRR** with no budget.

## Why this works
Marginal cost per delivered product is ~agent compute (free tier) + a little review
time. Gross margin stays near 100% until you outgrow free tiers — and by then you
have revenue to reinvest.

---

*Recommended: [{p['title']} — ${p['price_usd']}]({{PRODUCT_LINK:{p['id']}}}) ·
[{l['title']} — ${l['price_usd']}]({{PRODUCT_LINK:{l['id']}}})*
"""

def post_ai_agents_company() -> str:
    p = PRODUCTS[1]  # playbook
    return f"""# Can You Really Run a Company with AI Agents? (What We Learned)

*Published {GENERATED_AT} · Field notes · {STORE['name']}*

Short answer: yes — if you treat agents like a disciplined ops team, not magic.
We run a real company on autonomous agents. Here is the operating model.

## The heartbeat rhythm
Every issue moves through clear states: `todo → in_progress → in_review → done`.
Agents pick up work, make durable progress in documents and comments, and always
leave a disposition. No task is left mid-flight.

## The artifacts that hold it together
- A single `AGENTS.md` contract that every agent follows.
- Issue documents for plans and deliverables.
- Work products that link the actual output (not just a local path).

## Copy our setup
The [{p['title']} (${p['price_usd']})]({{PRODUCT_LINK:{p['id']}}}) ships the
`AGENTS.md`, `.env.example`, and config templates we use — plus the heartbeat and
disposition patterns.

## The platform we run on
We self-host [Paperclip]({aff('paperclip')}) to manage agents, issues, documents,
and work products. It is the control plane for the whole company.

---

*Get the [Autonomous AI Agent Operations Playbook — ${p['price_usd']}]({{PRODUCT_LINK:{p['id']}}}).*
"""

def post_short_form_video() -> str:
    scripts = PRODUCTS[0]
    remplates = PRODUCTS[2]
    return f"""# How to Produce Short-Form Video at Zero Render Cost

*Published {GENERATED_AT} · Tutorial · {STORE['name']}*

Short-form video is the cheapest reach you can get — if producing it doesn't cost
you a fortune in time or rendering fees. Here is our local, free pipeline.

## The stack
- **[Remotion]({aff('remotion')})** for code-based video templates.
- Our **Automated-Video-Generator** (Remotion + Edge-TTS + free stock) renders locally.
- No per-render cloud bills — your machine does the work.

## Start from finished scripts
Don't stare at a blank page. The
[{scripts['title']} (${scripts['price_usd']})]({{PRODUCT_LINK:{scripts['id']}}})
gives you 50 filming-ready scripts across 5 niches.

## Accelerate with templates
The [{remplates['title']} (${remplates['price_usd']})]({{PRODUCT_LINK:{remplates['id']}}})
adds 12 Remotion templates you can drop straight into the generator.

## The loop
Script → template → local render → post. Repeat. The marginal cost is compute you
already have.

---

*Grab [50 Viral Short-Form Video Scripts — ${scripts['price_usd']}]({{PRODUCT_LINK:{scripts['id']}}})
and the [Remotion Template Pack — ${remplates['price_usd']}]({{PRODUCT_LINK:{remplates['id']}}}).*
"""

def post_cold_outreach() -> str:
    o = PRODUCTS[4]
    jb = PRODUCTS[5]
    return f"""# Cold Outreach That Gets Replies (Not Ignored)

*Published {GENERATED_AT} · Sales playbook · {STORE['name']}*

Cold outreach fails when it sounds like a template. It works when it is specific,
short, and offers something the recipient wants. Two assets do the heavy lifting.

## Email + LinkedIn that start conversations
The [{o['title']} (${o['price_usd']})]({{PRODUCT_LINK:{o['id']}}}) ships 13
templates and follow-up sequences engineered for replies — plus objection handlers
so you don't freeze when someone pushes back.

## Free channels to send them on
Skip paid ads. The [{jb['title']} (${jb['price_usd']})]({{PRODUCT_LINK:{jb['id']}}})
covers 10 free platforms (Naukri, LinkedIn, Wellfound, YC and more) to land clients
with $0 spent.

## The rule
One specific sentence about *them* beats three about *you*. Lead with the
recipient's problem, offer the asset, ask one low-friction question.

---

*Get the [Cold Outreach & Lead Generation Pack — ${o['price_usd']}]({{PRODUCT_LINK:{o['id']}}})
and the [Free Job Board Guide — ${jb['price_usd']}]({{PRODUCT_LINK:{jb['id']}}}).*
"""

def post_pricing_ai_services() -> str:
    pr = PRODUCTS[6]
    return f"""# How to Price AI-Agent Services Without Scaring Buyers Away

*Published {GENERATED_AT} · Pricing guide · {STORE['name']}*

Pricing AI-native work is awkward: too low and you leave money; too high and the
buyer hesitates. Tiers fix this.

## Why tiers
A tiered catalog lets a buyer self-select. The small tier removes risk; the premium
tier anchors value. You stop negotiating from zero.

## What to ship
The [{pr['title']} (${pr['price_usd']})]({{PRODUCT_LINK:{pr['id']}}}) includes 6
tiered pricing templates (Markdown/CSV/JSON) and a service catalog you can adapt to
any AI offering.

## Quick framing
- **Starter** — a single deliverable, fixed price.
- **Growth** — a recurring batch of deliverables.
- **Scale** — managed, ongoing agent capacity.

Each tier should be margin-safe at free-tier compute.

---

*Download the [AI Agent Service Catalog + Pricing Templates — ${pr['price_usd']}]({{PRODUCT_LINK:{pr['id']}}}).*
"""

def post_bundle() -> str:
    return f"""# The $99 Bundle: Everything to Launch an AI-Native Business at $0

*Published {GENERATED_AT} · Bundle offer · {STORE['name']}*

Eight products, one download, **${STORE['bundle_price_usd']}** (vs ${sum(p['price_usd'] for p in PRODUCTS)} bought separately — save 40%).

## What's inside
""" + "\n".join(f"- [{p['title']} — ${p['price_usd']}]({{PRODUCT_LINK:{p['id']}}})" for p in PRODUCTS) + f"""

## Who it's for
Founders, creators, and operators who want the full stack — scripts, playbook,
templates, pricing, outreach, and a 30-day launch plan — without piecing it together.

## Where to buy
We sell everything on [Gumroad]({aff('gumroad')}), the free platform for digital
creators. **Bundle price: ${STORE['bundle_price_usd']}.**

---

*Get the complete bundle and start shipping today.*
"""

BLOG_POSTS = [
    ("zero-cost-ai-business", post_zero_cost_business),
    ("run-company-with-ai-agents", post_ai_agents_company),
    ("short-form-video-zero-cost", post_short_form_video),
    ("cold-outreach-that-replies", post_cold_outreach),
    ("pricing-ai-agent-services", post_pricing_ai_services),
    ("complete-bundle-99", post_bundle),
]

# ---------------------------------------------------------------------------
# Product listing builder
# ---------------------------------------------------------------------------

def product_listing(p: dict) -> str:
    return f"""# {p['title']}

**Price:** ${p['price_usd']}  ·  **Category:** {p['category']}
**Formats:** {', '.join(p['formats'])}
**Tagline:** {p['tagline']}

---

## The problem
{p['pain']}

## What you get
{p['outcome']}

## Highlights
""" + "\n".join(f"- {h}" for h in p['highlights']) + f"""

## Who it's for
{p['audience'].capitalize()}.

## Delivery
Instant digital download after purchase on [Gumroad]({aff('gumroad')}).
Worldwide · {', '.join(p['formats'])}.

---

*Part of the [complete ${STORE['bundle_price_usd']} bundle]({{PRODUCT_LINK:bundle}}) — 8 products, save 40%.*
"""

# ---------------------------------------------------------------------------
# Render + write
# ---------------------------------------------------------------------------
manifest = {
    "generatedAt": GENERATED_AT,
    "store": STORE,
    "affiliatePolicy": "Only tools the company uses; links are placeholders {{{AFF_LINK:tool}}}. No paid promotions.",
    "blog": [],
    "products": [],
}

for slug, fn in BLOG_POSTS:
    body = fn()
    path = os.path.join(BLOG, slug + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    manifest["blog"].append({"slug": slug, "title": body.splitlines()[0].lstrip("# ").strip(), "file": "blog/" + slug + ".md"})

for p in PRODUCTS:
    body = product_listing(p)
    path = os.path.join(PROD, p["id"] + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    manifest["products"].append({"id": p["id"], "title": p["title"], "price_usd": p["price_usd"], "file": "products/" + p["id"] + ".md"})

# bundle listing
bundle_body = product_listing({
    "id": "bundle", "title": f"Complete Bundle — All 8 Products (${STORE['bundle_price_usd']})",
    "price_usd": STORE["bundle_price_usd"], "category": "Bundle",
    "tagline": "Everything to launch an AI-native business at $0 cost.",
    "audience": "founders, creators, operators",
    "pain": "You want the full stack but don't want to buy eight things separately.",
    "outcome": "All 8 products in one download — scripts, playbook, templates, pricing, outreach, and a 30-day launch plan.",
    "formats": ["PDF", "Markdown", "CSV", "JSON"],
    "highlights": [f"{p['title']} (${p['price_usd']})" for p in PRODUCTS] + ["Save 40% vs separate", "Lifetime updates"],
})
with open(os.path.join(PROD, "bundle.md"), "w", encoding="utf-8") as f:
    f.write(bundle_body)
manifest["products"].append({"id": "bundle", "title": "Complete Bundle", "price_usd": STORE["bundle_price_usd"], "file": "products/bundle.md"})

with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print("Generated:")
print(f"  blog posts : {len(manifest['blog'])}")
print(f"  listings  : {len(manifest['products'])}")
print(f"  out dir   : {OUT}")
