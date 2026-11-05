# Lesson 24: Observability: logging, tracing a call, and knowing your costs

**Time:** about 45 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 04 and 21 · **You need:** Just the lesson files. No SDK needed.

A server in production answers three questions on demand: what just happened, why did this call do that, and what is this costing. This lesson builds the minimum honest observability for an MCP server: structured logs on the right channels, a trace of one call across client and server, and a cost model that counts the currencies a server actually spends (latency, upstream quota, and model tokens its answers induce).

## Logging that survives contact with stdio

Two channels, never confused. Operational logs for the operator go to stderr or a file, structured as JSON lines with timestamp, level, event, and a correlation id per call. Protocol logging (`notifications/message`) goes to the client for the host's log view, at the level the client set. On stdio, a single operational log line to stdout is a protocol incident (Lessons 02 and 17), so the logger is configured before anything else runs, and a smoke test asserts the server's stdout parses as pure protocol, a test this repo's twin already models.

## Tracing one call

When a user says the booking came out wrong, you need the call's biography: the raw request as received, the tool and arguments, which logic path ran, what the upstream returned, the result as sent, and timings between the marks. The correlation id threads it: generated per call, stamped on every log line the call produces, and included in error reference ids (Lesson 21), so a user quoting an error and an operator reading logs meet at the same record. Keep traces free of secrets and personal data beyond what debugging needs; logs are a data store with readers, treat them under the same discipline as the database.

## The costs a server really spends

Your server's own compute is usually the smallest bill. The real currencies: upstream API quota and rate limits (a chatty list tool can drain a day's allowance), latency the user feels (p95 per tool, not averages that hide the tail), and induced model cost: verbose results are re read by the model on every subsequent turn of that conversation, so a tool returning a 40 kilobyte dump taxes every later message. Design returns for the question asked (summaries first, detail on request, pagination for lists), and measure with the same scripted client from Lesson 09 so numbers compare across versions.

## Run it

Run `python3 trace_demo.py`, which executes one instrumented capture against the logic layer and prints the JSON log lines with their correlation id, then the smoke test. Note what is deliberately absent from the log lines.

## Common failures

- **Logging arguments wholesale.** Arguments contain personal data and occasionally secrets a caller pasted. Log shapes, ids, and outcomes; keep raw payloads out or behind a deliberate debug flag that production never sets.
- **Averages as latency truth.** A p50 of 80 milliseconds can hide a p95 of 9 seconds that users experience as 'the flaky server'. Report the tail or say nothing.
- **Free verbosity.** Every extra kilobyte in a tool result is a recurring charge on the conversation. Verbose debug shapes belong behind an explicit parameter, never the default.

## Recap checklist

- [ ] My server logs structured lines with a correlation id, on stderr or file only.
- [ ] I can reconstruct one call's biography from my logs alone.
- [ ] My list tools paginate or summarise by default, and I can say why in cost terms.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
