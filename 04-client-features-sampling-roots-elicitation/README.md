# Lesson 04: Client features: sampling, roots, elicitation, logging, and progress

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 03 · **You need:** Just the lesson files. No SDK needed.

Communication in MCP runs both ways. A server can ask the client for things, and those reverse requests are where much of the protocol's power and most of its risk live. This lesson covers the three client features (sampling, roots, elicitation) plus the two cross cutting utilities (logging and progress) that servers use constantly. It also states their current status honestly: sampling and roots are long standing features that the 2026-07-28 specification revision deprecates, while elicitation remains active. You need to understand all three, because the servers and clients in wide use implement the handshake era model.

## Sampling: the server borrows the client's model

With `sampling/createMessage`, a server asks the host to run a model completion on its behalf and return the result. The server needs no API key of its own, and the host keeps control: it can review, modify, or refuse the request, and the user approves. A document server might ask for a summary of the document it just served. The dangers mirror the power: a malicious or sloppy server can spend the user's model budget or fish for completions the user never intended, which is why hosts gate sampling and why the newest specification revision steps back from it. Design rule for this course: treat sampling as an optimisation you add last, never as a load bearing wall.

## Roots: the client states the boundaries

Roots tell a server which directories or URIs it may operate on. A client sends `roots/list`, and notifies with `notifications/roots/list_changed` when the set changes. A filesystem server that respects roots cannot be talked into wandering the whole disk by a clever tool argument. The server's duty is to treat roots as a ceiling, not a suggestion, and to re check on change notifications. If your server touches files, roots are its fence; Lesson 20 returns to this under security.

## Elicitation: asking the user, mid task

Elicitation lets a server request missing information from the user through the client's interface, using `elicitation/create` with a small schema for what it needs: a date, a choice, a confirmation. A booking tool that lacks a timezone should elicit it rather than guess or fail. Two hard rules: never elicit secrets (passwords, keys, payment data), because the channel is not a credential vault; and always let the user decline, handling the decline path in your tool. Elicitation is the primitive that turns dead end errors into conversations.

## Logging and progress: the quiet utilities

Servers send log messages to clients with `notifications/message` at standard levels (debug through emergency), and clients can set the floor with `logging/setLevel`. Progress is opt in per request: the client attaches a `progressToken` in the request's `_meta`, and the server sends `notifications/progress` as work advances. Both write to the client's side channels, never to stdout on stdio, and both are what separate a server that feels professional from one that hangs silently for thirty seconds.

## Run it

Run `python3 features_twin.py`. It extends the twin exchange with a simulated elicitation round trip and a progress sequence, printing each message with its direction, so you can see reverse requests in the same notation as forward ones. Then run the smoke test.

## Common failures

- **Eliciting secrets.** Never. Elicitation is for ordinary missing facts. Credentials belong in the server's own configuration or an OAuth flow (Lesson 19).
- **Assuming sampling exists.** It exists only if the client advertised it in `initialize`. Check capabilities before designing around it, and degrade gracefully.
- **Ignoring roots changes.** A root removed mid session is a permission revoked. Servers that cache the first list and never listen for the change notification keep access they no longer have.

## Recap checklist

- [ ] I can describe sampling, roots, and elicitation in one sentence each, with who approves what.
- [ ] I know the current status of each feature, including the 2026-07-28 deprecations.
- [ ] I can explain how progress reporting is switched on for a single request.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP specification: elicitation](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation)
