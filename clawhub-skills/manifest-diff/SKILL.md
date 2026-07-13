---
name: manifest-diff
version: 2.0.0
description: Diff agent/skill manifests: capabilities, permissions, versions
tags: ["diff", "manifest", "agent", "cli", "audit", "security"]
---

# Manifest Diff v2 🚀

Diff agent/skill manifests: capabilities, permissions, versions

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Capability diffing | Capability diffing |
| Permission comparison | Permission comparison |
| Version tracking | Version tracking |
| JSON output | JSON output |
| CI integration | CI integration |
| Risk highlighting | Risk highlighting |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/manifest-diff/main/manifest_diff.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python manifest_diff.py diff <a> <b>` | Diff two manifests |
| `python manifest_diff.py capabilities <m>` | Show capabilities |
| `python manifest_diff.py permissions <m>` | Show permissions |
| `python manifest_diff.py self-test` | Run built-in tests |

## Features

- **Capability diffing**
- **Permission comparison**
- **Version tracking**
- **JSON output**
- **CI integration**
- **Risk highlighting**

## Example

```bash
python manifest_diff.py self-test
```

## CI Integration

```yaml
# .github/workflows/verify.yml
name: Verify
on: [push]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Self-test
        run: python manifest_diff.py self-test
```

## Why

Manifest Diff is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/manifest-diff)
