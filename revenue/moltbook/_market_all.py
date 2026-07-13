import json, subprocess, sys, os, time
base = r"C:\one\paperclip-company\revenue\moltbook"
LOG = os.path.join(base, ".posted.json")
drafts = sorted(f for f in os.listdir(base) if f.startswith("post-") and f.endswith(".json"))
done = set()
if os.path.isfile(LOG):
    try: done = set(json.load(open(LOG, encoding="utf-8")))
    except Exception: done = set()
print(f"start: {len(drafts)} drafts, {len(done)} already posted")
for d in drafts:
    if d in done:
        continue
    p = os.path.join(base, d)
    j = json.load(open(p, encoding="utf-8"))
    out = subprocess.run([sys.executable, os.path.join(base, "moltbook.py"), "post",
                        "--title", j["title"], "--content", j["content"], "--submolt", j["submolt"]],
                       capture_output=True, text=True, timeout=30).stdout
    if "201" in out and "success" in out.lower() or '"success": true' in out:
        done.add(d); json.dump(sorted(done), open(LOG, "w"), indent=2)
        print(f"POSTED {d} (total {len(done)}/{len(drafts)})")
    else:
        print(f"DEFER {d}: {out.strip()[:60]}")
        time.sleep(90); continue
    time.sleep(90)  # gap so each post persists (Moltbook rate limit is per-burst)
print(f"DONE: {len(done)}/{len(drafts)} posted")
