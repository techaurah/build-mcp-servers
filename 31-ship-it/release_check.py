"""Lesson 31: local release rehearsal checks for this repo."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def main():
    checks = [
        ("capstone spec exists (Lesson 28)",
         os.path.exists(os.path.join(ROOT, "28-capstone-spec-and-scaffolding", "capstone", "SPEC.md"))),
        ("gate suite exists (Lesson 30)",
         os.path.exists(os.path.join(ROOT, "30-harden-and-test-leaddesk", "gate_suite.py"))),
        ("release notes draft covers the sections",
         all(s in DRAFT for s in ["What it does", "What changed", "Known limits"])),
    ]
    for label, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {label}")
    return 0 if all(ok for _, ok in checks) else 1

DRAFT = """# LeadDesk MCP 1.0.0
## What it does
A safe lead pipeline for an AI assistant: capture, score, list, draft, book.
## What changed
First release. Full Lesson 28 surface, gate suite green, demo mode default.
## Known limits
Teaching build: in memory and SQLite stores, no hosted auth, sends nothing.
"""

if __name__ == "__main__":
    raise SystemExit(main())
