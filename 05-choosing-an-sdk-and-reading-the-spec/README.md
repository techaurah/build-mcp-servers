# Lesson 05: Choosing an SDK, and reading the specification without fear

**Time:** about 45 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 02 to 04 · **You need:** Just the lesson files. Web access helps for the spec exercise.

You will build with the official Python SDK in this course, but you will read other people's servers in TypeScript, Go, and more, and you will meet a name collision that confuses the whole ecosystem. This lesson maps the SDK landscape as observed in November 2026, separates the two FastMCPs, and teaches a way to read the specification that turns it from a wall into a reference: find the method, read its schema, check the capability flag, note the revision.

## The official SDKs and their tiers

The MCP project lists official SDKs by tier. TypeScript, Python, C#, Go, Rust, and Ruby sit in the top tier; Java in the second; Swift, PHP, and Kotlin in the third, per the SDKs page summarised in current guides. Tier reflects completeness and maintenance, not permission: any of them speaks the same protocol. Choose by the language your system already runs, because the server is an adapter over that system. This course is Python first, with one TypeScript lesson (Lesson 26) so you can read the other major dialect.

## The two FastMCPs, disambiguated forever

FastMCP began as a standalone Python framework by Jeremiah Lowin at Prefect. Its 1.0 was merged into the official Python SDK in 2024, where it lives, effectively frozen, at `mcp.server.fastmcp`. The standalone project continued independently (2.x, then 3.x and beyond) at `from fastmcp import FastMCP`, adding composition, proxying, OpenAPI generation, auth providers, and its own client. Same class name, different packages, occasionally different behaviour. In SDK v2, the official built in class was renamed `MCPServer`. Rule: decide which one a project uses from its imports and its requirements file, never from the class name, and never install both into one project.

## Reading the spec in four moves

One: name the method (`tools/call`, `resources/read`). Two: open that method's page in the specification for the revision your SDK implements and read the request and result schemas literally. Three: check the capability negotiation: is this method gated on a flag your handshake set? Four: check the revision notes if behaviour surprises you, because dated revisions (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28) changed real things: Streamable HTTP replaced HTTP plus SSE in 2025-03-26, and the 2026-07-28 revision restructured sessions and deprecated sampling and roots. Ten minutes with the right page beats a day of guessing from blog posts written against other revisions.

## Run it

Run `python3 sdk_map.py`, which prints the landscape table this lesson teaches, then `python3 smoke_test.py`. For the spec move, open the specification page for `tools/call` in the 2025-11-25 revision and find the `isError` field in the result schema with your own eyes.

## Common failures

- **Trusting a tutorial's imports without its date.** A 2025 tutorial's `mcp.server.fastmcp` and a 2026 guide's `MCPServer` can both be correct, for different SDK lines. Match the tutorial to your installed version or pin deliberately, as Lesson 00 does.
- **Installing both FastMCPs.** The name collision becomes a runtime collision. One project, one FastMCP.
- **Reading the latest spec against an older SDK.** SDKs adopt revisions on their own schedules. The spec page to trust is the one your SDK claims to implement.

## Recap checklist

- [ ] I can tell the two FastMCPs apart from an import line and a requirements file.
- [ ] I can find any method's schema in the spec in under five minutes.
- [ ] I know which dated revision my pinned SDK line implements.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [FastMCP standalone documentation](https://gofastmcp.com)
