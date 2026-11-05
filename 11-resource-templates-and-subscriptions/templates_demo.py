"""Lesson 11: URI templates and the subscribe/notify sequence.

Pure simulation in the lesson's notation. Run: python3 templates_demo.py
"""
import re

TEMPLATE = "leaddesk://leads/{lead_id}"
PATTERN = re.compile(r"^leaddesk://leads/(?P<lead_id>LD-\d{3})$")

def expand(lead_id):
    return TEMPLATE.replace("{lead_id}", lead_id)

def parse(uri):
    m = PATTERN.match(uri)
    return m.group("lead_id") if m else None

if __name__ == "__main__":
    for lid in ["LD-001", "LD-002"]:
        uri = expand(lid)
        print(f"expand {lid} -> {uri} -> parse back: {parse(uri)}")
    print("parse leaddesk://leads/evil -> ", parse("leaddesk://leads/evil"))
    print()
    print("client -> server  resources/subscribe {uri: leaddesk://pipeline/summary}")
    print("... a capture_lead call succeeds on a write path ...")
    print("server -> client  notifications/resources/updated {uri: leaddesk://pipeline/summary}")
    print("client -> server  resources/read (only if it still cares)")
