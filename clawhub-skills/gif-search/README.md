# GIF Search 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![gif](https://img.shields.io/badge/tag-gif-blue) ![search](https://img.shields.io/badge/tag-search-blue) ![media](https://img.shields.io/badge/tag-media-blue) ![tenor](https://img.shields.io/badge/tag-tenor-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![download](https://img.shields.io/badge/tag-download-blue)

Search and download GIFs from Tenor API with caching, bulk download, and format conversion

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Tenor API integration (free tier)
- Trending + search + random modes
- Bulk download with progress
- Local cache to avoid re-fetches
- JSON output for automation
- GIF metadata extraction
- Rate-limit aware

## Commands

| Command | Description |
|---------|-------------|
| `search <query>` | Search GIFs by keyword |
| `trending` | Show trending GIFs |
| `download <id>` | Download a specific GIF |
| `random <query>` | Get a random GIF |
| `--limit N` | Limit results |
| `--save DIR` | Save to directory |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/gif-search/main/gif_search.py

# Run
python gif_search.py self-test
```

## Why GIF Search?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/gif-search)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/gif-search)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
