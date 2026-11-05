"""Lesson 08: LeadDesk annotation truth table, with reasoning."""
TABLE = [
    ("score_lead", True, False, True, False,
     "Pure calculation. Same facts, same score, nothing stored."),
    ("list_leads", True, False, True, False,
     "Reads only. Repeating it changes nothing."),
    ("capture_lead", False, False, True, False,
     "Writes, but dedup on email makes repeats safe. Closed world: our pipeline only."),
    ("draft_followup", True, False, True, False,
     "Returns a draft. Sending is a different tool with its own gates."),
    ("book_appointment", False, True, False, False,
     "Creates an external event. Not idempotent until Lesson 21 adds keys."),
]
if __name__ == "__main__":
    for name, ro, dest, idem, ow, why in TABLE:
        print(f"{name:18s} readOnly={ro} destructive={dest} idempotent={idem} openWorld={ow}")
        print(f"{'':18s} {why}")
