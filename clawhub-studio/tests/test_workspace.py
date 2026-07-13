"""tests/test_workspace.py - on-disk skill scaffolding."""
import os
import sys
import tempfile
import shutil
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import studio.workspace as ws


class TestWorkspace(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_scaffold_creates_skill_md_and_tool(self):
        folder = ws.scaffold(self.d, "demo", {"name": "Demo", "version": "1.0.0", "description": "x"})
        self.assertTrue(os.path.isdir(folder))
        self.assertTrue(os.path.isfile(os.path.join(folder, "SKILL.md")))
        self.assertTrue(any(f.endswith(".py") for f in os.listdir(folder)))

    def test_generated_tool_self_tests(self):
        folder = ws.scaffold(self.d, "demo", {"name": "Demo", "version": "0.1.0", "description": "d"})
        tool = [f for f in os.listdir(folder) if f.endswith(".py")][0]
        import subprocess
        r = subprocess.run([sys.executable, os.path.join(folder, tool), "self-test"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn("self-test: PASS", r.stdout)

    def test_exists(self):
        self.assertFalse(ws.exists(self.d, "nope"))
        ws.scaffold(self.d, "x", {"name": "X", "version": "0.1.0", "description": "d"})
        self.assertTrue(ws.exists(self.d, "x"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
