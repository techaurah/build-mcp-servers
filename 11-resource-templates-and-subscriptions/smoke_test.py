"""Smoke test for Lesson 11."""
from templates_demo import expand, parse

def main():
    assert parse(expand("LD-042")) == "LD-042"
    assert parse("leaddesk://leads/evil") is None
    assert parse("leaddesk://pipeline/summary") is None
    print("smoke ok: template expands, parses, and rejects bad ids")

if __name__ == "__main__":
    main()
