---
name: youtube-content
version: 2.0.0
description: Extract transcripts, summaries, and metadata from YouTube videos for content repurposing
tags: ["youtube", "transcript", "content", "video", "cli", "automation"]
---

# YouTube Content Tools v2 🚀

Extract transcripts, summaries, and metadata from YouTube videos for content repurposing

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Transcript extraction (multi-l | Transcript extraction (multi-language) |
| Auto-summarization | Auto-summarization |
| Metadata + chapter extraction | Metadata + chapter extraction |
| Batch processing | Batch processing |
| JSON output for pipelines | JSON output for pipelines |
| Content repurposing ready | Content repurposing ready |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/youtube-content/main/youtube_content.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python youtube_content.py transcript <url>` | Get video transcript |
| `python youtube_content.py summary <url>` | Summarize video content |
| `python youtube_content.py metadata <url>` | Extract video metadata |
| `python youtube_content.py chapters <url>` | Get chapter markers |
| `python youtube_content.py --lang CODE` | Language preference |
| `python youtube_content.py --json` | JSON output |
| `python youtube_content.py self-test` | Run built-in tests |

## Features

- **Transcript extraction (multi-language)**
- **Auto-summarization**
- **Metadata + chapter extraction**
- **Batch processing**
- **JSON output for pipelines**
- **Content repurposing ready**

## Example

```bash
python youtube_content.py self-test
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
        run: python youtube_content.py self-test
```

## Why

YouTube Content Tools is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/youtube-content)
