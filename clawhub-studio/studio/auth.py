"""auth.py - signed session tokens (HMAC-SHA256).

ClawHub Studio is local-first: there is no password DB. "Login" mints a
signed token from a shared studio secret (random per data dir, or env
CLAWHUB_STUDIO_SECRET). Any request with a valid signature is authed.
This is enough for a single-user local tool and avoids storing plaintext creds.
"""
import hashlib
import hmac
import os
import secrets
import time

TOKEN_TTL = 60 * 60 * 12  # 12h


def _secret(data_dir: str) -> bytes:
    env = os.environ.get("CLAWHUB_STUDIO_SECRET")
    if env:
        return env.encode()
    path = os.path.join(data_dir, ".studio_secret")
    if os.path.isfile(path):
        with open(path, "rb") as f:
            return f.read()
    tok = secrets.token_bytes(32)
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(tok)
    return tok


def mint_token(data_dir: str) -> str:
    """Return a signed token: <expiry>.<nonce>.<sig>."""
    exp = int(time.time()) + TOKEN_TTL
    nonce = secrets.token_hex(8)
    sig = _sign(data_dir, f"{exp}.{nonce}".encode())
    return f"{exp}.{nonce}.{sig}"


def verify_token(data_dir: str, token: str) -> bool:
    try:
        exp_s, nonce, sig = token.split(".")
        if int(exp_s) < time.time():
            return False
        expected = _sign(data_dir, f"{exp_s}.{nonce}".encode())
        return hmac.compare_digest(expected, sig)
    except Exception:
        return False


def _sign(data_dir: str, msg: bytes) -> str:
    return hmac.new(_secret(data_dir), msg, hashlib.sha256).hexdigest()
