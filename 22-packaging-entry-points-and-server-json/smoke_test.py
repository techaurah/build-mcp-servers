"""Smoke test for Lesson 22."""
import os
from check_packaging import check_manifest

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    problems = check_manifest(os.path.join(here, "server.json"))
    assert problems == [], problems
    print("smoke ok: server.json satisfies the registry field rules")

if __name__ == "__main__":
    main()
