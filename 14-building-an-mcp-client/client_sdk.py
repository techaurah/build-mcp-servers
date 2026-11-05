"""Lesson 14: the SDK client shape (reference file).

NEEDS THE SDK: pip install "mcp[cli]>=1.28,<2".
The v1 client API: stdio_client owns the process through
StdioServerParameters; ClientSession owns the protocol.
Compare each block with client_twin.py to see what the SDK
carries for you, and what it hides (the handshake order and
the error shapes are still yours to handle).
"""
import asyncio
import sys

async def main():
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    params = StdioServerParameters(
        command=sys.executable, args=["server_sdk.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])
            result = await session.call_tool("score_lead_tool", {
                "budget_usd": 1500, "timeline_days": 10,
                "is_decision_maker": True})
            print("Result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
