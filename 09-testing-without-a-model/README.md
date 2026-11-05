# Lesson 09: Testing without a model: Inspector, scripted clients, and smoke tests

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06 to 08 · **You need:** Just the lesson files for the scripted path. The Inspector path uses `mcp dev` or npx.

If a server only ever gets tested by chatting with a model, its failures arrive as vibes: the model 'seemed confused'. This lesson builds the three layer testing habit the course uses everywhere. The MCP Inspector for human exploration. A scripted client that performs exact exchanges and asserts exact results. And unit tests on the logic layer, which is where most bugs actually live. A server tested this way fails loudly in CI, not quietly in someone's demo.

## The Inspector: the reference client

The Inspector is the MCP project's own developer tool, shipped as the npm package `@modelcontextprotocol/inspector` (current releases need a recent Node) and also launched for Python servers through the SDK's `mcp dev` command. It connects, shows capabilities, lists tools with their schemas, lets you call them with your own arguments, reads resources, renders prompts, and displays the raw JSON-RPC traffic. Its debugging law, worth memorising: if it works in the Inspector and fails in a host, the problem is the host configuration; if it fails in the Inspector, the problem is your server. That one split halves every debugging session.

## Scripted clients: the Inspector's assertions, automated

Everything the Inspector does by hand, a script can assert. This lesson's `client_twin.py` pattern grows into a test client: handshake, list, call with known inputs, assert exact outputs, call with bad inputs, assert the error shape. Deterministic logic (Lesson 06's architecture) makes exact assertions possible: score 100 and band hot for the canonical facts, dedup true on the repeat capture. The smoke tests in this repo are exactly this pattern, small enough to run on every push.

## What to test at which layer

Logic layer: formulas, validation, dedup, state transitions, the works, in plain unit tests with no protocol at all. Protocol layer: handshake order, discovery matching the catalogue, error codes, isError behaviour, resource and prompt round trips. Host layer: one manual pass per host you support (config file, restart, one real call), because config formats differ and no automation fully covers them. Skipping the middle layer is the common mistake: teams unit test the logic, demo in a host, and ship protocol bugs that a thirty line script would have caught.

## Run it

Run `python3 smoke_test.py` here (it is the scripted client pattern, extended), then run the repository wide habit: every lesson's smoke test, the same loop CI runs. If you have the SDK, repeat one call in the Inspector and compare the raw traffic with the twin's.

## Common failures

- **Testing through a model.** A model will route around your bug, misreport your error, and pass a broken server on a good day. Models are users of the server, not tests of it.
- **Golden outputs copied from the server itself.** Assertions must come from the specification of the behaviour (the rubric, the lesson), not from whatever the code printed today, or tests become change detectors that bless regressions.
- **No negative tests.** The unknown tool call, the bad email, the missing argument: error behaviour is half the contract and the half models depend on to recover.

## Recap checklist

- [ ] My server passes a scripted client with positive and negative assertions.
- [ ] I can state the Inspector debugging law and when each layer of testing applies.
- [ ] CI runs my smoke tests on every push.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
