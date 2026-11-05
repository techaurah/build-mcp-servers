# Competitor research: learning to build MCP servers

Written 2026-11-06, before any lesson was drafted, per the TechAurah
GitHub programme rule: competitor research first, always. Every fact
below was observed in web search results or pages fetched on that
date. Star counts are point-in-time observations from the named
source, not live guarantees, and where sources disagree or a claim
could not be verified, that is recorded rather than smoothed over.

## The official path: documentation and quickstarts

Source: modelcontextprotocol.io, the "Build an MCP server" tutorial
page (the 2024-11-05 docs tree, crawled 2026-11-05), read 2026-11-06.

- The official quickstart builds one weather server with two tools
  (`get_alerts`, `get_forecast`) and connects it to Claude for
  Desktop. It is offered in Python, TypeScript, Java, Kotlin, C#,
  Ruby, Rust, and Go from the same page.
- The Python path requires Python 3.10 or higher and, on the page
  read, the Python MCP SDK 1.2.0 or higher. Its teaching API is
  FastMCP: the page states that the FastMCP class uses type hints
  and docstrings to generate tool definitions.
- The page's durable warnings are the ones every builder meets:
  never write to stdout on stdio servers, and configure hosts
  through `claude_desktop_config.json` and its `mcpServers` key
  with an absolute launch command.
- A second, newer docs tree (the 2026-07-28 revision path, seen in
  search results) pins a 2.x SDK line and a renamed server class.
  The two trees coexisting is itself a finding: version literacy
  is now part of learning MCP, and most tutorials do not teach it.

Strengths to respect: canonical, current per revision, free.
Weaknesses we can beat: a quickstart is one server deep. It does
not teach tool design as a discipline, testing without a model,
remote auth, security threat models, packaging, or publishing,
and it cannot, at its length.

## The SDKs themselves, as teaching material

Sources: the MCP Python SDK README (via search result mirrors and
the raw README), current guides comparing the SDK lines (mcp.so's
Python SDK v2 guide, October 2026; dreaming.press, FastMCP versus
the official SDK), and the FastMCP project's documentation site,
all read 2026-11-06.

- Official Python SDK, v1 line: install `mcp` (recommended with
  uv as `mcp[cli]`), server class `FastMCP` at
  `mcp.server.fastmcp`, decorators for tools, resources, and
  prompts, a low level `Server` API beneath, the `mcp` CLI with
  `mcp dev` (Inspector) and `mcp install`. The README quickstart
  builds a calculator tool and a greeting resource.
- Official Python SDK, v2 line: the built in class is renamed
  `MCPServer` (`from mcp.server import MCPServer`); the v2 guide
  read for this scan ran against `mcp` 2.3.0 and the 2026-07-28
  protocol revision, and warns that `mcp.server.fastmcp` no
  longer resolves. One community course found in this scan pins
  `mcp[cli]>=1.28,<2` for exactly this reason, which this course
  also does.
- Standalone FastMCP (Prefect): a separate package, `from fastmcp
  import FastMCP`, adding composition, proxying, OpenAPI and
  FastAPI generation, auth providers, and its own client. One
  source in this scan (Augment Code's FastMCP page) observed it
  at 23.4k GitHub stars. The name collision with the SDK's bundled
  FastMCP 1.0 is a documented, recurring source of learner bugs.
- TypeScript SDK: `@modelcontextprotocol/sdk`, high level
  `McpServer` with `registerTool` (older examples use `tool`),
  Zod generated schemas, stdio and Streamable HTTP transports.
- The MCP Inspector is the reference developer tool: npm package
  `@modelcontextprotocol/inspector`, web UI plus CLI and TUI
  clients in current versions, requiring a recent Node (22.19.0
  or newer per current guides).

## The specification, as it stands

Sources: the specification summaries and revision reporting in
Stacklok's MCP primer, PromptXP's MCP guide, Class Central's
best courses guide (checked against the July 2026 revision), and
Scalar's testing guide, all read 2026-11-06.

- Dated revisions: 2024-11-05, 2025-03-26, 2025-06-18,
  2025-11-25, 2026-07-28. Streamable HTTP replaced the HTTP plus
  SSE transport in 2025-03-26. The 2026-07-28 revision is the
  largest yet: a stateless core, protocol level sessions and the
  `initialize` handshake restructured, and sampling, roots, and
  logging deprecated (still working; removal no earlier than a
  revision a year later, per the reporting read).
- Server primitives are tools (model controlled), resources
  (application controlled), and prompts (user controlled).
  Client features are sampling, roots, and elicitation, with
  elicitation remaining active in the newest revision.
- Governance: MCP was released by Anthropic in November 2024 and
  donated to the Agentic AI Foundation under the Linux
  Foundation in December 2025, per multiple sources in this scan.
- SDK tiers, per the SDKs page as summarised in current guides:
  TypeScript, Python, C#, Go, Rust, and Ruby in the top tier;
  Java next; Swift, PHP, and Kotlin after.

## Curricula and courses

- **Microsoft, MCP for Beginners** (github.com/microsoft/mcp-for-beginners):
  the largest free curriculum in this scan. Eleven modules in the
  listings read (one directory page said 11 modules and 50 plus
  lessons; Class Central described modules 0 to 11 plus a 13 lab
  capstone), with code in C#, Java, JavaScript, Rust, Python, and
  TypeScript, aligned in its own text to specification
  2025-11-25, MIT licensed. A directory page observed it at 15k
  plus stars. Its capstone builds one PostgreSQL server across
  13 labs. Strength: cross language depth nobody else matches.
  Gap for us: breadth across six languages trades against depth
  in one; it is not organised around a single running server the
  learner publishes, nor around offline testability of every
  lesson.
- **Anthropic's own courses** (Skilljar, moving to Claude Academy):
  Introduction to Model Context Protocol (build servers and
  clients in Python, a document management project, Inspector
  testing) and MCP Advanced Topics (sampling, progress
  notifications, roots, transports including StreamableHTTP,
  production deployment). Video led, platform hosted, with
  certificates on the Academy path. Strength: the source teaching
  itself. Gap: platform shaped, project is theirs, and the
  artefact a learner keeps is a certificate rather than a
  published server.
- **Hugging Face MCP Course** (with Anthropic): free, three units
  (fundamentals; an end to end use case; a deployed use case),
  certificates for fundamentals and for completion. Strength:
  community and deployment on the HF ecosystem. Gap: unit sized,
  not a server builder's full arc from protocol to publishing.
- **DeepLearning.AI short course**, "MCP: Build Rich-Context AI
  Apps with Anthropic" (observed at 1 hour 58 minutes in a
  catalogue guide): concise, application focused. A good
  afternoon, not a curriculum.
