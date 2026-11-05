"""Smoke test: a full twin protocol exchange over stdio.

Launches server_twin.py as a subprocess, handshakes, discovers
tools, calls them, and checks resources and prompts list. No SDK,
no network, no credentials. Run: python3 smoke_test.py
"""
import json
import subprocess
import sys


def rpc(proc, _id, method, params=None):
    msg = {"jsonrpc": "2.0", "id": _id, "method": method}
    if params:
        msg["params"] = params
    proc.stdin.write(json.dumps(msg) + "\n")
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())


def main():
    proc = subprocess.Popen([sys.executable, "server_twin.py"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            text=True, bufsize=1)
    try:
        init = rpc(proc, 1, "initialize", {"protocolVersion": "2025-11-25",
                     "capabilities": {}, "clientInfo": {"name": "smoke", "version": "0"}})
        assert init["result"]["serverInfo"]["name"] == "leaddesk-twin", init
        tools = rpc(proc, 2, "tools/list")["result"]["tools"]
        names = {t["name"] for t in tools}
        assert {"capture_lead", "score_lead", "list_leads"} <= names, names
        call = rpc(proc, 3, "tools/call", {"name": "score_lead", "arguments": {
            "budget_usd": 1500, "timeline_days": 10, "is_decision_maker": True}})
        out = json.loads(call["result"]["content"][0]["text"])
        assert out["score"] == 100 and out["band"] == "hot", out
        bad = rpc(proc, 4, "tools/call", {"name": "nope", "arguments": {}})
        assert bad["error"]["code"] == -32602, bad
        res = rpc(proc, 5, "resources/list")["result"]["resources"]
        assert res and res[0]["uri"].startswith("leaddesk://"), res
        prompts = rpc(proc, 6, "prompts/list")["result"]["prompts"]
        assert prompts and prompts[0]["name"] == "qualify-lead", prompts
        print(f"smoke ok: handshake, {len(tools)} tools, call, error, resources, prompts")
    finally:
        proc.stdin.close()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
