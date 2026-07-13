---
name: json-tools
version: 2.0.0
description: Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths
tags: ["json", "tools", "validate", "query", "diff", "cli", "data"]
---

# JSON Tools v2 🚀

Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| 8 commands (validate/format/qu | 8 commands (validate/format/query/diff/filter/stats/flatten/merge) |
| Dot-notation querying | Dot-notation querying |
| JSON diff with structural comp | JSON diff with structural comparison |
| Array filtering | Array filtering |
| Flatten nested structures | Flatten nested structures |
| Deep merge | Deep merge |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/json-tools/main/json_tools.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python json_tools.py validate <file>` | Validate JSON syntax |
| `python json_tools.py format <file>` | Pretty-print JSON |
| `python json_tools.py query <file> <path>` | Query with dot-notation |
| `python json_tools.py diff <a> <b>` | Diff two JSON files |
| `python json_tools.py filter <file> <expr>` | Filter array elements |
| `python json_tools.py flatten <file>` | Flatten nested JSON |
| `python json_tools.py merge <a> <b>` | Deep-merge JSON |
| `python json_tools.py stats <file>` | Show statistics |
| `python json_tools.py self-test` | Run built-in tests |

## Features

- **8 commands (validate/format/query/diff/filter/stats/flatten/merge)**
- **Dot-notation querying**
- **JSON diff with structural comparison**
- **Array filtering**
- **Flatten nested structures**
- **Deep merge**

## Example

```bash
python json_tools.py self-test
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
        run: python json_tools.py self-test
```

## Why

JSON Tools is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/json-tools)
