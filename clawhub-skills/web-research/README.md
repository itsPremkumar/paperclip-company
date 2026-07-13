# Web Research Toolkit 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![web](https://img.shields.io/badge/tag-web-blue) ![research](https://img.shields.io/badge/tag-research-blue) ![search](https://img.shields.io/badge/tag-search-blue) ![duckduckgo](https://img.shields.io/badge/tag-duckduckgo-blue) ![wikipedia](https://img.shields.io/badge/tag-wikipedia-blue) ![cli](https://img.shields.io/badge/tag-cli-blue)

DuckDuckGo + Wikipedia research CLI with URL fetching, content extraction, and citation export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- DuckDuckGo Lite scraping
- Wikipedia API integration
- URL content extraction (HTMLParser)
- Auto-summarization
- Citation export
- Rate-limit aware

## Commands

| Command | Description |
|---------|-------------|
| `search <query>` | Search DuckDuckGo Lite |
| `wiki <topic>` | Search Wikipedia |
| `fetch <url>` | Fetch and extract text from URL |
| `summarize <url>` | Summarize a page |
| `--limit N` | Limit results |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/web-research/main/web_research.py

# Run
python web_research.py self-test
```

## Why Web Research Toolkit?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/web-research)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/web-research)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
