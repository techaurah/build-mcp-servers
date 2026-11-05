"""Lesson 00: verify the environment this course needs.

Checks Python version, the pinned SDK import (reported, not
fatal, because every lesson has an offline path), and that a
subprocess can be spawned for stdio work. Run: python3 check_environment.py
"""
import subprocess
import sys

def main():
    ok = True
    major, minor = sys.version_info[:2]
    print(f"Python {major}.{minor}")
    if (major, minor) < (3, 11):
        print("FAIL: this course needs Python 3.11 or newer")
        ok = False
    else:
        print("OK: Python version")
    try:
        from mcp.server.fastmcp import FastMCP  # noqa: F401
        print("OK: MCP Python SDK v1 line import (mcp.server.fastmcp)")
    except ImportError:
        print("NOTE: SDK v1 import not found. The offline twins still run.")
        print('      For SDK lessons run: pip install "mcp[cli]>=1.28,<2"')
    out = subprocess.run([sys.executable, "-c", "print('stdio ok')"],
                         capture_output=True, text=True)
    print("OK: subprocess spawn" if out.stdout.strip() == "stdio ok" else "FAIL: subprocess")
    ok = ok and out.stdout.strip() == "stdio ok"
    print("READY" if ok else "NOT READY: fix the FAIL lines above")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
