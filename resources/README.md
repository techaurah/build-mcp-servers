# Resources

Curated resources for Build MCP Servers, grouped by theme.
Lessons link to the items they use; this page is the full shelf.
Official documentation first, because it ages best. If a link here
breaks, that is a lesson problem: please open an issue so it gets
fixed for everyone.

New to a word? The [glossary](glossary.md) defines every term this
course uses, in plain language.

## Official MCP

- [Model Context Protocol documentation](https://modelcontextprotocol.io): the home of the docs, the quickstarts, and the SDK pages.
- [MCP specification, 2025-11-25 revision](https://modelcontextprotocol.io/specification/2025-11-25): this course's protocol reference. Lesson 25 explains the dated revision system and the 2026-07-28 revision.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk): the official Python SDK. This course pins its v1 line; the repository also carries the v2 line and its migration notes.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk): the other major dialect, covered in Lesson 26.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector): the reference developer tool for testing and debugging servers (Lesson 09).
- [MCP Registry](https://registry.modelcontextprotocol.io): the official catalogue of published servers, and the home of the server.json schema (Lessons 22 and 23).
- [Official example servers](https://github.com/modelcontextprotocol/servers): the project's own reference servers, worth reading after Lesson 14.

## Learning further

- [Microsoft, MCP for Beginners](https://github.com/microsoft/mcp-for-beginners): the large cross language curriculum surveyed in RESEARCH.md; the natural next step for C#, Java, Rust, or TypeScript depth.
- [Anthropic's MCP courses](https://anthropic.skilljar.com): Introduction to Model Context Protocol and MCP Advanced Topics, from the protocol's creators.
- [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/unit0/introduction): a free three unit course built with Anthropic, strong on deployed use cases.
- [FastMCP standalone documentation](https://gofastmcp.com): the Prefect framework's own docs; read them as the other FastMCP (Lesson 05), never as the SDK's.
- [Agentic AI for Beginners](https://github.com/techaurah/agentic-ai-for-beginners): Course 1 of this programme; agents in depth, including the Lesson 14 teaching model this course grows from.
- [AI Automation with n8n](https://github.com/techaurah/ai-automation-with-n8n): Course 2 of this programme; its Lesson 26 covers MCP in both directions inside a workflow platform.

## Production reference

- [LeadPipe MCP](https://github.com/techaurah/leadpipe-mcp): TechAura's production lead pipeline server, the design reference for LeadDesk's safety model: demo mode, dry run and approval writes, server side scoring, idempotent booking.
- [Python documentation](https://docs.python.org/3/): the standard library every twin, logic layer, and checker in this course is built on.

## Going further in this repo

- [resources/glossary.md](glossary.md): every course term, defined plainly.
- The capstone [showcase](../showcase/): finished LeadDesk servers from learners, each one runnable in demo mode.
