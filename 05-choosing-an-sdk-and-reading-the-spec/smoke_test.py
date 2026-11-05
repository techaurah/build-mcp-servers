"""Smoke test for Lesson 05."""
import sdk_map

def main():
    imports = [r[2] for r in sdk_map.ROWS]
    assert any("mcp.server.fastmcp" in i for i in imports)
    assert any("from fastmcp import" in i for i in imports)
    assert any("MCPServer" in i for i in imports)
    print("smoke ok: v1, v2, and standalone FastMCP are all distinguished")

if __name__ == "__main__":
    main()
