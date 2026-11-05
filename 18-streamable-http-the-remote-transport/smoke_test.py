"""Smoke test for Lesson 18."""
from http_exchange import EXCHANGE, NOTES

def main():
    text = " ".join(a + b + c for a, b, c in EXCHANGE) + " ".join(NOTES)
    for needle in ["Mcp-Session-Id", "text/event-stream", "deprecated", "Origin"]:
        assert needle in text, needle
    print("smoke ok: session header, streaming answer, deprecation, and Origin all covered")

if __name__ == "__main__":
    main()
