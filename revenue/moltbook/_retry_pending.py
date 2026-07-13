import json, subprocess, sys, os, time
base = r"C:\one\paperclip-company\revenue\moltbook"
# all pending drafts (4 new + 2 still rate-limited from before)
drafts = ["post-dev-prompts", "post-company-ops", "post-agent-cost-tracker",
          "post-skill-lint", "post-prompt-lint", "post-agent-health"]
for f in drafts:
    p = os.path.join(base, f + ".json")
    if not os.path.isfile(p):
        print(f, "-> missing, skip"); continue
    d = json.load(open(p, encoding="utf-8"))
    posted = False
    for attempt in range(20):  # up to ~10 min with 30s backoff
        r = subprocess.run([sys.executable, os.path.join(base, "moltbook.py"), "post",
                            "--title", d["title"], "--content", d["content"], "--submolt", d["submolt"]],
                           capture_output=True, text=True)
        out = (r.stdout or r.stderr).strip()
        if "201" in out:
            print(f, "-> POSTED 201"); posted = True; break
        if "403" in out:
            print(f, "-> 403 claimed-agent required, stop"); break
        time.sleep(30)
    if not posted:
        print(f, "-> NOT posted (rate-limited after retries)")
