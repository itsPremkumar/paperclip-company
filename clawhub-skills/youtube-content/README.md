# YouTube Content Tools 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![youtube](https://img.shields.io/badge/tag-youtube-blue) ![transcript](https://img.shields.io/badge/tag-transcript-blue) ![content](https://img.shields.io/badge/tag-content-blue) ![video](https://img.shields.io/badge/tag-video-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![automation](https://img.shields.io/badge/tag-automation-blue)

Extract transcripts, summaries, and metadata from YouTube videos for content repurposing

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Transcript extraction (multi-language)
- Auto-summarization
- Metadata + chapter extraction
- Batch processing
- JSON output for pipelines
- Content repurposing ready

## Commands

| Command | Description |
|---------|-------------|
| `transcript <url>` | Get video transcript |
| `summary <url>` | Summarize video content |
| `metadata <url>` | Extract video metadata |
| `chapters <url>` | Get chapter markers |
| `--lang CODE` | Language preference |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/youtube-content/main/youtube_content.py

# Run
python youtube_content.py self-test
```

## Why YouTube Content Tools?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/youtube-content)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/youtube-content)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
