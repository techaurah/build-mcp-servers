# Lesson 21: Errors, retries, timeouts, and idempotent writes

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lessons 08 and 20 · **You need:** Just the lesson files. No SDK needed.

Reliability in a tool server is mostly a policy, written before the outage. Which failures return isError and which raise protocol errors. What may be retried, by whom, with what backoff. How long a call may run before someone is told. And the property that makes retries safe instead of dangerous: idempotency, designed into write tools with keys and dedup, the way LeadPipe's booking returns the existing event instead of a second one. This lesson writes LeadDesk's policy and implements its centrepiece.

## An error policy on one page

Classify every failure your server can produce into exactly one bucket. Caller error (bad arguments, unknown id): isError result, text that teaches the fix, never retried automatically. Transient upstream failure (a network API timed out): the tool may retry internally a bounded number of times, or return isError marked transient so the client can decide. Server bug: protocol level internal error is honest in development; in production, log the detail server side and return a clean isError with a reference id. Policy lives in a document reviewers can read (this lesson's `policy.json`) and in code reviewers can test.

## Retries belong to the layer that can judge

Blind retry loops inside clients turn a sick upstream into a dead one. The server, which knows whether its write is idempotent and which upstream failed, is usually the right place for bounded retries with backoff and jitter on transient reads. Writes are retried only when idempotent by design. Progress notifications (Lesson 04) plus a stated timeout per tool keep long operations honest: a booking tool that may legitimately take ten seconds says so, and the client is not left guessing at thirty.

## Idempotency keys, concretely

The pattern: the caller supplies or the server derives a stable key for the intended effect (lead email for capture, a booking request id for appointments). The server records key to outcome. A repeat call with the same key returns the recorded outcome with a flag saying nothing new was created, exactly as LeadDesk's capture dedup does and as this lesson's booking demo implements with explicit keys. Keys need a lifetime and a store (Lesson 13); 'remember forever in a dict' is the demo version, and naming it as such is the honest version.

## Run it

Run `python3 booking_demo.py` to watch the same booking key produce one event across three calls, including one interleaved failure, then read `policy.json`. Finish with the smoke test, which asserts the idempotency contract.

## Common failures

- **Retrying non idempotent writes.** A timeout does not mean the write failed; it often means the answer was lost. Retrying a booking without a key manufactures duplicates at the exact moment you feel safest.
- **Timeout theatre.** A client timeout shorter than the server's real work produces phantom failures and duplicate retries. State per tool expectations and set timeouts from them.
- **Error text as a diary.** Stack traces and internal ids in model facing errors leak architecture and confuse the model. Reference ids for your logs, plain language for the caller.

## Recap checklist

- [ ] My server has a written error policy with every failure in one bucket.
- [ ] Every write tool is idempotent by design or documented as never auto retried.
- [ ] Long tools declare expected durations and report progress.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
