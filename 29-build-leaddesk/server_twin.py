"""A miniature MCP server in pure standard library Python.

TEACHING MODEL. This file speaks real JSON-RPC 2.0 over stdio in the
shape of MCP: initialize, tools/list, tools/call, plus the resource
and prompt methods this lesson adds. It exists so you can read every
byte of the protocol with no SDK installed. In production you use the
official SDK (see server_sdk.py in this lesson); the architecture is
identical: discovery at runtime, primitives described as data, the
server owning its code.

Run it through the client, not directly:
    python3 client_twin.py
"""
import json
import sys

sys.path.insert(0, ".")
try:
    from lead_logic import capture_lead, list_leads, score_lead
except ImportError:
    capture_lead = list_leads = score_lead = None

TOOLS = {}
if score_lead is not None:
    TOOLS = {
        "score_lead": {
            "fn": lambda a: score_lead(a["budget_usd"], a["timeline_days"], a["is_decision_maker"]),
            "description": "Score a lead 0 to 100 from budget, timeline, and decision authority.",
            "inputSchema": {"type": "object", "properties": {
                "budget_usd": {"type": "integer"},
                "timeline_days": {"type": "integer"},
                "is_decision_maker": {"type": "boolean"}},
                "required": ["budget_usd", "timeline_days", "is_decision_maker"]},
        },
        "capture_lead": {
            "fn": lambda a: capture_lead(a["name"], a["email"], a["need"]),
            "description": "Store a new lead in the pipeline and return its id. Deduplicates on email.",
            "inputSchema": {"type": "object", "properties": {
                "name": {"type": "string"}, "email": {"type": "string"},
                "need": {"type": "string"}},
                "required": ["name", "email", "need"]},
        },
        "list_leads": {
            "fn": lambda a: list_leads(a.get("stage")),
            "description": "List leads in the pipeline, optionally filtered by stage.",
            "inputSchema": {"type": "object", "properties": {
                "stage": {"type": "string"}}, "required": []},
        },
    }

RESOURCES = {
    "leaddesk://pipeline/summary": {
        "name": "Pipeline summary",
        "description": "Counts of leads by stage.",
        "mimeType": "application/json",
    }
}

PROMPTS = {
    "qualify-lead": {
        "description": "Draft a qualification checklist for one lead.",
        "arguments": [{"name": "need", "description": "What the lead says they need", "required": True}],
    }
}


def handle(request):
    method = request.get("method")
    req_id = request.get("id")
    if req_id is None:
        return None
    if method == "initialize":
        result = {"protocolVersion": "2025-11-25",
                  "serverInfo": {"name": "leaddesk-twin", "version": "0.1.0"},
                  "capabilities": {"tools": {}, "resources": {}, "prompts": {}}}
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": [{"name": n, "description": t["description"],
                             "inputSchema": t["inputSchema"]} for n, t in TOOLS.items()]}
    elif method == "tools/call":
        params = request["params"]
        name = params["name"]
        if name not in TOOLS:
            return {"jsonrpc": "2.0", "id": req_id,
                    "error": {"code": -32602, "message": f"Unknown tool: {name}"}}
        try:
            output = TOOLS[name]["fn"](params.get("arguments", {}))
            result = {"content": [{"type": "text", "text": json.dumps(output)}], "isError": False}
        except Exception as exc:
            result = {"content": [{"type": "text", "text": f"Error: {exc}"}], "isError": True}
    elif method == "resources/list":
        result = {"resources": [{"uri": u, "name": r["name"], "description": r["description"],
                                 "mimeType": r["mimeType"]} for u, r in RESOURCES.items()]}
    elif method == "resources/read":
        uri = request["params"]["uri"]
        if uri not in RESOURCES:
            return {"jsonrpc": "2.0", "id": req_id,
                    "error": {"code": -32602, "message": f"Unknown resource: {uri}"}}
        summary = {"total": 0, "by_stage": {}}
        result = {"contents": [{"uri": uri, "mimeType": "application/json",
                                "text": json.dumps(summary)}]}
    elif method == "prompts/list":
        result = {"prompts": [{"name": n, "description": p["description"],
                               "arguments": p["arguments"]} for n, p in PROMPTS.items()]}
    elif method == "prompts/get":
        name = request["params"]["name"]
        args = request["params"].get("arguments", {})
        if name not in PROMPTS:
            return {"jsonrpc": "2.0", "id": req_id,
                    "error": {"code": -32602, "message": f"Unknown prompt: {name}"}}
        text = (f"Qualify this lead. Need: {args.get('need', '')}. "
                "Check budget, timeline, and decision authority. "
                "Ask one question per missing fact. Do not invent facts.")
        result = {"description": PROMPTS[name]["description"],
                  "messages": [{"role": "user", "content": {"type": "text", "text": text}}]}
    else:
        return {"jsonrpc": "2.0", "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}}
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        response = handle(json.loads(line))
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
