# Agent Logger 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![logging](https://img.shields.io/badge/tag-logging-blue) ![agent](https://img.shields.io/badge/tag-agent-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![observability](https://img.shields.io/badge/tag-observability-blue) ![json](https://img.shields.io/badge/tag-json-blue) ![audit](https://img.shields.io/badge/tag-audit-blue)

Structured logging for agents: JSON logs, rotation, query, and replay

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Structured JSON logs
- Log rotation
- Query/filter
- Session replay
- Tail mode
- Audit trail

## Commands

| Command | Description |
|---------|-------------|
| `log <msg>` | Write a log entry |
| `query <filter>` | Query logs |
| `replay <session>` | Replay a session |
| `tail` | Follow live logs |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/agent-logger/main/agent_logger.py

# Run
python agent_logger.py self-test
```

## Why Agent Logger?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/agent-logger)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/agent-logger)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
