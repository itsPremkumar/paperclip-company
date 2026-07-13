import json, urllib.request, os

HERE = "C:/one/paperclip-company"
IID = "8dd054e4-cffb-4442-82a0-bc9a48d49bd9"
BASE = "http://localhost:3100"

jar = open(f"{HERE}/watchdog-cj.txt").read()
ck = ""
for ln in jar.split("\n"):
    if ln and not ln.startswith("#") and len(ln.split("\t")) >= 7:
        p = ln.split("\t")
        ck = f"{p[5]}={p[6].strip()}"
        break

def get(path):
    req = urllib.request.Request(BASE + path, headers={"Origin": BASE, "Cookie": ck})
    return urllib.request.urlopen(req, timeout=20).read()

os.makedirs(f"{HERE}/revenue", exist_ok=True)
wp = json.loads(get(f"/api/issues/{IID}/work-products"))
print("work products:", len(wp))
for w in wp:
    att = (w.get("metadata") or {}).get("attachmentId")
    title = w.get("title") or "asset"
    if not att:
        print("skip (no att):", title)
        continue
    data = get(f"/api/attachments/{att}/content")
    fn = title.lower().replace(" ", "-").replace("(", "").replace(")", "") + ".md"
    open(f"{HERE}/revenue/{fn}", "wb").write(data)
    print(f"  saved revenue/{fn}  ({len(data)} bytes)  [{title}]")
print("DONE")
