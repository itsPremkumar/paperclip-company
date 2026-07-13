"""publish.py - publish a skill to ClawHub via the local `clawhub` CLI.

We shell out to `clawhub` (already authed as itsPremkumar). The function is
side-effecting (network) but is isolated so tests can mock it / skip it.
"""
import json
import os
import shutil
import subprocess
import sys


def _clawhub() -> str:
    exe = shutil.which("clawhub")
    return exe or "clawhub"


def is_available() -> bool:
    return shutil.which("clawhub") is not None


def publish_skill(folder: str, dry_run: bool = False) -> dict:
    """Publish a skill folder to ClawHub.

    Returns {published, rc, output, command}.
    """
    if not os.path.isdir(folder):
        return {"published": False, "rc": -1, "output": f"no such folder: {folder}", "command": ""}
    cmd = [_clawhub(), "publish", folder]
    if dry_run:
        return {"published": False, "rc": 0, "output": "dry-run (skipped)", "command": " ".join(cmd)}
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        out = (r.stdout + r.stderr).strip()
        published = r.returncode == 0 and "success" in out.lower()
        return {"published": published, "rc": r.returncode, "output": out, "command": " ".join(cmd)}
    except subprocess.TimeoutExpired:
        return {"published": False, "rc": -2, "output": "timed out", "command": " ".join(cmd)}
    except FileNotFoundError:
        return {"published": False, "rc": -3, "output": "clawhub CLI not found on PATH", "command": " ".join(cmd)}
