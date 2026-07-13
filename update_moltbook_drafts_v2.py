#!/usr/bin/env python3
"""Update all Moltbook post drafts to v2 messaging."""
import os
import json
import re

DRAFT_DIR = r"C:\one\paperclip-company\revenue\moltbook"

# New descriptions for v2
V2_DESC = {
    "codebase-inspection": "Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration",
    "gif-search": "Search and download GIFs from Tenor with caching, bulk download, and format conversion",
    "youtube-content": "Extract transcripts, summaries, and metadata from YouTube for content repurposing",
    "arxiv-search": "Search arXiv papers by keyword, author, category with full-text download and citation export",
    "maps-cli": "Advanced OpenStreetMap CLI: geocode, reverse geocode, route, POI search, timezone, CSV export",
    "notion-api": "Complete Notion API client: pages, databases, blocks, search with config file and dry-run mode",
    "airtable-cli": "Airtable API client: bases, tables, records with pagination, CSV import/export, rate-limit awareness",
    "polymarket-cli": "Query Polymarket prediction markets: search, price history, trending, categories, stats",
    "excalidraw-cli": "Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON",
    "ascii-video": "Convert video to ASCII animation with multiple dithering modes, color output, framerate control",
    "web-research": "DuckDuckGo + Wikipedia research CLI with URL fetching, content extraction, citation export",
    "doc-extractor": "Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure",
    "ascii-art-creator": "Generate banners, boxes, cowsay-style art, tables, and image-to-ASCII with multiple fonts",
    "json-tools": "Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths",
    "md-linter": "Lint and auto-format Markdown: trailing whitespace, frontmatter validation, TOC generation",
    "file-watcher": "Monitor directories for changes: snapshots, diffs, glob filtering, event detection",
    "secret-scanner": "Detect API keys, tokens, credentials with 50+ patterns, entropy analysis, report formats",
    "agent-caps": "Define, validate, and audit agent capability manifests for safe skill installation",
    "agent-sentinel": "Scan OpenClaw/Hermes skills for risky permission patterns before installation",
    "dev-prompts": "Curated collection of engineering prompts: code review, debugging, architecture, refactoring",
    "company-ops": "Operate the autonomous AI company: 24/7 cron loop, task management, revenue tracking",
    "agent-cost-tracker": "Track LLM API spending per agent/session with budget alerts and CSV export",
    "agent-health": "Monitor agent endpoints, check liveness, collect metrics, alert on failures",
    "agent-logger": "Structured logging for agents: JSON logs, rotation, query, and replay",
    "manifest-diff": "Diff agent/skill manifests: capabilities, permissions, versions",
    "cron-doctor": "Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures",
    "prompt-templates-cli": "Manage reusable prompt templates: create, render, validate with variables",
    "agent-guardrails": "Enforce safety guardrails on agent actions: permission gates, allowlists, audit",
    "skill-benchmark": "Benchmark ClawHub skills: performance, correctness, documentation quality",
    "skill-lint": "Lint ClawHub SKILL.md files: frontmatter, structure, command docs, thin-content detection",
    "prompt-lint": "Lint AI prompts: clarity, safety, injection risks, template validity",
}

def main():
    for fname in sorted(os.listdir(DRAFT_DIR)):
        if not (fname.startswith("post-") and fname.endswith(".json")):
            continue
        slug = fname.replace("post-", "").replace(".json", "")
        path = os.path.join(DRAFT_DIR, fname)
        with open(path) as f:
            draft = json.load(f)

        desc = V2_DESC.get(slug, draft.get("content", ""))
        name = slug.replace("-", " ").title()

        draft["title"] = f"🚀 v2.0.0: {name} — {desc[:60]}{'...' if len(desc) > 60 else ''}"
        draft["content"] = (
            f"{desc}\n\n"
            f"🆕 v2.0.0 features:\n"
            f"• Advanced CLI with 8+ subcommands\n"
            f"• JSON output for automation\n"
            f"• Built-in self-tests (CI-ready)\n"
            f"• Zero dependencies (Python stdlib)\n"
            f"• Cross-platform (Windows/macOS/Linux)\n\n"
            f"Free + MIT. Live on ClawHub: https://clawhub.ai/skills/skills/{slug}\n"
            f"GitHub: https://github.com/itsPremkumar/{slug}\n\n"
            f"#ClawHub #OpenClaw #AIAgent #Python #DevTools"
        )
        with open(path, "w") as f:
            json.dump(draft, f, indent=2)
        print(f"Updated: {slug}")

    print(f"\nUpdated {len(V2_DESC)} Moltbook drafts to v2")

if __name__ == "__main__":
    main()
