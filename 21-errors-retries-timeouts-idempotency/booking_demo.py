"""Lesson 21: idempotency keys make retries safe.

The booking store records key -> event. Repeats return the
recorded event with created=False. Run: python3 booking_demo.py
"""
class BookingStore:
    def __init__(self):
        self.by_key = {}
        self.events = []
        self._n = 0

    def book(self, key, lead_id, slot):
        if key in self.by_key:
            return {**self.by_key[key], "created": False}
        self._n += 1
        event = {"event_id": f"EVT-{self._n:03d}", "lead_id": lead_id,
                 "slot": slot, "created": True}
        self.by_key[key] = event
        self.events.append(event)
        return event

if __name__ == "__main__":
    store = BookingStore()
    first = store.book("req-abc", "LD-001", "2026-11-10T10:00")
    print("first call: ", first)
    print("retry (timeout, same key):", store.book("req-abc", "LD-001", "2026-11-10T10:00"))
    print("retry again:              ", store.book("req-abc", "LD-001", "2026-11-10T10:00"))
    print("different key, same slot: ", store.book("req-def", "LD-001", "2026-11-10T10:00"))
    print(f"events created: {len(store.events)} (the double booking question is a policy question: see the lesson)")
