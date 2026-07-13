---
name: arxiv-search
version: 2.0.0
description: Search arXiv papers by keyword, author, category with full-text download and citation export
tags: ["arxiv", "research", "papers", "academic", "cli", "search"]
---

# arXiv Search v2 🚀

Search arXiv papers by keyword, author, category with full-text download and citation export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| arXiv API integration | arXiv API integration |
| Author + category filters | Author + category filters |
| PDF download | PDF download |
| BibTeX citation export | BibTeX citation export |
| JSON output for automation | JSON output for automation |
| Rate-limit aware | Rate-limit aware |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/arxiv-search/main/arxiv_search.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python arxiv_search.py search <query>` | Search papers by keyword |
| `python arxiv_search.py author <name>` | Search by author |
| `python arxiv_search.py category <cat>` | Filter by category (cs.AI, etc.) |
| `python arxiv_search.py download <id>` | Download PDF |
| `python arxiv_search.py --limit N` | Limit results |
| `python arxiv_search.py --json` | JSON output |
| `python arxiv_search.py self-test` | Run built-in tests |

## Features

- **arXiv API integration**
- **Author + category filters**
- **PDF download**
- **BibTeX citation export**
- **JSON output for automation**
- **Rate-limit aware**

## Example

```bash
python arxiv_search.py self-test
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
        run: python arxiv_search.py self-test
```

## Why

arXiv Search is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/arxiv-search)
