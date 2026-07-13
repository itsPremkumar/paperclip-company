#!/usr/bin/env python3
"""Push each ClawHub skill folder to its dedicated GitHub repo with v2 docs."""
import os
import subprocess

BASE = r"C:\one\paperclip-company\clawhub-skills"

# Some repos use different URLs
URL_MAP = {
    "agent-caps": "https://github.com/itsPremkumar/prem-agent-caps.git",
    "agent-sentinel": "https://github.com/itsPremkumar/agent-sentinel.git",
    "dev-prompts": "https://github.com/itsPremkumar/dev-prompts-pack.git",
}

def run(cmd, cwd):
    r = subprocess.run(cmd, shell=True, cwd=cwd,
                      capture_output=True, text=True, timeout=60)
    return r.returncode, r.stdout, r.stderr

def main():
    for slug in sorted(os.listdir(BASE)):
        folder = os.path.join(BASE, slug)
        if not os.path.isdir(folder):
            continue
        url = URL_MAP.get(slug, f"https://github.com/itsPremkumar/{slug}.git")
        print(f"\n=== {slug} ===")

        # Init fresh repo
        run("git init", folder)
        run('git remote remove origin', folder)
        run(f'git remote add origin {url}', folder)

        # Add, commit
        rc, out, err = run("git add -A", folder)
        rc, out, err = run('git commit -m "v2.0.0: advanced features + docs + README"', folder)
        if rc != 0:
            print(f"  commit failed: {err[:200]}")
            continue

        # Branch + pull rebase + push
        run("git branch -m master main", folder)
        rc, out, err = run("git pull origin main --rebase -X theirs", folder)
        # Remove pycache if present
        run("git rm -r --cached __pycache__ 2>/dev/null; echo '__pycache__/' >> .gitignore; echo '*.pyc' >> .gitignore", folder)
        run("git add -A", folder)
        run('git commit -m "chore: remove pycache"', folder)
        rc, out, err = run("git push origin main", folder)
        if rc == 0:
            print(f"  ✅ Pushed {slug}")
        else:
            print(f"  ❌ Push failed: {err[:200]}")

if __name__ == "__main__":
    main()
