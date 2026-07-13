"""testrunner.py - run skill tests and report structured results.

Two modes:
  - run_self_test(tool_path): `python <tool>.py self-test` -> (passed, output)
  - run_portfolio(folder): reuse the studio's 7-axis harness if present, else a
    lightweight check, returning a result dict the UI can render.

Pure-ish: only touches the given folder + subprocess. No network.
"""
import json
import os
import subprocess
import sys


def run_self_test(tool_path: str, timeout: int = 60) -> dict:
    """Run `<tool>.py self-test` and return {passed, rc, output}."""
    if not os.path.isfile(tool_path):
        return {"passed": False, "rc": -1, "output": f"no such file: {tool_path}"}
    try:
        r = subprocess.run(
            [sys.executable, tool_path, "self-test"],
            capture_output=True, text=True, timeout=timeout,
        )
        out = (r.stdout + r.stderr).strip()
        passed = r.returncode == 0 and "PASS" in out
        return {"passed": passed, "rc": r.returncode, "output": out}
    except subprocess.TimeoutExpired:
        return {"passed": False, "rc": -2, "output": f"timed out after {timeout}s"}


def run_portfolio(folder: str) -> dict:
    """Run the studio 7-axis harness against a skill folder.

    Falls back to a minimal self-test scan if the harness isn't available.
    """
    harness = os.path.join(os.path.dirname(__file__), "..", "ci", "verify_product.py")
    harness = os.path.abspath(harness)
    if os.path.isfile(harness):
        r = subprocess.run(
            [sys.executable, harness, folder],
            capture_output=True, text=True, timeout=120,
        )
        out = (r.stdout + r.stderr).strip()
        passed = r.returncode == 0 and "RESULT: PASS" in out
        return {"passed": passed, "rc": r.returncode, "output": out}
    # fallback: find a tool with self-test
    tools = [f for f in os.listdir(folder) if f.endswith(".py") and not f.startswith("_")]
    if not tools:
        return {"passed": False, "rc": -1, "output": "no .py tool found in folder"}
    res = run_self_test(os.path.join(folder, tools[0]))
    return {"passed": res["passed"], "rc": res["rc"], "output": res["output"]}


def summarize(run_result: dict) -> str:
    return "PASS" if run_result.get("passed") else "FAIL"
