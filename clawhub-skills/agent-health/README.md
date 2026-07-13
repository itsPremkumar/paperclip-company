# Agent Health Monitor 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![health](https://img.shields.io/badge/tag-health-blue) ![monitor](https://img.shields.io/badge/tag-monitor-blue) ![agent](https://img.shields.io/badge/tag-agent-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![observability](https://img.shields.io/badge/tag-observability-blue) ![alerts](https://img.shields.io/badge/tag-alerts-blue)

Monitor agent endpoints, check liveness, collect metrics, alert on failures

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Endpoint liveness checks
- Metric collection
- Failure alerting
- Watch mode
- JSON output
- Multi-agent support

## Commands

| Command | Description |
|---------|-------------|
| `check <endpoint>` | Health check an agent |
| `metrics <agent>` | Collect metrics |
| `watch <agent>` | Continuous monitoring |
| `alerts` | Show active alerts |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-health/main/agent_health.py

# Run
python agent_health.py self-test
```

## Why Agent Health Monitor?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-health)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-health)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
