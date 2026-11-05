"""Smoke test for Lesson 19."""
from auth_flow import allowed

def main():
    assert allowed({"read"}, "list_leads") is True
    assert allowed({"read"}, "book_appointment") is False
    assert allowed({"draft"}, "capture_lead") is False
    assert allowed({"read", "write"}, "capture_lead") is True
    print("smoke ok: scope tiers allow and refuse as designed")

if __name__ == "__main__":
    main()
