"""Lesson 30: the capstone gate suite (twin and logic level).

Gate 1: scripted exchange subset. Gate 2: catalogue and
annotation spot checks. Gate 3: failure rehearsal shapes.
Packaging and README gates run in Lesson 31 with their own
tools. Run: python3 gate_suite.py
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
    verdicts = []
    proc = subprocess.Popen([sys.executable, "server_twin.py"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    try:
        init = rpc(proc, 1, "initialize", {"protocolVersion": "2025-11-25",
                   "capabilities": {}, "clientInfo": {"name": "gate", "version": "0"}})
        verdicts.append(("handshake names the server",
                         init["result"]["serverInfo"]["name"] == "leaddesk-twin"))
        tools = rpc(proc, 2, "tools/list")["result"]["tools"]
        names = {t["name"] for t in tools}
        verdicts.append(("catalogue covers the core tools",
                         {"capture_lead", "score_lead", "list_leads"} <= names))
        ok = rpc(proc, 3, "tools/call", {"name": "score_lead", "arguments": {
            "budget_usd": 1500, "timeline_days": 10, "is_decision_maker": True}})
        out = json.loads(ok["result"]["content"][0]["text"])
        verdicts.append(("canonical score is 100 hot", out == {"score": 100, "band": "hot"}))
        bad = rpc(proc, 4, "tools/call", {"name": "capture_lead", "arguments": {
            "name": "X", "email": "not-an-email", "need": "y"}})
        verdicts.append(("bad email lands as isError, not a crash",
                         bad["result"]["isError"] is True))
        unknown = rpc(proc, 5, "tools/call", {"name": "nope", "arguments": {}})
        verdicts.append(("unknown tool is a protocol error",
                         unknown["error"]["code"] == -32602))
    finally:
        proc.stdin.close()
        proc.wait(timeout=5)
    for label, passed in verdicts:
        print(f"{'PASS' if passed else 'FAIL'}  {label}")
    print(f"{sum(p for _, p in verdicts)}/{len(verdicts)} gate checks passed")
    return 0 if all(p for _, p in verdicts) else 1

if __name__ == "__main__":
    raise SystemExit(main())
