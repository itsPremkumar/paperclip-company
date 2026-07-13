# Agent Capability Manifest 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![agent](https://img.shields.io/badge/tag-agent-blue) ![caps](https://img.shields.io/badge/tag-caps-blue) ![security](https://img.shields.io/badge/tag-security-blue) ![manifest](https://img.shields.io/badge/tag-manifest-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![safety](https://img.shields.io/badge/tag-safety-blue)

Define, validate, and audit agent capability manifests for safe skill installation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Manifest schema validation
- Skill audit before install
- Capability diffing
- Risk scoring
- JSON output
- CI integration

## Commands

| Command | Description |
|---------|-------------|
| `validate <manifest>` | Validate capability manifest |
| `audit <skill>` | Audit a skill folder |
| `diff <a> <b>` | Compare manifests |
| `report <agent>` | Generate capability report |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-caps/main/agent_caps.py

# Run
python agent_caps.py self-test
```

## Why Agent Capability Manifest?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-caps)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-caps)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
