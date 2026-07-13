---
name: notion-api
version: 2.0.0
description: Complete Notion API client: pages, databases, blocks, search with config file and dry-run mode
tags: ["notion", "api", "notes", "database", "cli", "productivity"]
---

# Notion API Toolkit v2 🚀

Complete Notion API client: pages, databases, blocks, search with config file and dry-run mode

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Full Notion API coverage | Full Notion API coverage |
| Config file support (notion_co | Config file support (notion_config.json) |
| Markdown → blocks converter | Markdown → blocks converter |
| Dry-run mode for safety | Dry-run mode for safety |
| JSON/text output | JSON/text output |
| Env var override for API key | Env var override for API key |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/notion-api/main/notion_api.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python notion_api.py list-pages` | List all pages |
| `python notion_api.py get-page <id>` | Get page content |
| `python notion_api.py search <query>` | Search workspace |
| `python notion_api.py create-page` | Create a new page |
| `python notion_api.py update-page <id>` | Update page properties |
| `python notion_api.py append-blocks <id>` | Append content blocks |
| `python notion_api.py list-databases` | List databases |
| `python notion_api.py query-database <id>` | Query a database |
| `python notion_api.py --json` | JSON output |
| `python notion_api.py self-test` | Run built-in tests |

## Features

- **Full Notion API coverage**
- **Config file support (notion_config.json)**
- **Markdown → blocks converter**
- **Dry-run mode for safety**
- **JSON/text output**
- **Env var override for API key**

## Example

```bash
python notion_api.py self-test
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
        run: python notion_api.py self-test
```

## Why

Notion API Toolkit is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/notion-api)
