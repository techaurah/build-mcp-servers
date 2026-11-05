"""Lesson 01: server, function, or no AI? A decision drill.

Prints five scenarios with the course's answer and reasoning.
Run: python3 decide.py
"""
SCENARIOS = [
    ("Your agent script needs today's date.",
     "No AI, no server",
     "A standard library call. Wrapping the clock in a protocol adds nothing."),
    ("Three different AI apps your team uses should all query the company CRM.",
     "MCP server",
     "One server, every host reuses it. This is the M times N problem MCP removes."),
    ("One private script classifies its own log lines with a helper function.",
     "Plain function",
     "One caller, forever. A function is simpler and honest about it."),
    ("A spreadsheet pipeline needs dedup and scoring rules enforced for any assistant.",
     "MCP server",
     "The rules must live server side so no caller can skip them. The LeadPipe pattern."),
    ("Marketing wants a weekly summary email drafted from the pipeline.",
     "It depends",
     "The drafting is a prompt; the data access is the server's resources. Both, in layers."),
]

if __name__ == "__main__":
    for i, (job, answer, why) in enumerate(SCENARIOS, 1):
        print(f"{i}. {job}\n   -> {answer}: {why}\n")
