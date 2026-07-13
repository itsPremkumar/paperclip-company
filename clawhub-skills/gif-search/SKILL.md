---
name: gif-search
version: 2.0.0
description: Search and download GIFs from Tenor API with caching, bulk download, and format conversion
tags: ["gif", "search", "media", "tenor", "cli", "download"]
---

# GIF Search v2 🚀

Search and download GIFs from Tenor API with caching, bulk download, and format conversion

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Tenor API integration (free ti | Tenor API integration (free tier) |
| Trending + search + random mod | Trending + search + random modes |
| Bulk download with progress | Bulk download with progress |
| Local cache to avoid re-fetche | Local cache to avoid re-fetches |
| JSON output for automation | JSON output for automation |
| GIF metadata extraction | GIF metadata extraction |
| Rate-limit aware | Rate-limit aware |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/gif-search/main/gif_search.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python gif_search.py search <query>` | Search GIFs by keyword |
| `python gif_search.py trending` | Show trending GIFs |
| `python gif_search.py download <id>` | Download a specific GIF |
| `python gif_search.py random <query>` | Get a random GIF |
| `python gif_search.py --limit N` | Limit results |
| `python gif_search.py --save DIR` | Save to directory |
| `python gif_search.py --json` | JSON output |
| `python gif_search.py self-test` | Run built-in tests |

## Features

- **Tenor API integration (free tier)**
- **Trending + search + random modes**
- **Bulk download with progress**
- **Local cache to avoid re-fetches**
- **JSON output for automation**
- **GIF metadata extraction**
- **Rate-limit aware**

## Example

```bash
python gif_search.py self-test
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
        run: python gif_search.py self-test
```

## Why

GIF Search is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/gif-search)
