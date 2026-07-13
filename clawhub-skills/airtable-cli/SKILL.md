---
name: airtable-cli
version: 2.0.0
description: Airtable API client: bases, tables, records with pagination, CSV import/export, rate-limit awareness
tags: ["airtable", "api", "database", "cli", "spreadsheet", "automation"]
---

# Airtable CLI v2 🚀

Airtable API client: bases, tables, records with pagination, CSV import/export, rate-limit awareness

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Full Airtable API coverage | Full Airtable API coverage |
| Pagination support | Pagination support |
| CSV import/export | CSV import/export |
| Field filtering | Field filtering |
| Rate-limit awareness | Rate-limit awareness |
| Config file (airtable_config.j | Config file (airtable_config.json) |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/airtable-cli/main/airtable_cli.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python airtable_cli.py list-bases` | List all bases |
| `python airtable_cli.py list-tables <base>` | List tables in a base |
| `python airtable_cli.py list-records <base> <table>` | List records |
| `python airtable_cli.py get-record <base> <table> <id>` | Get one record |
| `python airtable_cli.py create-record` | Create a record |
| `python airtable_cli.py update-record` | Update a record |
| `python airtable_cli.py delete-record` | Delete a record |
| `python airtable_cli.py query <base> <table>` | Query with filter |
| `python airtable_cli.py --json` | JSON output |
| `python airtable_cli.py self-test` | Run built-in tests |

## Features

- **Full Airtable API coverage**
- **Pagination support**
- **CSV import/export**
- **Field filtering**
- **Rate-limit awareness**
- **Config file (airtable_config.json)**

## Example

```bash
python airtable_cli.py self-test
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
        run: python airtable_cli.py self-test
```

## Why

Airtable CLI is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/airtable-cli)
