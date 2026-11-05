# Lesson 13: State, files, and databases inside a server

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 10 to 12 · **You need:** Just the lesson files. No SDK needed. Uses the standard library sqlite3 module.

Real servers remember things. This lesson covers where server state should live and how it should behave: in memory for demos, files and SQLite for single machine servers, and external databases or APIs for remote ones. The rules that matter are not storage trivia: keep state behind the logic layer, make writes transactional where they matter, seed demo data deterministically, and design the demo mode that lets anyone try your server with zero credentials, the adoption pattern LeadPipe's offline demo proves out.

## The state ladder

Rung one, in memory: perfect for teaching and demos, gone on restart, and honest about it. Rung two, a local file or SQLite database: survives restarts, one writer at a time, ideal for stdio servers that serve one user. Rung three, an external store behind an API (a hosted database, a SaaS like a sheet or a CRM): required when the server is remote or shared, and the point where credentials, pooling, and migrations enter. Climb only as high as your deployment (Lessons 17 and 18) demands; a stdio server reaching for a distributed database is wearing someone else's problems.

## SQLite, the stdio server's friend

Python ships `sqlite3` in the standard library: a real, transactional database in one file, no server process, no credentials. This lesson's `lead_store.py` persists LeadDesk leads in SQLite with the same function signatures as the in memory logic, so the swap is visible: same contract, different backing. Use parameterised queries always (string built SQL in a tool server is an injection waiting for a creative model), commit deliberately, and keep the schema in code with a version note, because your future self is also a maintainer.

## Demo mode and seed data

A server nobody can try is a server nobody adopts. Demo mode means: a flag or subcommand that runs the full server against seeded, fake data with no credentials, exactly the pattern in LeadPipe's walkthrough. Seed data must be deterministic (fixed names, fixed order) so documentation, screenshots, and smoke tests agree run after run. State the mode loudly in the server name or startup log, because a demo mistaken for production is a data incident wearing a friendly face.

## Run it

Run `python3 lead_store.py` to watch the SQLite store capture, dedup, and summarise against a temp file, then `python3 smoke_test.py`. Compare its output with Lesson 06's in memory run and note the one difference that matters (persistence across the two store instances in the demo).

## Common failures

- **State in the SDK layer.** If your tool functions hold the only copy of the data structures, testing needs the protocol. State belongs behind the logic layer, where Lesson 09's tests live.
- **String built SQL.** Parameterise. A model that can place `Robert'); DROP TABLE leads;` into a name field is not hypothetical, it is a Tuesday.
- **Silent demo data in production paths.** If seed data can leak into a real store through a shared default path, it will. Demo mode gets its own database file, named like one.

## Recap checklist

- [ ] My state lives behind the logic layer with the same contract at each rung.
- [ ] All SQL is parameterised and writes commit deliberately.
- [ ] Demo mode is seeded, deterministic, and visibly labelled.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
