"""Smoke test for Lesson 21."""
from booking_demo import BookingStore

def main():
    store = BookingStore()
    a = store.book("k1", "LD-001", "2026-11-10T10:00")
    b = store.book("k1", "LD-001", "2026-11-10T10:00")
    c = store.book("k1", "LD-001", "2026-11-10T10:00")
    assert a["created"] is True and b["created"] is False and c["created"] is False
    assert len({a["event_id"], b["event_id"], c["event_id"]}) == 1
    assert len(store.events) == 1
    print("smoke ok: one key, one event, across three calls")

if __name__ == "__main__":
    main()
