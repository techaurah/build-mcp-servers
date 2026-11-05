"""Lesson 18: a Streamable HTTP exchange, annotated.

Read top to bottom. Headers that carry protocol meaning are
kept; the JSON bodies are the same shapes as Lesson 02.
Run: python3 http_exchange.py
"""
EXCHANGE = [
    ("POST /mcp", "Accept: application/json, text/event-stream",
     "initialize request (JSON-RPC in the body)"),
    ("200 OK", "Content-Type: application/json; Mcp-Session-Id: s-123",
     "initialize result; the server assigns a session id in this model"),
    ("POST /mcp", "Mcp-Session-Id: s-123; MCP-Protocol-Version: 2025-11-25",
     "tools/list request"),
    ("200 OK", "Content-Type: application/json", "the tool catalogue"),
    ("POST /mcp", "Mcp-Session-Id: s-123", "tools/call for a slow tool"),
    ("200 OK", "Content-Type: text/event-stream",
     "the answer is a stream: progress notifications, then the final result, then close"),
    ("DELETE /mcp", "Mcp-Session-Id: s-123", "explicit session termination in this model"),
]
NOTES = [
    "One endpoint. No separate /sse URL: that shape is the deprecated transport.",
    "Origin header is validated by the server against DNS rebinding.",
    "A stateless deployment skips session ids entirely and scales more simply.",
]
if __name__ == "__main__":
    for step, headers, note in EXCHANGE:
        print(f"{step:14s} {headers}\n{'':14s} {note}\n")
    for n in NOTES:
        print("NOTE:", n)
