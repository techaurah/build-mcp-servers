# Lesson 14: Building an MCP client in Python

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 02 and 09 · **You need:** Just the lesson files for the twin client. The SDK client section needs the pinned SDK.

Server builders who have written a client debug faster, because they have stood on both ends of the wire. This lesson builds a real client twice: the twin client you already know, extended into a reusable class with clean session handling, and the SDK client shape (`ClientSession` with a stdio client context) that production hosts use. The concepts are identical; the SDK version shows how much ceremony the library removes and what it hides that you still need to know.

## The client session, end to end

A client session has four phases: connect (spawn or reach the server over a transport), initialise (exchange versions and capabilities, then the initialised notification), work (list and call, read, get, handling notifications), and close (shut down streams and let the server process exit cleanly). The twin client implements each phase explicitly. The SDK wraps them in context managers: `stdio_client` owns the process, `ClientSession` owns the protocol, `session.initialize()` performs the handshake. When an SDK client hangs, it is almost always phase one or two, and your twin experience tells you which.

## Handling what servers send back

A robust client distinguishes the three outcomes of a call: a result with content, a result with isError true (show the text to the model or user as a recoverable failure), and a protocol error (the conversation broke; log the code and message, do not retry blindly). It also expects notifications: progress updates during long calls, log messages, list changed announcements that should refresh its cached catalogues. Caching `tools/list` forever is the client side classic bug; servers evolve, and Lesson 11 gave them a polite way to say so.

## Clients as test harnesses and as products

The scripted client from Lesson 09 is this lesson's client with assertions. The product version swaps assertions for a model loop: present tools to the model, dispatch its choices, feed results back. Everything between (transport, session, discovery) is shared. That is why this course builds the client before the capstone: your capstone's acceptance test is a client you own, not a prayer inside a chat window.

## Run it

Run `python3 client_twin.py`, then read `client_sdk.py` (no run needed without the SDK) and annotate each line with the twin phase it replaces. Finish with the smoke test, which drives the twin client class as an imported library rather than a script.

## Common failures

- **Leaking server processes.** A client that does not close stdin and wait leaves orphaned stdio servers holding memory and file locks. Context managers exist precisely here.
- **Retrying protocol errors in a loop.** A -32601 will still be a -32601 in 200 milliseconds. Retry transient transport failures with backoff; surface protocol errors immediately.
- **Trusting server output into your own UI unsanitised.** Tool results are third party content. A client that renders them as raw HTML has built an injection delivery service (Lesson 20).

## Recap checklist

- [ ] I can run a full client session and name its four phases in code.
- [ ] My client handles results, isError results, and protocol errors differently.
- [ ] Closing my client leaves no server process behind.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
