#!/usr/bin/env python3
"""
Fiverr Gig Factory — Pipeline #1 from MONEY_AUTOMATION_IDEAS.md

Generates ready-to-publish Fiverr gig packages (title, description, 3 tiers,
SEO tags) + an importable n8n workflow JSON for the delivery automation.

Usage:
  python fiverr_gig_factory.py --service "email-automation" --price 500
  python fiverr_gig_factory.py --list            # show all service templates
  python fiverr_gig_factory.py --service video --out video_gig.json
  python fiverr_gig_factory.py self-test         # verify it works end-to-end

Zero dependencies (stdlib only). Part of the autonomous money system.
"""
import argparse
import json
import os
import sys

# ---- Validated 2026 pricing data (from MONEY_AUTOMATION_IDEAS.md research) ----
SERVICES = {
    "email-automation": {
        "title": "I will automate your email marketing with n8n workflows",
        "outcome": "a fully automated email sequence that nurtures leads and recovers abandoned carts",
        "tools": "n8n + Mautic + Listmonk (all free/self-hosted)",
        "margin_note": "AI cost per delivery $3–$8 vs $350–$800 gig price = 95–99% margin",
        "tags": ["email automation", "n8n", "mailchimp alternative", "drip campaign",
                 "lead nurture", "marketing automation", "newsletter setup"],
        "default_price": 500,
    },
    "chatbot": {
        "title": "I will build you an AI customer support chatbot",
        "outcome": "a 24/7 support bot trained on your FAQs, deployed on Chatwoot",
        "tools": "Chatwoot + Hermes/OpenClaw + agent-sentinel (all free)",
        "margin_note": "$500–$1,500 setup + $99–$299/mo managed support",
        "tags": ["ai chatbot", "customer support", "chatwoot", "n8n",
                 "ai assistant", "helpdesk automation", "faq bot"],
        "default_price": 800,
    },
    "video": {
        "title": "I will create an AI-generated product promo video",
        "outcome": "a professional 30–60s promo video from your product URL or script",
        "tools": "Automated-Video-Generator (Remotion+Edge-TTS) + CogVideoX",
        "margin_note": "$100–$500/video, your own edge project = Product #1",
        "tags": ["ai video", "product video", "video generation", "promo video",
                 "explainer video", "remotion", "ai editing"],
        "default_price": 250,
    },
    "lead-enrichment": {
        "title": "I will enrich your leads with automated web research",
        "outcome": "a clean CSV of enriched leads (emails, titles, socials) from any company list",
        "tools": "n8n + Firecrawl/Crawl4AI + maps-cli patterns",
        "margin_note": "$0.10–$0.50/lead or $29–$99/mo SaaS tier",
        "tags": ["lead generation", "data enrichment", "web scraping",
                 "b2b leads", "prospect list", "n8n automation"],
        "default_price": 300,
    },
    "seo-audit": {
        "title": "I will run an automated SEO & security audit of your website",
        "outcome": "a branded PDF report with code-quality, security, and SEO fixes",
        "tools": "codebase-inspection + secret-scanner + skill-lint + Stirling-PDF",
        "margin_note": "$49–$199/mo per site, pure recurring",
        "tags": ["seo audit", "website audit", "security scan", "technical seo",
                 "site report", "n8n report"],
        "default_price": 149,
    },
    "contract": {
        "title": "I will generate your legal contract or proposal",
        "outcome": "a tailored, legally-structured doc from a simple intake form",
        "tools": "DocAssemble + Hermes drafting + your doc-extractor skill",
        "margin_note": "$50–$300/doc, $5 AI cost",
        "tags": ["legal document", "contract generator", "proposal writer",
                 "freelance contract", "nda", "docassemble"],
        "default_price": 120,
    },
    "social-content": {
        "title": "I will auto-generate 30 days of social media content",
        "outcome": "a month of posts (text + video + gif) scheduled across platforms",
        "tools": "n8n + Mautic + youtube-content + gif-search + ascii-art-creator",
        "margin_note": "$300–$800/mo per client done-for-you",
        "tags": ["social media", "content creation", "content calendar",
                 "n8n", "ai content", "social automation"],
        "default_price": 400,
    },
    "rag-kb": {
        "title": "I will build a private RAG knowledge base for your business",
        "outcome": "a searchable AI brain trained on your docs, embedded in your site",
        "tools": "Mem0 + pgvector + Graphiti + Docling + Open WebUI",
        "margin_note": "$1,000–$3,000 project + $99–$199/mo hosting",
        "tags": ["rag", "knowledge base", "ai search", "chatgpt for business",
                 "document ai", "vector database"],
        "default_price": 1500,
    },
}


