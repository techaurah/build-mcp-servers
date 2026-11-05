"""Smoke test for Lesson 25."""
from timeline import REVISIONS

def main():
    dates = [d for d, _ in REVISIONS]
    assert dates == sorted(dates) and len(dates) == 5
    assert "Streamable HTTP" in REVISIONS[1][1]
    assert "deprecated" in REVISIONS[4][1]
    print("smoke ok: timeline ordered, headline changes present")

if __name__ == "__main__":
    main()
