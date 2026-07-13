#!/usr/bin/env python3
"""
AI Agent Retainer Builder — Pipeline #15 (from research/MONEY_IDEAS_2026.md, rank #1)

Generates ready-to-sell AI-agent-integration retainer packages (title, description,
3 tiers, SEO tags) + an importable n8n workflow JSON for delivery automation.

Validated 2026 market data (see research/MONEY_IDEAS_2026.md for full citations):
  - AI-agent integration retainers: $2,500–$6,000/mo (betonai rate card, 54 operators,
    betonai.net/.../real-rates-from-54-operators/)
  - n8n self-hosted projects pay 40–60% more than Zapier equivalents; flat-fee
    client automation $1,800–$4,500 (same source)
  - Fiverr AI gigs grew 340% YoY in Q1 2026 (betonai playbook)
  - Free stack: n8n (n8n.io) + Hermes/OpenClaw agent + Crawl4AI + pgvector + Chatwoot.

Usage:
  python pipeline15_agent_retainer.py --vertical "ecommerce" --price 3500
  python pipeline15_agent_retainer.py --list
  python pipeline15_agent_retainer.py --vertical realestate --out ret.json
  python pipeline15_agent_retainer.py self-test
Zero dependencies (stdlib only).
"""
import argparse
import json
import sys

# ---- Validated 2026 pricing data (AI-agent retainers) ----
# Anchored to betonai rate card: AI-agent integration retainers $2,500–$6,000/mo.
# Per-vertical scoped to the lower end of that band for a solo operator.
VERTICALS = {
    "ecommerce": {
        "title": "I will run a monthly AI-agent retainer for your e-commerce store",
        "outcome": "an autonomous agent that monitors stock, drafts listings, replies to tickets, and reports weekly",
        "tools": "n8n + Hermes/OpenClaw + Crawl4AI + pgvector + Chatwoot — all free/self-hosted",
        "margin_note": "Charge $2,500–$5,000/mo retainer; your inference cost <$20/mo (local models)",
        "tags": ["ai agent", "ecommerce automation", "n8n", "autonomous agent",
                 "shopify automation", "customer support ai", "ai retainer"],
        "default_price": 3500,
    },
    "realestate": {
        "title": "I will run a monthly AI-agent retainer for your real-estate team",
        "outcome": "an agent that qualifies leads, drafts follow-ups, and logs hot prospects to your CRM",
        "tools": "n8n + Hermes/OpenClaw + Crawl4AI + pgvector + Chatwoot — all free/self-hosted",
        "margin_note": "Charge $2,500–$6,000/mo retainer; <$20/mo inference",
        "tags": ["ai agent", "real estate lead gen", "n8n", "crm automation",
                 "lead qualification", "autonomous agent", "ai retainer"], "default_price": 4000,
    },
    "agencies": {
        "title": "I will run a monthly AI-agent retainer for your marketing agency",
        "outcome": "an agent that researches prospects, drafts outreach, and posts approved content",
        "tools": "n8n + Hermes/OpenClaw + Crawl4AI + pgvector + Listmonk — all free/self-hosted",
        "margin_note": "Charge $2,000–$4,500/mo retainer; <$15/mo inference",
        "tags": ["ai agent", "agency automation", "n8n", "lead research",
                 "content automation", "outreach", "ai retainer"], "default_price": 3000,
    },
    "smb": {
        "title": "I will run a monthly AI-agent retainer for your small business",
        "outcome": "an agent that handles inbox triage, data entry, and a weekly ops summary",
        "tools": "n8n + Hermes/OpenClaw + Crawl4AI + pgvector + Chatwoot — all free/self-hosted",
        "margin_note": "Charge $1,800–$3,800/mo retainer; <$15/mo inference",
        "tags": ["ai agent", "small business automation", "n8n", "inbox triage",
                 "ops automation", "autonomous agent", "ai retainer"], "default_price": 2500,
    },
}


