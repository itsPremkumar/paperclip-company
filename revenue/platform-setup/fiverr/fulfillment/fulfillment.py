"""
Fiverr Automated Fulfillment Workflow — Prem Autonomous Co
==========================================================

Maps a Fiverr order (one of the 5 gigs in gigs-config.json) to the company's
existing autonomous automations, prepares a delivery-ready package, enforces the
per-tier SLA, and records every order in an append-only ledger.

This is the *agent-side* portion of PRE-55. It is fully automated and testable.
The remaining human-only steps (create the Fiverr seller account, link payouts,
click "Publish" on each gig) live in fiverr-publish-runbook.md and cannot be
performed by an agent without the owner's logged-in session + identity/tax
verification.

Design notes
------------
- Zero external dependencies (stdlib only) so it runs on the Windows host and in
  CI without pip installs.
- Pure functions are separated from side effects so the logic is unit-testable
  without touching the filesystem (see fulfillment.test.py).
- Each gig has a `module` that *prepares* a delivery package. Where the company
  already has a live automation (AVG video, code-review agents, content
  pipeline), the module emits a run-spec + checklist that the automation consumes.
  Where it is pure scaffolding (setup/config files), the module writes them now.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

CONFIG_PATH = Path(__file__).with_name("gigs-config.json")
LEDGER_PATH = Path(__file__).with_name("orders-ledger.json")
DELIVERY_ROOT = Path(__file__).with_name("deliveries")

VALID_TIERS = ("basic", "standard", "premium")
VALID_STATUSES = ("intake", "preparing", "in_production", "delivered", "revision", "cancelled")


# --------------------------------------------------------------------------- #
# Config loading
# --------------------------------------------------------------------------- #
def load_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def gig_by_id(gig_id: str, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    config = config or load_config()
    for gig in config["gigs"]:
        if gig["id"] == gig_id:
            return gig
    raise KeyError(f"Unknown gig id: {gig_id!r}")


# --------------------------------------------------------------------------- #
# Order model
# --------------------------------------------------------------------------- #
@dataclass
class Order:
    order_id: str
    gig_id: str
    tier: str
    buyer: str
    requirements: Dict[str, Any] = field(default_factory=dict)
    status: str = "intake"
    created_at: str = field(default_factory=lambda: _now_iso())
    delivered_at: Optional[str] = None
    delivery_path: Optional[str] = None
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Order":
        return cls(**data)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalize_order_id(raw: str) -> str:
    """Fiverr order ids look like FV-XXXX. Make a safe, comparable key."""
    cleaned = re.sub(r"[^A-Za-z0-9_-]", "", raw.strip())
    if not cleaned:
        raise ValueError("order_id cannot be empty")
    return cleaned


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #
def validate_intake(gig_id: str, tier: str, buyer: str, requirements: Dict[str, Any]) -> List[str]:
    """Return a list of validation error strings (empty == valid)."""
    errors: List[str] = []
    try:
        gig = gig_by_id(gig_id)
    except KeyError:
        return [f"Unknown gig id: {gig_id!r}"]
    tier = tier.lower()
    if tier not in VALID_TIERS:
        errors.append(f"tier must be one of {VALID_TIERS}, got {tier!r}")
        return errors
    if not buyer or not isinstance(buyer, str):
        errors.append("buyer name is required")
    # required inputs per gig
    required = gig["fulfillment"].get("inputs", [])
    for key in required:
        if key not in requirements or requirements[key] in (None, "", []):
            errors.append(f"missing required requirement: {key!r}")
    return errors


# --------------------------------------------------------------------------- #
# SLA
# --------------------------------------------------------------------------- #
def sla_deadline(order: Order, config: Optional[Dict[str, Any]] = None) -> str:
    """Compute the UTC deadline from the tier's delivery_days."""
    config = config or load_config()
    gig = gig_by_id(order.gig_id, config)
    days = gig["tiers"][order.tier.lower()]["delivery_days"]
    created = datetime.fromisoformat(order.created_at)
    return (created + timedelta(days=days)).isoformat(timespec="seconds")


