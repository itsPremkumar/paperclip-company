"""tests/test_backend.py - real unit tests for ClawHub Studio backend layers.

Run:  python -m unittest tests.test_backend -v
Or:  python studio/__main__.py self-test   (calls this)
Uses temp dirs; no network; no secrets.
"""
import os
import sys
import tempfile
import shutil
import unittest

# make the studio package importable
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import studio.db as db
import studio.auth as auth


class TestDB(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.p = os.path.join(self.d, "studio.db")
        self.con = db.connect(self.p)

    def tearDown(self):
        self.con.close()
        shutil.rmtree(self.d, ignore_errors=True)

    def test_schema_version(self):
        v = self.con.execute("PRAGMA user_version").fetchone()[0]
        self.assertEqual(v, db.SCHEMA_VERSION)

    def test_skill_crud(self):
        sid = db.create_skill(self.con, "demo", "Demo")
        self.assertEqual(sid, 1)
        self.assertIsNotNone(db.get_skill(self.con, "demo"))
        self.assertEqual([s["slug"] for s in db.list_skills(self.con)], ["demo"])

    def test_version_crud(self):
        db.create_skill(self.con, "demo", "Demo")
        vid = db.add_version(self.con, "demo", "1.0.0",
                              '{"name":"demo","version":"1.0.0","description":"x"}')
        self.assertEqual(vid, 1)
        vs = db.list_versions(self.con, "demo")
        self.assertEqual([(v["version"], v["status"]) for v in vs], [("1.0.0", "draft")])
        self.assertIsNotNone(db.get_version(self.con, "demo", "1.0.0"))

    def test_run_crud(self):
        db.create_skill(self.con, "demo", "Demo")
        vid = db.add_version(self.con, "demo", "1.0.0", "{}")
        rid = db.record_run(self.con, vid, "self-test", True, "PASS")
        self.assertEqual(rid, 1)
        self.assertEqual(len(db.list_runs(self.con, vid)), 1)

    def test_missing_skill_raises(self):
        with self.assertRaises(KeyError):
            db.add_version(self.con, "nope", "1.0.0", "{}")


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_mint_and_verify(self):
        tok = auth.mint_token(self.d)
        self.assertTrue(auth.verify_token(self.d, tok))

    def test_rejects_garbage(self):
        self.assertFalse(auth.verify_token(self.d, "1.2.3"))

    def test_rejects_wrong_dir(self):
        other = tempfile.mkdtemp()
        tok = auth.mint_token(self.d)
        try:
            self.assertFalse(auth.verify_token(other, tok))
        finally:
            shutil.rmtree(other, ignore_errors=True)

    def test_env_secret(self):
        os.environ["CLAWHUB_STUDIO_SECRET"] = "unittest-secret"
        try:
            tok = auth.mint_token(self.d)
            self.assertTrue(auth.verify_token(self.d, tok))
        finally:
            del os.environ["CLAWHUB_STUDIO_SECRET"]


if __name__ == "__main__":
    unittest.main(verbosity=2)
