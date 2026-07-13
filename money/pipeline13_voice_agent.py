#!/usr/bin/env python3
"""
Voice AI Agent Deployer — Pipeline #13 (from research/MONEY_IDEAS_2026.md, rank #2)

Generates ready-to-sell voice-agent service packages (title, description, 3 tiers,
SEO tags) + an importable n8n workflow JSON for delivery automation.

Validated 2026 market data (see research/MONEY_IDEAS_2026.md for full citations):
  - Global AI voice-agent market: $2.4–$3.14B (2024) -> $35–$47.5B by 2033–34 (CAGR 34–39%)
    Source: deepresearch.ninja/2026/05/AI-Voice-Agent-Adoption-and-Demand-in-SMEs/
  - 78% of customers hire the company that responds first (speed-to-lead)
    Source: deantek.co/blog/ai-automation-small-business-statistics-2026
  - Free stack: Piper (local TTS) + Whisper (local STT) + Hermes/OpenClaw agent +
    Chatwoot (github.com/chatwoot/chatwoot) + n8n (n8n.io) — all open-source.

Usage:
  python pipeline13_voice_agent.py --niche "plumbing" --price 900
  python pipeline13_voice_agent.py --list
  python pipeline13_voice_agent.py --niche salons --out salon_voice.json
  python pipeline13_voice_agent.py self-test
Zero dependencies (stdlib only).
"""
import argparse
import json
import sys

# ---- Validated 2026 pricing data (per-niche voice-agent retainers) ----
# Retainer range anchored on betonai rate card: AI-agent integration retainers
# $2,500–$6,000/mo (betonai.net/.../real-rates-from-54-operators/), scoped to a
# single-vertical voice agent (lower end of that band).
NICHE_TEMPLATES = {
    "plumbing": {
        "title": "I will deploy a 24/7 AI voice receptionist for your plumbing business",
        "outcome": "an AI voice agent that answers calls, books jobs, and texts you the details — so you stop losing the 27% of calls owners miss",
        "tools": "Piper (local TTS) + Whisper (local STT) + Hermes/OpenClaw + Chatwoot + n8n — all free/self-hosted",
        "margin_note": "Charge $900–$1,800 setup + $299–$599/mo; your inference cost ~$0 (local) to <$5/mo",
        "tags": ["ai voice agent", "phone answering", "plumbing automation", "virtual receptionist",
                 "chatwoot", "n8n", "small business automation", "missed call recovery"],
        "default_price": 1200,
    },
    "salons": {
        "title": "I will build an AI voice booking assistant for your salon or spa",
        "outcome": "an AI voice agent that handles appointment booking, reschedules, and sends reminders — never double-books again",
        "tools": "Piper + Whisper + Hermes/OpenClaw + Chatwoot + n8n — all free/self-hosted",
        "margin_note": "Charge $800–$1,500 setup + $249–$499/mo managed",
        "tags": ["ai voice agent", "salon booking", "appointment scheduler", "spa automation",
                 "virtual assistant", "n8n", "chatwoot", "missed call text back"],
        "default_price": 1000,
    },
    "dental": {
        "title": "I will set up an AI voice agent that answers dental-practice calls 24/7",
        "outcome": "an AI voice agent that books new-patient appointments, confirms visits, and routes emergencies — captures after-hours demand",
        "tools": "Piper + Whisper + Hermes/OpenClaw + Chatwoot + n8n — all free/self-hosted",
        "margin_note": "Charge $1,200–$2,000 setup + $399–$799/mo managed",
        "tags": ["ai voice agent", "dental automation", "appointment booking", "healthcare ai",
                 "virtual receptionist", "n8n", "hipaa friendly self-host"], "default_price": 1500,
    },
    "realestate": {
        "title": "I will deploy an AI voice agent that qualifies real-estate leads by phone",
        "outcome": "an AI voice agent that calls back leads in <60s, qualifies them, and logs hot ones to your CRM",
        "tools": "Piper + Whisper + Hermes/OpenClaw + Chatwoot + n8n — all free/self-hosted",
        "margin_note": "Charge $1,000–$2,000 setup + $349–$699/mo managed",
        "tags": ["ai voice agent", "real estate lead gen", "lead qualification", "speed to lead",
                 "n8n", "crm automation", "virtual assistant"], "default_price": 1400,
    },
}