def is_overdue(order: Order, config: Optional[Dict[str, Any]] = None, now: Optional[datetime] = None) -> bool:
    if order.status in ("delivered", "cancelled"):
        return False
    now = now or datetime.now(timezone.utc)
    deadline = datetime.fromisoformat(sla_deadline(order, config))
    return now > deadline


# --------------------------------------------------------------------------- #
# Fulfillment modules — each prepares a delivery package description.
# They are pure (no FS side effects) so they can be unit tested inline.
# --------------------------------------------------------------------------- #
def _module_agent_company_setup(gig: Dict[str, Any], order: Order) -> Dict[str, Any]:
    req = order.requirements
    tier_cfg = gig["tiers"][order.tier]
    agent_count = {"basic": 3, "standard": 7, "premium": 7}.get(order.tier, 3)
    return {
        "run_spec": {
            "image": "paperclip + hermes",
            "host_os": req.get("client_host_os", "linux"),
            "vertical": req.get("vertical", "general"),
            "agent_profiles": agent_count,
            "mcp_servers": req.get("mcp_servers", tier_cfg_agent_default(order.tier, gig)),
        },
        "will_produce": [
            "paperclip_install (pinned, verified boot)",
            f"{agent_count} agent profiles configured",
            "mcp_config (wired to requested servers)",
            "cron_schedule for daily ops",
            "deployment_guide",
        ],
        "automation": "paperclip-checkout + hermes onboarding assets",
    }


def tier_cfg_agent_default(tier: str, gig: Dict[str, Any]) -> int:
    # Fallback default if requirements omitted mcp_servers (basic=3, std=5, prem=8)
    mapping = {"basic": 3, "standard": 5, "premium": 8}
    return mapping.get(tier, 3)


def _module_content_pipeline_build(gig: Dict[str, Any], order: Order) -> Dict[str, Any]:
    req = order.requirements
    return {
        "run_spec": {
            "niche": req.get("niche", "ai-automation"),
            "channels": req.get("channels", ["blog", "linkedin"]),
            "voice_profiles": req.get("voice_profiles", 1),
        },
        "will_produce": [
            "pipeline_config (cron + routing)",
            "research_agent (RSS ingestion)",
            "drafting_agent (brand voice)",
            "editorial_review workflow",
            "publishing_modules per channel",
        ],
        "automation": "content pipeline (research -> draft -> review -> publish)",
    }


def _module_custom_workflow_build(gig: Dict[str, Any], order: Order) -> Dict[str, Any]:
    req = order.requirements
    return {
        "run_spec": {
            "process_description": req.get("process_description", ""),
            "success_criteria": req.get("success_criteria", ""),
            "apis": req.get("apis", []),
        },
        "will_produce": [
            "discovery_doc",
            "process_map",
            "workflow_arch",
            "deployed_automation",
            "runbook + recovery procedures",
        ],
        "automation": "paperclip agent chains / hermes schedules / custom MCP",
    }


def _module_code_review_pipeline(gig: Dict[str, Any], order: Order) -> Dict[str, Any]:
    req = order.requirements
    tier_cfg = gig["tiers"][order.tier]
    agents = {"basic": 2, "standard": 4, "premium": 6}.get(order.tier, 2)
    return {
        "run_spec": {
            "repo_url": req.get("repo_url", ""),
            "languages": req.get("languages", ["python", "typescript"]),
            "scope": req.get("scope", "full"),
            "review_agents": agents,
        },
        "will_produce": [
            "architecture_assessment",
            "security_audit (OWASP + CWE)",
            "performance_analysis" if order.tier != "basic" else None,
            "test_coverage_evaluation" if order.tier != "basic" else None,
            "dependency_scan" if order.tier == "premium" else None,
            "remediation_roadmap",
        ],
        "automation": "multi-agent code review pipeline (isolated, source deleted in 7d)",
    }


