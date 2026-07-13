---
name: polymarket-cli
version: 2.0.0
description: Query Polymarket prediction markets: search, price history, trending, categories, stats
tags: ["polymarket", "prediction", "markets", "trading", "cli", "crypto"]
---

# Polymarket CLI v2 🚀

Query Polymarket prediction markets: search, price history, trending, categories, stats

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Gamma API integration (no key  | Gamma API integration (no key needed for reads) |
| Price history with CSV export | Price history with CSV export |
| Trending + categories | Trending + categories |
| Cached requests | Cached requests |
| Price alerts (text) | Price alerts (text) |
| Pagination support | Pagination support |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/polymarket-cli/main/polymarket_cli.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python polymarket_cli.py search <query>` | Search markets |
| `python polymarket_cli.py list-markets` | List active markets |
| `python polymarket_cli.py get-market <id>` | Get market details |
| `python polymarket_cli.py price-history <id>` | Get price history |
| `python polymarket_cli.py trending` | Show trending markets |
| `python polymarket_cli.py categories` | List categories |
| `python polymarket_cli.py stats` | Show market stats |
| `python polymarket_cli.py --json` | JSON output |
| `python polymarket_cli.py self-test` | Run built-in tests |

## Features

- **Gamma API integration (no key needed for reads)**
- **Price history with CSV export**
- **Trending + categories**
- **Cached requests**
- **Price alerts (text)**
- **Pagination support**

## Example

```bash
python polymarket_cli.py self-test
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
        run: python polymarket_cli.py self-test
```

## Why

Polymarket CLI is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/polymarket-cli)
