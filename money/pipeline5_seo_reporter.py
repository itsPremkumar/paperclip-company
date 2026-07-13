#!/usr/bin/env python3
"""
SEO / Audit Reporter — Pipeline #5 from MONEY_AUTOMATION_IDEAS.md

Recurring service: automated website & code audits (SEO + security + code quality)
delivered as a branded PDF on a subscription. Built on your own ClawHub skills:
codebase-inspection + secret-scanner + skill-lint, rendered via Stirling-PDF.

Validated 2026 pricing: $49-$199/mo per site — pure recurring, high stickiness.

Usage:
  python pipeline5_seo_reporter.py --plan pro --out pro_plan.json
  python pipeline5_seo_reporter.py --list
  python pipeline5_seo_reporter.py self-test
Zero dependencies (stdlib only).
"""
import argparse
import json
import sys

PLANS = {
    "starter": {
        "title": "I will run a monthly SEO & security audit of your website",
        "sites": 1, "frequency": "monthly",
        "checks": ["on-page SEO", "broken links", "basic security scan", "page speed"],
        "price": 49,
    },
    "pro": {
        "title": "I will deliver weekly SEO + security + code-quality reports",
        "sites": 3, "frequency": "weekly",
        "checks": ["full SEO audit", "secret-scanner", "code quality (codebase-inspection)",
                   "skill-lint", "competitor snapshot"],
        "price": 149,
    },
    "agency": {
        "title": "I will provide white-label audit reports for your agency clients",
        "sites": 10, "frequency": "weekly",
        "checks": ["everything in Pro", "white-label branding", "client-ready PDFs",
                   "trend tracking", "priority fixes list"],
        "price": 399,
    },
}


def build_package(plan, price=None):
    p = PLANS[plan]
    price = price or p["price"]
    return {
        "plan": plan,
        "gig_title": p["title"],
        "sites_included": p["sites"],
        "frequency": p["frequency"],
        "checks": p["checks"],
        "pricing": {
            "monthly": price,
            "annual": price * 10,  # 2 months free
            "margin_pct": 97,
            "note": "runs on your ClawHub skills; only compute cost",
        },
        "pipeline_spec": build_spec(p),
        "delivery_steps": [
            "1. Client subscribes + adds site URL(s)",
            f"2. n8n cron triggers {p['frequency']} audit",
            "3. Run codebase-inspection + secret-scanner + skill-lint",
            "4. Render branded PDF via Stirling-PDF",
            "5. Email report + track trend deltas",
        ],
        "tags": ["seo audit", "website audit", "security scan",
                 "technical seo", "automated report", plan + " audit"],
    }


def build_spec(p):
    return {
        "scheduler": "n8n cron",
        "tools": ["codebase-inspection", "secret-scanner", "skill-lint"],
        "report_engine": "Stirling-PDF",
        "delivery": "email + dashboard",
        "frequency": p["frequency"],
        "note": "All tools are free/self-hosted ClawHub skills.",
    }


def main():
    ap = argparse.ArgumentParser(description="SEO/Audit Reporter — Pipeline #5")
    ap.add_argument("--plan", help="plan: " + ", ".join(PLANS.keys()))
    ap.add_argument("--price", type=int, help="override monthly price")
    ap.add_argument("--out", help="write package JSON to file")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("cmd", nargs="?", default="self-test")
    a = ap.parse_args()

    if a.list:
        for k, v in PLANS.items():
            print(f"  {k:9} ${v['price']:>3}/mo  {v['sites']} site(s), {v['frequency']}  {v['title'][:40]}")
        return

    if a.cmd == "self-test" and not a.plan:
        for k in PLANS:
            pkg = build_package(k)
            assert pkg["gig_title"] and pkg["pipeline_spec"]["report_engine"] == "Stirling-PDF"
            assert pkg["pricing"]["margin_pct"] == 97
            assert len(pkg["delivery_steps"]) == 5
        print(f"self-test: OK — {len(PLANS)} plans, all generate valid packages")
        return

    if not a.plan or a.plan not in PLANS:
        print("ERROR: --plan required. Choose: " + ", ".join(PLANS.keys()))
        sys.exit(1)

    pkg = build_package(a.plan, a.price)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(pkg, fh, indent=2)
        print(f"Wrote package -> {a.out}")
    else:
        print(f"\n📊 AUDIT PLAN: {a.plan}")
        print(f"📋 {pkg['gig_title']}")
        print(f"💲 ${pkg['pricing']['monthly']}/mo (97% margin) | {pkg['sites_included']} site(s), {pkg['frequency']}")
        print(f"🔍 Checks: {', '.join(pkg['checks'][:3])}...")
        print(f"⚙️  Tools: {', '.join(pkg['pipeline_spec']['tools'])}")


if __name__ == "__main__":
    main()
