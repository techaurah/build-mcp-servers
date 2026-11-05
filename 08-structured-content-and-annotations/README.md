# Lesson 08: Structured content, return types, and tool annotations

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 07 · **You need:** Just the lesson files. No SDK needed.

A tool result is richer than a string. MCP results carry a list of content items (text, image, audio, embedded resources), an optional structured content object matching a declared output schema, and the `isError` flag. Servers can also annotate tools with hints about their behaviour: whether they are read only, destructive, idempotent, or open world. This lesson teaches you to return data models can build on, and to annotate honestly, because hosts use those hints to decide what needs a human's confirmation.

## Content items and structured content

The text content item is the workhorse: most tools return one, holding either prose or a JSON string, as the twin does. When a tool returns a Python dict through the SDK, the SDK can also place it in the result's `structuredContent` when the function's return annotation gives it a shape to validate against, and serialise a copy as text for clients that only read text. Prefer returning real structures from your logic (LeadDesk always returns dicts) and let the layers format them. Images and embedded resources exist for tools that genuinely produce them; do not wrap ordinary data in exotic content types to look advanced.

## Annotations are promises hosts rely on

Four hints, defined in the specification. `readOnlyHint`: the tool does not modify its environment. `destructiveHint`: it may make destructive updates (only meaningful when not read only). `idempotentHint`: repeating a call with the same arguments has no additional effect. `openWorldHint`: the tool interacts with an open world of external entities, like the web, rather than a closed system. Hosts use these to group tools, to auto approve the safe ones, and to warn on the dangerous ones. A false `readOnlyHint` is therefore not a white lie; it is a safety bug. LeadDesk's truth table: list and score are read only; capture is not read only, is idempotent (dedup), and is closed world; booking is neither read only nor idempotent without its idempotency key, which Lesson 21 adds.

## Titles and display names

Servers may also give tools a human facing title alongside the programmatic name. Keep names stable for models and code; use titles for people. Renaming a tool's programmatic name is a breaking change for every saved prompt and client habit, which is why Lesson 24 treats the catalogue as a versioned API surface.

## Run it

Run `python3 annotations.py` to print LeadDesk's annotation truth table with the reasoning per tool, then the smoke test, which asserts the read only set and the idempotent set match the lesson text exactly.

## Common failures

- **Annotating for convenience.** Marking a write tool read only so a host stops asking for confirmation is the fastest way to teach users to distrust your server, and the hardest to take back.
- **Returning prose where a structure was promised.** If the output schema says an object with `score` and `band`, a paragraph containing those numbers is a contract breach, however readable.
- **Forgetting isError on handled failures.** A caught exception returned as ordinary success content trains the model to present failures as results.

## Recap checklist

- [ ] I can name the four annotation hints and state LeadDesk's value for each tool.
- [ ] I know when a result carries structured content and who validates it.
- [ ] I treat a tool rename as a breaking change.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
