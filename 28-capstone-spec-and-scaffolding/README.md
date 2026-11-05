# Lesson 28: Capstone spec and scaffolding: LeadDesk MCP

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** All previous lessons · **You need:** Just the lesson files. The capstone builds across Lessons 28 to 31.

The capstone assembles the whole course into one server you could hand to a stranger: **LeadDesk MCP**, a lead pipeline server for a small service business without a CRM, in the spirit of TechAura's production LeadPipe but sized for teaching and built entirely from parts you have already made. This lesson is the specification and the scaffold: the exact tool, resource, and prompt surface, the safety model, the data rules, and the acceptance tests your build must pass in Lessons 29 to 31. No new concepts live here; the discipline is in refusing to improvise the spec mid build.

## The surface, fixed in advance

Tools: `capture_lead` (write, idempotent on email), `score_lead` (read only calculation), `list_leads` (read only, paged summaries), `get_lead` (read only detail), `draft_followup` (read only, returns a draft, never sends), `book_appointment` (write, approval aware, idempotent on a request key). Resources: `leaddesk://pipeline/summary`, `leaddesk://pipeline/stages`, and the template `leaddesk://leads/{lead_id}`. Prompts: `qualify-lead` and `daily-digest` from Lesson 12. Every entry names its Lesson of origin; if your build invents a seventh tool, it is out of spec and belongs in your own fork's roadmap, not the capstone.

## The safety model, fixed in advance

Demo mode is the default: seeded fake leads, no credentials, no external calls. Writes support three modes in the LeadPipe pattern: direct, dry_run (report what would happen, change nothing), and approval (prepare the change and require an explicit confirmation flag before applying). Scores are computed server side. Stages move forward only, with LOST reachable from anywhere (Lesson 13). Nothing is ever sent to anyone by any tool. These are not features to add if time permits; they are the acceptance criteria.

## Acceptance, fixed in advance

Four gates, all automatable. One: the full scripted client suite (Lesson 09's pattern, extended in the scaffold's smoke test) passes against the stdio server. Two: the design checker (Lesson 07) passes on the final catalogue, and annotations (Lesson 08) match the truth table. Three: packaging checks (Lesson 22) pass on the shipped server.json and project file. Four: the README passes the Lesson 23 audit, including an honest Limits section. Lesson 30 runs the gates; Lesson 31 publishes through them.

## Run it

Read the scaffold: `capstone/SPEC.md` is the normative text, `capstone/server_twin.py` and its smoke test are the starting skeleton with the full surface stubbed at twin level. Run the smoke test now; it passes on the scaffold's implemented subset and lists what Lessons 29 builds next.

## Common failures

- **Spec drift during the build.** A capstone that quietly grows features teaches improvisation, not engineering. Park new ideas in a roadmap file the moment they appear.
- **Safety as a final lesson.** Modes, dedup, and stage rules are load bearing in the design. Retrofitting them in Lesson 30 week would rewrite every tool; they are specified here, before code, on purpose.
- **Acceptance by demo.** 'It worked in my chat' is not a gate. The four gates run from a clean clone by a script, or they do not count.

## Recap checklist

- [ ] I can state the capstone surface, safety model, and four gates without reopening the lesson.
- [ ] My scaffold smoke test runs and I know exactly what remains unbuilt.
- [ ] New ideas are parked in a roadmap, not smuggled into the build.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [LeadPipe MCP, the production reference](https://github.com/techaurah/leadpipe-mcp)
