#!/usr/bin/env python3
"""
skill-lint.py - validate a ClawHub/OpenClaw skill folder before publishing.

Checks the required shape: SKILL.md with YAML frontmatter (name/version/description/
tags), no nested skill dirs, README present or optional, and flags common rejects
(missing frontmatter, bad version, huge files). Zero deps.

Usage:
  python skill-lint.py check <folder> [--json]
  python skill-lint.py self-test
"""
import argparse
import json
import os
import re
import sys

FRONT = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
REQUIRED = ["name", "version", "description"]


def check(folder, as_json):
    issues = []
    skill = os.path.join(folder, "SKILL.md")
    if not os.path.isfile(skill):
        issues.append("MISSING: SKILL.md")
    else:
        txt = open(skill, encoding="utf-8").read()
        m = FRONT.match(txt)
        if not m:
            issues.append("MISSING: YAML frontmatter (--- ... ---)")
        else:
            fm = m.group(1)
            for key in REQUIRED:
                if not re.search(rf'^{key}\s*:', fm, re.M):
                    issues.append(f"MISSING frontmatter field: {key}")
            if not re.search(r'version:\s*[\d.]+', fm):
                issues.append("version not semver-ish")
        if len(txt) > 60_000:
            issues.append("SKILL.md over 60KB (likely too large)")
    # nested skill dirs not allowed
    for root, dirs, _ in os.walk(folder):
        for d in dirs:
            if d in ("skills", "node_modules", ".git"):
                issues.append(f"nested dir not allowed: {d}")
    # large binaries
    for root, _, fs in os.walk(folder):
        for fn in fs:
            fp = os.path.join(root, fn)
            if os.path.getsize(fp) > 500_000:
                issues.append(f"large file: {fn} (>500KB)")
    ok = len(issues) == 0
    res = {"folder": os.path.abspath(folder), "valid": ok, "issues": issues}
    print(json.dumps(res, indent=2) if as_json else ("VALID" if ok else "INVALID:\n - " + "\n - ".join(issues)))
    return res


def self_test():
    import tempfile, shutil
    d = tempfile.mkdtemp()
    open(os.path.join(d, "SKILL.md"), "w").write("---\nname: x\nversion: 1.0.0\ndescription: y\n---\nbody\n")
    good = check(d, False)
    shutil.rmtree(d)
    bad_d = tempfile.mkdtemp()
    open(os.path.join(bad_d, "README.md"), "w").write("no skill md")
    bad = check(bad_d, False)
    shutil.rmtree(bad_d)
    ok = good["valid"] and not bad["valid"]
    print("self-test:", "PASS" if ok else "FAIL", f"(good={good['valid']} bad={bad['valid']})")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser(description="skill-lint")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("folder"); c.add_argument("--json", action="store_true")
    sub.add_parser("self-test")
    a = p.parse_args()
    if a.cmd == "self-test": return self_test()
    if a.cmd == "check": check(a.folder, a.json); return 0


if __name__ == "__main__":
    sys.exit(main())
