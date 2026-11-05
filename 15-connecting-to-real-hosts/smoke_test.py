"""Smoke test for Lesson 15."""
import os
from check_config import check

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    for name, key in [("claude_desktop_config.json", "mcpServers"),
                      ("vscode_mcp.json", "servers")]:
        assert check(os.path.join(here, name), key) == [], name
    print("smoke ok: both host configs are valid and absolute")

if __name__ == "__main__":
    main()
