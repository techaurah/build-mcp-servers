# Lesson 23: Publishing and discovery: Registry, directories, and a README that gets you found

**Time:** about 45 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 22 · **You need:** Just the lesson files. No accounts needed for the lesson itself.

Publishing an MCP server is not one act but three: releasing the package, listing it where clients and directories look, and writing the README that decides whether a stranger trusts it enough to run it. This lesson walks the real landscape as TechAura practised it with LeadPipe: the official MCP Registry, community directories and scanners such as Glama and M8ven, and the repository itself as the front door. No growth tricks: discovery follows clarity and proof, the same attention plus value standard as the rest of the programme.

## The official Registry and server.json

The official MCP Registry is the ecosystem's canonical catalogue: servers publish the `server.json` manifest from Lesson 22 under a namespace they prove they control (GitHub or DNS verification), and clients, hosts, and other directories build on its data. Publication is a deliberate release act with the registry's own tooling and identity checks. Treat the manifest as release metadata: versioned with the package, reviewed like code.

## Directories and scanners

Around the Registry sits a layer of directories and evaluators. Glama lists servers and inspects them, showing tools and quality signals; LeadPipe carries a Glama listing from its real publication. M8ven scores servers and issues listing badges; LeadPipe shows a verified publisher listing at grade B, 89 out of 100, as recorded in TechAura's registry work in November 2026. PulseMCP and similar directories round out the shelf. Each reads overlapping manifest and repository facts, which is the practical argument for Lesson 22's accuracy: one truthful source, many surfaces. Listings are never bought or gamed in this course; a listing you cannot defend line by line is a liability, not an asset.

## The README is the listing that matters most

Most install decisions happen on the repository page. The README pattern that earns them, proven on LeadPipe: one sentence saying what the server does and for whom; a zero credential demo that runs in minutes; the full tool list with plain descriptions; the safety model stated before the features (demo mode, dry run, approval as defaults); client config snippets that can be pasted; and honest limits (what it is not, what it never does). Badges come after proof, and the proof is a stranger running the demo successfully without asking you anything.

## Run it

Run `python3 readme_audit.py`, which checks a README draft (the one in this lesson) for the pattern's required sections, then read the SOLUTION for the ordering argument. Your capstone README in Lesson 31 is built to this audit.

## Common failures

- **Listing before the demo works.** Directories and strangers arrive once, early. A broken first run costs more than a late listing ever will. Sequence: demo green, README honest, then publish.
- **Feature lists without a safety model.** For a server asking to touch real business data, the absence of a safety section is itself the loudest statement on the page.
- **Keyword stuffed descriptions.** Registry and directory search rewards accurate nouns (lead pipeline, Google Sheets, booking) and punishes hype adjectives. Write for the person comparing three servers, not for an algorithm you imagine.

## Recap checklist

- [ ] My publication sequence is demo, README, manifest, registry, directories, in that order.
- [ ] My README passes the audit: purpose, demo, tools, safety, config, limits.
- [ ] Every directory claim I make is verifiable from the repository itself.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP Registry](https://registry.modelcontextprotocol.io)
- [Glama MCP servers](https://glama.ai/mcp/servers)
- [LeadPipe MCP on GitHub](https://github.com/techaurah/leadpipe-mcp)
