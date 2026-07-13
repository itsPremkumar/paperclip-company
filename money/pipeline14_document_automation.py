#!/usr/bin/env python3
"""
Document Automation Service — Pipeline #14 (from research/MONEY_IDEAS_2026.md, rank #5)

Generates ready-to-sell document-automation service packages (title, description,
3 tiers, SEO tags) + an importable n8n workflow JSON for delivery automation.

Validated 2026 market data (see research/MONEY_IDEAS_2026.md for full citations):
  - PDF/document automation is a live Fiverr category: fiverr.com/gigs/pdf-automation
  - AI document-processing SaaS tier benchmarks: $49–$199/mo (broad market)
  - Free stack: Stirling-PDF (github.com/Stirling-Tools/Stirling-PDF) + Docling
    (github.com/DS4SD/docling) + n8n (n8n.io) + your doc-extractor skill — all OSS.

Usage:
  python pipeline14_document_automation.py --service "pdf-extract" --price 149
  python pipeline14_document_automation.py --list
  python pipeline14_document_automation.py --service contract-gen --out doc.json
  python pipeline14_document_automation.py self-test
Zero dependencies (stdlib only).
"""
import argparse
import json
import sys

# ---- Validated 2026 pricing data (document-automation services) ----
SERVICES = {
    "pdf-extract": {
        "title": "I will automate PDF extraction & data entry with free open-source tools",
        "outcome": "a workflow that turns messy PDFs/invoices into clean CSV/JSON — zero manual typing",
        "tools": "Stirling-PDF + Docling + n8n + your doc-extractor skill — all free/self-hosted",
        "margin_note": "Charge $99–$299 setup + $49–$149/mo; your cost $0 (self-hosted)",
        "tags": ["pdf automation", "data extraction", "invoice processing", "stirling pdf",
                 "docling", "n8n", "document automation", "pdf to excel"],
        "default_price": 149,
    },
    "contract-gen": {
        "title": "I will generate your legal contracts & proposals from a simple form",
        "outcome": "a tailored, legally-structured doc generated automatically from intake answers",
        "tools": "DocAssemble + Stirling-PDF + Hermes drafting + your doc-extractor skill — all free",
        "margin_note": "Charge $50–$300/doc, ~$0 AI cost",
        "tags": ["legal document", "contract generator", "proposal writer", "nda",
                 "docassemble", "pdf automation", "freelance contract"], "default_price": 120,
    },
    "doc-redact": {
        "title": "I will auto-redact & watermark sensitive PDFs at scale",
        "outcome": "a batch pipeline that finds PII, redacts it, and watermarks every page",
        "tools": "Stirling-PDF + n8n + your secret-scanner skill — all free/self-hosted",
        "margin_note": "Charge $149–$399 setup + $79–$199/mo per client",
        "tags": ["pdf redaction", "pii removal", "document security", "stirling pdf",
                 "data privacy", "batch pdf", "compliance automation"], "default_price": 199,
    },
    "form-to-doc": {
        "title": "I will turn your forms & surveys into branded PDF reports",
        "outcome": "a pipeline that ingests form responses and emails a branded PDF report instantly",
        "tools": "Stirling-PDF + n8n + Listmonk (email) — all free/self-hosted",
        "margin_note": "Charge $99–$249 setup + $49–$129/mo",
        "tags": ["pdf report", "form automation", "survey to pdf", "stirling pdf",
                 "n8n", "branded documents", "report automation"], "default_price": 149,
    },
}


def build_package(service_key, price=None):
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
1. You tell me your document types/goals (form on order)
2. I build & test the automation
3. I hand over + record a 5-min Loom walkthrough

⚡ Why me: I use the same tools that power a 100-skill autonomous company.
"""
    return {
        "service": service_key,
        "package_title": s["title"],
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
         "features": ["Single template", "1 workflow", "Email support"]},
        {"name": "Standard", "price": price,
         "delivery": "5 days", "revisions": 2,
         "features": ["Setup + test", "Up to 3 templates", "Loom walkthrough", "7-day support"]},
        {"name": "Premium", "price": price * 2,
         "delivery": "7 days", "revisions": 3,
         "features": ["Full system", "Unlimited templates", "Monthly retainer option", "Priority support"]},
    ]


def bullet_tiers(tiers):
    out = []
    for t in tiers:
        out.append(f"• {t['name']} (${t['price']}, {t['delivery']}, {t['revisions']} rev): "
                   + ", ".join(t["features"]))
    return "\n".join(out)


def build_n8n_workflow(service_key, s):
    return {
        "name": f"deliver-doc-{service_key}",
        "nodes": [
            {"parameters": {}, "name": "Webhook (intake)",
             "type": "n8n-nodes-base.webhook", "typeVersion": 1, "position": [0, 0]},
            {"parameters": {}, "name": "Stirling-PDF / Docling transform",
             "type": "n8n-nodes-base.code", "typeVersion": 1, "position": [300, 0]},
            {"parameters": {}, "name": "Deliver + notify",
             "type": "n8n-nodes-base.emailSend", "typeVersion": 1, "position": [600, 0]},
        ],
        "connections": {
            "Webhook (intake)": {"main": [[{"node": "Stirling-PDF / Docling transform", "type": "main", "index": 0}]]},
            "Stirling-PDF / Docling transform": {"main": [[{"node": "Deliver + notify", "type": "main", "index": 0}]]},
        },
        "note": f"Tools: {s['tools']}. Replace code node with your doc logic.",
    }


def main():
    p = argparse.ArgumentParser(description="Document Automation Service — Pipeline #14")
    p.add_argument("--service", help="service key: " + ", ".join(SERVICES.keys()))
    p.add_argument("--price", type=int, help="override price")
    p.add_argument("--out", help="write package JSON to file")
    p.add_argument("--list", action="store_true", help="list services")
    p.add_argument("cmd", nargs="?", default="self-test")
    a = p.parse_args()

    if a.list:
        for k, v in SERVICES.items():
            print(f"  {k:14} {v['default_price']:>5}/gig  {v['title'][:46]}")
        return

    if a.cmd == "self-test" and not a.service:
        for k in SERVICES:
            pkg = build_package(k)
            assert pkg["package_title"] and pkg["description"] and len(pkg["packages"]) == 3
            assert pkg["n8n_workflow"]["name"].startswith("deliver-doc-")
            assert all(isinstance(t, str) and t for t in pkg["tags"])
        print(f"self-test: OK — {len(SERVICES)} services, all generate valid packages + n8n stubs")
        return

    if not a.service or a.service not in SERVICES:
        print("ERROR: --service required. Choose from: " + ", ".join(SERVICES.keys()))
        sys.exit(1)

    pkg = build_package(a.service, a.price)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(pkg, f, indent=2)
        print(f"Wrote package JSON -> {a.out}")
    else:
        pkgs = ", ".join(f"{t['name']}(${t['price']})" for t in pkg["packages"])
        print(f"\n📦 PACKAGE: {pkg['package_title']}")
        print(f"💲 Price: ${pkg['price']} | Tags: {', '.join(pkg['tags'][:5])}")
        print(f"📋 Packages: {pkgs}")
        print(f"⚙️  n8n workflow: {pkg['n8n_workflow']['name']} ({len(pkg['n8n_workflow']['nodes'])} nodes)")


if __name__ == "__main__":
    main()
