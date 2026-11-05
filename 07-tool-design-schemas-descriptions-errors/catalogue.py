"""Lesson 07: the LeadDesk tool catalogue as data.

In a real SDK server this catalogue is generated from your
decorated functions (tools/list). Keeping it as data here lets
the checker audit the design with no SDK installed.
"""
CATALOGUE = [
    {"name": "capture_lead",
     "description": "Store a new lead in the pipeline and return its id. Deduplicates on normalised email, so repeating a call with the same email is safe and returns the existing lead. Sends nothing to anyone.",
     "inputSchema": {"type": "object", "properties": {
         "name": {"type": "string"}, "email": {"type": "string"},
         "need": {"type": "string"}},
         "required": ["name", "email", "need"]}},
    {"name": "score_lead",
     "description": "Score a lead 0 to 100 from budget, timeline, and decision authority. The score is computed by the server from these facts; callers cannot supply a score directly.",
     "inputSchema": {"type": "object", "properties": {
         "budget_usd": {"type": "integer"}, "timeline_days": {"type": "integer"},
         "is_decision_maker": {"type": "boolean"}},
         "required": ["budget_usd", "timeline_days", "is_decision_maker"]}},
    {"name": "list_leads",
     "description": "List leads in the pipeline, newest last. Optionally filter by stage: NEW, QUALIFIED, BOOKED, or LOST.",
     "inputSchema": {"type": "object", "properties": {
         "stage": {"type": "string", "enum": ["NEW", "QUALIFIED", "BOOKED", "LOST"]}},
         "required": []}},
]
if __name__ == "__main__":
    for t in CATALOGUE:
        print(f"{t['name']}: {t['description']}")
