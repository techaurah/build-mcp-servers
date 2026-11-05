"""Lesson 16: symptom cards. Pick the first move before reading on."""
CARDS = [
    ("Server does not appear in the host at all",
     "Run the exact config command in a terminal",
     "Most causes live in config, paths, or interpreter. A silent wait means the server starts fine and the host is the problem."),
    ("Inspector shows a non JSON line before the first response",
     "Find what writes to stdout in the server",
     "A banner or print corrupts the stream. Log to stderr or the logging channel."),
    ("Tool is listed, Inspector calls it, model never does",
     "Fix the description, not the code",
     "Discovery and execution are proven. Selection is a Lesson 07 writing problem."),
    ("tools/call returns isError with a validation message",
     "Read the message and fix the arguments",
     "The logic layer rejected the input and said why. That channel is working as designed."),
    ("Server works for you, fails for a teammate",
     "Diff environments: paths, cwd, env vars, data files",
     "Same code, different context. The context is the bug until proven otherwise."),
    ("A call hangs with no feedback for 30 seconds",
     "Check progress support and the timeout policy",
     "Long work needs notifications/progress and a Lesson 21 timeout story."),
]
if __name__ == "__main__":
    for symptom, move, why in CARDS:
        print(f"SYMPTOM: {symptom}\n  FIRST MOVE: {move}\n  WHY: {why}\n")
