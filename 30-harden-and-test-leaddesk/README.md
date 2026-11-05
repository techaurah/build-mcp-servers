# Lesson 30: Harden and test LeadDesk: approval writes, dry runs, and the gate suite

**Time:** about 2 hours · **Difficulty:** Advanced · **Prerequisites:** Lesson 29 · **You need:** Just the lesson files. No SDK needed for the gate suite.

Now attack your own work before strangers do. This lesson runs the capstone through the course's accumulated defences: the write mode matrix (direct, dry run, approval) exercised per write tool, the security audit pattern from Lesson 20 applied to LeadDesk's own surface, the error policy from Lesson 21 checked bucket by bucket, and the four acceptance gates from Lesson 28 executed as one suite. Anything that fails here is a gift: it failed at your desk, in your tests, instead of in a user's first run.

## The write mode matrix

For each write tool (capture, book), each mode must behave exactly: direct applies and reports; dry_run reports the would be outcome and leaves the store provably unchanged (the test asserts counts before and after); approval prepares the change, returns a pending description without applying, and applies only when the confirmation arrives in the specified form. Demo mode defaults to approval for booking and direct with dedup for capture, mirroring the production pattern: the cheap, reversible write flows, the consequential one waits for a human.

## The self audit

Run Lesson 20's lens over your own catalogue. Descriptions contain no hidden instructions and no pleas to bypass modes. Annotations match reality (run Lesson 08's truth table against the build). No tool accepts a score, a permission, or a credential as an argument. Resources refuse ids outside the vocabulary. Result text quoting lead supplied fields is returned as data fields, not concatenated into instruction shaped prose. Each check is a line in the gate suite, not a hope in a review comment.

## Failure rehearsal

The suite also rehearses the bad day: unknown tool, unknown lead id, backwards stage move, duplicate booking key, slot collision under a second key, invalid email, and a booking attempted in approval mode without confirmation. Each must land in its Lesson 21 bucket with the specified shape. A server is trustworthy in proportion to how boring its failures are, and boring is a test result, not a personality trait.

## Run it

Run `python3 gate_suite.py`: it executes the mode matrix, the annotation checks, and the failure rehearsal against the twin and logic, printing a verdict per gate. Fix what it finds in the lesson's code only if you introduced the divergence in Lesson 29's exercise; otherwise study the failure until its layer is obvious.

## Common failures

- **Testing modes by reading code.** Modes are behaviour; only calls prove them. A dry run that writes is invisible to code review and obvious to a count assertion.
- **Approving by prompt.** 'The model said the user agreed' is not confirmation. Approval arrives through the mechanism the spec defines (an explicit flag or a host mediated elicitation), never through conversational vibes.
- **Gates that only run once.** A suite you ran last week describes last week's server. The gates wire into CI in Lesson 31 and run on every change from then on.

## Recap checklist

- [ ] The gate suite passes end to end, including every failure rehearsal case.
- [ ] Dry run provably changes nothing; approval without confirmation provably applies nothing.
- [ ] I can point each rehearsed failure at its error policy bucket.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
