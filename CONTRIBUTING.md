# Contributing to Build MCP Servers

Thank you for helping improve this course. Contributions that make a lesson clearer, fix broken code, or add a well scoped lesson are welcome. This guide states the quality bar so reviews are quick and predictable.

## The two-tier rule

- **Small fixes go straight to a pull request.** Typos, a clarified paragraph, a corrected code comment, a broken link, a small code fix that keeps the lesson's behaviour: just open the PR.
- **Big changes start with an issue.** A new lesson, a major rewrite of an existing lesson, and a new translation language all start with an issue using the matching template, so a maintainer can confirm fit and nobody duplicates work. This protects your time, not our turf.

Showcase rows are the exception that proves the rule: one row per learner, straight to a PR, format in [showcase/README.md](showcase/README.md).

## The lesson quality bar

Every lesson, new or edited, must hold these properties:

1. **Complete unit.** A lesson folder holds a written lesson (`README.md`), runnable artifacts, an `exercise.md`, and a worked solution under `solution/`. No part may be a stub or a "coming soon".
2. **Offline path.** Twins, logic modules, checkers, and smoke tests run on the Python 3.11+ standard library with no credentials. SDK files pin the v1 line, import `mcp.server.fastmcp`, say so at the top, and keep logic outside the wrapper. JSON examples pass `tools/validate_servers.py`.
3. **Exercise plus solution.** The exercise must change the worked example in a meaningful direction, not repeat it, and it ships with a worked solution and an explanation.
4. **Plain language.** Short sentences, every technical term defined on first use or present in [resources/glossary.md](resources/glossary.md), and no em dashes anywhere.
5. **Honest numbers and current facts.** No invented statistics. MCP versions by date and SDKs rename APIs across major lines: check version, transport, and API claims against current MCP documentation before submitting, and name the revision or line you verified.
6. **Resources.** Each lesson ends with 3 to 6 curated links, official documentation first.

## Pull request checklist

- One lesson or one concern per PR; small PRs review faster.
- If you edited the lessons table in the root README, check every folder link still resolves (CI runs the link checker).
- If you edited JSON examples, run `tools/validate_servers.py` and say so in the PR description.
- If you edited code, confirm any `smoke_test.py` in that lesson passes; CI runs them.
- Translations follow [translations/README.md](translations/README.md).

## Reporting problems

Lesson bugs (code that does not run, broken links, instructions that do not work) are issues, filed with the lesson problem template. Questions about content belong in Discussions, not issues.

## Code of conduct

Participation is covered by the [Code of Conduct](CODE_OF_CONDUCT.md).
