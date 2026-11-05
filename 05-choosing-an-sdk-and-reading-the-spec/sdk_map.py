"""Lesson 05: the SDK landscape as this course teaches it.

Facts as observed in November 2026 from the official docs,
the SDK repositories, and current guides. Versions move;
the disambiguation rules do not. Run: python3 sdk_map.py
"""
ROWS = [
    ("Official Python SDK v1", "pip: mcp", "from mcp.server.fastmcp import FastMCP",
     "This course's pin (>=1.28,<2). Quickstart API."),
    ("Official Python SDK v2", "pip: mcp (2.x)", "from mcp.server import MCPServer",
     "Renamed class; 2026-07-28 era. Lesson 25 covers migration."),
    ("Standalone FastMCP", "pip: fastmcp", "from fastmcp import FastMCP",
     "Prefect project: composition, proxying, OpenAPI, auth, own client."),
    ("Official TypeScript SDK", "npm: @modelcontextprotocol/sdk",
     "import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'",
     "High level server plus low level Server. Lesson 26."),
    ("Other official SDKs", "C#, Go, Rust, Ruby, Java, Swift, PHP, Kotlin",
     "see the SDKs page", "Same protocol, tiered by completeness."),
]
if __name__ == "__main__":
    for name, install, imp, note in ROWS:
        print(f"{name}\n  install: {install}\n  import:  {imp}\n  note:    {note}\n")
