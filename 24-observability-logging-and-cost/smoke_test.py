"""Smoke test for Lesson 24."""
import io
import json
from contextlib import redirect_stderr
import trace_demo

def main():
    trace_demo.reset()
    buf = io.StringIO()
    with redirect_stderr(buf):
        trace_demo.traced_capture("testcid1", "Bo", "bo@example.com", "Need")
    lines = [json.loads(l) for l in buf.getvalue().strip().splitlines()]
    assert {l["cid"] for l in lines} == {"testcid1"}
    assert [l["event"] for l in lines] == ["call.received", "call.completed"]
    assert "amara" not in buf.getvalue().lower()
    print("smoke ok: correlated JSON logs, no payload data logged")

if __name__ == "__main__":
    main()
