"""Lesson 19: the remote auth flow and LeadDesk scope tiers."""
FLOW = [
    "Client asks the server for a protected resource and receives a 401 with metadata pointers.",
    "Client reads the protected resource metadata and learns the authorisation server.",
    "Client runs OAuth 2.1 with PKCE against that server and receives an access token.",
    "Client calls the MCP endpoint with Authorization: Bearer <token>.",
    "Server validates signature, expiry, and audience, then maps scopes to allowed actions.",
    "Each tool checks its tier; resources filter rows by the caller's identity.",
]
TIERS = {"read": {"list_leads", "score_lead"},
         "draft": {"draft_followup"},
         "write": {"capture_lead", "book_appointment"}}

def allowed(scopes, tool):
    return any(tool in TIERS.get(s, set()) for s in scopes)

if __name__ == "__main__":
    for i, step in enumerate(FLOW, 1):
        print(f"{i}. {step}")
    print()
    print("read only token may book?", allowed({"read"}, "book_appointment"))
    print("read plus write may book?", allowed({"read", "write"}, "book_appointment"))
