# Maps CLI 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![maps](https://img.shields.io/badge/tag-maps-blue) ![osm](https://img.shields.io/badge/tag-osm-blue) ![geocode](https://img.shields.io/badge/tag-geocode-blue) ![routing](https://img.shields.io/badge/tag-routing-blue) ![poi](https://img.shields.io/badge/tag-poi-blue) ![cli](https://img.shields.io/badge/tag-cli-blue)

Advanced OpenStreetMap CLI: geocode, reverse geocode, route, POI search, timezone, CSV export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

- OpenStreetMap Nominatim geocoding
- OSRM routing engine
- Overpass API for POI search
- Timezone lookup
- CSV export
- Zero external dependencies

## Commands

| Command | Description |
|---------|-------------|
| `geocode <query>` | Geocode a place name |
| `reverse <lat> <lon>` | Reverse geocode coordinates |
| `route <s> <d>` | Driving route between points |
| `poi <lat> <lon>` | Find points of interest |
| `timezone <lat> <lon>` | Lookup timezone |
| `export <lat> <lon>` | Export POIs as CSV |
| `--json` | JSON output |
| `self-test` | Run built-in tests |

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/maps-cli/main/maps_cli.py

# Run
python maps_cli.py self-test
```

## Why Maps CLI?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/maps-cli)  
⭐ Star on [GitHub](https://github.com/itsPremkumar/maps-cli)  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
