# Agent Cost Tracker 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![cost](https://img.shields.io/badge/tag-cost-blue) ![tracking](https://img.shields.io/badge/tag-tracking-blue) ![llm](https://img.shields.io/badge/tag-llm-blue) ![budget](https://img.shields.io/badge/tag-budget-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![finance](https://img.shields.io/badge/tag-finance-blue)

Track LLM API spending per agent/session with budget alerts and CSV export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Per-agent cost tracking
- Session-level attribution
- Budget alerts
- CSV export
- Daily/weekly rollups
- JSON output

## Commands

| Command | Description |
|---------|-------------|
| `track <agent> <cost>` | Log a cost event |
| `report` | Generate cost report |
| `budget <agent> <limit>` | Set budget |
| `alerts` | Show budget alerts |
| `export` | Export to CSV |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-cost-tracker/main/agent_cost_tracker.py

# Run
python agent_cost_tracker.py self-test
```

## Why Agent Cost Tracker?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-cost-tracker)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-cost-tracker)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
