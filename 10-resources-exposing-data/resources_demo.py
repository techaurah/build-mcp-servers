"""Lesson 10: resources/list and resources/read, printed in full."""
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
        listing = rpc(proc, 2, "resources/list")["result"]
        print("resources/list ->", json.dumps(listing, indent=2))
        uri = listing["resources"][0]["uri"]
        read = rpc(proc, 3, "resources/read", {"uri": uri})["result"]
        print(f"resources/read {uri} ->", json.dumps(read, indent=2))
    finally:
        proc.stdin.close()
        proc.wait(timeout=5)
