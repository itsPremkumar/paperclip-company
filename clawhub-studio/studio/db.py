"""db.py - SQLite-backed repository for ClawHub Studio.

Single source of truth for skills, versions, runs. Zero-dependency.
Schema is versioned via PRAGMA user_version so migrations are explicit.
"""
import sqlite3
import os
import time

SCHEMA_VERSION = 1


def connect(path: str) -> sqlite3.Connection:
    """Open (and migrate) the studio database."""
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    _migrate(con)
    return con


def _migrate(con: sqlite3.Connection) -> None:
    cur = con.execute("PRAGMA user_version").fetchone()[0]
    if cur < 1:
        con.executescript(
            """
            CREATE TABLE skill (
                id          INTEGER PRIMARY KEY,
                slug        TEXT UNIQUE NOT NULL,
                name        TEXT NOT NULL,
                created_at  REAL NOT NULL,
                updated_at  REAL NOT NULL
            );
            CREATE TABLE version (
                id          INTEGER PRIMARY KEY,
                skill_id    INTEGER NOT NULL REFERENCES skill(id) ON DELETE CASCADE,
                version     TEXT NOT NULL,
                manifest    TEXT NOT NULL,
                status      TEXT NOT NULL DEFAULT 'draft',
                published   INTEGER NOT NULL DEFAULT 0,
                created_at  REAL NOT NULL,
                UNIQUE (skill_id, version)
            );
            CREATE TABLE run (
                id          INTEGER PRIMARY KEY,
                version_id  INTEGER NOT NULL REFERENCES version(id) ON DELETE CASCADE,
                kind        TEXT NOT NULL,
                passed      INTEGER,
                output      TEXT NOT NULL,
                created_at  REAL NOT NULL
            );
            CREATE INDEX idx_version_skill ON version(skill_id);
            CREATE INDEX idx_run_version ON run(version_id);
            """
        )
        con.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        con.commit()


# ---- skill ----------------------------------------------------------------
def create_skill(con, slug: str, name: str) -> int:
    now = time.time()
    cur = con.execute(
        "INSERT INTO skill (slug, name, created_at, updated_at) VALUES (?,?,?,?)",
        (slug, name, now, now),
    )
    con.commit()
    return cur.lastrowid


def get_skill(con, slug: str):
    return con.execute("SELECT * FROM skill WHERE slug=?", (slug,)).fetchone()


def list_skills(con):
    return con.execute("SELECT * FROM skill ORDER BY updated_at DESC").fetchall()


# ---- version --------------------------------------------------------------
def add_version(con, slug: str, version: str, manifest: str, status: str = "draft") -> int:
    sk = get_skill(con, slug)
    if sk is None:
        raise KeyError(f"skill {slug!r} does not exist")
    now = time.time()
    cur = con.execute(
        "INSERT INTO version (skill_id, version, manifest, status, created_at) VALUES (?,?,?,?,?)",
        (sk["id"], version, manifest, status, now),
    )
    con.commit()
    return cur.lastrowid


def get_version(con, slug: str, version: str):
    return con.execute(
        "SELECT v.* FROM version v JOIN skill s ON v.skill_id=s.id WHERE s.slug=? AND v.version=?",
        (slug, version),
    ).fetchone()


def list_versions(con, slug: str):
    return con.execute(
        "SELECT v.* FROM version v JOIN skill s ON v.skill_id=s.id WHERE s.slug=? ORDER BY v.created_at DESC",
        (slug,),
    ).fetchall()


# ---- run -------------------------------------------------------------------
def record_run(con, version_id: int, kind: str, passed: bool, output: str) -> int:
    cur = con.execute(
        "INSERT INTO run (version_id, kind, passed, output, created_at) VALUES (?,?,?,?,?)",
        (version_id, kind, 1 if passed else 0, output, time.time()),
    )
    con.commit()
    return cur.lastrowid


def list_runs(con, version_id: int):
    return con.execute(
        "SELECT * FROM run WHERE version_id=? ORDER BY created_at DESC", (version_id,)
    ).fetchall()
