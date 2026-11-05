"""Smoke test for Lesson 13: SQLite store dedups and persists."""
import os
import tempfile
from lead_store import LeadStore

def main():
    path = os.path.join(tempfile.mkdtemp(), "t.db")
    store = LeadStore(path)
    a = store.capture("Amara", "amara@example.com", "Booking assistant")
    b = store.capture("Dup", "amara@EXAMPLE.com", "Again")
    assert a["created"] is True and b["deduped"] is True, (a, b)
    store.close()
    again = LeadStore(path)
    assert again.summary()["total"] == 1
    again.close()
    print("smoke ok: sqlite dedup and persistence across reopen")

if __name__ == "__main__":
    main()
