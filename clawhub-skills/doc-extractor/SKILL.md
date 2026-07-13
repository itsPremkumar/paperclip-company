---
name: doc-extractor
version: 2.0.0
description: Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure
tags: ["pdf", "docx", "extract", "text", "cli", "documents"]
---

# Document Text Extractor v2 🚀

Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| PDF extraction (pymupdf option | PDF extraction (pymupdf optional) |
| DOCX via zipfile + xml | DOCX via zipfile + xml |
| TXT with encoding detection | TXT with encoding detection |
| Page/paragraph structure | Page/paragraph structure |
| Metadata extraction | Metadata extraction |
| Batch processing | Batch processing |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/doc-extractor/main/doc_extractor.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python doc_extractor.py extract <file>` | Extract text from document |
| `python doc_extractor.py pages <file>` | List pages (PDF) |
| `python doc_extractor.py metadata <file>` | Extract metadata |
| `python doc_extractor.py --format txt|md|json` | Output format |
| `python doc_extractor.py --json` | JSON output |
| `python doc_extractor.py self-test` | Run built-in tests |

## Features

- **PDF extraction (pymupdf optional)**
- **DOCX via zipfile + xml**
- **TXT with encoding detection**
- **Page/paragraph structure**
- **Metadata extraction**
- **Batch processing**

## Example

```bash
python doc_extractor.py self-test
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
        run: python doc_extractor.py self-test
```

## Why

Document Text Extractor is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/doc-extractor)
