# Lesson 31: Ship it: publish, document, and showcase your server

**Time:** about 90 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 22, 23, and 30 · **You need:** Your finished capstone from Lessons 29 and 30. A GitHub account for the showcase step.

The last lesson turns a passing capstone into a published one, in the order Lesson 23 fixed: verify from a clean clone, finish the README to the audit, finalise the packaging, wire the gates into CI, release with a version and notes, list where listing is honest, and submit your build to this course's showcase. Shipping is a sequence of small, checkable acts, and this lesson is the checklist that keeps them in order.

## The release routine

One: clean clone test. Clone your capstone repo fresh, follow only its README, and reach a green gate suite; anything you have to remember is a README bug. Two: README to the audit (purpose, demo, tools, safety, config, limits), with the demo command literally first among equals. Three: packaging finalised (version bumped deliberately, server.json regenerated or updated in the same commit, changelog entry written in human words). Four: CI wiring, this repo's workflow pattern extended with your gate suite, green on the release commit. Five: tag and release notes that say what the server does, what changed, and what is known to be limited. Six: registry and directory submissions where your server qualifies, manifest first. Seven: the showcase row below.

## What done looks like

Done is not 'on GitHub'. Done is: a stranger with a host and ten minutes reaches a working demo from your README alone; your catalogue, annotations, and safety model read exactly as the server behaves; your gates run on every push; and your limits section is honest enough that a disappointed reader still trusts you. That artefact, in your account, inspectable and runnable, is this course's completion proof. There is no certificate, and after this build you should understand why the artefact outranks one.

## Where to go next

The roadmap you parked in Lesson 28 is your syllabus now: a real backing store, a remote deployment with enforced scopes, a second server in TypeScript, a gateway composition. The programme's other courses meet you at the borders: Course 1 for the agent side of the calls your server receives, Course 2 for automation platforms that consume and expose MCP in both directions, and the testing and multi agent courses for depth on either side of the wire. Build in the open, keep the gates green, and let the showcase know what you ship.

## Run it

Run the full local rehearsal of the release routine against this lesson's checklist file (`python3 release_check.py`), which verifies the artefacts this repo itself can check: the capstone spec exists, the gate suite is present two lessons back, and your release notes draft in this folder covers the required sections. Then execute the routine on your own capstone repository.

## Common failures

- **Publishing before the clean clone test.** Your machine is a liar: it has env vars, warm caches, and a demo database from Lesson 29. The clone is the first honest environment your strangers will meet.
- **Release notes as a commit list.** Humans need what changed for them: new tools, changed behaviour, known limits. Generate the commit list if you like; write the notes yourself.
- **Showcase shame.** An unfinished looking but honest capstone (gates green, limits stated) belongs in the showcase. A polished page over a broken demo does not, and maintainers check the demo, not the adjectives.

## Recap checklist

- [ ] A clean clone of my capstone reaches a green gate suite from its README alone.
- [ ] My release is tagged, noted, packaged, and listed with a manifest that matches.
- [ ] My capstone is submitted to the showcase with an honest one line description.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Course showcase](../showcase/)
