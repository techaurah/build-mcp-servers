"""Lesson 12: prompts/list and prompts/get, printed in full."""
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

if __name__ == "__main__":
    proc = subprocess.Popen([sys.executable, "server_twin.py"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    try:
        rpc(proc, 1, "initialize", {"protocolVersion": "2025-11-25",
            "capabilities": {}, "clientInfo": {"name": "demo", "version": "0"}})
        print("prompts/list ->", json.dumps(rpc(proc, 2, "prompts/list")["result"], indent=2))
        got = rpc(proc, 3, "prompts/get", {"name": "qualify-lead",
                  "arguments": {"need": "AI booking assistant for a dental clinic"}})
        print("prompts/get ->", json.dumps(got["result"], indent=2))
    finally:
        proc.stdin.close()
        proc.wait(timeout=5)
