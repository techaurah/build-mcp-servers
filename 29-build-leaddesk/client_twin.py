"""A miniature MCP client in pure standard library Python.

Launches the twin server as a subprocess (the stdio transport),
performs the handshake, discovers primitives at runtime, and calls
them. Because discovery happens at runtime, this client works with
any server that speaks the same methods. Run: python3 client_twin.py
"""
import json
import subprocess
import sys


class TwinClient:
    def __init__(self, server_command):
        self.proc = subprocess.Popen(server_command, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, text=True, bufsize=1)
        self._next_id = 1

    def request(self, method, params=None):
        req_id = self._next_id
        self._next_id += 1
        message = {"jsonrpc": "2.0", "id": req_id, "method": method}
        if params:
            message["params"] = params
        self.proc.stdin.write(json.dumps(message) + "\n")
        self.proc.stdin.flush()
        response = json.loads(self.proc.stdout.readline())
        if "error" in response:
            raise RuntimeError(f"Server error: {response['error']['message']}")
        return response["result"]

    def notify(self, method):
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": method}) + "\n")
        self.proc.stdin.flush()

    def call_tool(self, name, arguments):
        result = self.request("tools/call", {"name": name, "arguments": arguments})
        if result.get("isError"):
            raise RuntimeError(result["content"][0]["text"])
        return json.loads(result["content"][0]["text"])

    def close(self):
        self.proc.stdin.close()
        self.proc.wait(timeout=5)


if __name__ == "__main__":
    client = TwinClient([sys.executable, "server_twin.py"])
    try:
        info = client.request("initialize", {
            "protocolVersion": "2025-11-25",
            "capabilities": {},
            "clientInfo": {"name": "twin-client", "version": "0.1.0"}})
        print(f"Connected to {info['serverInfo']['name']} v{info['serverInfo']['version']}")
        client.notify("notifications/initialized")
        tools = client.request("tools/list")["tools"]
        print(f"Discovered {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool['name']}: {tool['description']}")
        lead = client.call_tool("capture_lead", {
            "name": "Amara", "email": "amara@example.com",
            "need": "AI booking assistant for a dental clinic"})
        print(f"\ncapture_lead -> {json.dumps(lead)}")
        score = client.call_tool("score_lead", {
            "budget_usd": 1500, "timeline_days": 10, "is_decision_maker": True})
        print(f"score_lead   -> {json.dumps(score)}")
        print(f"list_leads   -> {json.dumps(client.call_tool('list_leads', {}))}")
    finally:
        client.close()