def build_gig(service_key, price=None):
    s = SERVICES[service_key]
    price = price or s["default_price"]
    tiers = build_tiers(service_key, price)
    desc = f"""🔧 {s['title']}

I deliver {s['outcome']} using {s['tools']}.

✅ What you get:
• Done-for-you setup — no technical skills needed
• Free, open-source tools (you own it, no lock-in)
• {s['margin_note']}
• 7-day support after delivery

📦 Packages:
{bullet_tiers(tiers)}

🚀 How it works:
1. You tell me your stack/goal (form on order)
2. I build & test the automation
3. I hand over + record a 5-min Loom walkthrough

⚡ Why me: I use the same tools that power a 31-skill autonomous company.
"""
    return {
        "service": service_key,
        "gig_title": s["title"],
        "price": price,
        "tags": s["tags"],
        "description": desc,
        "packages": tiers,
        "n8n_workflow": build_n8n_workflow(service_key, s),
    }


def build_tiers(service_key, price):
    return [
        {"name": "Basic", "price": max(price // 4, 30),
         "delivery": "3 days", "revisions": 1,
         "features": ["Setup only", "1 workflow", "Email support"]},
        {"name": "Standard", "price": price,
         "delivery": "5 days", "revisions": 2,
         "features": ["Setup + test", "Up to 3 workflows", "Loom walkthrough", "7-day support"]},
        {"name": "Premium", "price": price * 2,
         "delivery": "7 days", "revisions": 3,
         "features": ["Full system", "Unlimited workflows", "Monthly retainer option", "Priority support"]},
    ]


def bullet_tiers(tiers):
    out = []
    for t in tiers:
        out.append(f"• {t['name']} (${t['price']}, {t['delivery']}, {t['revisions']} rev): "
                   + ", ".join(t["features"]))
    return "\n".join(out)


def build_n8n_workflow(service_key, s):
    """Generate a minimal importable n8n workflow JSON stub."""
    return {
        "name": f"deliver-{service_key}",
        "nodes": [
            {"parameters": {}, "name": "Webhook (order intake)",
             "type": "n8n-nodes-base.webhook", "typeVersion": 1, "position": [0, 0]},
            {"parameters": {}, "name": "Build automation",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [300, 0]},
            {"parameters": {}, "name": "Deliver + notify",
             "type": "n8n-nodes-base.emailSend", "typeVersion": 1, "position": [600, 0]},
        ],
        "connections": {
            "Webhook (order intake)": {"main": [[{"node": "Build automation", "type": "main", "index": 0}]]},
            "Build automation": {"main": [[{"node": "Deliver + notify", "type": "main", "index": 0}]]},
        },
        "note": f"Tools: {s['tools']}. Replace code node with your delivery logic.",
    }


def main():
    p = argparse.ArgumentParser(description="Fiverr Gig Factory — Pipeline #1")
    p.add_argument("--service", help="service key: " + ", ".join(SERVICES.keys()))
    p.add_argument("--price", type=int, help="override gig price")
    p.add_argument("--out", help="write gig JSON to file")
    p.add_argument("--list", action="store_true", help="list services")
    p.add_argument("cmd", nargs="?", default="self-test")
    a = p.parse_args()

    if a.list:
        for k, v in SERVICES.items():
            print(f"  {k:18} {v['default_price']:>5}/gig  {v['title'][:50]}")
        return

    if a.cmd == "self-test" and not a.service:
        # verify all services generate cleanly
        for k in SERVICES:
            g = build_gig(k)
            assert g["gig_title"] and g["description"] and len(g["packages"]) == 3
            assert g["n8n_workflow"]["name"].startswith("deliver-")
        print(f"self-test: OK — {len(SERVICES)} services, all generate valid gigs + n8n stubs")
        return

    if not a.service or a.service not in SERVICES:
        print("ERROR: --service required. Choose from: " + ", ".join(SERVICES.keys()))
        sys.exit(1)

    gig = build_gig(a.service, a.price)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(gig, f, indent=2)
        print(f"Wrote gig JSON -> {a.out}")
    else:
        pkgs = ", ".join(f"{t['name']}(${t['price']})" for t in gig['packages'])
        print(f"\n📦 GIG: {gig['gig_title']}")
        print(f"💲 Price: ${gig['price']} | Tags: {', '.join(gig['tags'][:5])}")
        print(f"📋 Packages: {pkgs}")
        print(f"⚙️  n8n workflow: {gig['n8n_workflow']['name']} ({len(gig['n8n_workflow']['nodes'])} nodes)")
        print("\n--- DESCRIPTION PREVIEW ---")
        print(gig["description"][:400] + "...")


if __name__ == "__main__":
    main()
