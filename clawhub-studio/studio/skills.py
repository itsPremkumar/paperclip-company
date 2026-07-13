"""skills.py - skill domain model, validation, and helpers for ClawHub Studio.

A "skill" in the studio has:
  - a slug (id) and name
  - one or more versions (semver), each carrying a manifest (the SKILL.md frontmatter
    as JSON) and status (draft | ready | published) and a published flag
  - runs (test results) per version

This module is pure logic: no I/O except what callers pass in. Persistence lives in db.py.
"""
import re
import json

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
REQUIRED_FIELDS = ("name", "version", "description")


def parse_skill_md(text: str) -> dict:
    """Parse a SKILL.md into {"frontmatter": {...}, "body": str}.

    Frontmatter is the YAML-ish block between the first two '---' lines.
    We only support simple `key: value` pairs (no nested structures) to stay
    zero-dependency and safe.
    """
    if not text.startswith("---"):
        return {"frontmatter": {}, "body": text}
    end = text.find("\n---", 3)
    if end == -1:
        return {"frontmatter": {}, "body": text}
    block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in block.splitlines():
        if not line.strip() or ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return {"frontmatter": fm, "body": body}


def validate_manifest(manifest: dict) -> list:
    """Return a list of error strings (empty == valid)."""
    errs = []
    if not isinstance(manifest, dict):
        return ["manifest must be a JSON object"]
    for f in REQUIRED_FIELDS:
        if not manifest.get(f):
            errs.append(f"missing required field: {f}")
    ver = manifest.get("version")
    if ver and not SEMVER.match(str(ver)):
        errs.append(f"version {ver!r} is not semver (x.y.z)")
    return errs


def status_of(manifest: dict, has_tests: bool, published: bool) -> str:
    """Derive a skill version's status for the UI."""
    if published:
        return "published"
    if validate_manifest(manifest):
        return "draft"  # invalid -> still draft
    if has_tests:
        return "ready"
    return "draft"


def bump_version(version: str, part: str = "patch") -> str:
    """Return the next semver for part in {major,minor,patch}."""
    if not SEMVER.match(str(version)):
        raise ValueError(f"not semver: {version!r}")
    major, minor, patch = (int(x) for x in str(version).split("."))
    if part == "major":
        major += 1; minor = 0; patch = 0
    elif part == "minor":
        minor += 1; patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError(f"unknown bump part: {part!r}")
    return f"{major}.{minor}.{patch}"


def manifest_to_skill_md(manifest: dict, body: str = "") -> str:
    """Serialize a manifest back to a SKILL.md string."""
    lines = ["---"]
    for k in ("name", "version", "description"):
        if manifest.get(k):
            lines.append(f"{k}: {manifest[k]}")
    for k, v in manifest.items():
        if k in ("name", "version", "description"):
            continue
        lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(body or "# Skill\n\n(add usage / notes here)")
    return "\n".join(lines)
