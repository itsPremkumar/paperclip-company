---
name: web-research
version: 2.0.0
description: DuckDuckGo + Wikipedia research CLI with URL fetching, content extraction, and citation export
tags: ["web", "research", "search", "duckduckgo", "wikipedia", "cli"]
---

# Web Research Toolkit v2 🚀

DuckDuckGo + Wikipedia research CLI with URL fetching, content extraction, and citation export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| DuckDuckGo Lite scraping | DuckDuckGo Lite scraping |
| Wikipedia API integration | Wikipedia API integration |
| URL content extraction (HTMLPa | URL content extraction (HTMLParser) |
| Auto-summarization | Auto-summarization |
| Citation export | Citation export |
| Rate-limit aware | Rate-limit aware |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/web-research/main/web_research.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python web_research.py search <query>` | Search DuckDuckGo Lite |
| `python web_research.py wiki <topic>` | Search Wikipedia |
| `python web_research.py fetch <url>` | Fetch and extract text from URL |
| `python web_research.py summarize <url>` | Summarize a page |
| `python web_research.py --limit N` | Limit results |
| `python web_research.py --json` | JSON output |
| `python web_research.py self-test` | Run built-in tests |

## Features

- **DuckDuckGo Lite scraping**
- **Wikipedia API integration**
- **URL content extraction (HTMLParser)**
- **Auto-summarization**
- **Citation export**
- **Rate-limit aware**

## Example

```bash
python web_research.py self-test
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
        run: python web_research.py self-test
```

## Why

Web Research Toolkit is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/web-research)
