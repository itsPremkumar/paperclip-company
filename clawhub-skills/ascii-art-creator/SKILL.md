---
name: ascii-art-creator
version: 2.0.0
description: Generate banners, boxes, cowsay-style art, tables, and image-to-ASCII with multiple fonts
tags: ["ascii", "art", "banner", "cowsay", "cli", "terminal"]
---

# ASCII Art Creator v2 🚀

Generate banners, boxes, cowsay-style art, tables, and image-to-ASCII with multiple fonts

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| 3 fonts × 5 commands | 3 fonts × 5 commands |
| Banner generation | Banner generation |
| 4 box styles | 4 box styles |
| 5 cow faces | 5 cow faces |
| ASCII tables | ASCII tables |
| Image-to-ASCII (PIL/pymupdf/PP | Image-to-ASCII (PIL/pymupdf/PPM) |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/ascii-art-creator/main/ascii_art.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python ascii_art.py banner <text>` | Create a text banner |
| `python ascii_art.py box <text>` | Draw a box around text |
| `python ascii_art.py cow <text>` | Cowsay-style speech bubble |
| `python ascii_art.py table <data>` | ASCII table from data |
| `python ascii_art.py image <file>` | Convert image to ASCII |
| `python ascii_art.py --font N` | Select font (3 available) |
| `python ascii_art.py self-test` | Run built-in tests |

## Features

- **3 fonts × 5 commands**
- **Banner generation**
- **4 box styles**
- **5 cow faces**
- **ASCII tables**
- **Image-to-ASCII (PIL/pymupdf/PPM)**

## Example

```bash
python ascii_art.py self-test
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
        run: python ascii_art.py self-test
```

## Why

ASCII Art Creator is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/ascii-art-creator)
