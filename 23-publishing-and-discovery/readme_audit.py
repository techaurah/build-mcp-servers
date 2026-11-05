"""Lesson 23: audit a server README for the required pattern."""
REQUIRED = ["What", "Demo", "Tools", "Safety", "Client config", "Limits"]
DRAFT = """# LeadDesk MCP
## What it is
A teaching MCP server that gives an AI assistant a safe lead pipeline.
## Demo
Zero credentials: run the walkthrough and watch capture, scoring, and booking.
## Tools
capture_lead, score_lead, list_leads, draft_followup, book_appointment.
## Safety model
Demo mode by default, dry run for writes, approval before real bookings.
## Client config
Paste the mcpServers snippet from Lesson 15 with absolute paths.
## Limits
Not a CRM. Sends nothing. Demo data is fake and labelled.
"""

def audit(text):
    return [s for s in REQUIRED if s.lower() not in text.lower()]

if __name__ == "__main__":
    missing = audit(DRAFT)
    print("missing sections:", missing if missing else "none, the draft passes")
