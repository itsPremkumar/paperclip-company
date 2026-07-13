"""tests/test_skills.py - unit tests for studio.skills (pure domain logic)."""
import os
import sys
import tempfile
import shutil
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import studio.skills as S


class TestParse(unittest.TestCase):
    def test_parses_frontmatter(self):
        md = "---\nname: demo\ndescription: A demo\nversion: 1.0.0\n---\n# Body\ntext"
        p = S.parse_skill_md(md)
        self.assertEqual(p["frontmatter"]["name"], "demo")
        self.assertEqual(p["frontmatter"]["version"], "1.0.0")
        self.assertIn("Body", p["body"])

    def test_no_frontmatter(self):
        p = S.parse_skill_md("just text")
        self.assertEqual(p["frontmatter"], {})


class TestValidate(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(S.validate_manifest({"name": "d", "version": "1.0.0", "description": "x"}), [])

    def test_missing_fields(self):
        errs = S.validate_manifest({"name": "d"})
        self.assertIn("missing required field: version", errs)
        self.assertIn("missing required field: description", errs)

    def test_bad_semver(self):
        errs = S.validate_manifest({"name": "d", "version": "1.0", "description": "x"})
        self.assertTrue(any("semver" in e for e in errs))


class TestBump(unittest.TestCase):
    def test_patch(self):
        self.assertEqual(S.bump_version("1.0.0", "patch"), "1.0.1")

    def test_minor_resets_patch(self):
        self.assertEqual(S.bump_version("1.2.3", "minor"), "1.3.0")

    def test_major_resets_all(self):
        self.assertEqual(S.bump_version("1.2.3", "major"), "2.0.0")

    def test_bad_version(self):
        with self.assertRaises(ValueError):
            S.bump_version("not-semver")


class TestStatus(unittest.TestCase):
    def test_published(self):
        self.assertEqual(S.status_of({}, has_tests=True, published=True), "published")

    def test_ready_with_tests(self):
        m = {"name": "d", "version": "1.0.0", "description": "x"}
        self.assertEqual(S.status_of(m, has_tests=True, published=False), "ready")

    def test_draft_invalid(self):
        self.assertEqual(S.status_of({"name": "d"}, has_tests=True, published=False), "draft")


class TestSerialize(unittest.TestCase):
    def test_roundtrip(self):
        md = S.manifest_to_skill_md({"name": "n", "version": "0.1.0", "description": "d"}, "hello")
        p = S.parse_skill_md(md)
        self.assertEqual(p["frontmatter"]["name"], "n")
        self.assertIn("hello", p["body"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
