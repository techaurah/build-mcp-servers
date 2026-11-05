# Lesson 26: TypeScript servers in one lesson, for Python learners

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06 and 25 · **You need:** Just the lesson files for the reading path. Running the TypeScript example needs Node 18 or newer and npm, and is optional.

You will read more TypeScript MCP code in the wild than any other dialect, because the TypeScript SDK was first and the ecosystem grew around it. This lesson gives a Python learner the mapping: the same server, LeadDesk's scorer, expressed with the official TypeScript SDK's high level `McpServer`, Zod schemas standing where your type hints stood, and the stdio transport class standing where `mcp.run` stood. The protocol does not change. The furniture does.

## The mapping, concept by concept

Instance: `new McpServer({ name, version })` for `FastMCP("leaddesk")`. Tool registration: `server.registerTool(name, { description, inputSchema }, handler)` (older examples use `server.tool` with a similar shape) for `@mcp.tool()`. Schemas: Zod objects (`z.object({ budget_usd: z.number() })`) generate the same JSON Schema your type hints generated; validators and schemas are one artefact in this dialect, which many teams prefer. Handler returns: the same content array (text items holding JSON strings) and isError flag. Transport: `StdioServerTransport` connected explicitly, or the Streamable HTTP transport class with a web framework, where Python's `run(transport=...)` folded it into one call.

## What genuinely differs

Three honest differences. The TypeScript SDK exposes the low level `Server` class more prominently, so more code in the wild hand manages handlers you would meet in the Python low level API too. The ecosystem's examples lean on npm packaging and npx distribution (Lesson 22's equivalent is a different registry with the same manifest idea). And async is the native idiom everywhere, where Python FastMCP lets sync functions ride along. None of these change a single wire message, which is the point of a protocol: Lesson 02's exchange is byte for byte the contract both dialects honour.

## Reading TypeScript servers as a Python builder

Your transfer skill is the catalogue: find the registrations, read names, descriptions, and schemas, and you know the server's surface without reading its implementation language fluently. Apply Lesson 20's vetting in this order when you meet a TypeScript server: catalogue first, description diff on updates, env demands, then code. The example in this lesson is deliberately tiny so the mapping, not the language, is the content.

## Run it

Read `server.ts` beside Lesson 06's `server_sdk.py` and complete the mapping table in `mapping.md` from memory before checking it. If Node is available, you may build and run the example (`npm install`, `npm run build`, then the Inspector), but the lesson passes on the reading path alone. The smoke test here checks the mapping file, not Node.

## Common failures

- **Assuming the dialects are dialects of the framework.** They are dialects of the protocol. Code does not translate line by line; catalogues and contracts do.
- **Copying a TypeScript schema into Python by eye.** Zod constraints (min, max, defaults, strict objects) carry meaning your type hints must restate deliberately, or the two servers diverge while looking identical.
- **Skipping the version check.** The TypeScript SDK also moved across major lines; an example's `server.tool` versus `registerTool` tells you its era, the same discipline as Lesson 25.

## Recap checklist

- [ ] I can read a TypeScript server's catalogue and restate it in Python terms.
- [ ] I can name the Zod to type hints, McpServer to FastMCP, and transport mappings.
- [ ] I vet a foreign dialect server by catalogue, descriptions, and env, in that order.

## Resources

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)
