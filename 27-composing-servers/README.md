# Lesson 27: Composing servers: many servers, one client, and routing

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 14 and 26 · **You need:** Just the lesson files. No SDK needed.

Real hosts rarely connect to one server. They connect to a filesystem server, a docs server, your LeadDesk, and a search server at once, and present one merged catalogue to the model. This lesson teaches composition from both chairs: as a client author merging catalogues without collisions or confusion, and as a server author designing for a crowded shelf, where your names, descriptions, and resource URIs share a namespace with strangers.

## The merged catalogue problem

Tool names are only unique per server. Two servers can both offer `search`, and hosts handle it by namespacing internally (server name plus tool name) while models see some prefixed or contextual form depending on the host. Collisions you cannot prevent, you can still design against: choose distinctive tool names (`capture_lead` travels better than `create`), assume your descriptions will be read beside competitors', and write the first sentence of each to identify the domain ('Store a new lead in the LeadDesk pipeline...'), so a model choosing between two capture shaped tools has evidence. Resource URI schemes are yours by design (Lesson 10), which is why a personal scheme beats a generic one.

## Routing and delegation patterns

Beyond hosts, composition appears inside architectures: a gateway server that fronts several backends, a proxy that adds policy (the standalone FastMCP's composition and proxying features exist for this), and agent frameworks that mount servers per task. The design questions repeat at every layer: who owns discovery, whose auth applies, and what happens when one backend is down (partial catalogues beat total failure for read shaped work, and are dangerous for write shaped work without clear signalling). This course's stance: compose at the host first; build gateways only when policy must be enforced between the host and your servers, and then treat the gateway as a server in its own right, with this whole course applying to it.

## Versioning a shelf, not a server

When other people's clients hold your catalogue, your release discipline from Lessons 22 to 25 extends: announce breaking changes, keep old tool names working through a deprecation window where you can, and remember that a host's saved prompts may name your tools and resources explicitly. The cheapest compatibility is a stable catalogue; the second cheapest is a changelog that treats renames as the breaking changes they are.

## Run it

Run `python3 merge_demo.py`, which merges LeadDesk's catalogue with a second small server's, detects the planted collision, and applies the course's namespacing and description fixes. Finish with the smoke test.

## Common failures

- **Generic tool names in a shared world.** `get`, `search`, and `create` collide and confuse. Prefix by domain in the name or the description's first sentence, preferably both in spirit.
- **Failing the whole catalogue for one dead server.** A host or gateway that hides every tool because one backend is down teaches users to remove servers. Degrade visibly instead.
- **Treating a gateway as plumbing.** A proxy that can see and alter calls is a security principal. It gets the Lesson 20 review, its own credentials, and its own logs.

## Recap checklist

- [ ] I can merge two catalogues and resolve collisions with namespacing and description evidence.
- [ ] I know when composition belongs at the host and when a gateway earns its complexity.
- [ ] My catalogue names and descriptions assume a crowded shelf.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
