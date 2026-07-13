# JSON Tools 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![json](https://img.shields.io/badge/tag-json-blue) ![tools](https://img.shields.io/badge/tag-tools-blue) ![validate](https://img.shields.io/badge/tag-validate-blue) ![query](https://img.shields.io/badge/tag-query-blue) ![diff](https://img.shields.io/badge/tag-diff-blue) ![cli](https://img.shields.io/badge/tag-cli-blue)

Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- 8 commands (validate/format/query/diff/filter/stats/flatten/merge)
- Dot-notation querying
- JSON diff with structural comparison
- Array filtering
- Flatten nested structures
- Deep merge

## Commands

| Command | Description |
|---------|-------------|
| `validate <file>` | Validate JSON syntax |
| `format <file>` | Pretty-print JSON |
| `query <file> <path>` | Query with dot-notation |
| `diff <a> <b>` | Diff two JSON files |
| `filter <file> <expr>` | Filter array elements |
| `flatten <file>` | Flatten nested JSON |
| `merge <a> <b>` | Deep-merge JSON |
| `stats <file>` | Show statistics |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/json-tools/main/json_tools.py

# Run
python json_tools.py self-test
```

## Why JSON Tools?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/json-tools)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/json-tools)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
