---
name: agent-health
version: 1.0.0
description: Probe an agent's dependency endpoints (gateways/APIs/DBs) and report up/down + latency. Stdlib.
tags: [health, monitoring, observability, openclaw, hermes, agent]
---

# agent-health — is everything your agent needs actually up?

Points agent-health at a list of URLs your agent depends on (gateway, APIs, Postgres)
and gets a table of up/down + latency. Honest: it only probes, it doesn't fix. Zero deps.

## Usage
```bash
# endpoints.txt: one "name url" per line
python agent_health.py check endpoints.txt [--json]
```

## Why
Half of "the agent is broken" is really "an upstream is down". Check first. Free + MIT.

## Support
Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar  *(add your link)*
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar      *(add your link)*
