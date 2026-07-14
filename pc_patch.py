#!/usr/bin/env python
# Paperclip issue PATCH/POST helper (no jq on host).
# Usage: pc_patch.py <issueId> <status> <comment_file>
#   or:  pc_patch.py --post <relative_path> <json_file>
import sys, os, json, urllib.request, urllib.error

API = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if not API.endswith("/api"):
    API += "/api"
CID = "3056c999-62ba-4321-ae69-799a61286bad"
KEY = os.environ["PAPERCLIP_API_KEY"]
RID = os.environ["PAPERCLIP_RUN_ID"]

def req(method, path, body=None):
    url = f"{API}/{path}"
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method)
    r.add_header("Authorization", f"Bearer {KEY}")
    r.add_header("X-Paperclip-Run-Id", RID)
    r.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            print("STATUS", resp.status, "->", resp.read().decode()[:400])
    except urllib.error.HTTPError as e:
        print("HTTPERR", e.code, "->", e.read().decode()[:400])

if sys.argv[1] == "--post":
    rel = sys.argv[2]
    jf = sys.argv[3]
    body = json.load(open(jf, encoding="utf-8"))
    req("POST", rel, body)
else:
    iid = sys.argv[1]
    status = sys.argv[2]
    comment = open(sys.argv[3], encoding="utf-8").read()
    body = {"status": status, "comment": comment}
    req("PATCH", f"issues/{iid}", body)
