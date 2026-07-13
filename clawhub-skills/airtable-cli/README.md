# Airtable CLI 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![airtable](https://img.shields.io/badge/tag-airtable-blue) ![api](https://img.shields.io/badge/tag-api-blue) ![database](https://img.shields.io/badge/tag-database-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![spreadsheet](https://img.shields.io/badge/tag-spreadsheet-blue) ![automation](https://img.shields.io/badge/tag-automation-blue)

Airtable API client: bases, tables, records with pagination, CSV import/export, rate-limit awareness

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Full Airtable API coverage
- Pagination support
- CSV import/export
- Field filtering
- Rate-limit awareness
- Config file (airtable_config.json)

## Commands

| Command | Description |
|---------|-------------|
| `list-bases` | List all bases |
| `list-tables <base>` | List tables in a base |
| `list-records <base> <table>` | List records |
| `get-record <base> <table> <id>` | Get one record |
| `create-record` | Create a record |
| `update-record` | Update a record |
| `delete-record` | Delete a record |
| `query <base> <table>` | Query with filter |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/airtable-cli/main/airtable_cli.py

# Run
python airtable_cli.py self-test
```

## Why Airtable CLI?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/airtable-cli)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/airtable-cli)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