def build_package(vertical_key, price=None):
    s = VERTICALS[vertical_key]
    price = price or s["default_price"]
    tiers = build_tiers(vertical_key, price)
    desc = f"""🔧 {s['title']}

I operate {s['outcome']} using {s['tools']}.

✅ What you get:
• A live AI agent working for you every month (not a one-off build)
• Free, open-source tools (you own the stack, no SaaS lock-in)
• {s['margin_note']}
• Weekly report + monthly strategy call

📦 Tiers:
{bullet_tiers(tiers)}

🚀 How it works:
1. You tell me the process to automate (form on order)
2. I build + deploy the agent on your infra
3. I monitor, improve, and report every month

⚡ Why me: I run the same agent stack that powers a 100-skill autonomous company.
"""
    return {
        "vertical": vertical_key,
        "package_title": s["title"],
        "price": price,
        "tags": s["tags"],
        "description": desc,
        "packages": tiers,
        "n8n_workflow": build_n8n_workflow(vertical_key, s),
    }


def build_tiers(vertical_key, price):
    return [
        {"name": "Pilot", "price": max(price // 3, 800),
         "delivery": "1 week", "revisions": 0,
         "features": ["1 agent", "Core workflow", "Email support", "Weekly report"]},
        {"name": "Growth", "price": price,
         "delivery": "1 week", "revisions": 0,
         "features": ["2–3 agents", "CRM/marketplace hooks", "Loom updates", "Monthly call"]},
        {"name": "Scale", "price": price * 2,
         "delivery": "2 weeks", "revisions": 0,
         "features": ["Unlimited agents", "Full autonomy", "Priority support", "Quarterly roadmap"]},
    ]


def bullet_tiers(tiers):
    out = []
    for t in tiers:
        out.append(f"• {t['name']} (${t['price']}/mo, {t['delivery']}): " + ", ".join(t["features"]))
    return "\n".join(out)


def build_n8n_workflow(vertical_key, s):
    return {
        "name": f"deliver-agent-{vertical_key}",
        "nodes": [
            {"parameters": {}, "name": "Schedule / Webhook (trigger)",
             "type": "n8n-nodes-base.webhook", "typeVersion": 1, "position": [0, 0]},
            {"parameters": {}, "name": "Hermes agent (reason + act)",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [300, 0]},
            {"parameters": {}, "name": "Deliver + log to pgvector",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [600, 0]},
        ],
        "connections": {
            "Schedule / Webhook (trigger)": {"main": [[{"node": "Hermes agent (reason + act)", "type": "main", "index": 0}]]},
            "Hermes agent (reason + act)": {"main": [[{"node": "Deliver + log to pgvector", "type": "main", "index": 0}]]},
        },
        "note": f"Tools: {s['tools']}. Replace code node with your agent logic.",
    }


def main():
    p = argparse.ArgumentParser(description="AI Agent Retainer Builder — Pipeline #15")
    p.add_argument("--vertical", help="vertical key: " + ", ".join(VERTICALS.keys()))
    p.add_argument("--price", type=int, help="override monthly price")
    p.add_argument("--out", help="write package JSON to file")
    p.add_argument("--list", action="store_true", help="list verticals")
    p.add_argument("cmd", nargs="?", default="self-test")
    a = p.parse_args()

    if a.list:
        for k, v in VERTICALS.items():
            print(f"  {k:12} {v['default_price']:>5}/mo  {v['title'][:46]}")
        return

    if a.cmd == "self-test" and not a.vertical:
        for k in VERTICALS:
            pkg = build_package(k)
            assert pkg["package_title"] and pkg["description"] and len(pkg["packages"]) == 3
            assert pkg["n8n_workflow"]["name"].startswith("deliver-agent-")
            assert all(isinstance(t, str) and t for t in pkg["tags"])
        print(f"self-test: OK — {len(VERTICALS)} verticals, all generate valid packages + n8n stubs")
        return

    if not a.vertical or a.vertical not in VERTICALS:
        print("ERROR: --vertical required. Choose from: " + ", ".join(VERTICALS.keys()))
        sys.exit(1)

    pkg = build_package(a.vertical, a.price)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(pkg, f, indent=2)
        print(f"Wrote package JSON -> {a.out}")
    else:
        pkgs = ", ".join(f"{t['name']}(${t['price']}/mo)" for t in pkg["packages"])
        print(f"\n📦 PACKAGE: {pkg['package_title']}")
        print(f"💲 Price: ${pkg['price']}/mo | Tags: {', '.join(pkg['tags'][:5])}")
        print(f"📋 Tiers: {pkgs}")
        print(f"⚙️  n8n workflow: {pkg['n8n_workflow']['name']} ({len(pkg['n8n_workflow']['nodes'])} nodes)")


if __name__ == "__main__":
    main()
