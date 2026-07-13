#!/usr/bin/env python3
"""studio/__main__.py - CLI entry for ClawHub Studio.

Usage:
  python -m studio serve [--port 8000] [--data-dir ./data] [--open]
  python -m studio self-test
"""
import argparse
import os
import sys


def _self_test() -> int:
    """Run the backend unit suite; 0 pass / 1 fail."""
    import unittest
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName("tests.test_backend")
    res = unittest.TextTestRunner(verbosity=1).run(suite)
    return 0 if res.wasSuccessful() else 1


def _serve() -> int:
    from studio import server
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--data-dir", default=os.path.join(os.getcwd(), "data"))
    p.add_argument("--open", action="store_true")
    a = p.parse_args(sys.argv[2:])
    server.run(port=a.port, data_dir=a.data_dir, auto_open=a.open)
    return 0


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("usage: python -m studio {serve|self-test}")
        return 2
    cmd = sys.argv[1]
    if cmd == "self-test":
        return _self_test()
    if cmd == "serve":
        return _serve()
    print(f"unknown command: {cmd}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
