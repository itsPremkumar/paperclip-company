#!/usr/bin/env python3
"""Batch upgrade: generate README.md + v2 SKILL.md for all 31 ClawHub skills."""
import os
import re
import json

BASE = r"C:\one\paperclip-company\clawhub-skills"

# Mapping: folder → display name, primary tool, description, features
SKILLS = {
    "codebase-inspection": {
        "name": "Codebase Inspector", "tool": "codebase_inspector.py",
        "desc": "Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration",
        "tags": ["codebase", "analysis", "metrics", "devtools", "python", "cli", "ci", "reports"],
        "commands": [
            ("analyze <dir>", "Analyze directory, print text report"),
            ("--json", "JSON output for pipelines"),
            ("--html FILE", "Generate visual HTML report with charts"),
            ("--csv", "CSV export for spreadsheets"),
            ("--badge", "Generate shields.io badge URL"),
            ("--snapshot", "Save as trend data point"),
            ("--trend", "Show historical trends"),
            ("--diff <dir2>", "Compare two codebases"),
            ("--exclude DIRS", "Skip custom directories"),
            ("self-test", "Run 13 built-in checks"),
        ],
        "features": [
            "Automatic language detection (40+ extensions → 30+ languages)",
            "Smart directory skipping (.git, node_modules, __pycache__, etc.)",
            "Blank/comment/code line counting",
            "HTML visual report with bar charts + summary cards",
            "Historical trend tracking (snapshot-based)",
            "Git-aware codebase diffing",
            "SVG badge generation for README",
            "CSV export for dashboards",
            "JSON mode for CI/CD pipelines",
            "Cross-platform (Windows/macOS/Linux)",
            "13 built-in self-tests",
        ],
    },
    "gif-search": {
        "name": "GIF Search", "tool": "gif_search.py",
        "desc": "Search and download GIFs from Tenor API with caching, bulk download, and format conversion",
        "tags": ["gif", "search", "media", "tenor", "cli", "download"],
        "commands": [
            ("search <query>", "Search GIFs by keyword"),
            ("trending", "Show trending GIFs"),
            ("download <id>", "Download a specific GIF"),
            ("random <query>", "Get a random GIF"),
            ("--limit N", "Limit results"),
            ("--save DIR", "Save to directory"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Tenor API integration (free tier)",
            "Trending + search + random modes",
            "Bulk download with progress",
            "Local cache to avoid re-fetches",
            "JSON output for automation",
            "GIF metadata extraction",
            "Rate-limit aware",
        ],
    },
    "youtube-content": {
        "name": "YouTube Content Tools", "tool": "youtube_content.py",
        "desc": "Extract transcripts, summaries, and metadata from YouTube videos for content repurposing",
        "tags": ["youtube", "transcript", "content", "video", "cli", "automation"],
        "commands": [
            ("transcript <url>", "Get video transcript"),
            ("summary <url>", "Summarize video content"),
            ("metadata <url>", "Extract video metadata"),
            ("chapters <url>", "Get chapter markers"),
            ("--lang CODE", "Language preference"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Transcript extraction (multi-language)",
            "Auto-summarization",
            "Metadata + chapter extraction",
            "Batch processing",
            "JSON output for pipelines",
            "Content repurposing ready",
        ],
    },
    "arxiv-search": {
        "name": "arXiv Search", "tool": "arxiv_search.py",
        "desc": "Search arXiv papers by keyword, author, category with full-text download and citation export",
        "tags": ["arxiv", "research", "papers", "academic", "cli", "search"],
        "commands": [
            ("search <query>", "Search papers by keyword"),
            ("author <name>", "Search by author"),
            ("category <cat>", "Filter by category (cs.AI, etc.)"),
            ("download <id>", "Download PDF"),
            ("--limit N", "Limit results"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "arXiv API integration",
            "Author + category filters",
            "PDF download",
            "BibTeX citation export",
            "JSON output for automation",
            "Rate-limit aware",
        ],
    },
    "maps-cli": {
        "name": "Maps CLI", "tool": "maps_cli.py",
        "desc": "Advanced OpenStreetMap CLI: geocode, reverse geocode, route, POI search, timezone, CSV export",
        "tags": ["maps", "osm", "geocode", "routing", "poi", "cli", "location"],
        "commands": [
            ("geocode <query>", "Geocode a place name"),
            ("reverse <lat> <lon>", "Reverse geocode coordinates"),
            ("route <s> <d>", "Driving route between points"),
            ("poi <lat> <lon>", "Find points of interest"),
            ("timezone <lat> <lon>", "Lookup timezone"),
            ("export <lat> <lon>", "Export POIs as CSV"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "OpenStreetMap Nominatim geocoding",
            "OSRM routing engine",
            "Overpass API for POI search",
            "Timezone lookup",
            "CSV export",
            "Zero external dependencies",
        ],
    },
    "notion-api": {
        "name": "Notion API Toolkit", "tool": "notion_api.py",
        "desc": "Complete Notion API client: pages, databases, blocks, search with config file and dry-run mode",
        "tags": ["notion", "api", "notes", "database", "cli", "productivity"],
        "commands": [
            ("list-pages", "List all pages"),
            ("get-page <id>", "Get page content"),
            ("search <query>", "Search workspace"),
            ("create-page", "Create a new page"),
            ("update-page <id>", "Update page properties"),
            ("append-blocks <id>", "Append content blocks"),
            ("list-databases", "List databases"),
            ("query-database <id>", "Query a database"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Full Notion API coverage",
            "Config file support (notion_config.json)",
            "Markdown → blocks converter",
            "Dry-run mode for safety",
            "JSON/text output",
            "Env var override for API key",
        ],
    },
    "airtable-cli": {
        "name": "Airtable CLI", "tool": "airtable_cli.py",
        "desc": "Airtable API client: bases, tables, records with pagination, CSV import/export, rate-limit awareness",
        "tags": ["airtable", "api", "database", "cli", "spreadsheet", "automation"],
        "commands": [
            ("list-bases", "List all bases"),
            ("list-tables <base>", "List tables in a base"),
            ("list-records <base> <table>", "List records"),
            ("get-record <base> <table> <id>", "Get one record"),
            ("create-record", "Create a record"),
            ("update-record", "Update a record"),
            ("delete-record", "Delete a record"),
            ("query <base> <table>", "Query with filter"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Full Airtable API coverage",
            "Pagination support",
            "CSV import/export",
            "Field filtering",
            "Rate-limit awareness",
            "Config file (airtable_config.json)",
        ],
    },
    "polymarket-cli": {
        "name": "Polymarket CLI", "tool": "polymarket_cli.py",
        "desc": "Query Polymarket prediction markets: search, price history, trending, categories, stats",
        "tags": ["polymarket", "prediction", "markets", "trading", "cli", "crypto"],
        "commands": [
            ("search <query>", "Search markets"),
            ("list-markets", "List active markets"),
            ("get-market <id>", "Get market details"),
            ("price-history <id>", "Get price history"),
            ("trending", "Show trending markets"),
            ("categories", "List categories"),
            ("stats", "Show market stats"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Gamma API integration (no key needed for reads)",
            "Price history with CSV export",
            "Trending + categories",
            "Cached requests",
            "Price alerts (text)",
            "Pagination support",
        ],
    },
    "excalidraw-cli": {
        "name": "Excalidraw CLI", "tool": "excalidraw_cli.py",
        "desc": "Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON",
        "tags": ["excalidraw", "diagrams", "flowchart", "architecture", "cli", "drawing"],
        "commands": [
            ("create flowchart", "Generate a flowchart"),
            ("create sequence", "Generate a sequence diagram"),
            ("create arch", "Generate architecture diagram"),
            ("create gantt", "Generate a Gantt chart"),
            ("render <file>", "Render to SVG/PNG"),
            ("export <file>", "Export diagram"),
            ("list", "List templates"),
            ("show <file>", "Show diagram JSON"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Valid Excalidraw JSON output",
            "Multiple diagram types (flowchart, sequence, arch, gantt)",
            "Colored elements",
            "Text labels",
            "Compatible with excalidraw.com",
            "Zero dependencies",
        ],
    },
    "ascii-video": {
        "name": "ASCII Video Converter", "tool": "ascii_video.py",
        "desc": "Convert video to ASCII animation with multiple dithering modes, color output, framerate control",
        "tags": ["ascii", "video", "animation", "terminal", "cli", "art"],
        "commands": [
            ("convert <video>", "Convert video to ASCII"),
            ("play <file>", "Play ASCII animation in terminal"),
            ("capture <video>", "Capture single frame"),
            ("info <video>", "Show video info"),
            ("list", "List presets"),
            ("--mode braille|block|grey", "Dithering mode"),
            ("--color", "ANSI color output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Braille/block/greyscale dithering",
            "ANSI color output",
            "Framerate control",
            "Palette modes",
            "Single-frame capture",
            "Terminal playback",
        ],
    },
    "web-research": {
        "name": "Web Research Toolkit", "tool": "web_research.py",
        "desc": "DuckDuckGo + Wikipedia research CLI with URL fetching, content extraction, and citation export",
        "tags": ["web", "research", "search", "duckduckgo", "wikipedia", "cli"],
        "commands": [
            ("search <query>", "Search DuckDuckGo Lite"),
            ("wiki <topic>", "Search Wikipedia"),
            ("fetch <url>", "Fetch and extract text from URL"),
            ("summarize <url>", "Summarize a page"),
            ("--limit N", "Limit results"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "DuckDuckGo Lite scraping",
            "Wikipedia API integration",
            "URL content extraction (HTMLParser)",
            "Auto-summarization",
            "Citation export",
            "Rate-limit aware",
        ],
    },
    "doc-extractor": {
        "name": "Document Text Extractor", "tool": "doc_extractor.py",
        "desc": "Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure",
        "tags": ["pdf", "docx", "extract", "text", "cli", "documents"],
        "commands": [
            ("extract <file>", "Extract text from document"),
            ("pages <file>", "List pages (PDF)"),
            ("metadata <file>", "Extract metadata"),
            ("--format txt|md|json", "Output format"),
            ("--json", "JSON output"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "PDF extraction (pymupdf optional)",
            "DOCX via zipfile + xml",
            "TXT with encoding detection",
            "Page/paragraph structure",
            "Metadata extraction",
            "Batch processing",
        ],
    },
    "ascii-art-creator": {
        "name": "ASCII Art Creator", "tool": "ascii_art.py",
        "desc": "Generate banners, boxes, cowsay-style art, tables, and image-to-ASCII with multiple fonts",
        "tags": ["ascii", "art", "banner", "cowsay", "cli", "terminal"],
        "commands": [
            ("banner <text>", "Create a text banner"),
            ("box <text>", "Draw a box around text"),
            ("cow <text>", "Cowsay-style speech bubble"),
            ("table <data>", "ASCII table from data"),
            ("image <file>", "Convert image to ASCII"),
            ("--font N", "Select font (3 available)"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "3 fonts × 5 commands",
            "Banner generation",
            "4 box styles",
            "5 cow faces",
            "ASCII tables",
            "Image-to-ASCII (PIL/pymupdf/PPM)",
        ],
    },
    "json-tools": {
        "name": "JSON Tools", "tool": "json_tools.py",
        "desc": "Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths",
        "tags": ["json", "tools", "validate", "query", "diff", "cli", "data"],
        "commands": [
            ("validate <file>", "Validate JSON syntax"),
            ("format <file>", "Pretty-print JSON"),
            ("query <file> <path>", "Query with dot-notation"),
            ("diff <a> <b>", "Diff two JSON files"),
            ("filter <file> <expr>", "Filter array elements"),
            ("flatten <file>", "Flatten nested JSON"),
            ("merge <a> <b>", "Deep-merge JSON"),
            ("stats <file>", "Show statistics"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "8 commands (validate/format/query/diff/filter/stats/flatten/merge)",
            "Dot-notation querying",
            "JSON diff with structural comparison",
            "Array filtering",
            "Flatten nested structures",
            "Deep merge",
        ],
    },
    "md-linter": {
        "name": "Markdown Linter", "tool": "md_linter.py",
        "desc": "Lint and auto-format Markdown: trailing whitespace, frontmatter validation, TOC generation",
        "tags": ["markdown", "lint", "format", "toc", "cli", "docs"],
        "commands": [
            ("check <file>", "Lint a Markdown file"),
            ("frontmatter <file>", "Validate YAML frontmatter"),
            ("toc <file>", "Generate table of contents"),
            ("format <file>", "Auto-format (dry-run by default)"),
            ("toc --insert <file>", "Insert TOC into file"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Trailing whitespace detection (CI-friendly exit 1)",
            "Frontmatter validation",
            "TOC generation with nesting",
            "Format with dry-run",
            "TOC insertion",
            "Multiple rule sets",
        ],
    },
    "file-watcher": {
        "name": "File Watcher", "tool": "file_watcher.py",
        "desc": "Monitor directories for changes: snapshots, diffs, glob filtering, event detection",
        "tags": ["file", "watch", "monitor", "diff", "cli", "automation"],
        "commands": [
            ("once <dir>", "Take a snapshot"),
            ("once <dir> --output FILE", "Save snapshot to file"),
            ("diff <a> <b>", "Diff two snapshots"),
            ("watch <dir>", "Watch for changes (long-running)"),
            ("--glob PATTERN", "Filter by glob"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Snapshot capture",
            "Hash/MD5 tracking",
            "Glob filtering",
            "Create/delete/modify detection",
            "Diff between snapshots",
            "Watch mode",
        ],
    },
    "secret-scanner": {
        "name": "Secret Scanner", "tool": "secret_scanner.py",
        "desc": "Detect API keys, tokens, and credentials in code with 50+ patterns, entropy analysis, and multiple report formats",
        "tags": ["security", "secret", "scan", "audit", "cli", "credentials"],
        "commands": [
            ("scan <path>", "Scan directory for secrets"),
            ("check <file>", "Deep-scan single file"),
            ("list-patterns", "List all detection patterns"),
            ("validate-line <text>", "Test a single line"),
            ("export-report <path>", "Export report (text/json/csv/html)"),
            ("watch <dir>", "Watch directory for new secrets"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "50+ detection patterns",
            "Context display (surrounding lines)",
            ".gitignore-aware",
            "Multiple report formats (text/json/csv/html)",
            "Entropy detection for random keys",
            "GitHub PAT, OpenAI, JWT, MongoDB, Stripe, SSH",
        ],
    },
    "agent-caps": {
        "name": "Agent Capability Manifest", "tool": "agent_caps.py",
        "desc": "Define, validate, and audit agent capability manifests for safe skill installation",
        "tags": ["agent", "caps", "security", "manifest", "cli", "safety"],
        "commands": [
            ("validate <manifest>", "Validate capability manifest"),
            ("audit <skill>", "Audit a skill folder"),
            ("diff <a> <b>", "Compare manifests"),
            ("report <agent>", "Generate capability report"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Manifest schema validation",
            "Skill audit before install",
            "Capability diffing",
            "Risk scoring",
            "JSON output",
            "CI integration",
        ],
    },
    "agent-sentinel": {
        "name": "Agent Sentinel", "tool": "agent_sentinel.py",
        "desc": "Scan OpenClaw/Hermes skills for risky permission patterns before installation",
        "tags": ["security", "audit", "skill", "openclaw", "hermes", "vetting"],
        "commands": [
            ("scan <skill-folder>", "Risk report for a skill"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Simple-named skill requesting shell → HIGH",
            "Shell/exec capability requested → MEDIUM",
            "Hardcoded secret detection → HIGH",
            "No human approval gate → LOW",
            "Network egress without reason",
            "Offline, private, no telemetry",
        ],
    },
    "dev-prompts": {
        "name": "Developer Prompts Pack", "tool": None,
        "desc": "Curated collection of engineering prompts: code review, debugging, architecture, refactoring",
        "tags": ["prompts", "dev", "engineering", "templates", "ai", "productivity"],
        "commands": [
            ("list", "List available prompts"),
            ("show <name>", "Show a prompt template"),
            ("search <query>", "Find relevant prompts"),
        ],
        "features": [
            "30+ engineering prompt templates",
            "Code review prompts",
            "Debugging workflows",
            "Architecture decision prompts",
            "Refactoring guides",
            "Copy-paste ready",
        ],
    },
    "company-ops": {
        "name": "Company Ops", "tool": "autonomy-loop.py",
        "desc": "Operate the autonomous AI company: 24/7 cron loop, task management, revenue tracking",
        "tags": ["company", "ops", "autonomous", "cron", "automation", "ai"],
        "commands": [
            ("loop", "Run autonomy loop tick"),
            ("tasks", "List pending tasks"),
            ("revenue", "Show revenue dashboard"),
            ("status", "Company status report"),
        ],
        "features": [
            "24/7 autonomy loop",
            "Task queue management",
            "Revenue channel tracking",
            "Constitution-as-OS",
            "GitHub source of truth",
            "Human-in-the-loop gates",
        ],
    },
    "agent-cost-tracker": {
        "name": "Agent Cost Tracker", "tool": "agent_cost_tracker.py",
        "desc": "Track LLM API spending per agent/session with budget alerts and CSV export",
        "tags": ["cost", "tracking", "llm", "budget", "cli", "finance"],
        "commands": [
            ("track <agent> <cost>", "Log a cost event"),
            ("report", "Generate cost report"),
            ("budget <agent> <limit>", "Set budget"),
            ("alerts", "Show budget alerts"),
            ("export", "Export to CSV"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Per-agent cost tracking",
            "Session-level attribution",
            "Budget alerts",
            "CSV export",
            "Daily/weekly rollups",
            "JSON output",
        ],
    },
    "agent-health": {
        "name": "Agent Health Monitor", "tool": "agent_health.py",
        "desc": "Monitor agent endpoints, check liveness, collect metrics, alert on failures",
        "tags": ["health", "monitor", "agent", "cli", "observability", "alerts"],
        "commands": [
            ("check <endpoint>", "Health check an agent"),
            ("metrics <agent>", "Collect metrics"),
            ("watch <agent>", "Continuous monitoring"),
            ("alerts", "Show active alerts"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Endpoint liveness checks",
            "Metric collection",
            "Failure alerting",
            "Watch mode",
            "JSON output",
            "Multi-agent support",
        ],
    },
    "agent-logger": {
        "name": "Agent Logger", "tool": "agent_logger.py",
        "desc": "Structured logging for agents: JSON logs, rotation, query, and replay",
        "tags": ["logging", "agent", "cli", "observability", "json", "audit"],
        "commands": [
            ("log <msg>", "Write a log entry"),
            ("query <filter>", "Query logs"),
            ("replay <session>", "Replay a session"),
            ("tail", "Follow live logs"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Structured JSON logs",
            "Log rotation",
            "Query/filter",
            "Session replay",
            "Tail mode",
            "Audit trail",
        ],
    },
    "manifest-diff": {
        "name": "Manifest Diff", "tool": "manifest_diff.py",
        "desc": "Diff agent/skill manifests: capabilities, permissions, versions",
        "tags": ["diff", "manifest", "agent", "cli", "audit", "security"],
        "commands": [
            ("diff <a> <b>", "Diff two manifests"),
            ("capabilities <m>", "Show capabilities"),
            ("permissions <m>", "Show permissions"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Capability diffing",
            "Permission comparison",
            "Version tracking",
            "JSON output",
            "CI integration",
            "Risk highlighting",
        ],
    },
    "cron-doctor": {
        "name": "Cron Doctor", "tool": "cron_doctor.py",
        "desc": "Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures",
        "tags": ["cron", "doctor", "diagnostics", "cli", "scheduler", "debug"],
        "commands": [
            ("diagnose", "Diagnose cron issues"),
            ("list", "List cron jobs"),
            ("fix <job>", "Attempt auto-fix"),
            ("history <job>", "Show run history"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Missed-run detection",
            "Overlap detection",
            "Silent-failure alerts",
            "Auto-fix suggestions",
            "Run history",
            "JSON output",
        ],
    },
    "prompt-templates-cli": {
        "name": "Prompt Templates CLI", "tool": "prompt_templates_cli.py",
        "desc": "Manage reusable prompt templates: create, render, validate with variables",
        "tags": ["prompts", "templates", "cli", "ai", "automation", "render"],
        "commands": [
            ("list", "List templates"),
            ("render <name> --vars x=y", "Render a template"),
            ("create <name>", "Create template"),
            ("validate <name>", "Validate syntax"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Template library",
            "Variable substitution",
            "Validation",
            "Import/export",
            "JSON output",
            "Versioning",
        ],
    },
    "agent-guardrails": {
        "name": "Agent Guardrails", "tool": "agent_guardrails.py",
        "desc": "Enforce safety guardrails on agent actions: permission gates, allowlists, audit",
        "tags": ["guardrails", "safety", "agent", "cli", "security", "policy"],
        "commands": [
            ("check <action>", "Check if action is allowed"),
            ("policy <agent>", "Show agent policy"),
            ("audit <agent>", "Audit violations"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Permission gating",
            "Allowlist/denylist",
            "Policy definition",
            "Violation audit",
            "JSON output",
            "CI integration",
        ],
    },
    "skill-benchmark": {
        "name": "Skill Benchmark", "tool": "skill_benchmark.py",
        "desc": "Benchmark ClawHub skills: performance, correctness, documentation quality",
        "tags": ["benchmark", "skill", "quality", "cli", "testing", "metrics"],
        "commands": [
            ("run <skill>", "Run benchmark suite"),
            ("report <skill>", "Generate report"),
            ("compare <a> <b>", "Compare skills"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Performance benchmarking",
            "Correctness checks",
            "Doc quality scoring",
            "Comparison reports",
            "JSON output",
            "CI integration",
        ],
    },
    "skill-lint": {
        "name": "Skill Linter", "tool": "skill_lint.py",
        "desc": "Lint ClawHub SKILL.md files: frontmatter, structure, command docs, thin-content detection",
        "tags": ["lint", "skill", "clawhub", "cli", "docs", "quality"],
        "commands": [
            ("lint <skill>", "Lint a SKILL.md"),
            ("fix <skill>", "Auto-fix issues"),
            ("audit <dir>", "Audit a skill directory"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Frontmatter validation",
            "Structure checks",
            "Command doc verification",
            "Thin-content detection",
            "Auto-fix mode",
            "JSON output",
        ],
    },
    "prompt-lint": {
        "name": "Prompt Linter", "tool": "prompt_lint.py",
        "desc": "Lint AI prompts: clarity, safety, injection risks, template validity",
        "tags": ["lint", "prompt", "ai", "cli", "safety", "quality"],
        "commands": [
            ("lint <prompt>", "Lint a prompt"),
            ("fix <prompt>", "Suggest fixes"),
            ("scan <dir>", "Scan prompt files"),
            ("self-test", "Run built-in tests"),
        ],
        "features": [
            "Clarity scoring",
            "Safety checks",
            "Injection detection",
            "Template validation",
            "Auto-suggestions",
            "JSON output",
        ],
    },
}

def generate_readme(slug, info):
    name = info["name"]
    tool = info.get("tool")
    desc = info["desc"]
    tags = info["tags"]
    cmds = info["commands"]
    feats = info["features"]

    tag_badges = " ".join(f"![{t}](https://img.shields.io/badge/tag-{t.replace(' ', '%20')}-blue)" for t in tags[:6])

    cmd_table = "\n".join(f"| `{c}` | {d} |" for c, d in cmds)
    feat_list = "\n".join(f"- {f}" for f in feats)

    readme = f"""# {name} 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
{tag_badges}

{desc}

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ Features

{feat_list}

## Commands

| Command | Description |
|---------|-------------|
{cmd_table}

## Quick Start

```bash
# Download (no pip needed)
curl -O https://raw.githubusercontent.com/itsPremkumar/{slug}/main/{tool or 'SKILL.md'}

# Run
python {tool or 'SKILL.md'} self-test
```

## Why {name}?

- **Zero deps** — runs in any Python 3.8+ environment
- **Offline-first** — no telemetry, no uploads, fully private
- **CI-ready** — JSON output + self-tests for pipelines
- **Cross-platform** — identical output on Windows/macOS/Linux

---

📦 Also on [ClawHub](https://clawhub.ai/skills/skills/{slug})  
⭐ Star on [GitHub](https://github.com/itsPremkumar/{slug})  
☕ [Buy Me a Coffee](https://buymeacoffee.com/itsPremkumar)
"""
    return readme

def generate_skill_md(slug, info, existing_frontmatter=None):
    name = info["name"]
    desc = info["desc"]
    tags = info["tags"]
    cmds = info["commands"]
    feats = info["features"]
    tool = info.get("tool")

    cmd_table = "| Command | Description |\n|---------|-------------|\n" + "\n".join(f"| `python {tool} {c}` | {d} |" if tool else f"| `{c}` | {d} |" for c, d in cmds)
    feat_list = "\n".join(f"- **{f}**" for f in feats)

    skill = f"""---
name: {slug}
version: 2.0.0
description: {desc}
tags: [{', '.join(f'"{t}"' for t in tags)}]
---

# {name} v2 🚀

{desc}

Zero dependencies (Python stdlib only). Works on Windows, macOS, Linux.

## ✨ What's New in v2

| Feature | Description |
|---------|-------------|
{chr(10).join(f"| {f.split(' — ')[0] if ' — ' in f else f[:30]} | {f.split(' — ')[1] if ' — ' in f else f} |" for f in feats[:8])}

## Install

```bash
# Requires Python 3.8+. No pip install needed.
curl -O https://raw.githubusercontent.com/itsPremkumar/{slug}/main/{tool or 'SKILL.md'}

# Or copy the file anywhere — it's self-contained.
```

## Commands

{cmd_table}

## Features

{feat_list}

## Example

```bash
python {tool} self-test
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
        run: python {tool} self-test
```

## Why

{name} is built for agent-native workflows: zero dependencies, offline-first, CI-ready.
Part of the Hermes autonomous product stack (31 agent-native tools, all CI-tested).

## Support

Free + MIT. Sponsor if useful:
- GitHub Sponsors: https://github.com/sponsors/itsPremkumar
- Buy Me a Coffee: https://buymeacoffee.com/itsPremkumar

⭐ Star on [GitHub](https://github.com/itsPremkumar/{slug})
"""
    return skill

def main():
    for slug, info in SKILLS.items():
        folder = os.path.join(BASE, slug)
        if not os.path.isdir(folder):
            print(f"SKIP: {slug} (no local folder)")
            continue

        # Generate README.md
        readme = generate_readme(slug, info)
        with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme)

        # Generate v2 SKILL.md
        skill = generate_skill_md(slug, info)
        with open(os.path.join(folder, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(skill)

        # Update .gitignore
        gi_path = os.path.join(folder, ".gitignore")
        with open(gi_path, "a+", encoding="utf-8") as f:
            f.seek(0)
            content = f.read()
            if "__pycache__/" not in content:
                f.write("\n__pycache__/\n*.pyc\n")
        print(f"OK: {slug}")

    print(f"\nGenerated README.md + SKILL.md (v2) for {len(SKILLS)} skills")

if __name__ == "__main__":
    main()
