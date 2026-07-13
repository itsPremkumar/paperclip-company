#!/usr/bin/env python3
"""
Notion API Tool — CLI wrapper for the Notion REST API (v2025-09-03).

Read, create, update, search, and manage Notion pages, databases (data sources),
blocks, and users. All from the terminal with no pip dependencies — stdlib only.

Usage:
    export NOTION_API_KEY=secret_xxxxx

    python notion_api.py search <query>
    python notion_api.py list-databases
    python notion_api.py query-database <id> [--filter <json>] [--sorts <json>]
    python notion_api.py read-page <page-id>
    python notion_api.py read-page-md <page-id>
    python notion_api.py read-blocks <page-id> [--page-size 100]
    python notion_api.py create-page <database-id> --title <title> [--props <json>]
    python notion_api.py create-page-md <parent-id> --title <title> --md <file-or-string>
    python notion_api.py update-page <page-id> --props <json>
    python notion_api.py update-page-md <page-id> --md <file-or-string>
    python notion_api.py append-blocks <page-id> --blocks <json>
    python notion_api.py archive-page <page-id>
    python notion_api.py create-database <page-id> --title <title> --props <json>
    python notion_api.py list-users [--page-size 100]
    python notion_api.py get-user <user-id>
    python notion_api.py list-property-types
    python notion_api.py block-template <type>

Environment:
    NOTION_API_KEY   — required; your Notion integration token (starts with secret_ or ntn_)
    NOTION_VERSION   — optional; default "2025-09-03"
    NOTION_BASE_URL  — optional; default "https://api.notion.com/v1"
"""

import argparse
import json
import os
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants & defaults
# ---------------------------------------------------------------------------

DEFAULT_VERSION = "2025-09-03"
DEFAULT_BASE_URL = "https://api.notion.com/v1"

# Ordered dict of Notion property types with description and example value shape.
PROPERTY_TYPES = {
    "title": {
        "description": "Database title property (exactly one required per database)",
        "example": {"title": [{"text": {"content": "Page Title"}}]},
    },
    "rich_text": {
        "description": "Multi-line text with formatting",
        "example": {"rich_text": [{"text": {"content": "Some rich text content"}}]},
    },
    "number": {
        "description": "Numeric value (integer or float)",
        "example": {"number": 42},
    },
    "select": {
        "description": "Single-select from predefined options",
        "example": {"select": {"name": "Option Name"}},
    },
    "multi_select": {
        "description": "Multi-select from predefined options",
        "example": {"multi_select": [{"name": "Option A"}, {"name": "Option B"}]},
    },
    "date": {
        "description": "Date with optional end date",
        "example": {"date": {"start": "2026-01-15", "end": None}},
    },
    "checkbox": {
        "description": "Boolean checkbox",
        "example": {"checkbox": True},
    },
    "url": {
        "description": "Web URL",
        "example": {"url": "https://example.com"},
    },
    "email": {
        "description": "Email address",
        "example": {"email": "user@example.com"},
    },
    "phone_number": {
        "description": "Phone number (stored as string)",
        "example": {"phone_number": "+1-555-0123"},
    },
    "created_time": {
        "description": "Auto-set creation timestamp (read-only)",
        "example": {"created_time": "2026-01-01T00:00:00.000Z"},
    },
    "created_by": {
        "description": "Auto-set creator reference (read-only)",
        "example": {"created_by": {"id": "user-uuid"}},
    },
    "last_edited_time": {
        "description": "Auto-set last edit timestamp (read-only)",
        "example": {"last_edited_time": "2026-01-02T00:00:00.000Z"},
    },
    "last_edited_by": {
        "description": "Auto-set last editor reference (read-only)",
        "example": {"last_edited_by": {"id": "user-uuid"}},
    },
    "relation": {
        "description": "Links to pages in another database",
        "example": {"relation": [{"id": "target-page-id"}]},
    },
    "rollup": {
        "description": "Computed value from a relation (read-only)",
        "example": {"rollup": {"type": "number", "number": 7}},
    },
    "status": {
        "description": "Database status property (replaces select for status workflows)",
        "example": {"status": {"name": "In Progress"}},
    },
    "files": {
        "description": "File or image attachments",
        "example": {"files": [{"name": "photo.png", "type": "external", "external": {"url": "https://..."}}]},
    },
    "people": {
        "description": "List of Notion user references",
        "example": {"people": [{"id": "user-uuid"}]},
    },
    "formula": {
        "description": "Computed formula value (read-only)",
        "example": {"formula": {"type": "string", "string": "computed-value"}},
    },
    "unique_id": {
        "description": "Auto-incrementing unique ID (read-only)",
        "example": {"unique_id": {"prefix": "TASK", "number": 42}},
    },
    "button": {
        "description": "Button property for database views (read-only via API)",
        "example": {"button": {}},
    },
    "verification": {
        "description": "Verification status property",
        "example": {"verification": {"state": "verified", "verified_by": {"id": "user-uuid"}}},
    },
}

