# Lesson 16: Debugging: stdout traps, logs, and the failure catalogue

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 09 and 15 · **You need:** Just the lesson files. No SDK needed.

Debugging MCP has an unfair reputation, because the failures look identical from inside a chat window: nothing appears, or something vague failed. From the wire, they are distinct and mostly known. This lesson is the catalogue: the ten failures this course has taught you to cause and cure, organised by the phase where they bite, with the diagnostic move for each. Keep it; you will use it on every server you ever run, including other people's.

## Startup and handshake failures

Server never appears: config not read (host not restarted), relative path, wrong interpreter, or the file has a syntax error the host swallows. First move: run the exact command from the config in a terminal; a stdio server should start and wait silently. Handshake hangs or garbage errors: stdout pollution (a banner, a print, a library logging to stdout) corrupts the first frames. First move: the Inspector, whose raw traffic view shows the offending non JSON line immediately. Version mismatch: client and server settle on no common protocol revision. First move: compare the versions in the initialize exchange, then check which spec revision your SDK implements (Lesson 05).

## Discovery and call failures

Tool missing: it was never registered (decorator forgotten, import failed silently, or the host cached an old list; send or await list changed, restart the session). Tool present but model never calls it: a description problem (Lesson 07), not a protocol problem; the Inspector calling it successfully proves the split. Call fails with isError: the logic rejected the input; the error text is the lesson, read it. Call fails with a protocol error: argument types against the schema, or an unknown name; compare the raw call in the Inspector with the schema from tools/list, character by character.

## Runtime and lifecycle failures

Server dies mid session: an unhandled exception in a low level handler, or the process was killed by the host for flooding stdout. Long call looks hung: no progress notifications (Lesson 04), or genuinely slow work with no timeout policy (Lesson 21). Works on my machine, fails on theirs: environment again (cwd, env vars, data file paths) or state assumptions from a warm demo database. The meta rule under the whole catalogue: reproduce in the Inspector first, because it splits server faults from host faults in one step, and read the raw messages before reading anyone's theory, including this lesson's.

## Run it

Run `python3 diagnose.py`, which presents six symptom cards and asks you to pick the first diagnostic move for each before revealing the catalogue answer. Then deliberately break the twin in a scratch copy (add a startup print) and watch the client fail, so your hands know the stdout trap, not just your notes.

## Common failures

- **Debugging inside the chat window.** The model will improvise explanations for failures it cannot see. The Inspector and the raw traffic are evidence; the chat is hearsay.
- **Changing three things at once.** Config, code, and host restarts in one gesture leave you knowing it works and nothing about why. One variable per attempt, written down.
- **Trusting a silent host log.** Desktop hosts bury server stderr in log files most users never find. Running the config command in a terminal surfaces the same stderr instantly.

## Recap checklist

- [ ] I can place any symptom in its phase and name the first diagnostic move.
- [ ] I have seen the stdout trap break a client with my own eyes.
- [ ] My first move for a host failure is the Inspector split, every time.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