- **Let's Learn MCP with C#** (Microsoft tutorial series): setup,
  consuming servers, and building a production style server
  (Lunch Roulette) in .NET. The closest single language analogue
  to this course's shape, in a different stack.
- **Pamela Fox's PyCon 2026 tutorial** (pamelafox.github.io):
  a conference tutorial building a first Python server, which
  also documents the official SDK versus standalone FastMCP
  distinction cleanly. Single sitting depth.
- **Video and article tutorials** (the long tail): single server
  builds (weather, notes, orders, course catalogues) in blog and
  YouTube form, typically tools only, stdio only, no exercises
  with solutions, no testing or security pass, and frequently
  teaching the deprecated SSE transport or an unpinned SDK line.
  Several 2026 guides still present SSE as a current transport,
  which this scan treats as the clearest evidence that version
  and transport literacy is the unmet need.
- **TechAura's own Course 1, Lesson 14**: a teaching model of
  MCP in about 120 lines (hand rolled JSON-RPC over stdio with
  lead pipeline tools) plus the production pointer to LeadPipe.
  This course grows directly out of that lesson's proven shape.

## Gaps we can beat

1. **No forkable, Python first, server focused complete course.**
   Microsoft's curriculum is six languages wide; Anthropic's and
   Hugging Face's are platform courses with certificates. A
   repository course where the fork is the workbook, one running
   server grows for 32 lessons, and the completion artifact is
   the learner's own published server, does not exist yet for
   MCP.
2. **Version chaos, untaught.** Two docs trees, two SDK major
   lines, two FastMCPs, a renamed server class, and a deprecated
   transport still taught by current tutorials. Learners burn
   days on import and connection errors that are really era
   mismatches. A course that pins deliberately, labels eras at
   the file level, and teaches the timeline as content wins
   trust the quickstarts cannot.
3. **Testing and security are the skipped chapters.** The long
   tail stops at "it answered in my chat". Scripted clients,
   gate suites, tool poisoning, indirect injection, annotation
   honesty, and least privilege scopes are where servers earn
   trust, and they are systematically under-taught.
4. **Publishing is treated as an afterthought.** server.json,
   the official Registry, directories and scanners, and a README
   that states a safety model decide whether a stranger ever
   runs a server. Almost no tutorial walks that path; TechAura
   has walked it with a real server (LeadPipe: Glama listing,
   M8ven verified publisher) and can teach it from practice.
5. **Business shaped capstone.** Courses end with weather and
   calculators. A capstone that gives a small business a safe
   lead pipeline (dedup, scoring, approval gated booking)
   matches what learners actually get hired to build, and it is
   the shape of the production server this programme maintains.

## The differentiation this course takes

See DESIGN.md for the full design. In short: the Course 1 and 2
house standard applied to MCP servers. Thirty-two lessons in
nine modules, one arc, one running teaching server (LeadDesk),
one capstone assembled from it. Every lesson is a complete unit
with runnable code, an offline twin or logic layer wherever the
behaviour is testable without the SDK, one exercise, and a
worked solution. The version discipline is explicit: the SDK v1
line pinned and labelled, the v2 and 2026-07-28 story taught as
content. No certificate; the completion artifact is the learner's
public capstone server, indexed in the course showcase.
