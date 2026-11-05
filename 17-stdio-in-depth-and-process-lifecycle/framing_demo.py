"""Lesson 17: newline framing, and what one bad line does to it."""
import json

GOOD_1 = json.dumps({"jsonrpc": "2.0", "id": 1, "result": {}})
GOOD_2 = json.dumps({"jsonrpc": "2.0", "id": 2, "result": {"tools": []}})
POISON = "leaddesk starting up..."  # a banner: not JSON, not a message

def read_stream(lines):
    parsed, errors = [], []
    for line in lines:
        try:
            parsed.append(json.loads(line))
        except json.JSONDecodeError:
            errors.append(line)
    return parsed, errors

if __name__ == "__main__":
    stream = [GOOD_1, POISON, GOOD_2]
    parsed, errors = read_stream(stream)
    print(f"parsed {len(parsed)} messages; failed on {len(errors)} line(s): {errors}")
    print("One banner line cost the client a parse failure mid stream.")
    print("On a real connection that failure lands inside a request and looks like a server bug.")
