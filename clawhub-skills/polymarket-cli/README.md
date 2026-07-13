# Polymarket CLI 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![polymarket](https://img.shields.io/badge/tag-polymarket-blue) ![prediction](https://img.shields.io/badge/tag-prediction-blue) ![markets](https://img.shields.io/badge/tag-markets-blue) ![trading](https://img.shields.io/badge/tag-trading-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![crypto](https://img.shields.io/badge/tag-crypto-blue)

Query Polymarket prediction markets: search, price history, trending, categories, stats

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Gamma API integration (no key needed for reads)
- Price history with CSV export
- Trending + categories
- Cached requests
- Price alerts (text)
- Pagination support

## Commands

| Command | Description |
|---------|-------------|
| `search <query>` | Search markets |
| `list-markets` | List active markets |
| `get-market <id>` | Get market details |
| `price-history <id>` | Get price history |
| `trending` | Show trending markets |
| `categories` | List categories |
| `stats` | Show market stats |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/polymarket-cli/main/polymarket_cli.py

# Run
python polymarket_cli.py self-test
```

## Why Polymarket CLI?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/polymarket-cli)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/polymarket-cli)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
