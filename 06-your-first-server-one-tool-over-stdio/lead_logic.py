"""Shared lead pipeline logic for this lesson (standard library only).

This module is the part of the server that does the real work. It has
no MCP imports, so it can be unit tested offline with no SDK installed.
The MCP layer in the companion server file is a thin wrapper over
these functions. That separation is the pattern this course teaches:
logic first, protocol second.
"""
import re

LEADS = []
_counter = [0]

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def reset():
    LEADS.clear()
    _counter[0] = 0


def score_lead(budget_usd, timeline_days, is_decision_maker):
    """Score a lead from 0 to 100. The server computes the score.

    A model never supplies a score. It supplies facts, and this
    function turns facts into a number, so two runs with the same
    facts always agree.
    """
    score = 0
    score += 40 if budget_usd >= 1000 else 20 if budget_usd >= 500 else 5
    score += 35 if timeline_days <= 14 else 20 if timeline_days <= 30 else 5
    score += 25 if is_decision_maker else 5
    band = "hot" if score >= 80 else "warm" if score >= 55 else "cold"
    return {"score": score, "band": band}


def capture_lead(name, email, need):
    """Store a lead, deduplicating on normalised email."""
    if not EMAIL_RE.match(email or ""):
        raise ValueError("email does not look like an email address")
    key = email.strip().lower()
    for lead in LEADS:
        if lead["email"].lower() == key:
            return {"captured": lead, "created": False, "deduped": True,
                    "total_leads": len(LEADS)}
    _counter[0] += 1
    lead = {"id": f"LD-{_counter[0]:03d}", "name": name, "email": email,
            "need": need, "stage": "NEW", "score": None, "band": None}
    LEADS.append(lead)
    return {"captured": lead, "created": True, "deduped": False,
            "total_leads": len(LEADS)}


def list_leads(stage=None):
    rows = [l for l in LEADS if stage is None or l["stage"] == stage]
    return {"leads": rows, "count": len(rows)}


def pipeline_summary():
    by_stage = {}
    for lead in LEADS:
        by_stage[lead["stage"]] = by_stage.get(lead["stage"], 0) + 1
    return {"total": len(LEADS), "by_stage": by_stage}
