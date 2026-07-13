"""Unit tests for the Fiverr automated fulfillment workflow (PRE-55)."""
import importlib.util
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SPEC = importlib.util.spec_from_file_location("fulfillment", HERE / "fulfillment.py")
fulfillment = importlib.util.module_from_spec(SPEC)
sys.modules["fulfillment"] = fulfillment
SPEC.loader.exec_module(fulfillment)


def _sample_order(gig_id="code-review", tier="basic", req=None):
    return {
        "order_id": "FV-TEST-001",
        "gig_id": gig_id,
        "tier": tier,
        "buyer": "Acme Corp",
        "requirements": req or {"repo_url": "https://github.com/acme/app", "languages": ["python"]},
    }


def test_config_has_all_five_gigs(tmp_path):
    config = fulfillment.load_config()
    ids = {g["id"] for g in config["gigs"]}
    assert ids == {
        "ai-company-setup",
        "content-pipeline",
        "custom-ai-workflows",
        "code-review",
        "video-creation",
    }


def test_prices_match_issue_spec(tmp_path):
    config = fulfillment.load_config()
    prices = {g["id"]: (g["starting_price"], sorted(g["tiers"].items())) for g in config["gigs"]}
    # verify starting price == cheapest tier price
    for g in config["gigs"]:
        cheapest = min(t["price"] for t in g["tiers"].values())
        assert g["starting_price"] == cheapest


def test_validate_intake_rejects_bad_tier(tmp_path):
    errs = fulfillment.validate_intake("code-review", "platinum", "Acme", {"repo_url": "x"})
    assert any("tier" in e for e in errs)


def test_validate_intake_rejects_missing_requirement(tmp_path):
    errs = fulfillment.validate_intake("code-review", "basic", "Acme", {})
    assert any("repo_url" in e for e in errs)


def test_validate_intake_ok(tmp_path):
    errs = fulfillment.validate_intake("code-review", "basic", "Acme", {"repo_url": "x"})
    assert errs == []


def test_run_module_video_premium_includes_cutdowns(tmp_path):
    order = fulfillment.Order("FV-1", "video-creation", "premium", "Acme",
                              {"script_brief": "demo", "target_platform": "youtube"})
    spec = fulfillment.run_module("video-creation", order)
    assert any("5 social cutdowns" in p for p in spec["will_produce"])
    assert spec["run_spec"]["duration_seconds"] == 180


def test_run_module_video_basic_no_cutdowns(tmp_path):
    order = fulfillment.Order("FV-2", "video-creation", "basic", "Acme",
                              {"script_brief": "demo"})
    spec = fulfillment.run_module("video-creation", order)
    assert not any("cutdowns" in p for p in spec["will_produce"])
    assert spec["run_spec"]["duration_seconds"] == 60


def test_sla_deadline_basic_code_review_48h(tmp_path):
    order = fulfillment.Order("FV-3", "code-review", "basic", "Acme", {"repo_url": "x"})
    deadline = datetime.fromisoformat(fulfillment.sla_deadline(order))
    created = datetime.fromisoformat(order.created_at)
    assert (deadline - created) == timedelta(days=2)


def test_is_overdue(tmp_path):
    old = datetime.now(timezone.utc) - timedelta(days=10)
    order = fulfillment.Order("FV-4", "code-review", "basic", "Acme", {"repo_url": "x"})
    order.created_at = old.isoformat()
    assert fulfillment.is_overdue(order) is True
    delivered = fulfillment.Order("FV-5", "code-review", "basic", "Acme", {"repo_url": "x"})
    delivered.status = "delivered"
    assert fulfillment.is_overdue(delivered) is False


def test_intake_records_and_prepares(tmp_path):
    ledger = tmp_path / "ledger.json"
    delivery = tmp_path / "deliveries"
    result = fulfillment.intake(_sample_order(), root=delivery,
                                config=fulfillment.load_config())
    assert result["delivery_path"]
    man = Path(result["delivery_path"]) / "MANIFEST.json"
    assert man.exists()
    check = Path(result["delivery_path"]) / "CHECK-LIST.md"
    assert check.exists()
    manifest = json.loads(man.read_text())
    assert manifest["status"] == "preparing"
    # ledger recorded
    orders = fulfillment.load_ledger(ledger)
    assert any(o["order_id"] == "FV-TEST-001" for o in orders)


def test_intake_rejects_duplicate(tmp_path):
    fulfillment.intake(_sample_order(), root=tmp_path / "d", config=fulfillment.load_config())
    with pytest.raises(ValueError):
        fulfillment.intake(_sample_order(), root=tmp_path / "d", config=fulfillment.load_config())


def test_deliver_sets_status_and_timestamp(tmp_path):
    fulfillment.intake(_sample_order(), root=tmp_path / "d", config=fulfillment.load_config())
    o = fulfillment.update_order_status("FV-TEST-001", "delivered", path=tmp_path / "ledger.json")
    assert o.status == "delivered"
    assert o.delivered_at is not None


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
