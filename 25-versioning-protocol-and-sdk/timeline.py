"""Lesson 25: the revision timeline, as taught in this course.

Compiled from the specification and current guides as read in
November 2026. Revisions after this course's writing will
extend the list, which is the lesson.
"""
REVISIONS = [
    ("2024-11-05", "Original public revision. HTTP plus SSE transport."),
    ("2025-03-26", "Streamable HTTP replaces HTTP plus SSE. OAuth model formalised."),
    ("2025-06-18", "Structured tool output matures. Elicitation develops."),
    ("2025-11-25", "Stable revision widely aligned on. This course's protocol reference."),
    ("2026-07-28", "Stateless core. Sessions and the initialize handshake restructured. Sampling, roots, and logging deprecated."),
]
if __name__ == "__main__":
    for date, note in REVISIONS:
        print(f"{date}  {note}")
