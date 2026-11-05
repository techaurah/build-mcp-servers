"""Smoke test for Lesson 17."""
from framing_demo import GOOD_1, GOOD_2, POISON, read_stream

def main():
    parsed, errors = read_stream([GOOD_1, GOOD_2])
    assert len(parsed) == 2 and errors == []
    parsed, errors = read_stream([GOOD_1, POISON, GOOD_2])
    assert len(parsed) == 2 and errors == [POISON]
    print("smoke ok: framing parses clean lines and isolates the poisoned one")

if __name__ == "__main__":
    main()
