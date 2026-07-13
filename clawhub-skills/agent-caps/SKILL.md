---
name: agent-caps
version: 1.0.0
description: Validate, scaffold, and cross-check AI-agent capability manifests so agents stay swappable and safe. Zero dependencies (Python stdlib).
tags: [agent, manifest, validation, devtools, openclaw, paperclip]
---

# agent-caps — Agent Capability Manifest Toolkit

Lets an OpenClaw / Hermes / Paperclip-style agent declare, validate, and cross-check
its capabilities as a machine-readable manifest — implementing the standard agent
interface (Name / Version / Capabilities / Dependencies / Memory / Tools / API / Status)
so agents can be swapped or audited without breaking the system.

This is the runnable enforcement behind any "agent marketplace" idea: catch missing
fields, bad versions, illegal statuses, and unknown dependencies **before** an agent
goes live.

## Install
No dependencies. Requires Python 3.8+. Copy `agent_caps.py` anywhere.

## Commands
```bash
python agent_caps.py validate  path/to/manifest.json   # validate against schema
python agent_caps.py scaffold  ./my-agent --name X      # generate a manifest
python agent_caps.py check-deps a.json b.json          # cross-check dependencies
python agent_caps.py schema                          # print the JSON schema
```

## Example manifest
```json
{
  "name": "Hermes",
  "version": "1.0",
  "capabilities": ["executive reasoning", "planning", "documentation"],
  "dependencies": ["Paperclip API", "git CLI"],
  "memory_requirements": "256MB",
  "tools": ["terminal", "file", "browser"],
  "api": "hermes_local / hermes_gateway",
  "status": "active"
}
```

## Why
Most "agent marketplaces" are docs, not enforcement. agent-caps turns the standard
interface into a validator. It is MIT licensed, offline, no telemetry.

## Premium
A curated bundle (extra manifests for 10+ popular agents + a CI check script) is
available on Gumroad. This ClawHub skill is free and fully functional on its own.

> Note: this is a developer tool, not a revenue generator by itself — it saves
> real integration time when running multi-agent stacks.
