"""Lesson 03: tool, resource, or prompt? A classification drill."""
ITEMS = [
    ("Search the ticket database for open items about billing", "tool",
     "The model decides when a search is needed and with what query."),
    ("The current pipeline summary, refreshed whenever it changes", "resource",
     "The host decides to include it as context. Reading it changes nothing."),
    ("The team's standard incident write up, filled in per incident", "prompt",
     "A person invokes a known workflow on purpose, with arguments."),
    ("Book a 30 minute appointment and return the event id", "tool",
     "An action with side effects, chosen by the model, guarded by the server."),
    ("One lead record, addressed as leaddesk://leads/LD-001", "resource",
     "Readable data at a URI. The template form covers every lead."),
    ("Draft a follow up email in our house style for a stalled lead", "prompt",
     "A reusable template the user invokes. Sending it would be a separate tool."),
    ("Compute a lead score from budget, timeline, and authority", "tool",
     "A calculation the model requests with facts; the server owns the formula."),
    ("Subscribe to changes in the pipeline summary", "resource",
     "Subscriptions are a resource feature: notifications/resources/updated."),
]
if __name__ == "__main__":
    for i, (what, kind, why) in enumerate(ITEMS, 1):
        print(f"{i}. {what}\n   -> {kind}: {why}\n")
