"""server.py - REST API for ClawHub Studio (stdlib http.server, zero deps).

Endpoints (all JSON, Authorization: Bearer <token>):
  GET  /api/health
  POST /api/login                      -> {token}
  GET  /api/skills                     -> list
  POST /api/skills  {slug,name}        -> create
  GET  /api/skills/<slug>              -> one
  GET  /api/skills/<slug>/versions
  POST /api/skills/<slug>/versions {version,manifest} -> add version
  POST /api/skills/<slug>/<version>/test  -> run self-test (records run)
  POST /api/skills/<slug>/<version>/publish -> publish to ClawHub (dry by default)

The server stores data under --data-dir (sqlite) and serves the SPA from ./web.
"""
import json
import os
import functools
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import studio.db as db
import studio.auth as auth
import studio.skills as skills
import studio.testrunner as testrunner
import studio.publish as publish


def _json(handler, code, obj):
    body = json.dumps(obj).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def make_handler(data_dir):
    web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "web"))
    ctypes = {
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
        ".ico": "image/x-icon",
    }

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass  # quiet

        def _serve_static(self):
            # map "/" -> index.html; guard against path traversal
            rel = self.path.split("?", 1)[0].lstrip("/")
            if rel == "" or rel == "index.html":
                rel = "index.html"
            target = os.path.normpath(os.path.join(web_root, rel))
            if not target.startswith(web_root) or not os.path.isfile(target):
                return _json(self, 404, {"error": "not found"})
            ext = os.path.splitext(target)[1].lower()
            with open(target, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", ctypes.get(ext, "application/octet-stream"))
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _token(self):
            h = self.headers.get("Authorization", "")
            if h.startswith("Bearer "):
                return h[7:]
            return None

        def _auth(self):
            tok = self._token()
            return tok and auth.verify_token(data_dir, tok)

        def _body(self):
            n = int(self.headers.get("Content-Length", 0) or 0)
            if n == 0:
                return {}
            return json.loads(self.rfile.read(n).decode())

        def _con(self):
            return db.connect(os.path.join(data_dir, "studio.db"))

        def do_GET(self):
            if self.path.startswith("/api/"):
                return self._api_get()
            return self._serve_static()

        def _api_get(self):
            if self.path == "/api/health":
                return _json(self, 200, {"ok": True, "product": "clawhub-studio"})
            if self.path == "/api/skills":
                if not self._auth():
                    return _json(self, 401, {"error": "unauthorized"})
                con = self._con()
                try:
                    rows = db.list_skills(con)
                    return _json(self, 200, [dict(r) for r in rows])
                finally:
                    con.close()
            # /api/skills/<slug>  and  /api/skills/<slug>/versions
            parts = [p for p in self.path.split("/") if p]
            if len(parts) >= 2 and parts[0] == "api" and parts[1] == "skills":
                slug = parts[2]
                if not self._auth():
                    return _json(self, 401, {"error": "unauthorized"})
                con = self._con()
                try:
                    if len(parts) == 3:
                        sk = db.get_skill(con, slug)
                        if not sk:
                            return _json(self, 404, {"error": "not found"})
                        return _json(self, 200, dict(sk))
                    if len(parts) == 4 and parts[3] == "versions":
                        vs = db.list_versions(con, slug)
                        return _json(self, 200, [dict(v) for v in vs])
                finally:
                    con.close()
            return _json(self, 404, {"error": "not found"})

        def do_POST(self):
            parts = [p for p in self.path.split("/") if p]
            if self.path == "/api/login":
                tok = auth.mint_token(data_dir)
                return _json(self, 200, {"token": tok})
            if len(parts) < 2 or parts[0] != "api" or parts[1] != "skills":
                return _json(self, 404, {"error": "not found"})
            if not self._auth():
                return _json(self, 401, {"error": "unauthorized"})
            slug = parts[2] if len(parts) >= 3 else None
            con = self._con()
            try:
                if len(parts) == 2:  # POST /api/skills -> create skill
                    b = self._body()
                    try:
                        sid = db.create_skill(con, b["slug"], b["name"])
                    except Exception:
                        return _json(self, 409, {"error": "exists or invalid"})
                    return _json(self, 201, {"id": sid, "slug": b["slug"]})
                if len(parts) == 3:  # GET one skill (handled in GET); POST here is invalid
                    return _json(self, 405, {"error": "method not allowed"})
                if len(parts) == 4 and parts[3] == "versions":  # add version
                    b = self._body()
                    try:
                        vid = db.add_version(con, slug, b["version"], json.dumps(b.get("manifest", {})))
                        return _json(self, 201, {"id": vid, "version": b["version"]})
                    except KeyError:
                        return _json(self, 404, {"error": "skill missing"})
                    except Exception as e:
                        return _json(self, 400, {"error": str(e)})
                if len(parts) == 5 and parts[4] == "test":  # run self-test
                    ver = parts[3]
                    v = db.get_version(con, slug, ver)
                    if not v:
                        return _json(self, 404, {"error": "version missing"})
                    # locate the skill folder on disk (data_dir/skills/<slug>)
                    folder = os.path.join(data_dir, "skills", slug)
                    res = testrunner.run_portfolio(folder) if os.path.isdir(folder) \
                        else {"passed": False, "rc": -1, "output": "no skill folder"}
                    db.record_run(con, v["id"], "self-test", res["passed"], res["output"])
                    return _json(self, 200, res)
                if len(parts) == 5 and parts[4] == "publish":
                    ver = parts[3]
                    v = db.get_version(con, slug, ver)
                    if not v:
                        return _json(self, 404, {"error": "version missing"})
                    folder = os.path.join(data_dir, "skills", slug)
                    dry = self._body().get("dry_run", True)
                    res = publish.publish_skill(folder, dry_run=dry)
                    if res.get("published"):
                        con.execute("UPDATE version SET published=1 WHERE id=?", (v["id"],))
                        con.commit()
                    return _json(self, 200, res)
            finally:
                con.close()
            return _json(self, 404, {"error": "not found"})

    return Handler


def run(port: int = 8000, data_dir: str = "./data", auto_open: bool = False):
    os.makedirs(data_dir, exist_ok=True)
    web_root = os.path.join(os.path.dirname(__file__), "..", "web")
    Handler = make_handler(os.path.abspath(data_dir))
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}"
    print(f"ClawHub Studio on {url}  (data: {os.path.abspath(data_dir)})")
    if auto_open:
        import webbrowser
        webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
