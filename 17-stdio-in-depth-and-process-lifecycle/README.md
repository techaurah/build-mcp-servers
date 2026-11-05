# Lesson 17: Stdio in depth: process lifecycle, framing, and environment

**Time:** about 45 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 02 and 16 · **You need:** Just the lesson files. No SDK needed.

Stdio is called the simple transport, and it is, provided you respect that you are managing a child process with a byte stream for a mouth. This lesson goes one level deeper than the quickstart: newline delimited framing, who owns startup and shutdown, what environment and working directory the child actually gets, and how servers should behave when the pipe closes. These details decide whether a local server feels solid or flaky across hosts.

## Framing and the stream

On stdio, messages are newline delimited JSON: one complete JSON-RPC message per line, UTF-8, no embedded raw newlines inside a message. The reader accumulates until a newline, parses, dispatches. Two consequences. Anything else on stdout (logs, banners, a library's progress bar) is a framing attack on your own server. And a message must be written as one flushed unit; partial writes interleaved with another writer produce the classic intermittent corruption that vanishes under a debugger. The SDK serialises this for you; the twin shows why it must.

## Lifecycle ownership

The host spawns the server, owns its lifetime, and ends it, ideally by closing stdin and allowing a clean exit, forcibly if needed. Servers should treat stdin closing as a shutdown signal: finish the current unit of work, flush state (Lesson 13 commits), and exit promptly, because a host that has moved on will kill stragglers and remember your server as the one that leaks processes. Servers must never wait for interactive input, prompt on the terminal, or assume a controlling terminal exists.

## Environment and working directory

The child inherits what the host gives it: often a sparse PATH, the config's env block, and an arbitrary cwd. Defensive servers resolve their data paths from their own file location, read configuration from explicit env vars with loud failures when required ones are missing, and print nothing during startup. The Lesson 15 absolute path rule is the client side of this same coin.

## Run it

Run `python3 framing_demo.py`, which writes two protocol lines and one poisoned line through a pipe and shows the reader recovering the good messages and choking exactly where the poison lands. Then run the twin client and close it, watching the server exit on its own.

## Common failures

- **Logging libraries with stdout defaults.** Many frameworks log to stdout until told otherwise. Configure logging before anything else can emit, and audit dependencies for the same habit.
- **Buffering surprises.** A server whose responses sit in a buffer looks hung. Flush per message (the SDK and the twin both do), especially after writing results.
- **Assuming cwd.** A data file opened as `leads.db` lives wherever the host happened to stand. Anchor paths to the server file or an explicit env var.

## Recap checklist

- [ ] I can describe stdio framing and why stdout purity is a framing rule.
- [ ] My server exits promptly when stdin closes and commits state before exiting.
- [ ] My server resolves its paths independent of the host's working directory.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
