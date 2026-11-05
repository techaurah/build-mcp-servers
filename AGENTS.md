# AGENTS.md

Conventions for AI assistants working in this repository. Human contributors should read CONTRIBUTING.md; this file states the same rules in machine-checkable form.

## Repository shape

- Lessons live in root folders named `NN-kebab-lesson-name`, numbered 00 to 31, matching the lessons table in README.md exactly. Never rename a lesson folder without updating README.md, llms.txt, and PROGRESS.md in the same change.
- Each lesson folder contains: `README.md` (the lesson), runnable artifacts (Python twins, logic modules, SDK server files, JSON examples), `exercise.md`, and `solution/` with the worked solution.
- Root files: README.md (landing page), llms.txt (course index for AI assistants), PROGRESS.md (learner checklist), DESIGN.md (the design this repo was built to), RESEARCH.md (the competitor scan), resources/, showcase/, translations/, assets/, tools/.

## Writing rules

- Plain language, short sentences. Define every technical term on first use or ensure it exists in resources/glossary.md.
- No em dashes anywhere, in prose or code comments. Use commas, colons, or full stops instead.
- Question-shaped headings are welcome in lessons where natural.
- No invented statistics, learner counts, or results. Product and protocol facts (versions, spec revisions, SDK APIs) need a source or a check against current MCP documentation; the protocol versions by date and the SDK renames classes across major lines, so Lesson 25's verification habit applies to every factual edit.
- Do not promise certificates. The course's completion artifact is the public capstone showcase.

## Code rules

- Python twins, logic modules, checkers, and smoke tests run on the standard library (Python 3.11 or newer) with a zero-credential path. SDK server files pin the v1 line (`mcp[cli]>=1.28,<2`, import `mcp.server.fastmcp`) and must say so at the top; logic must live outside the SDK wrapper so it stays testable offline.
- Every JSON example must parse and pass tools/validate_servers.py: host configs carry the right top level key and absolute paths, server.json carries the registry fields and a namespaced name. CI runs it.
- A lesson may ship a `smoke_test.py`; CI runs every file with that name, so keep smoke tests fast, offline, and credential-free. TypeScript in Lesson 26 is a reading artefact; its smoke test checks consistency, never Node.
- Stdio discipline in every example: nothing writes to stdout except protocol messages. Logs go to stderr, always.

## Change rules

- Small fixes may go straight to a pull request. New lessons, rewritten lessons, and new translation languages start with an issue (the two-tier rule in CONTRIBUTING.md).
- If lesson titles change, update README.md, llms.txt, and PROGRESS.md together; the three must never disagree.
- Showcase rows are added by learners via PR, one row per learner, format in showcase/README.md.
