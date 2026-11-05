# Lesson 25: Versioning: protocol revisions, SDK lines, and keeping a course honest

**Time:** about 45 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 05 and 18 · **You need:** Just the lesson files. Web access helps for the verification exercise.

MCP versions by date, SDKs version by number, and the two clocks do not tick together. This lesson consolidates the version story scattered through the course into one timeline you can reason from, teaches how to tell which revision a given SDK implements, and gives you the maintenance habit that keeps servers and tutorials true after the next revision lands.

## The revision timeline that matters

2024-11-05: the original public revision, with the HTTP plus SSE transport. 2025-03-26: Streamable HTTP replaces it, OAuth authorisation is formalised. 2025-06-18: refinements including structured tool output and elicitation's maturation; this is the revision much of the deployed ecosystem aligned on through 2025. 2025-11-25: the stable revision the Microsoft curriculum and this course's protocol references target. 2026-07-28: the largest revision yet, moving the core to stateless, self describing requests, removing the protocol level session and the `initialize` handshake as the opening move, and deprecating sampling, roots, and logging (removal no earlier than a revision a year later, per the revision's own notes as reported in current guides). None of this makes handshake era servers wrong today: hosts and SDKs serve both eras, and the Inspector exercises each. It does mean a builder must know which era they are in.

## Which revision does my SDK speak

Read it, do not guess: the SDK's repository states the specification revisions it implements, and the `initialize` exchange itself negotiates a concrete version string your client can log. This course's pinned Python v1 line implements the handshake era through 2025-11-25 era behaviour; the v2 line targets the 2026-07-28 model and renames the server class, which is why Lesson 00 framed the pin as a readability decision, not a refusal of the future. When you evaluate any server or tutorial, its era is a fact to record beside its name, like its transport.

## Maintenance as a feature

Servers outlive the week they were written. The habits that keep them true: pin dependencies with ranges you understand, subscribe to your SDK's releases, re run your scripted client (Lesson 09) against new SDK versions in a branch before users do, and keep a short VERSIONS note in the repo stating the protocol revisions and SDK lines you support and have tested. Courses rot the same way servers do; this course's own defence is that every version claim in it names its source and its observation date, so a future maintainer can re verify instead of re guessing.

## Run it

Run `python3 timeline.py` and keep its output as your pocket timeline. Then pick one MCP resource you have used (a tutorial, a server README) and record its era from evidence: imports, transport, and any version strings. The smoke test checks the timeline's internal order.

## Common failures

- **Latest as a version strategy.** Installing whatever is newest on the day, with no record, guarantees a future morning where nothing imports. Pins plus a review habit beat vibes.
- **Assuming deprecation means disappearance.** Deprecated in 2026-07-28 still means implemented across the deployed base for a long tail. Removing sampling support from your mental model today would make most current servers unreadable to you.
- **Silent era mixing in one codebase.** A v1 server file and a v2 client example in one repo, unlabelled, teaches your future self a bug. Label eras at the file level, as this course does.

## Recap checklist

- [ ] I can order the five revisions and name the headline change in each.
- [ ] I can determine and record the era of any SDK, server, or tutorial I touch.
- [ ] My repos carry a VERSIONS note and my pins have a review habit behind them.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
