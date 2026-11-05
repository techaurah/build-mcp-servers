# Course design: Build MCP Servers

The design this repository was built to. Research behind it:
[RESEARCH.md](RESEARCH.md). House standard inherited from Course 1,
Agentic AI for Beginners, and Course 2, AI Automation with n8n:
numbered lesson folders, every lesson a complete unit (written
lesson, runnable artifact, exercise, worked solution), offline
path in every lesson, no em dashes, no invented statistics, no
certificates.

## Title and promise

**Build MCP Servers** is a free, complete course that teaches you
to design, build, test, secure, and publish Model Context
Protocol servers that real hosts can use, from speaking the
protocol by hand to a published capstone server.

## Audience

- Developers who can write Python and want the server side of
  MCP, not just connecting other people's servers in a host.
- Agent builders from Course 1 who met MCP in its Lesson 14 and
  want the full treatment, including publishing.
- Teams exposing an internal system (a spreadsheet, a database,
  a SaaS) to AI assistants safely, with rules enforced server
  side.

Not for: complete beginners who have never written Python or
read JSON (the prerequisites below are real), or anyone shopping
for a certificate. There is none; the capstone showcase is the
artifact.

## Prerequisites

- Working Python and comfort reading JSON. Python 3.11 or newer.
- The course pins the official Python MCP SDK v1 line
  (`mcp[cli]>=1.28,<2`) for SDK code; Lesson 00 states why and
  Lesson 25 teaches the v2 line and the 2026-07-28 revision.
- No paid API keys or model accounts. Every lesson has an
  offline path on the standard library alone. Node is optional,
  for the standalone Inspector and the TypeScript lesson only.

## The arc

One teaching server, LeadDesk, a lead pipeline for a small
service business without a CRM, grows through the whole course:
first as a protocol twin, then as an SDK server, then with
resources, prompts, state, and a client, then through
transports, auth, security, and packaging, until the capstone
finishes it to a fixed spec with a safety model (demo mode,
dry run, approval writes, idempotent booking) and four
acceptance gates. The production reference is TechAura's real
LeadPipe MCP, cited where its design decisions teach something,
never as an advertisement: the course stands alone without it.

## Lesson map: 32 lessons, 9 modules

### Module 0: Start here

| # | Lesson | Builds |
|---|--------|--------|
| 00 | Course setup: environment, versions, and how to use this repo | A verified checker and a defended version pin |
| 01 | What MCP is, and where a server fits | The host, client, server map as data |

### Module 1: The protocol, by hand

| # | Lesson | Builds |
|---|--------|--------|
| 02 | The protocol on the wire: JSON-RPC, lifecycle, and capabilities | A twin server and client speaking real MCP shapes |
| 03 | Tools, resources, prompts: the three server primitives | A classification drill and the full twin surface |
| 04 | Client features: sampling, roots, elicitation, logging, and progress | An annotated reverse request exchange |
| 05 | Choosing an SDK, and reading the specification without fear | The SDK landscape map and the two FastMCPs rule |

### Module 2: First servers with the Python SDK

| # | Lesson | Builds |
|---|--------|--------|
| 06 | Your first server: one tool over stdio with the Python SDK | An SDK server over a tested logic layer |
| 07 | Tool design: schemas, descriptions, and errors models can use | A catalogue and a design checker |
| 08 | Structured content, return types, and tool annotations | The annotation truth table for LeadDesk |
| 09 | Testing without a model: Inspector, scripted clients, and smoke tests | The three layer testing habit, automated |

### Module 3: Richer servers

| # | Lesson | Builds |
|---|--------|--------|
| 10 | Resources: exposing data the application controls | The summary resource, listed and read |
| 11 | Resource templates, subscriptions, and change notifications | A lead template and the subscribe, notify sequence |
| 12 | Prompts: reusable workflows users invoke on purpose | qualify-lead and the prompt design rules |
| 13 | State, files, and databases inside a server | A SQLite store behind the same contract, demo mode |

### Module 4: Clients and hosts

| # | Lesson | Builds |
|---|--------|--------|
| 14 | Building an MCP client in Python | A reusable twin client and the SDK client shape |
| 15 | Connecting to real hosts: config files, Claude Desktop, VS Code, and friends | Two validated host configs and a config checker |
| 16 | Debugging: stdout traps, logs, and the failure catalogue | A symptom drill over ten known failures |

### Module 5: Transports and going remote

| # | Lesson | Builds |
|---|--------|--------|
| 17 | Stdio in depth: process lifecycle, framing, and environment | A framing demo showing what one bad line costs |
| 18 | Streamable HTTP: the remote transport | An annotated remote exchange, headers included |
| 19 | Authentication for remote servers: OAuth 2.1, tokens, and least privilege | The auth flow and LeadDesk's scope tier map |

### Module 6: Production disciplines

| # | Lesson | Builds |
|---|--------|--------|
| 20 | Security hardening: tool poisoning, prompt injection, and sandboxing | A threat audit with planted problems, all caught |
| 21 | Errors, retries, timeouts, and idempotent writes | A written error policy and key based booking |
| 22 | Packaging: project layout, entry points, and server.json | A checked registry manifest and project file |
| 23 | Publishing and discovery: Registry, directories, and a README that gets you found | A README audit and the honest publication sequence |
| 24 | Observability: logging, tracing a call, and knowing your costs | Correlated JSON logs for one instrumented call |
| 25 | Versioning: protocol revisions, SDK lines, and keeping a course honest | The five revision timeline and a VERSIONS note pattern |

### Module 7: The wider shelf

| # | Lesson | Builds |
|---|--------|--------|
| 26 | TypeScript servers in one lesson, for Python learners | The same tool in the TypeScript dialect, with a mapping table |
| 27 | Composing servers: many servers, one client, and routing | A merged catalogue with its collision resolved |

### Module 8: Capstone: LeadDesk MCP

| # | Lesson | Builds |
|---|--------|--------|
| 28 | Capstone spec and scaffolding: LeadDesk MCP | The fixed spec, safety model, and four gates |
| 29 | Build LeadDesk: tools, resources, and prompts, end to end | The full server: logic, twin, and SDK layers |
| 30 | Harden and test LeadDesk: approval writes, dry runs, and the gate suite | The mode matrix, self audit, and failure rehearsal, automated |
| 31 | Ship it: publish, document, and showcase your server | The release routine and the showcase submission |

## Visuals

Generated by assets/visuals/generate_visuals.py in the Academy
style family (white canvas, navy primary, light blue secondary,
cyan arrows, amber gates):

| Diagram | Teaches | Used in |
|---|---|---|
| course-map.svg | Nine modules, one arc, one capstone | README |
| protocol-exchange.svg | Initialize, discover, call: the wire in order | Lesson 02 |
| three-primitives.svg | Tools, resources, prompts, and who decides each | Lesson 03 |
| transports.svg | Stdio beside Streamable HTTP, with the deprecated shape marked | Lessons 17, 18 |
| security-layers.svg | Annotations, scopes, approvals, and server side rules as layers | Lesson 20 |
| capstone-flow.svg | LeadDesk: capture, score, draft, book, with gates | Lessons 28 to 31 |

## Rules the build followed

- Every version or API claim names its source or its observation
  date (RESEARCH.md), and SDK code pins the v1 line with the
  reason stated in the file header.
- Every lesson folder complete on delivery: no stubs anywhere.
- All JSON examples parse and pass tools/validate_servers.py;
  all smoke tests pass offline; relative links pass
  tools/check_links.py; em dash count is zero repo wide.
