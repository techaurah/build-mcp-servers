# Lesson 02: The protocol on the wire: JSON-RPC, lifecycle, and capabilities

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lessons 00 and 01 · **You need:** Just the lesson files. No SDK needed.

This lesson removes the magic. You will speak MCP by hand, through a twin server written in pure standard library Python, and read every message. MCP messages are JSON-RPC 2.0: a request has an `id`, a `method`, and `params`; a response carries the same `id` and either a `result` or an `error`; a notification has no `id` and expects no reply. A session in the widely deployed revisions begins with `initialize`, where client and server exchange protocol versions and capabilities, followed by the `notifications/initialized` notification. Everything after that is method calls you can list on one page.

## The lifecycle, in order

One: the client sends `initialize` with its protocol version, its capabilities (what it can do for the server: sampling, roots, elicitation), and its client info. Two: the server replies with the version it will use, its own capabilities (tools, resources, prompts, logging), and its server info. Three: the client sends `notifications/initialized`. Only then do normal calls begin. Servers may reject calls that arrive before the handshake, which is why hand rolled clients that skip it break against real servers. A note on versions: the 2026-07-28 specification revision restructures this into stateless, self describing requests (see Lesson 25). The handshake model taught here is what the SDK lines in wide use implement, and the message shapes carry over.

## Capabilities are a contract, not decoration

If a server does not advertise `resources`, a client must not send `resources/list`, and a well behaved server errors if it does. If a client does not advertise `sampling`, the server must never ask it for a model completion. Reading the two capability objects in the handshake tells you, before any failure, which methods are even legal in this session. The twin prints its handshake so you can practise reading one.

## Errors have shapes too

JSON-RPC errors carry a numeric `code` and a `message`. The codes you will meet most: -32700 parse error, -32600 invalid request, -32601 method not found, -32602 invalid params (this course's twin also uses it for unknown tool names, matching common server behaviour), and -32603 internal error. Separately, a tool that ran and failed returns a normal result with `isError: true` and the failure as content, because the model should see and react to tool failures, while protocol errors mean the conversation itself is malformed. Lesson 21 builds your error policy on this distinction.

## Run it

Run `python3 client_twin.py`. It launches `server_twin.py`, handshakes, discovers, and calls. Then open both files and trace one call from the client's `request` method to the server's `handle` function and back. Finish with `python3 smoke_test.py`, which asserts the whole exchange, including the error case.

## Common failures

- **Writing to stdout inside a stdio server.** Stdout is the wire. One stray `print` corrupts the message stream and the client sees garbage or hangs. Log to stderr, always. This is the single most common MCP bug in the wild.
- **Treating notifications as requests.** Notifications have no `id` and get no response. A server that replies to one breaks the client's bookkeeping.
- **Skipping the handshake in a hand rolled client.** It works against forgiving test servers and fails against real ones. The twin enforces the order so you build the habit.

## Recap checklist

- [ ] I can read a raw MCP exchange and label every message.
- [ ] I can state what each side advertises in `initialize` and why it matters.
- [ ] I can explain the difference between a protocol error and a tool result with isError true.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
