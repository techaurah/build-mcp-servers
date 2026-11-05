"""Lesson 24: one instrumented call, as JSON log lines."""
import json
import sys
import time
import uuid

sys.path.insert(0, ".")
from lead_logic import capture_lead, reset

def log(cid, level, event, **fields):
    line = {"ts": round(time.time(), 3), "level": level,
            "event": event, "cid": cid, **fields}
    print(json.dumps(line), file=sys.stderr)

def traced_capture(cid, name, email, need):
    t0 = time.time()
    log(cid, "info", "call.received", tool="capture_lead",
        arg_keys=["name", "email", "need"])
    result = capture_lead(name, email, need)
    log(cid, "info", "call.completed", tool="capture_lead",
        created=result["created"], deduped=result["deduped"],
        ms=round((time.time() - t0) * 1000, 2))
    return result

if __name__ == "__main__":
    reset()
    cid = uuid.uuid4().hex[:8]
    out = traced_capture(cid, "Amara", "amara@example.com", "Booking assistant")
    print("result (stdout, the protocol channel):", json.dumps(out))
    print("(log lines went to stderr: run with 2>log.txt to separate them)", file=sys.stderr)
