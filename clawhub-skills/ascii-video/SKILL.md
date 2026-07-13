---
name: ascii-video
version: 2.0.0
description: Convert video to ASCII animation with multiple dithering modes, color output, framerate control
tags: ["ascii", "video", "animation", "terminal", "cli", "art"]
---

# ASCII Video Converter v2 🚀

Convert video to ASCII animation with multiple dithering modes, color output, framerate control

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| Braille/block/greyscale dither | Braille/block/greyscale dithering |
| ANSI color output | ANSI color output |
| Framerate control | Framerate control |
| Palette modes | Palette modes |
| Single-frame capture | Single-frame capture |
| Terminal playback | Terminal playback |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/ascii-video/main/ascii_video.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python ascii_video.py convert <video>` | Convert video to ASCII |
| `python ascii_video.py play <file>` | Play ASCII animation in terminal |
| `python ascii_video.py capture <video>` | Capture single frame |
| `python ascii_video.py info <video>` | Show video info |
| `python ascii_video.py list` | List presets |
| `python ascii_video.py --mode braille|block|grey` | Dithering mode |
| `python ascii_video.py --color` | ANSI color output |
| `python ascii_video.py self-test` | Run built-in tests |

## Features

- **Braille/block/greyscale dithering**
- **ANSI color output**
- **Framerate control**
- **Palette modes**
- **Single-frame capture**
- **Terminal playback**

## Example

```bash
python ascii_video.py self-test
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
        run: python ascii_video.py self-test
```

## Why

ASCII Video Converter is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/ascii-video)
