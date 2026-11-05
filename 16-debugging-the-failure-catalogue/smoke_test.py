"""Smoke test for Lesson 16."""
from diagnose import CARDS

def main():
    assert len(CARDS) == 6
    text = " ".join(c[1] for c in CARDS).lower()
    assert "stdout" in text and "terminal" in text
    print("smoke ok: six symptom cards with first moves")

if __name__ == "__main__":
    main()
