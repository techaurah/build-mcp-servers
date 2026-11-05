# Security policy

## Reporting a vulnerability

If you find a security problem in this repository, for example a lesson that teaches an unsafe pattern, example code that leaks credentials, or a config file containing a real secret, please do not open a public issue with the details.

Report it privately through the contact form at [techaurah.com](https://techaurah.com), with "Build MCP Servers course security" in the message. We aim to acknowledge reports within three working days and to fix or annotate confirmed problems in the affected lesson.

## Scope notes

- This is a teaching repository. Example servers favour clarity, and lessons say explicitly where production hardening differs from the teaching version (Lessons 19 and 20 are the hardening pass in depth).
- Never commit real API keys, tokens, or personal data to your fork. If you accidentally commit a secret, rotate it immediately; deleting the commit is not enough.
- The checkers in this repo (tools/validate_servers.py and the lesson audits) are tripwires for common shapes, not guarantees. If you find a shape they miss, that is a lesson improvement worth an issue, filed without the secret itself.
