"""tests/test_testrunner.py - tests for studio.testrunner + studio.publish.

Uses a temp skill folder; does NOT hit the network (publish uses dry_run).
"""
import os
import sys
import tempfile
import shutil
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import studio.testrunner as T
import studio.publish as P

GOOD_TOOL = (
    'import sys\n'
    'if __name__ == "__main__":\n'
    '    if len(sys.argv) > 1 and sys.argv[1] == "self-test":\n'
    '        print("self-test: PASS"); sys.exit(0)\n'
)
BAD_TOOL = (
    'import sys\n'
    'if __name__ == "__main__":\n'
    '    if len(sys.argv) > 1 and sys.argv[1] == "self-test":\n'
    '        print("self-test: FAIL"); sys.exit(1)\n'
)


class TestSelfTest(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.good = os.path.join(self.d, "good.py")
        self.bad = os.path.join(self.d, "bad.py")
        with open(self.good, "w") as f:
            f.write(GOOD_TOOL)
        with open(self.bad, "w") as f:
            f.write(BAD_TOOL)

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_pass(self):
        r = T.run_self_test(self.good)
        self.assertTrue(r["passed"])
        self.assertEqual(r["rc"], 0)

    def test_fail(self):
        r = T.run_self_test(self.bad)
        self.assertFalse(r["passed"])
        self.assertEqual(r["rc"], 1)

    def test_missing_file(self):
        r = T.run_self_test(os.path.join(self.d, "nope.py"))
        self.assertFalse(r["passed"])


class TestPortfolioFallback(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        open(os.path.join(self.d, "tool.py"), "w").write(GOOD_TOOL)

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_fallback_passes(self):
        r = T.run_portfolio(self.d)
        self.assertTrue(r["passed"])


class TestPublishDryRun(unittest.TestCase):
    def test_dry_run_no_network(self):
        d = tempfile.mkdtemp()
        try:
            r = P.publish_skill(d, dry_run=True)
            self.assertEqual(r["rc"], 0)
            self.assertIn("dry-run", r["output"])
        finally:
            shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
