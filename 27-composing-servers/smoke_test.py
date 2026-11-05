"""Smoke test for Lesson 27."""
from merge_demo import LEADDESK, NOTES, OTHER_SEARCH, collisions

def main():
    assert collisions(NOTES, OTHER_SEARCH) == ["search"]
    assert collisions(LEADDESK, NOTES) == []
    assert collisions(LEADDESK, OTHER_SEARCH) == []
    print("smoke ok: collision detected where planted, LeadDesk names travel clean")

if __name__ == "__main__":
    main()