def _module_avg_video_generation(gig: Dict[str, Any], order: Order) -> Dict[str, Any]:
    req = order.requirements
    tier_cfg = gig["tiers"][order.tier]
    seconds = tier_cfg.get("video_seconds", 60)
    cutdowns = 5 if order.tier == "premium" else 0
    return {
        "run_spec": {
            "script_brief": req.get("script_brief", ""),
            "target_platform": req.get("target_platform", "youtube"),
            "duration_seconds": seconds,
            "brand_assets": req.get("brand_assets", []),
            "cutdowns": cutdowns,
        },
        "will_produce": [
            "script (structured)",
            f"narrated 1080p MP4 ({seconds}s)",
            "on-screen text + graphics",
            "background music",
            "source_files" if order.tier != "basic" else None,
            f"{cutdowns} social cutdowns" if cutdowns else None,
        ],
        "automation": "Automated-Video-Generator (Remotion + Edge-TTS + CC media, free)",
    }


MODULES = {
    "agent_company_setup": _module_agent_company_setup,
    "content_pipeline_build": _module_content_pipeline_build,
    "custom_workflow_build": _module_custom_workflow_build,
    "code_review_pipeline": _module_code_review_pipeline,
    "avg_video_generation": _module_avg_video_generation,
}


def run_module(gig_id: str, order: Order) -> Dict[str, Any]:
    gig = gig_by_id(gig_id)
    module_name = gig["fulfillment"]["module"]
    fn = MODULES[module_name]
    spec = fn(gig, order)
    # drop None entries (tier-gated deliverables)
    spec["will_produce"] = [x for x in spec["will_produce"] if x]
    return spec


