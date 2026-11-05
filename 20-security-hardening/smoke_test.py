"""Smoke test for Lesson 20: the planted problems are all caught."""
from threat_check import PROFILE, audit

def main():
    flags = audit(PROFILE)
    assert len(flags) == 5, flags
    joined = " ".join(flags)
    for needle in ["poisoning", "read only", "open world", "least privilege", "environment"]:
        assert needle in joined, needle
    print("smoke ok: all five planted problems flagged")

if __name__ == "__main__":
    main()
