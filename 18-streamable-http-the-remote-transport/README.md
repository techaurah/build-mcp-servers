# Lesson 18: Streamable HTTP: the remote transport

**Time:** about 75 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 04 and 17 · **You need:** Just the lesson files for the design and the twin shaped HTTP exchange. The SDK path needs the pinned SDK plus a local port.

When a server must serve many users, live on another machine, or be reachable by web based hosts, stdio is the wrong tool. Streamable HTTP is the current remote transport: the server runs as an independent HTTP service with a single MCP endpoint that accepts POSTed JSON-RPC and can answer with plain JSON or open a Server-Sent Events stream within the response when it needs to push messages. This lesson teaches its shape, its session and header rules, and the decisions that separate it from the deprecated transport it replaced.

## One endpoint, two answer shapes

The client POSTs each JSON-RPC message to the one endpoint (commonly `/mcp`). A simple request gets a JSON response. A request that will produce server initiated messages (progress, sampling, elicitation) gets an SSE stream as its response body, carrying the related messages until the final result, then closing. Clients can also open a GET to the endpoint for a server to client stream in the handshake era model. The deprecated predecessor, called HTTP plus SSE, used two endpoints with a long lived GET stream for everything; tutorials that configure an `/sse` endpoint are teaching that older shape, replaced in the 2025-03-26 revision. The 2026-07-28 revision simplifies further toward stateless requests (Lesson 25); this lesson teaches the deployed Streamable HTTP model.

## Sessions, headers, and safety rails

In the session based model, the server may assign a session id at initialise, returned in the `Mcp-Session-Id` header, which the client then sends on later requests; servers can run statelessly instead, which scales better behind load balancers. Clients send `MCP-Protocol-Version` and must send an `Accept` header covering both JSON and SSE. Servers validate the `Origin` header to resist DNS rebinding, bind to localhost by default for local use, and treat authentication as a separate layer (next lesson) rather than a transport detail. Every one of these rules exists because a remote endpoint is reachable by more than its intended clients.

## When remote is wrong

Remote costs you hosting, auth, and an attack surface. A single user tool on their own machine should stay stdio: zero network, the host owns the process, nothing to secure. Choose remote when the server is shared, centralised, or must be reachable by hosts that cannot spawn processes (web chat interfaces are the common case). Many real servers ship both: the same logic (Lesson 06's separation) behind a transport flag, which in the SDK is one argument to `run`.

## Run it

Run `python3 http_exchange.py` to read a complete Streamable HTTP exchange as annotated messages, headers included. If you have the SDK, run the Lesson 06 server with `transport="streamable-http"` and repeat the Inspector pass against the URL, noting what changes and what does not.

## Common failures

- **Following an SSE tutorial in 2026.** Two endpoint `/sse` setups are the deprecated transport. If the guide's URL ends in /sse and it never mentions Streamable HTTP, it is teaching history.
- **Exposing a development server to the internet.** A no auth endpoint on a public address is an open tool shed. Localhost binding and Lesson 19's auth exist because this mistake is common and quiet.
- **Stateful assumptions behind a load balancer.** If requests can land on any instance, session state must be shared, resumable, or designed out. Decide deliberately, not by outage.

## Recap checklist

- [ ] I can describe the Streamable HTTP exchange, including when an answer is a stream.
- [ ] I can name the deprecated transport and recognise its tutorials.
- [ ] I can state the session, version, and Origin rules and why each exists.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP specification: transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
