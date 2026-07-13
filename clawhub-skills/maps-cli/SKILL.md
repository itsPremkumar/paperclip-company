---
name: maps-cli
version: 2.0.0
description: Advanced OpenStreetMap CLI: geocode, reverse geocode, route, POI search, timezone, CSV export
tags: ["maps", "osm", "geocode", "routing", "poi", "cli", "location"]
---

# Maps CLI v2 🚀

Advanced OpenStreetMap CLI: geocode, reverse geocode, route, POI search, timezone, CSV export

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
| OpenStreetMap Nominatim geocod | OpenStreetMap Nominatim geocoding |
| OSRM routing engine | OSRM routing engine |
| Overpass API for POI search | Overpass API for POI search |
| Timezone lookup | Timezone lookup |
| CSV export | CSV export |
| Zero external dependencies | Zero external dependencies |

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/maps-cli/main/maps_cli.py

# Or copy the file anywhere — it's self-contained.
```

## Commands

| Command | Description |
|---------|-------------|
| `python maps_cli.py geocode <query>` | Geocode a place name |
| `python maps_cli.py reverse <lat> <lon>` | Reverse geocode coordinates |
| `python maps_cli.py route <s> <d>` | Driving route between points |
| `python maps_cli.py poi <lat> <lon>` | Find points of interest |
| `python maps_cli.py timezone <lat> <lon>` | Lookup timezone |
| `python maps_cli.py export <lat> <lon>` | Export POIs as CSV |
| `python maps_cli.py --json` | JSON output |
| `python maps_cli.py self-test` | Run built-in tests |

## Features

- **OpenStreetMap Nominatim geocoding**
- **OSRM routing engine**
- **Overpass API for POI search**
- **Timezone lookup**
- **CSV export**
- **Zero external dependencies**

## Example

```bash
python maps_cli.py self-test
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
        run: python maps_cli.py self-test
```

## Why

Maps CLI is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/maps-cli)