# Mapping of block type names to their example JSON payloads.
BLOCK_TEMPLATES = {
    "paragraph": {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"text": {"content": "Hello world"}}]},
    },
    "heading_1": {
        "object": "block",
        "type": "heading_1",
        "heading_1": {"rich_text": [{"text": {"content": "Heading 1"}}]},
    },
    "heading_2": {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": [{"text": {"content": "Heading 2"}}]},
    },
    "heading_3": {
        "object": "block",
        "type": "heading_3",
        "heading_3": {"rich_text": [{"text": {"content": "Heading 3"}}]},
    },
    "bulleted_list_item": {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": [{"text": {"content": "List item"}}]},
    },
    "numbered_list_item": {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {"rich_text": [{"text": {"content": "Step 1"}}]},
    },
    "to_do": {
        "object": "block",
        "type": "to_do",
        "to_do": {"rich_text": [{"text": {"content": "Task"}}], "checked": False},
    },
    "toggle": {
        "object": "block",
        "type": "toggle",
        "toggle": {"rich_text": [{"text": {"content": "Click to expand"}}]},
    },
    "quote": {
        "object": "block",
        "type": "quote",
        "quote": {"rich_text": [{"text": {"content": "A wise quote"}}]},
    },
    "callout": {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"text": {"content": "Important note"}}],
            "icon": {"emoji": "💡"},
        },
    },
    "code": {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"text": {"content": "print('hello')"}}],
            "language": "python",
        },
    },
    "divider": {
        "object": "block",
        "type": "divider",
        "divider": {},
    },
    "bookmark": {
        "object": "block",
        "type": "bookmark",
        "bookmark": {"url": "https://example.com"},
    },
    "image": {
        "object": "block",
        "type": "image",
        "image": {
            "type": "external",
            "external": {"url": "https://example.com/photo.png"},
        },
    },
    "embed": {
        "object": "block",
        "type": "embed",
        "embed": {"url": "https://example.com"},
    },
    "video": {
        "object": "block",
        "type": "video",
        "video": {
            "type": "external",
            "external": {"url": "https://example.com/video.mp4"},
        },
    },
    "file": {
        "object": "block",
        "type": "file",
        "file": {
            "type": "external",
            "external": {"url": "https://example.com/file.pdf"},
        },
    },
    "pdf": {
        "object": "block",
        "type": "pdf",
        "pdf": {
            "type": "external",
            "external": {"url": "https://example.com/doc.pdf"},
        },
    },
    "table_of_contents": {
        "object": "block",
        "type": "table_of_contents",
        "table_of_contents": {"color": "gray"},
    },
    "breadcrumb": {
        "object": "block",
        "type": "breadcrumb",
        "breadcrumb": {},
    },
    "column_list": {
        "object": "block",
        "type": "column_list",
        "column_list": {"children": []},
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def die(msg: str, code: int = 1) -> None:
    """Print error to stderr and exit."""
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def require_env(var: str) -> str:
    """Get an env var or die."""
    val = os.environ.get(var)
    if not val:
        die(f"${var} is not set. Get an API key at https://notion.so/my-integrations")
    return val


def get_api_key() -> str:
    """Return the Notion API key from environment."""
    return require_env("NOTION_API_KEY")


def get_version() -> str:
    """Return the Notion API version header value."""
    return os.environ.get("NOTION_VERSION", DEFAULT_VERSION)


def get_base_url() -> str:
    """Return the Notion API base URL."""
    return os.environ.get("NOTION_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def build_headers() -> dict:
    """Build standard HTTP headers for Notion API calls."""
    return {
        "Authorization": f"Bearer {get_api_key()}",
        "Notion-Version": get_version(),
        "Content-Type": "application/json",
    }


# ---------------------------------------------------------------------------
# HTTP transport
# ---------------------------------------------------------------------------


def _request(
    method: str,
    path: str,
    body: dict | None = None,
    params: dict | None = None,
) -> dict:
    """
    Make an HTTP request to the Notion API and return the parsed JSON response.

    Raises SystemExit on non-2xx responses with the API error detail.
    """
    base = get_base_url()
    url = f"{base}{path}"

    if params:
        qs = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
        url = f"{url}?{qs}"

    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")

    req = urllib.request.Request(url, data=data, method=method)
    for k, v in build_headers().items():
        req.add_header(k, v)

    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        code = exc.code
        detail = ""
        try:
            err_body = exc.read().decode("utf-8")
            err_obj = json.loads(err_body)
            detail = err_obj.get("message", err_body)
            if err_obj.get("code"):
                detail = f"[{err_obj['code']}] {detail}"
        except Exception:
            detail = exc.reason or str(exc)
        die(f"HTTP {code}: {detail}")
    except urllib.error.URLError as exc:
        die(f"Network error: {exc.reason}")


def get(path: str, params: dict | None = None) -> dict:
    """GET request."""
    return _request("GET", path, params=params)


def post(path: str, body: dict) -> dict:
    """POST request."""
    return _request("POST", path, body=body)


def patch(path: str, body: dict) -> dict:
    """PATCH request."""
    return _request("PATCH", path, body=body)


def delete(path: str) -> dict:
    """DELETE request (Notion does not expose DELETE for pages; we PATCH archived=true)."""
    return _request("DELETE", path)


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------


def paginate(path: str, body: dict | None = None, page_size: int = 100) -> list[dict]:
    """
    Iterate over all pages of a paginated endpoint.
    For POST-based pagination (search, query) send body; for GET-based, pass params.
    """
    results: list[dict] = []
    cursor: str | None = None

    while True:
        payload = dict(body or {})
        payload["page_size"] = page_size
        if cursor:
            payload["start_cursor"] = cursor

        data = _request("POST" if body is not None else "GET", path, body=payload)
        results.extend(data.get("results", []))

        has_more = data.get("has_more", False)
        cursor = data.get("next_cursor")
        if not has_more or not cursor:
            break

    return results


# ---------------------------------------------------------------------------
# API command implementations
# ---------------------------------------------------------------------------


def cmd_search(args: argparse.Namespace) -> None:
    """Search across all pages and databases."""
    body: dict = {}
    if args.query:
        body["query"] = args.query

    results = paginate("/search", body=body, page_size=args.page_size)
    if not results:
        print("No results found.")
        return

    print(f"Found {len(results)} result(s):\n")
    for i, item in enumerate(results, 1):
        obj_type = item.get("object", "?")
        obj_id = item.get("id", "?")
        # Try to extract a title
        title = _extract_title(item)
        url = item.get("url", "")
        print(f"  {i}. [{obj_type}] {title}")
        print(f"     ID: {obj_id}")
        if url:
            print(f"     URL: {url}")
        print()


def cmd_list_databases(args: argparse.Namespace) -> None:
    """List/search databases via the search endpoint with object filter."""
    body: dict = {
        "filter": {"value": "data_source", "property": "object"},
    }
    if args.query:
        body["query"] = args.query

    results = paginate("/search", body=body, page_size=args.page_size)
    if not results:
        print("No databases found.")
        return

    print(f"Found {len(results)} database(s):\n")
    for i, item in enumerate(results, 1):
        title = _extract_title(item)
        db_id = item.get("id", "?")
        url = item.get("url", "")
        # data_source_id specific to 2025-09-03 API
        ds_id = item.get("data_source_id") or item.get("id", "?")
        print(f"  {i}. {title}")
        print(f"     database_id: {db_id}")
        print(f"     data_source_id: {ds_id}")
        if url:
            print(f"     URL: {url}")
        print()


def cmd_query_database(args: argparse.Namespace) -> None:
    """Query a database (data source) with optional filter and sorts."""
    ds_id = args.database_id
    body: dict = {}

    if args.filter:
        try:
            body["filter"] = json.loads(args.filter)
        except json.JSONDecodeError as e:
            die(f"Invalid filter JSON: {e}")

    if args.sorts:
        try:
            body["sorts"] = json.loads(args.sorts)
        except json.JSONDecodeError as e:
            die(f"Invalid sorts JSON: {e}")

    results = paginate(f"/data_sources/{ds_id}/query", body=body, page_size=args.page_size)
    if not results:
        print("No results found.")
        return

    print(f"Found {len(results)} result(s):\n")
    for i, item in enumerate(results, 1):
        title = _extract_title(item)
        item_id = item.get("id", "?")
        print(f"  {i}. {title}  (page_id: {item_id})")
        # Show properties summary
        props = item.get("properties", {})
        for pname, pval in props.items():
            display = _format_property_value(pval)
            if display:
                print(f"     {pname}: {display}")
        print()


def cmd_read_page(args: argparse.Namespace) -> None:
    """Read page metadata (properties)."""
    data = get(f"/pages/{args.page_id}")
    _print_page_details(data)


def cmd_read_page_md(args: argparse.Namespace) -> None:
    """Read page content as markdown."""
    data = get(f"/pages/{args.page_id}/markdown")
    # The markdown endpoint returns a JSON with a "markdown" field
    md = data.get("markdown", data.get("content", ""))
    print(md)


def cmd_read_blocks(args: argparse.Namespace) -> None:
    """Read all blocks (children) of a page."""
    results = paginate(f"/blocks/{args.page_id}/children", page_size=args.page_size)
    if not results:
        print("No blocks found.")
        return

    print(f"Found {len(results)} block(s):\n")
    for i, block in enumerate(results, 1):
        btype = block.get("type", "unknown")
        text = _extract_block_text(block)
        has_children = block.get("has_children", False)
        prefix = f"  {i:>3}. [{btype}]"
        if text:
            print(f"{prefix} {text[:120]}{'…' if len(text) > 120 else ''}")
        else:
            print(f"{prefix} (no text content)")
        if has_children:
            print(f"       ⤷ has children — use read-blocks <block-id> to read them")
        print()


def cmd_create_page(args: argparse.Namespace) -> None:
    """Create a new page in a database."""
    if not args.title:
        die("--title is required")
    if not args.database_id:
        die("database-id argument is required")

    # Build properties from positional title and optional --props JSON
    properties: dict = {
        "Title": {"title": [{"text": {"content": args.title}}]},
    }
    if args.props:
        try:
            extra = json.loads(args.props)
            properties.update(extra)
        except json.JSONDecodeError as e:
            die(f"Invalid --props JSON: {e}")

    body: dict = {
        "parent": {"database_id": args.database_id},
        "properties": properties,
    }
    if args.icon:
        body["icon"] = _parse_icon(args.icon)
    if args.cover:
        body["cover"] = _parse_cover(args.cover)

    data = post("/pages", body)
    print("Page created:")
    _print_page_details(data)


def cmd_create_page_md(args: argparse.Namespace) -> None:
    """Create a page from markdown content."""
    if not args.title:
        die("--title is required")
    if not args.parent_id:
        die("parent-id argument is required")

    md_content = _read_markdown(args.md)

    body: dict = {
        "parent": {"page_id": args.parent_id},
        "properties": {
            "title": [{"text": {"content": args.title}}],
        },
        "markdown": md_content,
    }

    data = post("/pages", body)
    print("Page created from markdown:")
    _print_page_details(data)


def cmd_update_page(args: argparse.Namespace) -> None:
    """Update page properties."""
    if not args.props:
        die("--props JSON is required")
    try:
        properties = json.loads(args.props)
    except json.JSONDecodeError as e:
        die(f"Invalid --props JSON: {e}")

    body: dict = {"properties": properties}
    data = patch(f"/pages/{args.page_id}", body)
    print("Page updated:")
    _print_page_details(data)


def cmd_update_page_md(args: argparse.Namespace) -> None:
    """Update a page with markdown content."""
    md_content = _read_markdown(args.md)
    body: dict = {"markdown": md_content}
    data = patch(f"/pages/{args.page_id}/markdown", body)
    print("Page updated with markdown.")
    print(f"  page_id: {data.get('id', '?')}")


def cmd_append_blocks(args: argparse.Namespace) -> None:
    """Append blocks to a page."""
    if not args.blocks:
        die("--blocks JSON is required")
    try:
        children = json.loads(args.blocks)
    except json.JSONDecodeError as e:
        die(f"Invalid --blocks JSON: {e}")

    if not isinstance(children, list):
        children = [children]

    body: dict = {"children": children}
    data = patch(f"/blocks/{args.page_id}/children", body)
    count = len(data.get("results", data.get("children", [])))
    print(f"Appended {count} block(s) to page {args.page_id}.")


def cmd_archive_page(args: argparse.Namespace) -> None:
    """Archive (move to trash) a page."""
    body: dict = {"archived": True}
    data = patch(f"/pages/{args.page_id}", body)
    print(f"Page '{args.page_id}' archived.")


def cmd_create_database(args: argparse.Namespace) -> None:
    """Create a new database (data source) under a parent page."""
    if not args.title:
        die("--title is required")
    if not args.props:
        die("--props JSON (property schema) is required")
    if not args.parent_id:
        die("parent-page-id argument is required")

    try:
        properties = json.loads(args.props)
    except json.JSONDecodeError as e:
        die(f"Invalid --props JSON: {e}")

    body: dict = {
        "parent": {"page_id": args.parent_id},
        "title": [{"text": {"content": args.title}}],
        "properties": properties,
    }
    if args.icon:
        body["icon"] = _parse_icon(args.icon)
    if args.description:
        body["description"] = [{"text": {"content": args.description}}]
    if args.is_inline:
        body["is_inline"] = True

    data = post("/data_sources", body)
    print("Database created:")
    _print_database_details(data)


def cmd_list_users(args: argparse.Namespace) -> None:
    """List all users in the workspace."""
    results = paginate("/users", page_size=args.page_size)
    if not results:
        print("No users found.")
        return

    print(f"Found {len(results)} user(s):\n")
    for i, user in enumerate(results, 1):
        uid = user.get("id", "?")
        name = user.get("name") or "(no name)"
        utype = user.get("type", "?")
        email = user.get("person", {}).get("email", "") if user.get("type") == "person" else ""
        print(f"  {i}. {name}")
        print(f"     ID: {uid}  Type: {utype}")
        if email:
            print(f"     Email: {email}")
        print()


def cmd_get_user(args: argparse.Namespace) -> None:
    """Get a single user's details."""
    data = get(f"/users/{args.user_id}")
    uid = data.get("id", "?")
    name = data.get("name") or "(no name)"
    utype = data.get("type", "?")
    email = data.get("person", {}).get("email", "") if "person" in data else ""
    avatar = data.get("avatar_url", "")

    print(f"User: {name}")
    print(f"  ID: {uid}")
    print(f"  Type: {utype}")
    if email:
        print(f"  Email: {email}")
    if avatar:
        print(f"  Avatar: {avatar}")


def cmd_list_property_types(args: argparse.Namespace) -> None:
    """Display all supported property types with descriptions and examples."""
    print(f"{'Property Type':<25} Description")
    print("-" * 80)
    for ptype, info in PROPERTY_TYPES.items():
        desc = info["description"]
        print(f"  {ptype:<23} {desc}")
    print()
    print("Use --example <type> to see the JSON shape.")
    if args.example and args.example in PROPERTY_TYPES:
        print(f"\nExample for '{args.example}':")
        print(json.dumps(PROPERTY_TYPES[args.example]["example"], indent=2))


def cmd_block_template(args: argparse.Namespace) -> None:
    """Print a JSON template for a given block type."""
    btype = args.block_type
    if btype not in BLOCK_TEMPLATES:
        types = ", ".join(sorted(BLOCK_TEMPLATES))
        die(f"Unknown block type '{btype}'. Available: {types}")

    print(json.dumps(BLOCK_TEMPLATES[btype], indent=2))


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------


def _extract_title(item: dict) -> str:
    """Extract the best available title from a Notion API object."""
    # Direct title property (most common)
    props = item.get("properties", {})
    for pname in ("title", "Name", "Title", "name"):
        pval = props.get(pname, {})
        if isinstance(pval, dict):
            title_ary = pval.get("title", [])
            if title_ary:
                parts = [t.get("plain_text", "") for t in title_ary]
                return "".join(parts).strip()

    # Object-level title (databases)
    obj_title = item.get("title", [])
    if isinstance(obj_title, list) and obj_title:
        parts = [t.get("plain_text", "") for t in obj_title]
        return "".join(parts).strip()

    # Child page title
    for key in ("child_page", "child_database"):
        child = item.get(key, {})
        if isinstance(child, dict) and child.get("title"):
            return child["title"]

    # Fallback: ID snippet
    return f"(untitled) — {item.get('id', '?')[:12]}…"


def _extract_block_text(block: dict) -> str:
    """Extract readable text from a block."""
    btype = block.get("type", "")
    bdata = block.get(btype, {})
    if btype in ("divider", "table_of_contents", "breadcrumb"):
        return ""
    if btype == "bookmark":
        return bdata.get("url", "")
    if btype == "image":
        caption = bdata.get("caption", [])
        if caption:
            return "".join(t.get("plain_text", "") for t in caption)
        ext = bdata.get("external", {})
        return ext.get("url", "(image)")
    if btype == "embed" or btype == "video" or btype == "file" or btype == "pdf":
        return bdata.get("url", f"({btype})")

    # Rich-text based blocks
    rich_text = bdata.get("rich_text", [])
    parts = [t.get("plain_text", "") for t in rich_text]
    return "".join(parts).strip()


def _format_property_value(pval: dict) -> str:
    """Format a Notion property value for display."""
    ptype = pval.get("type", "")
    if not ptype:
        # Inline-typed properties
        for known in (
            "title", "rich_text", "number", "select", "multi_select", "date",
            "checkbox", "url", "email", "phone_number", "status", "files",
            "people", "relation", "created_time", "created_by",
            "last_edited_time", "last_edited_by", "formula", "rollup",
            "unique_id", "button", "verification",
        ):
            if known in pval:
                ptype = known
                break

    if not ptype or ptype not in pval:
        return ""

    val = pval[ptype]

    if ptype == "title" or ptype == "rich_text":
        return "".join(t.get("plain_text", "") for t in val)
    if ptype == "number":
        return str(val)
    if ptype == "select":
        return val.get("name", "") if isinstance(val, dict) else str(val)
    if ptype == "multi_select":
        if isinstance(val, list):
            return ", ".join(v.get("name", "") for v in val)
        return str(val)
    if ptype == "date":
        start = val.get("start", "") if isinstance(val, dict) else ""
        end = val.get("end", "") if isinstance(val, dict) else ""
        return f"{start} → {end}" if end else start
    if ptype == "checkbox":
        return "✓" if val else "✗"
    if ptype == "url":
        return val or ""
    if ptype == "email":
        return val or ""
    if ptype == "phone_number":
        return val or ""
    if ptype == "status":
        if isinstance(val, dict):
            return val.get("name", "")
        return str(val)
    if ptype == "files":
        if isinstance(val, list):
            names = [f.get("name", "(file)") for f in val]
            return ", ".join(names)
        return str(val)
    if ptype == "people":
        if isinstance(val, list):
            names = [p.get("name", p.get("id", "")[:8]) for p in val]
            return ", ".join(names)
        return str(val)
    if ptype == "relation":
        if isinstance(val, list):
            ids = [r.get("id", "")[:12] for r in val]
            return ", ".join(ids)
        return str(val)
    if ptype in ("created_by", "last_edited_by"):
        return val.get("name", val.get("id", "")[:12]) if isinstance(val, dict) else str(val)
    if ptype == "created_time" or ptype == "last_edited_time":
        return val or ""
    if ptype == "formula":
        ftype = val.get("type", "")
        fval = val.get(ftype, "") if ftype else ""
        return str(fval)
    if ptype == "rollup":
        rtype = val.get("type", "")
        rval = val.get(rtype, "") if rtype else ""
        return str(rval)
    if ptype == "unique_id":
        prefix = val.get("prefix", "")
        number = val.get("number", "")
        return f"{prefix}-{number}" if prefix else str(number)
    if ptype == "button":
        return "(button)"
    if ptype == "verification":
        return val.get("state", "")

    return json.dumps(val, ensure_ascii=False) if val is not None else ""


def _print_page_details(data: dict) -> None:
    """Pretty-print a page object."""
    pid = data.get("id", "?")
    url = data.get("url", "")
    archived = data.get("archived", False)
    created_time = data.get("created_time", "")
    last_edited_time = data.get("last_edited_time", "")
    title = _extract_title(data)

    print(f"  Title:        {title}")
    print(f"  ID:           {pid}")
    if url:
        print(f"  URL:          {url}")
    print(f"  Archived:     {archived}")
    print(f"  Created:      {created_time}")
    print(f"  Updated:      {last_edited_time}")

    # Print all properties
    props = data.get("properties", {})
    if props:
        print(f"  Properties:")
        for pname, pval in props.items():
            display = _format_property_value(pval)
            if display:
                print(f"    {pname}: {display}")
    print()


def _print_database_details(data: dict) -> None:
    """Pretty-print a database (data source) object."""
    title = _extract_title(data)
    did = data.get("id", "?")
    ds_id = data.get("data_source_id", "?")
    url = data.get("url", "")
    props = data.get("properties", {})
    is_inline = data.get("is_inline", False)

    print(f"  Title:        {title}")
    print(f"  database_id:  {did}")
    print(f"  data_source_id: {ds_id}")
    if url:
        print(f"  URL:          {url}")
    print(f"  Inline:       {is_inline}")
    print(f"  Properties:")
    for pname, pdef in props.items():
        ptype = pdef.get("type", "?")
        print(f"    {pname}: {ptype}")
    print()


def _parse_icon(icon_str: str) -> dict:
    """Parse --icon argument into Notion icon format."""
    if icon_str.startswith("http://") or icon_str.startswith("https://"):
        return {"type": "external", "external": {"url": icon_str}}
    # Treat as emoji
    return {"type": "emoji", "emoji": icon_str}


def _parse_cover(cover_str: str) -> dict:
    """Parse --cover argument into Notion cover format."""
    return {"type": "external", "external": {"url": cover_str}}


def _read_markdown(md_source: str) -> str:
    """
    Read markdown content from a file path or inline string.

    If md_source starts with '@', it's treated as a file path.
    If md_source is '-', read from stdin.
    Otherwise treated as inline markdown.
    """
    if md_source == "-":
        return sys.stdin.read()
    if md_source.startswith("@"):
        path = Path(md_source[1:])
        if not path.exists():
            die(f"Markdown file not found: {path}")
        return path.read_text(encoding="utf-8")
    return md_source


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="notion_api",
        description=textwrap.dedent("""\
            Notion API Tool — manage pages, databases, blocks, and users.

            All commands require $NOTION_API_KEY. Get one at
            https://notion.so/my-integrations

            Examples:
              notion_api.py search "meeting notes"
              notion_api.py list-databases
              notion_api.py read-page-md <page-id>
              notion_api.py create-page <db-id> --title "Task"
        """),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Global options
    parser.add_argument("--page-size", type=int, default=100, help="Results per page (default: 100)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted text")

    sub = parser.add_subparsers(dest="command", metavar="<command>", required=True)

    # --- search ---
    p_search = sub.add_parser("search", help="Search across all pages and databases")
    p_search.add_argument("query", nargs="?", default="", help="Search query text")
    p_search.set_defaults(func=cmd_search)

    # --- list-databases ---
    p_list_db = sub.add_parser("list-databases", help="List/search databases (data sources)")
    p_list_db.add_argument("query", nargs="?", default="", help="Optional search filter")
    p_list_db.set_defaults(func=cmd_list_databases)

    # --- query-database ---
    p_qdb = sub.add_parser("query-database", help="Query a database (data source) with filter/sorts")
    p_qdb.add_argument("database_id", help="Database ID or data_source_id")
    p_qdb.add_argument("--filter", help="JSON filter object e.g. '{\"property\":\"Status\",\"select\":{\"equals\":\"Active\"}}'")
    p_qdb.add_argument("--sorts", help="JSON sorts array e.g. '[{\"property\":\"Date\",\"direction\":\"descending\"}]'")
    p_qdb.set_defaults(func=cmd_query_database)

    # --- read-page ---
    p_rp = sub.add_parser("read-page", help="Read page metadata and properties")
    p_rp.add_argument("page_id", help="Notion page ID (UUID)")
    p_rp.set_defaults(func=cmd_read_page)

    # --- read-page-md ---
    p_rpmd = sub.add_parser("read-page-md", help="Read page content as Markdown (agent-friendly)")
    p_rpmd.add_argument("page_id", help="Notion page ID (UUID)")
    p_rpmd.set_defaults(func=cmd_read_page_md)

    # --- read-blocks ---
    p_rb = sub.add_parser("read-blocks", help="Read all block children of a page")
    p_rb.add_argument("page_id", help="Page or block ID whose children to read")
    p_rb.set_defaults(func=cmd_read_blocks)

    # --- create-page ---
    p_cp = sub.add_parser("create-page", help="Create a new page in a database")
    p_cp.add_argument("database_id", help="Database (parent) ID")
    p_cp.add_argument("--title", required=True, help="Page title")
    p_cp.add_argument("--props", help="JSON object of additional property values")
    p_cp.add_argument("--icon", help="Emoji or image URL for page icon")
    p_cp.add_argument("--cover", help="Image URL for page cover")
    p_cp.set_defaults(func=cmd_create_page)

    # --- create-page-md ---
    p_cpmd = sub.add_parser("create-page-md", help="Create a page from Markdown content")
    p_cpmd.add_argument("parent_id", help="Parent page ID")
    p_cpmd.add_argument("--title", required=True, help="Page title")
    p_cpmd.add_argument("--md", required=True,
                        help='Markdown content, @filepath to read a file, or "-" for stdin')
    p_cpmd.set_defaults(func=cmd_create_page_md)

    # --- update-page ---
    p_up = sub.add_parser("update-page", help="Update page properties")
    p_up.add_argument("page_id", help="Page ID to update")
    p_up.add_argument("--props", required=True, help='JSON properties object e.g. \'{"Status":{"select":{"name":"Done"}}}\'')
    p_up.set_defaults(func=cmd_update_page)

    # --- update-page-md ---
    p_upmd = sub.add_parser("update-page-md", help="Update a page with Markdown content")
    p_upmd.add_argument("page_id", help="Page ID to update")
    p_upmd.add_argument("--md", required=True,
                        help='Markdown content, @filepath, or "-" for stdin')
    p_upmd.set_defaults(func=cmd_update_page_md)

    # --- append-blocks ---
    p_ab = sub.add_parser("append-blocks", help="Append blocks to a page")
    p_ab.add_argument("page_id", help="Page ID to append blocks to")
    p_ab.add_argument("--blocks", required=True,
                      help='JSON array of block objects (or a single block)')
    p_ab.set_defaults(func=cmd_append_blocks)

    # --- archive-page ---
    p_arch = sub.add_parser("archive-page", help="Archive (soft-delete / move to trash) a page")
    p_arch.add_argument("page_id", help="Page ID to archive")
    p_arch.set_defaults(func=cmd_archive_page)

    # --- create-database ---
    p_cdb = sub.add_parser("create-database", help="Create a new database (data source)")
    p_cdb.add_argument("parent_id", help="Parent page ID")
    p_cdb.add_argument("--title", required=True, help="Database title")
    p_cdb.add_argument("--props", required=True,
                       help='JSON properties schema e.g. \'{"Name":{"title":{}},"Status":{"select":{"options":[{"name":"Todo"},{"name":"Done"}]}}}\'')
    p_cdb.add_argument("--description", help="Database description")
    p_cdb.add_argument("--icon", help="Emoji or image URL for database icon")
    p_cdb.add_argument("--is-inline", action="store_true", help="Embed database inline in the parent page")
    p_cdb.set_defaults(func=cmd_create_database)

    # --- list-users ---
    p_lu = sub.add_parser("list-users", help="List all workspace users")
    p_lu.set_defaults(func=cmd_list_users)

    # --- get-user ---
    p_gu = sub.add_parser("get-user", help="Get a single user's details")
    p_gu.add_argument("user_id", help="User ID (UUID)")
    p_gu.set_defaults(func=cmd_get_user)

    # --- list-property-types ---
    p_lpt = sub.add_parser("list-property-types", help="List all Notion property types with descriptions")
    p_lpt.add_argument("--example", help="Show JSON example for a specific property type")
    p_lpt.set_defaults(func=cmd_list_property_types)

    # --- block-template ---
    p_bt = sub.add_parser("block-template", help="Print a JSON template for a block type")
    p_bt.add_argument("block_type", help="Block type name (paragraph, heading_1, to_do, divider, etc.)")
    p_bt.set_defaults(func=cmd_block_template)

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    # Import urllib.parse here for the qs builder
    import urllib.parse
    main()
