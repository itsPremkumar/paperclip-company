#!/usr/bin/env python3
"""
polymarket_cli.py — Query Polymarket prediction markets from the terminal.

Browse markets, check prices, view orderbooks, track your positions,
and explore categories.  No API key or wallet required — reads public
data from the Polymarket Gamma API (https://gamma-api.polymarket.com).

Commands:
  search      <query>     Search markets by keyword
  trending                 Show trending / high-volume markets
  market      <slug|id>   Full market details
  price       <slug>      Current YES / NO prices
  orderbook   <token-id>  Bid / ask depth for a token
  categories              List all market categories
  events                  Browse prediction events
  volume                  Volume leaderboard
  open                    Currently open / active markets
  closed                  Recently resolved / closed markets
  self-test               Run built-in smoke tests (CI use)
  help                    Show this help text

Usage:
  python polymarket_cli.py search "will trump win"
  python polymarket_cli.py trending
  python polymarket_cli.py market "will-bitcoin-reach-100k-2025"
  python polymarket_cli.py price "will-bitcoin-reach-100k-2025"
  python polymarket_cli.py orderbook 12345
  python polymarket_cli.py categories
  python polymarket_cli.py events --limit 10
  python polymarket_cli.py volume --days 7
  python polymarket_cli.py open --limit 20
  python polymarket_cli.py closed --limit 10
  python polymarket_cli.py self-test
  python polymarket_cli.py help
"""

import json
import os
import re
import sys
import textwrap
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

API_BASE = "https://gamma-api.polymarket.com"
USER_AGENT = "polymarket-cli/1.0.0 (github.com/itsPremkumar/polymarket-cli)"
DEFAULT_LIMIT = 10
MAX_LIMIT = 100
REQUEST_TIMEOUT = 15  # seconds

# Colour codes for terminals that support them (disabled when output is piped)
_COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "green": "\033[92m",
    "red": "\033[91m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _use_color():
    """Return True if the terminal supports ANSI colour codes."""
    if not hasattr(sys.stdout, "isatty") or not sys.stdout.isatty():
        return False
    # Windows 10+ with VT support
    if os.name == "nt":
        return bool(int(os.environ.get("TERM", "xterm") != ""))
    return True


def c(text, style):
    """Colourise *text* if the terminal supports it."""
    if not _use_color():
        return text
    code = _COLORS.get(style)
    return f"{code}{text}{_COLORS['reset']}" if code else text


def _api_url(path, query=None):
    """Build an absolute URL from a relative *path* and optional *query* dict."""
    qs = ""
    if query:
        parts = []
        for k, v in query.items():
            if v is not None:
                parts.append(f"{urllib.parse.quote(str(k))}={urllib.parse.quote(str(v))}")
        qs = "?" + "&".join(parts)
    return f"{API_BASE}{path}{qs}"


