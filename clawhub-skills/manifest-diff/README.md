# Manifest Diff 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![diff](https://img.shields.io/badge/tag-diff-blue) ![manifest](https://img.shields.io/badge/tag-manifest-blue) ![agent](https://img.shields.io/badge/tag-agent-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![audit](https://img.shields.io/badge/tag-audit-blue) ![security](https://img.shields.io/badge/tag-security-blue)

Diff agent/skill manifests: capabilities, permissions, versions

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Capability diffing
- Permission comparison
- Version tracking
- JSON output
- CI integration
- Risk highlighting

## Commands

| Command | Description |
|---------|-------------|
| `diff <a> <b>` | Diff two manifests |
| `capabilities <m>` | Show capabilities |
| `permissions <m>` | Show permissions |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/manifest-diff/main/manifest_diff.py

# Run
python manifest_diff.py self-test
```

## Why Manifest Diff?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/manifest-diff)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/manifest-diff)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
