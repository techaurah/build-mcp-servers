"""Smoke test for Lesson 08."""
from annotations import TABLE

def main():
    by_name = {r[0]: r for r in TABLE}
    readonly = {n for n, r in by_name.items() if r[1]}
    idempotent = {n for n, r in by_name.items() if r[3]}
    assert readonly == {"score_lead", "list_leads", "draft_followup"}, readonly
    assert "book_appointment" not in idempotent
    assert by_name["capture_lead"][3] is True
    print("smoke ok: annotation truth table matches the lesson")

if __name__ == "__main__":
    main()