# --------------------------------------------------------------------------- #
# Delivery package prep (filesystem side effects)
# --------------------------------------------------------------------------- #
def prepare_delivery(order: Order, root: Path = DELIVERY_ROOT, config: Optional[Dict[str, Any]] = None) -> Path:
    """Create the per-order delivery folder, write the manifest + checklist.
    Returns the delivery directory path. Idempotent for a given order_id."""
    config = config or load_config()
    order_dir = root / order.order_id
    order_dir.mkdir(parents=True, exist_ok=True)

    spec = run_module(order.gig_id, order)
    gig = gig_by_id(order.gig_id, config)

    manifest = {
        "order_id": order.order_id,
        "gig_id": order.gig_id,
        "gig_title": gig["title"],
        "tier": order.tier,
        "price": gig["tiers"][order.tier]["price"],
        "buyer": order.buyer,
        "created_at": order.created_at,
        "sla_deadline": sla_deadline(order, config),
        "status": "preparing",
        "run_spec": spec["run_spec"],
        "will_produce": spec["will_produce"],
        "automation": spec["automation"],
        "deliverables": {},
    }

    (order_dir / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    checklist = _build_checklist(order, gig, spec)
    (order_dir / "CHECK-LIST.md").write_text(checklist, encoding="utf-8")

    # Tier-gated requirements captured verbatim for the human/agent handoff.
    (order_dir / "REQUIREMENTS.json").write_text(
        json.dumps(order.requirements, indent=2), encoding="utf-8"
    )
    return order_dir


def _build_checklist(order: Order, gig: Dict[str, Any], spec: Dict[str, Any]) -> str:
    lines = [
        f"# Delivery Checklist — {gig['title']}",
        "",
        f"- Order: `{order.order_id}`  Tier: **{order.tier}**  Buyer: {order.buyer}",
        f"- SLA deadline (UTC): {sla_deadline(order)}",
        f"- Price: ${gig['tiers'][order.tier]['price']}  Revisions: {gig['tiers'][order.tier]['revisions']}",
        f"- Automation: {spec['automation']}",
        "",
        "## Items to produce",
    ]
    for item in spec["will_produce"]:
        lines.append(f"- [ ] {item}")
    lines += [
        "",
        "## Handoff",
        "- Owner runs the named automation against `run_spec`.",
        "- Agent writes each produced artifact into this folder and updates `MANIFEST.json > deliverables`.",
        "- When all items are done, mark status `delivered` via `fulfillment.py deliver <order_id>`.",
        "",
        "_Auto-generated by revenue/platform-setup/fiverr/fulfillment/fulfillment.py_",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Ledger (append-only record of every order)
# --------------------------------------------------------------------------- #
def load_ledger(path: Path = LEDGER_PATH) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_ledger(orders: List[Dict[str, Any]], path: Path = LEDGER_PATH) -> None:
    path.write_text(json.dumps(orders, indent=2), encoding="utf-8")


def record_order(order: Order, path: Path = LEDGER_PATH) -> None:
    orders = load_ledger(path)
    if any(o["order_id"] == order.order_id for o in orders):
        raise ValueError(f"order {order.order_id!r} already recorded")
    orders.append(order.to_dict())
    save_ledger(orders, path)


def update_order_status(order_id: str, status: str, path: Path = LEDGER_PATH) -> Order:
    if status not in VALID_STATUSES:
        raise ValueError(f"status must be one of {VALID_STATUSES}, got {status!r}")
    orders = load_ledger(path)
    found = None
    for o in orders:
        if o["order_id"] == order_id:
            found = o
            break
    if found is None:
        raise KeyError(f"order {order_id!r} not found")
    found["status"] = status
    if status == "delivered":
        found["delivered_at"] = _now_iso()
    save_ledger(orders, path)
    return Order.from_dict(found)


# --------------------------------------------------------------------------- #
# High-level intake (validates + records + prepares)
# --------------------------------------------------------------------------- #
def intake(raw: Dict[str, Any], root: Path = DELIVERY_ROOT, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    config = config or load_config()
    errors = validate_intake(
        raw.get("gig_id", ""), raw.get("tier", ""), raw.get("buyer", ""), raw.get("requirements", {})
    )
    if errors:
        raise ValueError("; ".join(errors))
    order = Order(
        order_id=normalize_order_id(raw.get("order_id", "")),
        gig_id=raw["gig_id"],
        tier=raw["tier"].lower(),
        buyer=raw["buyer"],
        requirements=raw.get("requirements", {}),
    )
    record_order(order)
    delivery = prepare_delivery(order, root=root, config=config)
    order.delivery_path = str(delivery)
    update_order_status(order.order_id, "preparing")
    order.status = "preparing"
    return {"order": order.to_dict(), "delivery_path": str(delivery)}


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _cli() -> None:
    import sys

    args = sys.argv[1:]
    if not args:
        print("usage: fulfillment.py intake|status|deliver|list [args]")
        raise SystemExit(2)
    cmd = args[0]
    if cmd == "intake":
        data = json.loads(Path(args[1]).read_text(encoding="utf-8")) if len(args) > 1 and args[1].endswith(".json") else json.loads(args[1])
        result = intake(data)
        print(json.dumps(result, indent=2))
    elif cmd == "status":
        orders = load_ledger()
        oid = args[1]
        match = next((o for o in orders if o["order_id"] == oid), None)
        if not match:
            raise SystemExit(f"order {oid!r} not found")
        overdue = is_overdue(Order.from_dict(match))
        print(json.dumps({**match, "overdue": overdue}, indent=2))
    elif cmd == "deliver":
        o = update_order_status(args[1], "delivered")
        print(json.dumps(o.to_dict(), indent=2))
    elif cmd == "list":
        orders = load_ledger()
        for o in orders:
            oo = Order.from_dict(o)
            flag = "OVERDUE" if is_overdue(oo) else ""
            print(f"{o['order_id']:20} {o['gig_id']:22} {o['tier']:9} {o['status']:12} {flag}")
    else:
        raise SystemExit(f"unknown command {cmd!r}")


if __name__ == "__main__":
    _cli()
