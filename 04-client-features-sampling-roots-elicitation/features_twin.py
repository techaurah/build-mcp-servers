"""Lesson 04: reverse requests and utilities, printed as an exchange.

A narrated simulation (no server process) so the direction of
each message is explicit. Real method names and shapes are used.
Run: python3 features_twin.py
"""
EXCHANGE = [
    ("client -> server", "tools/call book_appointment",
     "arguments include _meta.progressToken so progress is opt in per request"),
    ("server -> client", "elicitation/create",
     "missing timezone: schema asks for one string field, user may decline"),
    ("client -> server", "result: {action: accept, content: {tz: Europe/London}}",
     "the user answered through the host UI; no secrets travel this way"),
    ("server -> client", "notifications/progress {progress: 1, total: 3}",
     "checking the calendar"),
    ("server -> client", "notifications/message {level: info}",
     "log line on the logging channel, never on stdout for stdio servers"),
    ("server -> client", "result for tools/call",
     "the appointment, booked in the elicited timezone"),
    ("server -> client (any time)", "sampling/createMessage",
     "only if the client advertised sampling at initialize; host approves"),
    ("client -> server (any time)", "notifications/roots/list_changed",
     "the allowed boundary set changed; the server must re read roots/list"),
]
if __name__ == "__main__":
    for direction, message, note in EXCHANGE:
        print(f"{direction:28s} {message}\n{'':28s} note: {note}\n")