def build_package(niche_key, price=None):
    s = NICHE_TEMPLATES[niche_key]
    price = price or s["default_price"]
    tiers = build_tiers(niche_key, price)
    desc = f"""🔧 {s['title']}

I deploy {s['outcome']} using {s['tools']}.

✅ What you get:
• Done-for-you setup — no technical skills needed
• 100% free, open-source tools (you own it, no SaaS lock-in)
• {s['margin_note']}
• 7-day support after go-live

📦 Packages:
{bullet_tiers(tiers)}

🚀 How it works:
1. You tell me your call flow + tools (form on order)
2. I build, test, and voice-train the agent
3. I hand over + record a 5-min Loom walkthrough

⚡ Why me: I use the same free-tool stack that powers a 100-skill autonomous company.
"""
    return {
        "niche": niche_key,
        "package_title": s["title"],
        "price": price,
        "tags": s["tags"],
        "description": desc,
        "packages": tiers,
        "n8n_workflow": build_n8n_workflow(niche_key, s),
    }


def build_tiers(niche_key, price):
    return [
        {"name": "Basic", "price": max(price // 4, 200),
         "delivery": "3 days", "revisions": 1,
         "features": ["Single-line agent", "1 script", "Email support"]},
        {"name": "Standard", "price": price,
         "delivery": "5 days", "revisions": 2,
         "features": ["Full voice agent", "Booking/CRM hook", "Loom walkthrough", "7-day support"]},
        {"name": "Premium", "price": price * 2,
         "delivery": "7 days", "revisions": 3,
         "features": ["Multi-line + escalation", "Unlimited scripts", "Monthly retainer option", "Priority support"]},
    ]


def bullet_tiers(tiers):
    out = []
    for t in tiers:
        out.append(f"• {t['name']} (${t['price']}, {t['delivery']}, {t['revisions']} rev): "
                   + ", ".join(t["features"]))
    return "\n".join(out)


def build_n8n_workflow(niche_key, s):
    return {
        "name": f"deliver-voice-agent-{niche_key}",
        "nodes": [
            {"parameters": {}, "name": "Twilio/Webhook (inbound call)",
             "type": "n8n-nodes-base.webhook", "typeVersion": 1, "position": [0, 0]},
            {"parameters": {}, "name": "Whisper STT + Hermes agent",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [300, 0]},
            {"parameters": {}, "name": "Piper TTS + Chatwoot handoff",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [600, 0]},
        ],
        "connections": {
            "Twilio/Webhook (inbound call)": {"main": [[{"node": "Whisper STT + Hermes agent", "type": "main", "index": 0}]]},
            "Whisper STT + Hermes agent": {"main": [[{"node": "Piper TTS + Chatwoot handoff", "type": "main", "index": 0}]]},
        },
        "note": f"Tools: {s['tools']}. Replace code nodes with your STT/LLM/TTS logic.",
    }


def main():
    p = argparse.ArgumentParser(description="Voice AI Agent Deployer — Pipeline #13")
    p.add_argument("--niche", help="niche key: " + ", ".join(NICHE_TEMPLATES.keys()))
    p.add_argument("--price", type=int, help="override setup price")
    p.add_argument("--out", help="write package JSON to file")
    p.add_argument("--list", action="store_true", help="list niches")
    p.add_argument("cmd", nargs="?", default="self-test")
    a = p.parse_args()

    if a.list:
        for k, v in NICHE_TEMPLATES.items():
            print(f"  {k:12} {v['default_price']:>5}/setup  {v['title'][:48]}")
        return

    if a.cmd == "self-test" and not a.niche:
        for k in NICHE_TEMPLATES:
            pkg = build_package(k)
            assert pkg["package_title"] and pkg["description"] and len(pkg["packages"]) == 3
            assert pkg["n8n_workflow"]["name"].startswith("deliver-voice-agent-")
            # every tag must be a non-empty string
            assert all(isinstance(t, str) and t for t in pkg["tags"])
        print(f"self-test: OK — {len(NICHE_TEMPLATES)} niches, all generate valid packages + n8n stubs")
        return

    if not a.niche or a.niche not in NICHE_TEMPLATES:
        print("ERROR: --niche required. Choose from: " + ", ".join(NICHE_TEMPLATES.keys()))
        sys.exit(1)

    pkg = build_package(a.niche, a.price)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(pkg, f, indent=2)
        print(f"Wrote package JSON -> {a.out}")
    else:
        pkgs = ", ".join(f"{t['name']}(${t['price']})" for t in pkg["packages"])
        print(f"\n📦 PACKAGE: {pkg['package_title']}")
        print(f"💲 Setup: ${pkg['price']} | Tags: {', '.join(pkg['tags'][:5])}")
        print(f"📋 Tiers: {pkgs}")
        print(f"⚙️  n8n workflow: {pkg['n8n_workflow']['name']} ({len(pkg['n8n_workflow']['nodes'])} nodes)")


if __name__ == "__main__":
    main()
