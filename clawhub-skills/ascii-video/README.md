# ASCII Video Converter 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![ascii](https://img.shields.io/badge/tag-ascii-blue) ![video](https://img.shields.io/badge/tag-video-blue) ![animation](https://img.shields.io/badge/tag-animation-blue) ![terminal](https://img.shields.io/badge/tag-terminal-blue) ![cli](https://img.shields.io/badge/tag-cli-blue) ![art](https://img.shields.io/badge/tag-art-blue)

Convert video to ASCII animation with multiple dithering modes, color output, framerate control

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- Braille/block/greyscale dithering
- ANSI color output
- Framerate control
- Palette modes
- Single-frame capture
- Terminal playback

## Commands

| Command | Description |
|---------|-------------|
| `convert <video>` | Convert video to ASCII |
| `play <file>` | Play ASCII animation in terminal |
| `capture <video>` | Capture single frame |
| `info <video>` | Show video info |
| `list` | List presets |
| `--mode braille|block|grey` | Dithering mode |
| `--color` | ANSI color output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/ascii-video/main/ascii_video.py

# Run
python ascii_video.py self-test
```

## Why ASCII Video Converter?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/ascii-video)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/ascii-video)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
