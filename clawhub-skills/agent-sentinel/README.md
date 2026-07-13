# Agent Sentinel 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![security](https://img.shields.io/badge/tag-security-blue) ![audit](https://img.shields.io/badge/tag-audit-blue) ![skill](https://img.shields.io/badge/tag-skill-blue) ![openclaw](https://img.shields.io/badge/tag-openclaw-blue) ![hermes](https://img.shields.io/badge/tag-hermes-blue) ![vetting](https://img.shields.io/badge/tag-vetting-blue)

Scan OpenClaw/Hermes skills for risky permission patterns before installation

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Simple-named skill requesting shell → HIGH
- Shell/exec capability requested → MEDIUM
- Hardcoded secret detection → HIGH
- No human approval gate → LOW
- Network egress without reason
- Offline, private, no telemetry

## Commands

| Command | Description |
|---------|-------------|
| `scan <skill-folder>` | Risk report for a skill |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-sentinel/main/agent_sentinel.py

# Run
python agent_sentinel.py self-test
```

## Why Agent Sentinel?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-sentinel)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-sentinel)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
