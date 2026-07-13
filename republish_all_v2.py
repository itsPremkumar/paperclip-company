#!/usr/bin/env python3
"""Re-publish all 31 ClawHub skills at v2.0.0."""
import subprocess
import os

BASE = r"C:\one\paperclip-company\clawhub-skills"

INFO = {
    "codebase-inspection": ("Codebase Inspector", "codebase,analysis,metrics,devtools,python,cli,ci,reports"),
    "gif-search": ("GIF Search", "gif,search,media,tenor,cli,download"),
    "youtube-content": ("YouTube Content Tools", "youtube,transcript,content,video,cli,automation"),
    "arxiv-search": ("arXiv Search", "arxiv,research,papers,academic,cli,search"),
    "maps-cli": ("Maps CLI", "maps,osm,geocode,routing,poi,cli,location"),
    "notion-api": ("Notion API Toolkit", "notion,api,notes,database,cli,productivity"),
    "airtable-cli": ("Airtable CLI", "airtable,api,database,cli,spreadsheet,automation"),
    "polymarket-cli": ("Polymarket CLI", "polymarket,prediction,markets,trading,cli,crypto"),
    "excalidraw-cli": ("Excalidraw CLI", "excalidraw,diagrams,flowchart,architecture,cli,drawing"),
    "ascii-video": ("ASCII Video Converter", "ascii,video,animation,terminal,cli,art"),
    "web-research": ("Web Research Toolkit", "web,research,search,duckduckgo,wikipedia,cli"),
    "doc-extractor": ("Document Text Extractor", "pdf,docx,extract,text,cli,documents"),
    "ascii-art-creator": ("ASCII Art Creator", "ascii,art,banner,cowsay,cli,terminal"),
    "json-tools": ("JSON Tools", "json,tools,validate,query,diff,cli,data"),
    "md-linter": ("Markdown Linter", "markdown,lint,format,toc,cli,docs"),
    "file-watcher": ("File Watcher", "file,watch,monitor,diff,cli,automation"),
    "secret-scanner": ("Secret Scanner", "security,secret,scan,audit,cli,credentials"),
    "agent-caps": ("Agent Capability Manifest", "agent,caps,security,manifest,cli,safety"),
    "agent-sentinel": ("Agent Sentinel", "security,audit,skill,openclaw,hermes,vetting"),
    "dev-prompts": ("Developer Prompts Pack", "prompts,dev,engineering,templates,ai,productivity"),
    "company-ops": ("Company Ops", "company,ops,autonomous,cron,automation,ai"),
    "agent-cost-tracker": ("Agent Cost Tracker", "cost,tracking,llm,budget,cli,finance"),
    "agent-health": ("Agent Health Monitor", "health,monitor,agent,cli,observability,alerts"),
    "agent-logger": ("Agent Logger", "logging,agent,cli,observability,json,audit"),
    "manifest-diff": ("Manifest Diff", "diff,manifest,agent,cli,audit,security"),
    "cron-doctor": ("Cron Doctor", "cron,doctor,diagnostics,cli,scheduler,debug"),
    "prompt-templates-cli": ("Prompt Templates CLI", "prompts,templates,cli,ai,automation,render"),
    "agent-guardrails": ("Agent Guardrails", "guardrails,safety,agent,cli,security,policy"),
    "skill-benchmark": ("Skill Benchmark", "benchmark,skill,quality,cli,testing,metrics"),
    "skill-lint": ("Skill Linter", "lint,skill,clawhub,cli,docs,quality"),
    "prompt-lint": ("Prompt Linter", "lint,prompt,ai,cli,safety,quality"),
}

def main():
    ok, fail = 0, 0
    for slug, (name, tags) in INFO.items():
        folder = os.path.join(BASE, slug)
        cmd = f'clawhub publish "{folder}" --slug {slug} --name "{name}" --version 2.0.0 --tags "{tags}"'
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        if "Published" in r.stdout or "OK" in r.stdout:
            print(f"✅ {slug}@2.0.0")
            ok += 1
        else:
            print(f"❌ {slug}: {r.stdout[:100]} {r.stderr[:100]}")
            fail += 1
    print(f"\nPublished: {ok}  Failed: {fail}")

if __name__ == "__main__":
    main()
