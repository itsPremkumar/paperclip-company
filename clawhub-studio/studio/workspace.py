"""workspace.py - manage a skill's on-disk folder under data_dir/skills/<slug>.

When the studio creates/updates a skill version it scaffolds real files here so the
test-runner and ClawHub publisher operate on actual skill code, not an empty dir.

Folder layout:
  data_dir/skills/<slug>/
    SKILL.md      (frontmatter from manifest + body)
    <tool>.py     (a generated tool with a real `self-test` subcommand)
"""
import os

import studio.skills as skills

TOOL_TEMPLATE = '''"""Auto-generated tool scaffold for {name}.

Run `python {tool} self-test` to exercise a trivial assertion.
Replace the body of _self_test with your real logic.
"""
import sys


def _self_test() -> int:
    # TODO: replace with real checks for this tool
    assert {name!r}.strip(), "name must not be empty"
    print("self-test: PASS")
    return 0


def main():
    args = sys.argv[1:]
    if args and args[0] == "self-test":
        return _self_test()
    print("usage: python {tool} self-test")
    return 2


if __name__ == "__main__":
    sys.exit(main())
'''


def skill_dir(data_dir: str, slug: str) -> str:
    return os.path.join(data_dir, "skills", slug)


def _tool_name(manifest: dict, slug: str) -> str:
    base = (manifest.get("name") or slug).lower().replace(" ", "_").replace("-", "_")
    return f"{base}.py"


def scaffold(data_dir: str, slug: str, manifest: dict) -> str:
    """Create/update the skill folder from a manifest. Returns the folder path."""
    d = skill_dir(data_dir, slug)
    os.makedirs(d, exist_ok=True)
    body = f"# {manifest.get('name', slug)}\n\n{manifest.get('description', '')}\n"
    with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skills.manifest_to_skill_md(manifest, body=body))
    tool = _tool_name(manifest, slug)
    with open(os.path.join(d, tool), "w", encoding="utf-8") as f:
        f.write(TOOL_TEMPLATE.format(name=manifest.get("name", slug), tool=tool))
    return d


def exists(data_dir: str, slug: str) -> bool:
    return os.path.isdir(skill_dir(data_dir, slug))
