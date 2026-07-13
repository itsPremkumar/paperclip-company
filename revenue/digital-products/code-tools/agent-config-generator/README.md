# Agent Config Generator

**Interactive CLI tool that generates ready-to-use [Paperclip](https://paperclip.so) agent configuration JSON files.**

[![npm version](https://img.shields.io/npm/v/agent-config-generator.svg)](https://www.npmjs.com/package/agent-config-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)

---

## Overview

Stop hand-writing Paperclip agent configs. Answer **5 interactive questions** and instantly get a production-ready JSON configuration you can paste directly into the Paperclip API.

This is the official CLI companion to the **[Full Autonomous Company Starter Kit](https://premautonomous.co/starter-kit)** by Prem Autonomous Co.

### What you get

```json
{
  "name": "Paperclip Engineer",
  "adapterType": "hermes_local",
  "role": "engineer",
  "adapterConfig": {
    "model": "tencent/hy3:free",
    "provider": "openrouter",
    "maxIterations": 50,
    "timeoutSec": 1800,
    "enabledToolsets": ["terminal", "file", "web"],
    "heartbeat": {
      "enabled": true,
      "maxConcurrentRuns": 3
    }
  }
}
```

---

## Installation

```bash
# Install globally
npm install -g agent-config-generator

# Or run on the fly
npx agent-config-generator
```

## Usage

```bash
gen-agent
```

That's it. Answer the 5 prompts and choose to **print** to console, **save** to file, or **both**.

```
╔═══════════════════════════════════════════════════════════╗
║          Agent Config Generator  v1.0.0                   ║
║     Generate Paperclip agent configs — interactively      ║
║     by Prem Autonomous Co                                 ║
╚═══════════════════════════════════════════════════════════╝

? What role should the agent fill? (Use arrow keys)
❯ Engineer
  CTO
  Researcher
  Writer
  Analyst
  Architect
  Product Manager
  Custom
```

```
? Which model should power this agent? (Use arrow keys)
❯ DeepSeek V4 (tencent/hy3:free)     — Free, fast, general purpose
  Claude 3 Haiku (anthropic)         — Fast & affordable
  Claude 3.5 Sonnet (anthropic)      — Best-in-class coding
  GPT-4o (openai)                    — Strong all-rounder
  Gemini 2.0 Flash (google)          — Speed demon
  Custom model ID                     — Enter any model string
```

```
? Which tools should the agent have access to?
  ◉ terminal  — Shell / CLI execution
  ◉ file      — Read & write files
  ◉ web       — HTTP requests, browsing
  ◯ memory    — Long-term knowledge store
  ◯ search    — Semantic & keyword search
  ◯ github    — GitHub API integration
  ◯ gitlab    — GitLab API integration
  ◯ slack     — Slack messaging
  ◯ email     — Send & receive email
  ◯ browser   — Headless browser automation
```

### Command-line options

| Flag             | Description                |
|------------------|----------------------------|
| `--help`, `-h`   | Show help text             |
| `--version`, `-v`| Print version number       |

---

## The 5 Questions

| # | Question | What it does |
|---|----------|--------------|
| 1 | **Agent Role** | Set the agent's job function (`engineer`, `cto`, `researcher`, `writer`, `analyst`, `architect`, `product-manager`, or custom) |
| 2 | **Model** | Pick from popular presets or enter a custom model ID |
| 3 | **Provider** | Select the inference provider (OpenRouter, Anthropic, OpenAI, Google, or custom) |
| 4 | **Toolsets** | Enable the capabilities your agent needs (terminal, file, web, memory, search, GitHub, GitLab, Slack, email, browser) |
| 5 | **Heartbeat** | Configure background task execution and concurrency limits |

---

## Output

Your generated config is ready to use with the Paperclip API:

```bash
curl -X POST https://api.paperclip.so/api/companies/:companyId/agents \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "Content-Type: application/json" \
  -d @paperclip-agent-engineer.json
```

---

## 🚀 Premium: Multi-Agent Orchestration ($29)

Need a full autonomous company — not just one agent?

The **PRO version** generates a complete Paperclip **company configuration** with:

- **Multiple agent roles** orchestrated to work together
- **Inter-agent handoff** configuration
- **Shared memory & context** pipelines
- **Approval workflows** between agents
- **The Paperclip Company Seed Script** — bootstrap your entire autonomous org in one command
- **Priority support** & lifetime updates

👉 **[Get PRO → premium.premautonomous.co](https://premautonomous.co/products/agent-config-generator)**

---

## API Reference

### Paperclip Agent Config Schema

| Field | Type | Description |
|-------|------|-------------|
| `name` | `string` | Human-readable agent name |
| `adapterType` | `string` | Runtime adapter (`hermes_local`, `openai_assistant`, `anthropic`, `custom_api`) |
| `role` | `string` | Job function identifier |
| `adapterConfig.model` | `string` | LLM model identifier |
| `adapterConfig.provider` | `string` | Inference API provider |
| `adapterConfig.maxIterations` | `number` | Max reasoning loops |
| `adapterConfig.timeoutSec` | `number` | Request timeout in seconds |
| `adapterConfig.enabledToolsets` | `string[]` | Enabled capability groups |
| `adapterConfig.heartbeat.enabled` | `boolean` | Enable background tasks |
| `adapterConfig.heartbeat.maxConcurrentRuns` | `number` | Max concurrent background tasks |

**Paperclip API Endpoint**: `POST /api/companies/:companyId/agents`

---

## Development

```bash
# Clone
git clone https://github.com/premautonomousco/agent-config-generator.git
cd agent-config-generator

# Install dependencies
npm install

# Run in dev mode (watch for changes)
npm run dev

# Test (Node built-in test runner)
npm test
```

### Project structure

```
agent-config-generator/
├── src/
│   └── index.js          # Main CLI entry point
├── pro/
│   └── company-template.json  # PRO multi-agent orchestration config
├── package.json
├── README.md
└── .gitignore
```

---

## License

MIT © [Prem Autonomous Co](https://premautonomous.co)

Built for the **Full Autonomous Company Starter Kit** — the open-source blueprint for running autonomous AI companies.
