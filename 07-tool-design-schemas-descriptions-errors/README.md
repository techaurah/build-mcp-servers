# Lesson 07: Tool design: schemas, descriptions, and errors models can use

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 06 · **You need:** Just the lesson files. No SDK needed for the design checker.

Models choose tools from descriptions and call them from schemas. That makes tool design a writing and contract discipline before it is a coding one, the same law Course 1 teaches for function calling, now with an ecosystem reading your work. This lesson states the design rules this course enforces, ships a checker that audits a tool catalogue against them, and applies the rules to LeadDesk's growing catalogue, including the error shapes a model can actually recover from.

## Names and descriptions that carry weight

Name tools as verb phrases in snake case: `capture_lead`, `book_appointment`, never `lead` or `do_thing`. Write the description for a capable stranger who cannot see your code: what it does, when to use it, what it returns, and any behaviour the caller must know (deduplicates on email; never sends anything; requires approval mode for writes). One or two sentences is usually right. If two tools' descriptions could be swapped without a model noticing, at least one of them is wrong.

## Schemas: small, typed, honest

Keep parameter counts low; a tool with twelve parameters is two tools arguing. Type everything, use enums where the set is closed (stages, bands), mark required honestly, and give defaults only where a default is genuinely safe. Validate inside the tool anyway: schemas guide well behaved clients, they do not stop careless or hostile ones, so the logic layer re checks email shape and ranges, as `lead_logic.py` does. Return structured, stable shapes: the same keys on success every time, so callers can build on them.

## Errors the model can act on

Two channels, from Lesson 02: protocol errors for malformed conversations, and tool results with `isError: true` for calls that ran and failed. Inside tool results, write errors as instructions for recovery: what was wrong, what a valid call looks like. 'Invalid params' teaches nothing; 'email does not look like an email address; capture_lead needs a reachable email for the lead' lets the model fix the call or ask the user. Never leak stack traces, SQL, or internal paths into error text: the model will quote them to the user, and attackers will read them with interest.

## Run it

Run `python3 catalogue.py` to print LeadDesk's catalogue as data, then `python3 check_catalogue.py`, which audits it against this lesson's rules and prints a verdict per tool. Break one description on purpose in a scratch copy and watch the checker catch what a code review might wave through.

## Common failures

- **Descriptions that repeat the name.** 'capture_lead: captures a lead' spends the model's entire guidance budget on a tautology. Say what is not in the name: dedup, side effects, limits.
- **Accepting a score, a total, or a permission from the caller.** Anything safety or money shaped is computed or checked server side. If the model supplies it, the model controls it.
- **Boolean soup.** Three boolean flags that interact are a mode enum waiting to happen. `mode: direct, dry_run, or approval` (the LeadPipe write modes) reads better and validates better.

## Recap checklist

- [ ] Every tool in my catalogue passes the design checker.
- [ ] I can point at one description and say what behaviour it teaches beyond the mechanics.
- [ ] My tool errors tell the caller how to recover, without leaking internals.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
