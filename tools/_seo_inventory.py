import os, re, json

base = r"C:\one\paperclip-company\clawhub-skills"
skills = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))])
inv = {}
for s in skills:
    d = os.path.join(base, s)
    pys = [f for f in os.listdir(d) if f.endswith(".py") and not f.startswith("__")]
    skills_md = os.path.join(d, "SKILL.md")
    readme = os.path.join(d, "README.md")
    fm = {}
    if os.path.exists(skills_md):
        txt = open(skills_md, encoding="utf-8", errors="ignore").read()
        m = re.match(r"^---\s*\n(.*?)\n---", txt, re.S)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
    cli = set()
    for p in pys:
        src = open(os.path.join(d, p), encoding="utf-8", errors="ignore").read()
        for am in re.findall(r'add_argument\(\s*[\'"]([^\'"]+)[\'"]', src):
            for tok in am.split():
                cli.add(tok)
        for sm in re.findall(r'add_parser\(\s*[\'"]([^\'"]+)[\'"]', src):
            cli.add(sm)
    inv[s] = {
        "py": pys,
        "has_readme": os.path.exists(readme),
        "fm_name": fm.get("name", ""),
        "fm_version": fm.get("version", ""),
        "fm_desc": fm.get("description", ""),
        "fm_tags": fm.get("tags", ""),
        "cli_flags": sorted(cli),
    }

print("total skills:", len(inv))
missing_readme = [s for s, v in inv.items() if not v["has_readme"]]
print("missing README:", len(missing_readme), missing_readme)
with open(r"C:\one\paperclip-company\tools\_seo_inventory.json", "w") as f:
    json.dump(inv, f, indent=2)
print("saved inventory -> tools/_seo_inventory.json")
