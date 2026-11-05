# Lesson 06: Your first server: one tool over stdio with the Python SDK

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 00, 02, and 05 · **You need:** The course environment from Lesson 00, with the pinned SDK installed. The twin path needs no SDK.

Time to build the real thing. This lesson creates a working MCP server with the official Python SDK: one instance, one tool, stdio transport, tested three ways (the twin, the Inspector via `mcp dev`, and a host config). The tool is LeadDesk's `score_lead`, chosen because it is pure: same facts in, same score out, no state, no side effects. Every production habit in the course starts here in miniature: logic in its own module, the SDK file as a thin wrapper, logging to stderr, and a smoke test that would catch the classic stdout bug.

## The shape of an SDK server

Four moves. Import `FastMCP` from `mcp.server.fastmcp` (the v1 line this course pins). Create the instance with a name: `mcp = FastMCP("leaddesk")`. Decorate a function with `@mcp.tool()`; the SDK builds the tool's name from the function name, its description from the docstring, and its input schema from the type hints. Run it: `mcp.run(transport="stdio")` under a `__main__` guard. That is the whole skeleton. Everything else in the course is elaboration, and the elaboration is where the value is, but notice how small the protocol surface is once the SDK carries the plumbing you hand built in Lesson 02.

## Why the logic lives elsewhere

`server_sdk.py` in this lesson contains no scoring formula. It imports `score_lead` from `lead_logic.py` and wraps it. Three payoffs. The logic is testable offline with no SDK installed, which is how this repo's CI stays green for every learner. The formula can change without touching protocol code. And when you meet the TypeScript lesson, you will see the same logic wearing a different wrapper, which teaches the real lesson: the server is the logic plus a contract; the SDK is replaceable clothing.

## Stdio discipline

On stdio, stdout is the wire (Lesson 02). The SDK handles its own messages; your job is to never add yours. No `print` for debugging: use the `logging` module configured to stderr, or the protocol's logging channel (Lesson 04). A server that prints a friendly startup banner is a server that corrupts its first handshake, and the failure looks like a client bug, which is why this trap eats afternoons. The smoke test here launches the twin and asserts clean JSON on every line of stdout, the same check you should run on any server you write.

## Run it

With the SDK installed, run `python3 server_sdk.py` and watch it wait silently: silence is correct, it is listening on stdio. Stop it, then run `mcp dev server_sdk.py` to open the Inspector against it and call `score_lead_tool` by hand. Without the SDK, run `python3 client_twin.py` for the identical exchange through the twin, and `python3 smoke_test.py` either way.

## Common failures

- **Running the server file and expecting a prompt.** A stdio server waits for JSON on stdin. A silent terminal is success. Test it with a client or the Inspector, not by staring at it.
- **Docstrings as decoration.** In the SDK, the docstring is the tool description the model reads. A missing or lazy docstring is a missing interface, not a style issue. Lesson 07 goes deep on this.
- **Forgetting the __main__ guard.** Hosts import and relaunch server files in surprising ways. The guard keeps import from becoming execution.

## Recap checklist

- [ ] My SDK server starts silently and answers in the Inspector.
- [ ] My tool's description comes from its docstring and its schema from its type hints.
- [ ] Nothing my code prints can reach stdout.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
