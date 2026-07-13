# Agent Guardrails 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![guardrails](https://img.shields.io/badge/tag-guardrails-blue) ![safety](https://img.shields.io/badge/tag-safety-blue) ![agent](https://img.shields.io/badge/tag-agent-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![security](https://img.shields.io/badge/tag-security-blue) ![policy](https://img.shields.io/badge/tag-policy-blue)

Enforce safety guardrails on agent actions: permission gates, allowlists, audit

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Permission gating
- Allowlist/denylist
- Policy definition
- Violation audit
- JSON output
- CI integration

## Commands

| Command | Description |
|---------|-------------|
| `check <action>` | Check if action is allowed |
| `policy <agent>` | Show agent policy |
| `audit <agent>` | Audit violations |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-guardrails/main/agent_guardrails.py

# Run
python agent_guardrails.py self-test
```

## Why Agent Guardrails?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-guardrails)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-guardrails)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
