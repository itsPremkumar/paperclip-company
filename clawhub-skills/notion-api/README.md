# Notion API Toolkit 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![notion](https://img.shields.io/badge/tag-notion-blue) ![api](https://img.shields.io/badge/tag-api-blue) ![notes](https://img.shields.io/badge/tag-notes-blue) ![database](https://img.shields.io/badge/tag-database-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![productivity](https://img.shields.io/badge/tag-productivity-blue)

Complete Notion API client: pages, databases, blocks, search with config file and dry-run mode

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Full Notion API coverage
- Config file support (notion_config.json)
- Markdown → blocks converter
- Dry-run mode for safety
- JSON/text output
- Env var override for API key

## Commands

| Command | Description |
|---------|-------------|
| `list-pages` | List all pages |
| `get-page <id>` | Get page content |
| `search <query>` | Search workspace |
| `create-page` | Create a new page |
| `update-page <id>` | Update page properties |
| `append-blocks <id>` | Append content blocks |
| `list-databases` | List databases |
| `query-database <id>` | Query a database |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/notion-api/main/notion_api.py

# Run
python notion_api.py self-test
```

## Why Notion API Toolkit?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/notion-api)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/notion-api)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
