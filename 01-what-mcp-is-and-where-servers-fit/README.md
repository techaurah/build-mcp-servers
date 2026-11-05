# Lesson 01: What MCP is, and where a server fits

**Time:** about 45 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 00 · **You need:** Just the lesson files. No SDK needed.

Before MCP, every AI application integrated every tool by hand: M applications times N tools meant M times N pieces of glue, each with its own schema format and auth story. The Model Context Protocol, released by Anthropic in November 2024 and now stewarded by the Agentic AI Foundation under the Linux Foundation, standardises that connection. A tool author builds one MCP server. Any MCP host can connect to it, discover what it offers at runtime, and call it. This lesson gives you the architecture vocabulary the rest of the course uses, and places the server, the thing you will spend the course building, in its exact spot.

## The three roles: host, client, server

A **host** is the AI application the user touches: Claude Desktop, Claude Code, VS Code, Cursor, ChatGPT, or your own agent program. Inside the host, one or more **clients** each manage a connection to one server. A **server** is a program that offers capabilities: tools, resources, and prompts (Lesson 03). The model itself never speaks MCP. The host shows the model the discovered tools, the model asks for a call, the client carries it to the server, the server runs its own code, and the result travels back. Keeping these roles separate in your head is what makes debugging possible later: a discovery problem, a schema problem, and an implementation problem live in three different places.

## Why a protocol, not a library

A library would tie servers to one language and one vendor's client. A protocol ties them to a wire format: JSON-RPC 2.0 messages over a transport (Lesson 02). That is why a Python server from this course can serve a TypeScript host, and why the ecosystem could grow servers and hosts independently. It is also why this course teaches the wire shape once, by hand, before handing the plumbing to an SDK: when a connection misbehaves, the wire is where the truth is.

## Where servers fit in a real system

A server is an adapter with a contract. Behind it sits something real: a database, a file tree, a SaaS API, a spreadsheet, a calendar. The server's job is to expose a small, safe, well described surface over that system and to enforce the rules the raw system cannot: deduplication, scoring computed server side, writes that need approval. TechAura's production example, LeadPipe MCP, puts a guardrailed lead pipeline over a Google Sheet and Calendar precisely because the sheet alone offers raw row access with no rules. Your capstone, LeadDesk, is a teaching sized server with the same shape.

## Run it

Run `python3 decide.py` and work through its five scenarios. Each one asks whether a job wants an MCP server, a plain function call inside one program, or no AI at all, and explains the reasoning. Then read `architecture.json`, the machine readable map of the three roles used by later lessons.

## Common failures

- **Calling the host the client.** Hosts contain clients. When a config file says `mcpServers`, it is telling a host which servers to launch; each gets its own client connection. The distinction matters when one server works and another does not inside the same host.
- **Expecting the server to contain a model.** A plain server has no model and needs no API key. Server initiated model calls exist (sampling, Lesson 04) and are the exception, requested through the client, with user approval.
- **Building a server for a single internal function call.** If one program is the only caller forever, a function is simpler. MCP earns its keep when more than one host, team, or model should reuse the capability.

## Recap checklist

- [ ] I can name the host, client, and server in any MCP setup and say who decides what.
- [ ] I can explain why the model never speaks MCP directly.
- [ ] I can say when a job does not need a server at all.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [LeadPipe MCP, a production server by TechAura](https://github.com/techaurah/leadpipe-mcp)
