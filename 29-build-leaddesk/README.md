# Lesson 29: Build LeadDesk: tools, resources, and prompts, end to end

**Time:** about 3 hours · **Difficulty:** Advanced · **Prerequisites:** Lesson 28 · **You need:** The course environment. The twin build runs with no SDK; the SDK build uses the pinned line.

Build day. This lesson assembles LeadDesk to the Lesson 28 spec, in the order the course has practised all along: logic first with its tests, then the twin protocol layer for full offline verification, then the SDK server as a thin wrapper, then resources and prompts onto the same logic. The code in this lesson is the most complete in the course; work through it rather than skimming, because Lesson 30 will attack it and Lesson 31 will publish it.

## The logic layer, completed

`lead_logic.py` here is the course's fullest version: capture with dedup and validation, server side scoring, paged summary listing, per lead detail, stage movement with the forward only rule, follow up drafting from templates keyed by stage and band, and booking with idempotency keys and the slot rule from Lesson 21. Every behaviour the spec promises is a function here, and the smoke test exercises each one without a whisper of protocol. If a behaviour is hard to test at this layer, the design is wrong, not the test.

## The protocol layers, twin and SDK

The twin exposes the full surface over stdio with the methods from Lessons 02, 10, 11, and 12, so the scripted acceptance suite can run anywhere. The SDK file wraps the same logic with decorators, docstrings carrying Lesson 07's descriptions, and the Lesson 08 annotations expressed as the SDK allows. Two wrappers, one truth: any divergence between them is a bug in a wrapper, never a question about the logic. Run both through the same smoke expectations and watch them agree.

## Prompts and resources finish the surface

The two prompts from Lesson 12 ship with their declared arguments; the summary and stages resources compute from the logic layer; the lead template parses ids strictly and refuses unknown ones with the Lesson 11 error shape. With this, the merged surface matches SPEC.md line for line, which is the moment to stop building and start hardening: Lesson 30's gates assume a frozen surface, and every late addition reopens them.

## Run it

Run, in order: `python3 smoke_test.py` (logic plus twin acceptance), `python3 client_twin.py` (the human readable exchange), and, with the SDK installed, `mcp dev server_sdk.py` for the Inspector pass over the wrapped server. All three must tell the same story about the same facts.

## Common failures

- **Building the SDK version first.** It demos beautifully and tests terribly. Logic first is slower to show a friend and faster to finish, which is the trade this course always takes.
- **Two sources of truth.** A scoring tweak made in the SDK wrapper but not the logic module forks the product. Wrappers contain no behaviour; if you are typing a rule into one, stop and move it down a layer.
- **Calling it done at first green.** The smoke suite passing means the build exists. Lesson 30 exists because existence and trustworthiness are different properties.

## Recap checklist

- [ ] The full acceptance smoke suite passes against the twin from a clean run.
- [ ] The SDK server answers in the Inspector with identical results on the canonical calls.
- [ ] The shipped surface matches SPEC.md exactly, with nothing added or missing.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [LeadPipe MCP, the production reference](https://github.com/techaurah/leadpipe-mcp)
