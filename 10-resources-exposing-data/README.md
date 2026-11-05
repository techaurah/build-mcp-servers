# Lesson 10: Resources: exposing data the application controls

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 03 and 09 · **You need:** Just the lesson files. No SDK needed.

Resources are how a server offers data as context: a pipeline summary a host can pin, a lead record a user can attach, a document a model should read before answering. This lesson builds LeadDesk's resource surface properly: a small set of stable URIs, correct MIME types, reads computed from the same logic layer as the tools, and the discipline that reading never changes anything.

## URI design is API design

Give resources hierarchical, guessable URIs under your own scheme: `leaddesk://pipeline/summary`, `leaddesk://leads/LD-001`. A reviewer should be able to predict the URI for lead LD-002 without a manual. Keep the set small and meaningful; a resource per database row with no template (next lesson) is catalogue noise. Decide your scheme once, because hosts and saved prompts remember URIs the way they remember tool names: renaming one is a breaking change.

## What a read returns

`resources/read` returns a contents list: each item has the URI, a MIME type, and either `text` or base64 `blob`. Match the type to the content: JSON data as `application/json` text, prose as `text/plain`, binary as blob. Compute reads from the logic layer at call time (the twin's summary does), so a resource can never drift from the tools' view of the world. Cache only when you can also invalidate, which for most teaching and small production servers means: do not cache, compute.

## Listing honestly

`resources/list` is a catalogue promise. List what reads can actually serve, with names and descriptions a person can choose from, since hosts show this list to users. If a resource exists only sometimes (a summary only after the first lead), either list it with an empty state read, which is usually kinder, or use templates and dynamic listing deliberately (next lesson), never accidental absence that looks like a bug.

## Run it

Run `python3 client_twin.py` and find the summary resource in the code. Then run `python3 resources_demo.py`, which performs `resources/list` and `resources/read` explicitly and prints the contents envelope so you can see the exact shape a host receives.

## Common failures

- **Write shaped resources.** A read that refreshes a cache is fine; a read that books, sends, or deletes is a tool in disguise and loses every protection tools get (confirmation, annotations, error conventions).
- **URIs that leak internals.** File paths, SQL table names, and internal ids you would not print in a README do not belong in URIs. The scheme is public surface.
- **Stale snapshots.** Serving a JSON file written last week as 'the pipeline summary' is how assistants confidently quote dead numbers. Compute, or timestamp loudly.

## Recap checklist

- [ ] My resources have stable, guessable URIs under one scheme.
- [ ] Every listed resource reads successfully and returns a correctly typed content item.
- [ ] Reading any resource twice changes nothing.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
