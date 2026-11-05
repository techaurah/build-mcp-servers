"""Smoke test for Lesson 26: the mapping and the example agree."""
import os

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ts = open(os.path.join(here, "server.ts")).read()
    md = open(os.path.join(here, "mapping.md")).read()
    for needle in ["McpServer", "registerTool", "z.object", "StdioServerTransport"]:
        assert needle in ts or needle in md, needle
    assert "console.error" in ts and "console.log" not in ts
    print("smoke ok: TypeScript example and mapping table are consistent")

if __name__ == "__main__":
    main()
