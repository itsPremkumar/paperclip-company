# arXiv Search 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![arxiv](https://img.shields.io/badge/tag-arxiv-blue) ![research](https://img.shields.io/badge/tag-research-blue) ![papers](https://img.shields.io/badge/tag-papers-blue) ![academic](https://img.shields.io/badge/tag-academic-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![search](https://img.shields.io/badge/tag-search-blue)

Search arXiv papers by keyword, author, category with full-text download and citation export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- arXiv API integration
- Author + category filters
- PDF download
- BibTeX citation export
- JSON output for automation
- Rate-limit aware

## Commands

| Command | Description |
|---------|-------------|
| `search <query>` | Search papers by keyword |
| `author <name>` | Search by author |
| `category <cat>` | Filter by category (cs.AI, etc.) |
| `download <id>` | Download PDF |
| `--limit N` | Limit results |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/arxiv-search/main/arxiv_search.py

# Run
python arxiv_search.py self-test
```

## Why arXiv Search?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/arxiv-search)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/arxiv-search)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
