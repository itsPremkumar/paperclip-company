"""tests/test_server.py - end-to-end REST smoke test for studio.server.

Spins up the server on a free port with a temp data dir and exercises the API.
No network beyond localhost.
"""
import os
import sys
import json
import time
import tempfile
import shutil
import threading
import unittest
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from studio import server


def _free_port():
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.mkdtemp()
        cls.port = _free_port()
        threading.Thread(
            target=server.run, kwargs={"port": cls.port, "data_dir": cls.d, "auto_open": False},
            daemon=True,
        ).start()
        time.sleep(1.0)
        cls.base = f"http://127.0.0.1:{cls.port}"

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.d, ignore_errors=True)

    def call(self, method, path, token=None, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        if token:
            req.add_header("Authorization", "Bearer " + token)
        try:
            r = urllib.request.urlopen(req, timeout=10)
            return r.status, json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode())

    def test_health(self):
        self.assertEqual(self.call("GET", "/api/health")[0], 200)

    def test_login_and_auth(self):
        sc, login = self.call("POST", "/api/login")
        self.assertEqual(sc, 200)
        tok = login["token"]
        self.assertGreater(len(tok), 10)
        self.assertEqual(self.call("GET", "/api/skills", token=tok)[0], 200)
        # no token -> 401
        self.assertEqual(self.call("GET", "/api/skills")[0], 401)

    def test_create_and_version_flow(self):
        sc, login = self.call("POST", "/api/login")
        tok = login["token"]
        self.assertEqual(self.call("POST", "/api/skills", token=tok,
                                   body={"slug": "demo", "name": "Demo"})[0], 201)
        self.assertEqual(self.call("GET", "/api/skills", token=tok)[0], 200)
        self.assertEqual(self.call("POST", "/api/skills/demo/versions", token=tok,
                                   body={"version": "1.0.0",
                                         "manifest": {"name": "demo", "version": "1.0.0", "description": "x"}})[0], 201)
        sc, vs = self.call("GET", "/api/skills/demo/versions", token=tok)
        self.assertEqual(sc, 200)
        self.assertEqual(len(vs), 1)

    def test_publish_dry_run(self):
        sc, login = self.call("POST", "/api/login")
        tok = login["token"]
        self.call("POST", "/api/skills", token=tok, body={"slug": "p", "name": "P"})
        self.call("POST", "/api/skills/p/versions", token=tok,
                  body={"version": "0.1.0", "manifest": {"name": "p", "version": "0.1.0", "description": "x"}})
        # the studio writes skill files under data_dir/skills/<slug>; create it
        os.makedirs(os.path.join(self.d, "skills", "p"), exist_ok=True)
        sc, res = self.call("POST", "/api/skills/p/0.1.0/publish", token=tok, body={"dry_run": True})
        self.assertEqual(sc, 200)
        self.assertIn("dry-run", res["output"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
