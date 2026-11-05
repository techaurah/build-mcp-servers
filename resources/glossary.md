# Glossary

Every term this course uses, in plain language. If a lesson uses a word that is not defined here or in the lesson itself, that is a lesson problem: please open an issue.

**Annotation**: A hint a server attaches to a tool about its behaviour: read only, destructive, idempotent, open world. Hosts use annotations to decide what needs human confirmation (Lesson 08).

**Capability**: A feature flag exchanged at initialise: the server offers tools, resources, prompts, or logging; the client offers sampling, roots, or elicitation. Methods outside the negotiated set are not legal in that session (Lesson 02).

**Client**: The component inside a host that manages one connection to one server and carries its JSON-RPC messages (Lesson 01).

**Demo mode**: A server mode that runs the full surface against seeded fake data with no credentials, so anyone can try it safely. The default for teaching servers in this course (Lesson 13).

**Dry run**: A write mode that reports what a call would do and changes nothing. One of the three write modes with direct and approval (Lesson 30).

**Elicitation**: A client feature letting a server request missing information from the user mid task, through the host's interface, with a small schema. Never for secrets (Lesson 04).

**FastMCP (SDK)**: The high level server class bundled in the official Python SDK v1 line, imported from mcp.server.fastmcp. Decorators turn functions into tools, resources, and prompts (Lesson 06).

**FastMCP (standalone)**: A separate framework package by Prefect, imported from fastmcp, adding composition, proxying, OpenAPI generation, and auth. Same class name as the SDK's, different code (Lesson 05).

**Host**: The AI application the user touches (Claude Desktop, VS Code, your own agent). It contains clients, shows discovered tools to the model, and approves sensitive actions (Lesson 01).

**Idempotency key**: A stable identifier for an intended effect, recorded by the server so a repeat call returns the recorded outcome instead of repeating the effect (Lesson 21).

**Inspector**: The MCP project's reference developer tool for testing servers: lists and calls primitives and shows raw JSON-RPC traffic (Lesson 09).

**JSON-RPC 2.0**: The message format MCP uses: requests with an id, a method, and params; responses with a result or an error; notifications with no id (Lesson 02).

**MCP Server (SDK v2)**: The renamed server class in the official Python SDK v2 line, imported from mcp.server. Lesson 25 covers the rename and its era.

**Prompt (MCP)**: A server primitive: a named, argument taking message template a user invokes on purpose. User controlled (Lesson 12).

**Protocol revision**: A dated version of the MCP specification (for example 2025-11-25). Clients and servers negotiate the revision in the handshake era model (Lesson 25).

**Resource**: A server primitive: readable data at a URI that the application decides to include as context. Application controlled; reading changes nothing (Lesson 10).

**Resource template**: A URI pattern with variables (leaddesk://leads/{lead_id}) addressing many resources through one listing entry (Lesson 11).

**Roots**: A client feature telling a server which directories or URIs it may operate on. The server's fence for filesystem reach (Lesson 04).

**Sampling**: A client feature letting a server request a model completion from the host, with host and user approval. Deprecated in the 2026-07-28 revision (Lesson 04).

**Scope**: An OAuth permission tier (read, draft, write) checked per tool on remote servers, so a valid token never means unlimited action (Lesson 19).

**server.json**: The registry manifest describing a server: namespaced name, description, version, and how to obtain and run it (Lesson 22).

**Stdio transport**: The local transport: the host launches the server as a subprocess and exchanges newline delimited JSON-RPC over its standard input and output. Stdout carries protocol only (Lesson 17).

**Streamable HTTP**: The current remote transport: one HTTP endpoint accepting POSTed JSON-RPC, answering with JSON or an SSE stream within the response. Replaced HTTP plus SSE in the 2025-03-26 revision (Lesson 18).

**Structured content**: The machine readable part of a tool result, an object matching the tool's declared output shape, beside the text content for display (Lesson 08).

**Tool**: A server primitive: a function with a name, a description, and an input schema, which the model chooses to call. Model controlled (Lesson 03).

**Tool poisoning**: An attack where a tool description carries hidden instructions aimed at the model. Defence is vetting, pinning, and description review on updates (Lesson 20).

**Twin**: This course's term for a standard library model of a protocol behaviour: real message shapes, no SDK, runnable and testable offline.
