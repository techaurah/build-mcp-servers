"""The same server built with the official Python MCP SDK (v1 line).

NEEDS THE SDK: run  pip install "mcp[cli]>=1.28,<2"  first.
Import path verified against the official quickstart and the Python
SDK README as read in November 2026: FastMCP lives at
mcp.server.fastmcp in the v1 line. In SDK v2 the class was renamed
MCPServer (from mcp.server import MCPServer); Lesson 25 covers the
version story. This file pins v1 on purpose so the code you read
matches the code most tutorials and the official quickstart show.

The tool functions below are thin wrappers over lead_logic.py. All
real behaviour is tested there, offline, with no SDK installed.
"""
try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit(
        "The MCP Python SDK is not installed. Run: "
        'pip install "mcp[cli]>=1.28,<2"  (see Lesson 00).'
    ) from exc

from lead_logic import capture_lead, list_leads, score_lead

mcp = FastMCP("leaddesk")


@mcp.tool()
def score_lead_tool(budget_usd: int, timeline_days: int, is_decision_maker: bool) -> dict:
    """Score a lead 0 to 100 from budget, timeline, and decision authority."""
    return score_lead(budget_usd, timeline_days, is_decision_maker)


@mcp.tool()
def capture_lead_tool(name: str, email: str, need: str) -> dict:
    """Store a new lead in the pipeline and return its id. Deduplicates on email."""
    return capture_lead(name, email, need)


@mcp.tool()
def list_leads_tool(stage: str | None = None) -> dict:
    """List leads in the pipeline, optionally filtered by stage."""
    return list_leads(stage)


if __name__ == "__main__":
    mcp.run(transport="stdio")
