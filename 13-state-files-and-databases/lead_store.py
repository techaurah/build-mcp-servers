"""Lesson 13: LeadDesk logic backed by SQLite (stdlib sqlite3).

Same contract as lead_logic.py, different backing store.
Run directly to see persistence across two store instances:
    python3 lead_store.py
"""
import os
import sqlite3
import tempfile

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    need TEXT NOT NULL,
    stage TEXT NOT NULL DEFAULT 'NEW'
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_email ON leads (lower(email));
"""

class LeadStore:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.executescript(SCHEMA)

    def capture(self, name, email, need):
        cur = self.db.execute(
            "SELECT id FROM leads WHERE lower(email) = lower(?)", (email,))
        row = cur.fetchone()
        if row:
            return {"id": row[0], "created": False, "deduped": True}
        count = self.db.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
        lead_id = f"LD-{count + 1:03d}"
        self.db.execute(
            "INSERT INTO leads (id, name, email, need) VALUES (?, ?, ?, ?)",
            (lead_id, name, email, need))
        self.db.commit()
        return {"id": lead_id, "created": True, "deduped": False}

    def summary(self):
        rows = self.db.execute(
            "SELECT stage, COUNT(*) FROM leads GROUP BY stage").fetchall()
        return {"total": sum(c for _, c in rows), "by_stage": dict(rows)}

    def close(self):
        self.db.close()

if __name__ == "__main__":
    path = os.path.join(tempfile.mkdtemp(), "leaddesk-demo.db")
    first = LeadStore(path)
    print(first.capture("Amara", "amara@example.com", "Booking assistant"))
    print(first.capture("Amara Again", "AMARA@example.com", "Duplicate"))
    first.close()
    second = LeadStore(path)
    print("after reopen:", second.summary())
    second.close()
