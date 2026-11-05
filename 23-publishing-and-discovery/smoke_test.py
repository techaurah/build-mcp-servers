"""Smoke test for Lesson 23."""
from readme_audit import DRAFT, audit

def main():
    assert audit(DRAFT) == []
    assert audit("# Empty server\n") != []
    print("smoke ok: README audit passes the pattern and catches an empty page")

if __name__ == "__main__":
    main()
