"""Smoke test for Lesson 07: the shipped catalogue passes its own audit."""
from catalogue import CATALOGUE
from check_catalogue import check

def main():
    for tool in CATALOGUE:
        assert check(tool) == [], (tool["name"], check(tool))
    print(f"smoke ok: {len(CATALOGUE)} tools pass the design audit")

if __name__ == "__main__":
    main()