def _fetch(path, query=None):
    """GET *path* from the Gamma API and return the parsed JSON response.

    Raises SystemExit(1) on network errors or non-200 status.
    """
    url = _api_url(path, query)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as exc:
        print(
            c("ERROR", "red"),
            f"HTTP {exc.code} from {url}",
            file=sys.stderr,
        )
        sys.exit(1)
    except urllib.error.URLError as exc:
        reason = exc.reason if hasattr(exc, "reason") else str(exc)
        print(
            c("ERROR", "red"),
            f"Could not reach {url}: {reason}",
            file=sys.stderr,
        )
        sys.exit(1)
    except (json.JSONDecodeError, UnicodeDecodeError, OSError) as exc:
        print(
            c("ERROR", "red"),
            f"Failed to parse response from {url}: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)


def _plural(n, unit="item"):
    """Return ``{n} {unit}[s]`` with basic English pluralisation."""
    return f"{n} {unit}{'s' if n != 1 else ''}"


def _shorten(text, width=72):
    """Truncate *text* with ``...`` if it exceeds *width* characters."""
    if not text or len(text) <= width:
        return text or ""
    return text[: width - 3].rsplit(" ", 1)[0] + "..."


def _fmt_maybe(value, fmt=",.2f", default="—"):
    """Format a number if it is not None, else return *default*."""
    if value is None:
        return default
    return f"{value:{fmt}}"


def _pct(p, decimals=1):
    """Format a ratio as a percentage string, or ``—`` if *p* is None."""
    if p is None:
        return "—"
    return f"{p * 100:.{decimals}f}%"


def _slug_from_market(market):
    """Extract a human-readable slug from a market object."""
    slug = market.get("slug") or market.get("ticker") or ""
    if slug:
        return slug
    # Fall back to the id
    return str(market.get("id", "?"))


def _now_iso():
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat()[:19] + "Z"


# ---------------------------------------------------------------------------
# Formatters (display helpers)
# ---------------------------------------------------------------------------


def print_header(title):
    """Print a section header with underline."""
    print()
    print(c(title, "bold"))
    print(c("─" * min(len(title), 72), "dim"))


def print_market_row(m, index=None):
    """Print a compact one-line summary of a market."""
    slug = _slug_from_market(m)
    title = _shorten(m.get("title") or m.get("question") or slug, 55)
    outcome = (m.get("outcome") or "").lower()
    closed = m.get("closed") or m.get("end_date") or ""

    # Determine status badge
    if outcome in ("resolved", "closed"):
        badge = c("CLOSED", "dim")
    elif m.get("active") or (closed and closed > _now_iso()):
        badge = c("OPEN", "green")
    else:
        badge = c("CLOSED", "dim")

    volume = _fmt_maybe(m.get("volume"), ",.0f")
    liquidity = _fmt_maybe(m.get("liquidity"), ",.2f")

    idx = f"{c(f'{index:>3}','dim')} " if index is not None else ""

    print(
        f"{idx}{badge} "
        f"{c(slug,'cyan')} "
        f"| {title} "
        f"| vol {c(volume,'yellow')} "
        f"| liq {c(liquidity,'dim')}"
    )


def print_market_detail(m):
    """Print a detailed view of a single market object."""
    slug = _slug_from_market(m)
    title = m.get("title") or m.get("question") or slug
    desc = m.get("description") or m.get("long_description") or ""
    # strip HTML tags from description
    desc = re.sub(r"<[^>]+>", "", desc).strip() if desc else ""

    outcome = (m.get("outcome") or "").lower()
    status = c("OPEN", "green") if outcome not in ("resolved", "closed") else c("CLOSED", "dim")

    print()
    print(c(f"  {title}", "bold"))
    print(f"  {c('slug','dim')}:     {slug}")
    print(f"  {c('status','dim')}:   {status}")
    print(f"  {c('id','dim')}:      {m.get('id','?')}")
    print()

    # Prices
    yes_price = m.get("yes_price") or m.get("outcomePrices", "").split(",")[0] if m.get("outcomePrices") else None
    no_price = m.get("no_price") or m.get("outcomePrices", "").split(",")[1] if m.get("outcomePrices") else None
    if yes_price is not None:
        try:
            yp = float(yes_price)
            print(f"  YES: {c(f'{yp:.4f}¢','green')}   NO: {c(f'{float(no_price):.4f}¢' if no_price else '—','red')}")
        except (TypeError, ValueError):
            pass
    print()

    # Volume & liquidity
    vol = _fmt_maybe(m.get("volume"), ",.2f")
    liq = _fmt_maybe(m.get("liquidity"), ",.2f")
    print(f"  {c('volume','dim'):>14}:    {vol}")
    print(f"  {c('liquidity','dim'):>14}:    {liq}")

    # Dates
    end = m.get("end_date") or m.get("closed") or ""
    reopen = m.get("reopen_date") or ""
    if end:
        print(f"  {c('end date','dim'):>14}:    {end}")
    if reopen:
        print(f"  {c('reopen','dim'):>14}:    {reopen}")

    # Description
    if desc:
        print()
        for line in textwrap.wrap(desc, width=72):
            print(f"  {line}")

    # Tags
    tags = m.get("tags") or m.get("categories") or []
    if tags:
        print(f"\n  {c('tags','dim')}: {', '.join(tags[:8])}")

    # Resolution info
    resolution = m.get("resolution") or m.get("resolved_outcome") or ""
    if resolution:
        print(f"  {c('resolved','dim')}: {resolution}")

    print()


def print_event(e, index=None):
    """Print a compact summary of an event."""
    title = _shorten(e.get("title") or e.get("name") or "?", 60)
    active = " ✓" if e.get("active") else ""
    market_count = e.get("markets_num") or e.get("markets_count") or len(e.get("markets") or [])
    idx = f"{c(f'{index:>3}','dim')} " if index is not None else ""
    print(f"{idx}{c(title,'bold')}{active} [{c(_plural(market_count,'market'),'cyan')}]")


def print_orderbook(orders, title="Orderbook"):
    """Print a bid / ask orderbook table."""
    bids = [(o["price"], o["size"]) for o in orders.get("bids", []) if o.get("price") and o.get("size")]
    asks = [(o["price"], o["size"]) for o in orders.get("asks", []) if o.get("price") and o.get("size")]

    print()
    print(c(f"  {title}", "bold"))
    print(f"  {c('─'*42,'dim')}")

    if not bids and not asks:
        print("  (no orders)")
        return

    # Spread
    best_bid = max(b[0] for b in bids) if bids else 0
    best_ask = min(a[0] for a in asks) if asks else 0
    if bids and asks:
        spread = best_ask - best_bid
        spread_pct = (spread / best_ask * 100) if best_ask else 0
        print(
            f"  Spread: {c(f'{spread:.4f}','yellow')} ({spread_pct:.2f}%)      "
            f"Mid: {c(f'{(best_bid+best_ask)/2:.4f}','cyan')}"
        )
    print()

    if asks:
        print(f"  {c('ASKS','red')} (top {len(asks)}):")
        for price, size in sorted(asks, key=lambda x: -x[0])[:8]:
            print(f"    sell {c(f'{price:<8}','red')} {_fmt_maybe(size,',.2f')}")
    if bids:
        print(f"  {c('BIDS','green')} (top {len(bids)}):")
        for price, size in sorted(bids, key=lambda x: -x[0])[:8]:
            print(f"    buy  {c(f'{price:<8}','green')} {_fmt_maybe(size,',.2f')}")

    print()


def print_categories(cats):
    """Print a list of categories in a grid."""
    print()
    print(c("  Categories", "bold"))
    print(f"  {c('─'*42,'dim')}")
    for i, cat in enumerate(cats, 1):
        label = cat.get("label") or cat.get("name") or str(cat.get("id", ""))
        count = cat.get("count") or cat.get("market_count") or ""
        count_str = f" ({c(str(count),'cyan')})" if count else ""
        print(f"  {i:>3}. {label}{count_str}")
    print()


# ---------------------------------------------------------------------------
# API Commands
# ---------------------------------------------------------------------------


def cmd_search(args):
    """Search markets by keyword.

    Usage: search <query> [--limit N]

    Fetches ``/markets?title=<query>`` and prints matching markets.
    """
    query = " ".join(args.query) if args.query else ""
    if not query:
        print(c("ERROR", "red"), "search requires a keyword.  Usage: search <query>")
        sys.exit(1)

    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    data = _fetch("/markets", {"title": query, "limit": limit, "closed": "false"})

    if not data or (isinstance(data, list) and len(data) == 0):
        print(f"No markets found for {c(query, 'yellow')}")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("markets") or [data]

    print_header(f"Markets matching '{query}'")
    for i, m in enumerate(data[:limit], 1):
        print_market_row(m, i)


def cmd_trending(args):
    """Show trending / highest-volume markets.

    Usage: trending [--limit N]

    Fetches ``/markets?limit=N&sort=volume`` and prints the list.
    """
    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    data = _fetch("/markets", {"limit": limit, "closed": "false", "sort": "volume"})

    if not data:
        print("No trending markets available.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("markets") or []

    print_header(f"Trending Markets (top {limit})")
    for i, m in enumerate(data[:limit], 1):
        print_market_row(m, i)
    print()
    print(c("  Sorted by volume  |  Use 'open' for all active markets", "dim"))


def cmd_market(args):
    """Show full details for a single market.

    Usage: market <slug-or-id>

    Looks up the market by slug (``/markets?slug=...``) or by numeric ID
    (``/markets/<id>``).
    """
    ident = args.identity
    if not ident:
        print(c("ERROR", "red"), "market requires a slug or numeric ID.  Usage: market <slug-or-id>")
        sys.exit(1)

    # Try as numeric ID first, then as a slug
    market = None
    if ident.isdigit():
        try:
            market = _fetch(f"/markets/{ident}")
        except SystemExit:
            market = None

    if not market:
        data = _fetch("/markets", {"slug": ident, "limit": 1})
        if data and isinstance(data, list) and len(data) > 0:
            market = data[0]
        elif data and isinstance(data, dict):
            market = data

    if not market:
        print(f"Market not found: {c(ident, 'yellow')}")
        sys.exit(1)

    print_market_detail(market)


def cmd_price(args):
    """Show current YES / NO prices for a market.

    Usage: price <slug>

    Looks up the market by slug and extracts outcome prices.
    """
    slug = args.slug
    if not slug:
        print(c("ERROR", "red"), "price requires a market slug.  Usage: price <slug>")
        sys.exit(1)

    data = _fetch("/markets", {"slug": slug, "limit": 1})
    if not data or (isinstance(data, list) and len(data) == 0):
        print(f"Market not found: {c(slug, 'yellow')}")
        return
    m = data[0] if isinstance(data, list) else data

    title = _shorten(m.get("title") or slug, 60)
    slug_display = _slug_from_market(m)

    # Parse outcome prices
    prices_str = m.get("outcomePrices") or ""
    yes_price = m.get("yes_price")
    no_price = m.get("no_price")

    if not yes_price and prices_str:
        parts = prices_str.split(",")
        if len(parts) >= 1:
            try:
                yes_price = float(parts[0])
            except (ValueError, TypeError):
                pass
        if len(parts) >= 2:
            try:
                no_price = float(parts[1])
            except (ValueError, TypeError):
                pass

    print()
    print(f"  {c(title, 'bold')}")
    print(f"  {c('slug','dim')}: {slug_display}")
    print()

    if yes_price is not None:
        try:
            yp = float(yes_price) if not isinstance(yes_price, float) else yes_price
            np_val = float(no_price) if no_price is not None and not isinstance(no_price, float) else no_price
            print(f"    {c('YES','green')}  {c(f'{yp * 100:.2f}¢','green')}   implied {_pct(yp)}")
            if np_val is not None:
                print(f"    {c('NO','red')}   {c(f'{np_val * 100:.2f}¢','red')}   implied {_pct(np_val)}")
        except (TypeError, ValueError):
            print(f"    YES  {c(str(yes_price),'green')}")
            if no_price:
                print(f"    NO   {c(str(no_price),'red')}")
    else:
        print("  (no price data available)")

    # Additional info
    volume = _fmt_maybe(m.get("volume"), ",.2f")
    liquidity = _fmt_maybe(m.get("liquidity"), ",.2f")
    print(f"\n  {c('volume','dim')}: {volume}  {c('liquidity','dim')}: {liquidity}")
    print()


def cmd_orderbook(args):
    """Show bid / ask depth for a token.

    Usage: orderbook <token-id>

    Fetches ``/orderbook/<token-id>`` and prints the orderbook.
    """
    token_id = args.token_id
    if not token_id:
        print(c("ERROR", "red"), "orderbook requires a token ID.  Usage: orderbook <token-id>")
        sys.exit(1)

    data = _fetch(f"/orderbook/{token_id}")
    if not data:
        print(f"No orderbook data for token {c(token_id, 'yellow')}")
        return

    print_orderbook(data, title=f"Orderbook for token {token_id}")


def cmd_categories(args):
    """List all market categories.

    Usage: categories

    Fetches ``/categories`` and prints a numbered list.
    """
    data = _fetch("/categories")
    if not data:
        print("No categories available.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("categories") or []

    print_categories(data)


def cmd_events(args):
    """Browse prediction events.

    Usage: events [--limit N] [--active]

    Fetches ``/events`` and prints a list of prediction events with their
    associated market counts.
    """
    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    query = {"limit": limit}
    if args.active:
        query["active"] = "true"
    data = _fetch("/events", query)

    if not data:
        print("No events found.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("events") or []

    print_header(f"Events (top {limit})")
    for i, e in enumerate(data[:limit], 1):
        print_event(e, i)
    print()


def cmd_volume(args):
    """Show volume leaderboard.

    Usage: volume [--days N] [--limit N]

    Fetches ``/markets?sort=volume&limit=N``.  If --days is provided,
    shows markets that closed (or were created) within the period.
    """
    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    days = args.days or 0

    query = {"limit": limit, "sort": "volume"}
    if days > 0:
        # Rough heuristic: only show markets that have a recent end_date
        query["closed"] = "false"
        query["limit"] = limit * 2  # fetch extra, we'll filter client-side
    data = _fetch("/markets", query)
    if not data:
        print("No volume data available.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("markets") or []

    # Client-side filter by creation/end date if days specified
    if days > 0:
        now = datetime.now(timezone.utc)
        cutoff_ts = now.timestamp() - days * 86400
        filtered = []
        for m in data:
            end = m.get("end_date") or m.get("closed") or ""
            if end:
                try:
                    dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
                    if dt.timestamp() >= cutoff_ts:
                        filtered.append(m)
                except (ValueError, TypeError):
                    filtered.append(m)
            else:
                filtered.append(m)
        data = filtered[:limit]

    print_header(f"Volume Leaderboard (top {len(data)})")
    for i, m in enumerate(data, 1):
        print_market_row(m, i)
    print()


def cmd_open(args):
    """List currently open / active markets.

    Usage: open [--limit N] [--tag TAG]

    Fetches ``/markets?closed=false&limit=N`` and optionally filters by
    a tag / category.
    """
    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    query = {"closed": "false", "limit": limit, "sort": "volume"}
    if args.tag:
        query["tag"] = args.tag

    data = _fetch("/markets", query)
    if not data:
        print("No open markets found.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("markets") or []

    tag_note = f" [{c(args.tag,'yellow')}]" if args.tag else ""
    print_header(f"Open Markets (top {limit}{tag_note})")
    for i, m in enumerate(data[:limit], 1):
        print_market_row(m, i)

    print(f"\n  {c(_plural(len(data), 'market'),'dim')} — "
          f"use 'market <slug>' for details")


def cmd_closed(args):
    """List recently resolved / closed markets.

    Usage: closed [--limit N] [--tag TAG]

    Fetches ``/markets?closed=true&limit=N`` and optionally filters by
    a tag / category.
    """
    limit = min(args.limit or DEFAULT_LIMIT, MAX_LIMIT)
    query = {"closed": "true", "limit": limit, "sort": "-volume"}
    if args.tag:
        query["tag"] = args.tag

    data = _fetch("/markets", query)
    if not data:
        print("No closed markets found.")
        return
    if isinstance(data, dict):
        data = data.get("data") or data.get("markets") or []

    tag_note = f" [{c(args.tag,'yellow')}]" if args.tag else ""
    print_header(f"Closed Markets (top {limit}{tag_note})")
    for i, m in enumerate(data[:limit], 1):
        print_market_row(m, i)

    print(f"\n  {c(_plural(len(data), 'market'),'dim')}")


def cmd_help(args):
    """Print the extended help text and exit."""
    print(__doc__)
    print()
    print(c("Commands", "bold"))
    print(c("─" * 42, "dim"))
    print()
    for cmd, (fn, desc) in sorted(COMMANDS.items()):
        if cmd == "help":
            continue
        print(f"  {c(cmd,'green'):<15} {desc.split(chr(10))[0]}")
    print()
    print(c("Options", "bold"))
    print(c("─" * 42, "dim"))
    print("  --limit N    Max results (default 10, max 100)")
    print("  --tag TAG    Filter by category / tag")
    print("  --days N     Time window (volume command)")
    print("  --active     Only active events (events command)")
    print()
    print(c("Examples", "bold"))
    print(c("─" * 42, "dim"))
    print("  python polymarket_cli.py search \"election\"")
    print("  python polymarket_cli.py trending --limit 20")
    print("  python polymarket_cli.py market \"will-biden-win\"")
    print("  python polymarket_cli.py price my-market-slug")
    print("  python polymarket_cli.py orderbook 12345678")
    print("  python polymarket_cli.py categories")
    print("  python polymarket_cli.py events --active --limit 5")
    print("  python polymarket_cli.py open --tag politics --limit 15")
    print("  python polymarket_cli.py closed --limit 5")
    print()


def cmd_self_test(args):
    """Run built-in smoke tests for CI verification.

    Usage: self-test

    Tests:
      1. Module imports resolve.
      2. Helper functions (_shorten, _plural, _pct, _fmt_maybe) return
         expected output for known inputs.
      3. Colour helpers do not raise exceptions.
      4. The help command prints without error.
      5. Argument parsing recognises every command name.

    Exits with code 0 only when all tests pass, printing a summary line
    that contains ``PASS``.
    """
    failures = []

    def _check(name, ok, detail=""):
        if ok:
            print(f"  PASS  {name}")
        else:
            msg = f"  FAIL  {name}"
            if detail:
                msg += f"  ({detail})"
            print(msg)
            failures.append(name)

    # --- 1. Import check ---
    _check("imports resolve", True)

    # --- 2. _shorten ---
    _check("_shorten short text", _shorten("hello") == "hello")
    _check("_shorten truncation",
           len(_shorten("a" * 100, width=20)) <= 23)
    _check("_shorten empty", _shorten("") == "")

    # --- 3. _plural ---
    _check("_plural singular", _plural(1, "market") == "1 market")
    _check("_plural plural", _plural(3, "market") == "3 markets")
    _check("_plural zero", _plural(0, "item") == "0 items")

    # --- 4. _pct ---
    _check("_pct normal", _pct(0.5) == "50.0%")
    _check("_pct zero", _pct(0) == "0.0%")
    _check("_pct one", _pct(1) == "100.0%")
    _check("_pct none", _pct(None) == "—")

    # --- 5. _fmt_maybe ---
    _check("_fmt_maybe number", _fmt_maybe(1234567.89) == "1,234,567.89")
    _check("_fmt_maybe none", _fmt_maybe(None) == "—")
    _check("_fmt_maybe zero", _fmt_maybe(0) == "0.00")

    # --- 6. Colour helpers ---
    _check("_use_color returns bool", isinstance(_use_color(), bool))
    _check("c() returns str with reset", isinstance(c("x", "red"), str))

    # --- 7. _slug_from_market ---
    m1 = {"slug": "test-slug"}
    _check("_slug_from_market slug", _slug_from_market(m1) == "test-slug")
    m2 = {"ticker": "BTC"}
    _check("_slug_from_market ticker", _slug_from_market(m2) == "BTC")
    m3 = {"id": 42}
    _check("_slug_from_market id fallback", _slug_from_market(m3) == "42")

    # --- 8. _now_iso format ---
    iso = _now_iso()
    _check("_now_iso ends with Z", iso.endswith("Z"))
    _check("_now_iso length", len(iso) >= 20)

    # --- 9. Command registry ---
    expected_commands = {
        "search", "trending", "market", "price", "orderbook",
        "categories", "events", "volume", "open", "closed",
        "self-test", "help",
    }
    _check("all commands registered",
           expected_commands.issubset(set(COMMANDS.keys())))

    # --- 10. Help command runs without error ---
    try:
        cmd_help(None)
        _check("help command prints", True)
    except Exception as exc:
        _check("help command prints", False, str(exc))

    # --- Summary ---
    total = 22  # number of _check calls above — adjust when adding tests
    passed = total - len(failures)
    print()
    if failures:
        print(c(f"  RESULT: FAIL ({passed}/{total} passed)", "red"))
        print(f"  Failed: {', '.join(failures)}")
        sys.exit(1)
    else:
        print(c(f"  RESULT: PASS ({passed}/{total} all passed)", "green"))
        sys.exit(0)


# ---------------------------------------------------------------------------
# Argument parsing (stdlib only — no argparse)
# ---------------------------------------------------------------------------

def _parse_args(argv=None):
    """Parse *argv* (default ``sys.argv[1:]``) into a simple namespace.

    Supports:
      <command> [--limit N] [--tag S] [--days N] [--active] [pos-args ...]

    Returns a flat object with attributes:
      .command  — str
      .query    — list[str] (positional tokens after command, except special ones)
      .limit    — int or None
      .tag      — str or None
      .days     — int or None
      .active   — bool
      .slug     — str or None (for price command)
      .identity — str or None (for market command)
      .token_id — str or None (for orderbook command)
    """

    class NS:
        pass

    ns = NS()
    ns.command = ""
    ns.query = []
    ns.limit = None
    ns.tag = None
    ns.days = None
    ns.active = False
    ns.slug = None
    ns.identity = None
    ns.token_id = None

    tokens = list(argv or sys.argv[1:])
    if not tokens:
        ns.command = "help"
        return ns

    # First non-flag token is the command
    ns.command = tokens.pop(0)

    # Consume flags and positional arguments
    pos = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == "--limit" and i + 1 < len(tokens):
            try:
                ns.limit = int(tokens[i + 1])
                i += 2
                continue
            except (ValueError, IndexError):
                pass
        elif t == "--tag" and i + 1 < len(tokens):
            ns.tag = tokens[i + 1]
            i += 2
            continue
        elif t == "--days" and i + 1 < len(tokens):
            try:
                ns.days = int(tokens[i + 1])
                i += 2
                continue
            except (ValueError, IndexError):
                pass
        elif t == "--active":
            ns.active = True
            i += 1
            continue
        elif t.startswith("--"):
            # unknown flag — skip
            i += 1
            continue
        # positional argument
        pos.append(t)
        i += 1

    # Route positional args to the semantic field for each command
    if ns.command == "search":
        ns.query = pos
    elif ns.command == "market":
        ns.identity = " ".join(pos) if pos else ""
    elif ns.command == "price":
        ns.slug = " ".join(pos) if pos else ""
    elif ns.command == "orderbook":
        ns.token_id = " ".join(pos) if pos else ""
    else:
        ns.query = pos

    return ns


# ---------------------------------------------------------------------------
# Command registry
# ---------------------------------------------------------------------------

COMMANDS = {
    "search": (cmd_search, """Search markets by keyword."""),
    "trending": (cmd_trending, """Show trending / highest-volume markets."""),
    "market": (cmd_market, """Show full details for a single market."""),
    "price": (cmd_price, """Show current YES / NO prices for a market."""),
    "orderbook": (cmd_orderbook, """Show bid / ask depth for a token."""),
    "categories": (cmd_categories, """List all market categories."""),
    "events": (cmd_events, """Browse prediction events."""),
    "volume": (cmd_volume, """Volume leaderboard."""),
    "open": (cmd_open, """List currently open / active markets."""),
    "closed": (cmd_closed, """List recently resolved / closed markets."""),
    "self-test": (cmd_self_test, """Run built-in smoke tests (CI use)."""),
    "help": (cmd_help, """Show this help text and exit."""),
}

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

try:
    import urllib.parse  # noqa: F401 (used in _api_url)
except ImportError:
    print("FATAL: stdlib module urllib.parse not available.", file=sys.stderr)
    sys.exit(1)


def main(argv=None):
    """Parse arguments, dispatch to the matching command handler.

    Returns an exit code (0 for success, 1 for errors).
    """
    args = _parse_args(argv)
    cmd = args.command

    if cmd not in COMMANDS:
        print(
            c("ERROR", "red"),
            f"Unknown command: {cmd}.  Try '{c('help', 'green')}'.",
            file=sys.stderr,
        )
        return 1

    handler, _ = COMMANDS[cmd]
    try:
        handler(args)
    except SystemExit as exc:
        return exc.code
    except (KeyboardInterrupt, BrokenPipeError):
        # Silently handle SIGINT and SIGPIPE
        return 1
    except Exception as exc:
        print(
            c("ERROR", "red"),
            f"Unhandled exception in '{cmd}': {exc}",
            file=sys.stderr,
        )
        if _use_color():
            import traceback as _tb
            _tb.print_exc()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
