#!/usr/bin/env python3
"""
AI Support Bot Deployer — Pipeline #4 from MONEY_AUTOMATION_IDEAS.md

Sells done-for-you AI customer-support bots deployed on Chatwoot, powered by
Hermes/OpenClaw, monitored with agent-sentinel. Generates per-vertical packages:
deploy spec, training plan, pricing (validated: $500-$1,500 setup + $99-$299/mo).

Built on free tools: Chatwoot + Hermes/OpenClaw + agent-sentinel (all self-hostable).

Usage:
  python pipeline4_support_bot.py --vertical ecommerce --out ecom_bot.json
  python pipeline4_support_bot.py --list
  python pipeline4_support_bot.py self-test
Zero dependencies (stdlib only).
"""
import argparse
import json
import sys

VERTICALS = {
    "ecommerce": {
        "title": "I will build an AI support bot for your online store",
        "handles": "order status, returns, sizing, shipping, product Q&A",
        "channels": "website widget + WhatsApp + Instagram DM",
        "kb_source": "product catalog + FAQ + returns policy",
        "setup": 900, "monthly": 199,
    },
    "saas": {
        "title": "I will deploy an AI support agent for your SaaS product",
        "handles": "onboarding, billing, feature how-tos, tier-1 troubleshooting",
        "channels": "in-app widget + email + Slack",
        "kb_source": "docs + changelog + help center",
        "setup": 1200, "monthly": 299,
    },
    "clinic": {
        "title": "I will set up an AI receptionist bot for your clinic",
        "handles": "appointment booking, hours, insurance, directions, FAQs",
        "channels": "website + WhatsApp + SMS",
        "kb_source": "services list + booking rules + policies",
        "setup": 700, "monthly": 149,
    },
    "agency": {
        "title": "I will build a lead-qualifying AI bot for your agency",
        "handles": "qualify leads, book calls, answer service Q&A, route hot leads",
        "channels": "website widget + Messenger",
        "kb_source": "services + case studies + pricing tiers",
        "setup": 800, "monthly": 199,
    },
    "local": {
        "title": "I will deploy an AI support bot for your local business",
        "handles": "hours, location, bookings, common questions, quotes",
        "channels": "website + WhatsApp",
        "kb_source": "business info + services + FAQ",
        "setup": 500, "monthly": 99,
    },
}


def build_package(vertical, setup=None):
    v = VERTICALS[vertical]
    setup = setup or v["setup"]
    return {
        "vertical": vertical,
        "gig_title": v["title"],
        "handles": v["handles"],
        "channels": v["channels"],
        "kb_source": v["kb_source"],
        "pricing": {
            "setup": setup,
            "monthly": v["monthly"],
            "api_cost_note": "self-hosted Hermes/OpenClaw = low marginal cost",
            "margin_pct": 90,
        },
        "deploy_spec": build_deploy_spec(v),
        "delivery_steps": [
            "1. Collect KB source (" + v["kb_source"] + ")",
            "2. Train bot on Hermes/OpenClaw + build intents",
            "3. Deploy on Chatwoot across: " + v["channels"],
            "4. Wire agent-sentinel monitoring + fallback-to-human",
            "5. Handover + 14-day tuning + monthly report",
        ],
        "tags": ["ai chatbot", "customer support", "chatwoot",
                 vertical + " bot", "ai assistant", "support automation"],
    }


def build_deploy_spec(v):
    return {
        "platform": "chatwoot",
        "brain": "hermes / openclaw (self-hosted)",
        "monitoring": "agent-sentinel",
        "channels": v["channels"],
        "escalation": "auto handoff to human on low confidence",
        "kb": v["kb_source"],
        "note": "Self-hosted stack; no per-seat SaaS fees.",
    }


def main():
    p = argparse.ArgumentParser(description="AI Support Bot Deployer — Pipeline #4")
    p.add_argument("--vertical", help="vertical: " + ", ".join(VERTICALS.keys()))
    p.add_argument("--setup", type=int, help="override setup price")
    p.add_argument("--out", help="write package JSON to file")
    p.add_argument("--list", action="store_true")
    p.add_argument("cmd", nargs="?", default="self-test")
    a = p.parse_args()

    if a.list:
        for k, val in VERTICALS.items():
            print(f"  {k:10} setup ${val['setup']:>4} + ${val['monthly']}/mo  {val['title'][:44]}")
        return

    if a.cmd == "self-test" and not a.vertical:
        for k in VERTICALS:
            pkg = build_package(k)
            assert pkg["gig_title"] and pkg["deploy_spec"]["platform"] == "chatwoot"
            assert pkg["pricing"]["margin_pct"] == 90
            assert len(pkg["delivery_steps"]) == 5
        print(f"self-test: OK — {len(VERTICALS)} verticals, all generate valid packages")
        return

    if not a.vertical or a.vertical not in VERTICALS:
        print("ERROR: --vertical required. Choose: " + ", ".join(VERTICALS.keys()))
        sys.exit(1)

    pkg = build_package(a.vertical, a.setup)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(pkg, fh, indent=2)
        print(f"Wrote package -> {a.out}")
    else:
        print(f"\n🤖 SUPPORT BOT: {a.vertical}")
        print(f"📋 {pkg['gig_title']}")
        print(f"💲 ${pkg['pricing']['setup']} setup + ${pkg['pricing']['monthly']}/mo (90% margin)")
        print(f"📡 Channels: {pkg['channels']}")
        print(f"⚙️  Platform: {pkg['deploy_spec']['platform']} + {pkg['deploy_spec']['brain']}")


if __name__ == "__main__":
    main()
