# Lesson 00: Course setup: environment, versions, and how to use this repo

**Time:** about 30 minutes · **Difficulty:** Beginner · **Prerequisites:** None · **You need:** Python 3.11 or newer, a terminal, and git. No paid accounts, no API keys.

Every later lesson assumes this setup, so this one verifies it instead of describing it. You will check your Python version, create the virtual environment the course uses, install the pinned MCP Python SDK line this course teaches, and run the environment checker until it passes. You will also learn the one version fact that saves MCP learners the most pain, stated here once and repeated in Lesson 25: this course pins the SDK v1 line, because that is the API the official quickstart and most current tutorials use.

## The version decision, made once

The official quickstart at modelcontextprotocol.io, read in November 2026, teaches the Python server with `FastMCP` imported from `mcp.server.fastmcp` and requires SDK 1.2.0 or higher. That import is the v1 API. A v2 line of the SDK also exists and renames the class to `MCPServer` (`from mcp.server import MCPServer`), so code copied from a v2 guide fails on a v1 install with a confusing import error, and the reverse is also true. This course pins `mcp[cli]>=1.28,<2` in requirements.txt so every lesson runs as written. Lesson 25 teaches you to read which line a tutorial belongs to, and what migrating takes. Pinning is not fear of the new; it is how a course stays runnable.

## What gets installed, and what does not

Two layers. The standard library layer needs nothing: every lesson ships a twin or logic module that runs on Python alone, so the protocol and the business logic are always testable offline. The SDK layer adds the `mcp` package and its `mcp` command line tool, used for the real server files and for `mcp dev`, which launches the MCP Inspector against a server file. Node is optional and only needed if you want the standalone Inspector package or the TypeScript lesson's comparison; no lesson requires it to pass.

## How to use this repository

Fork the repository; your fork is your workbook. Each lesson folder holds a written lesson (README.md), runnable files, one exercise (exercise.md), and a worked solution (solution/SOLUTION.md). Work in order: later lessons reuse the LeadDesk server and vocabulary from earlier ones. Track yourself with PROGRESS.md. Where a lesson ships a `smoke_test.py`, run it; CI runs every smoke test in the repo, so green locally means green in CI.

## Run it

Run `python3 check_environment.py` in this folder. It checks the Python version, whether the SDK import this course uses resolves, and whether the twin in Lesson 02 will run. Then create the course environment: `python3 -m venv .venv`, activate it, and run `pip install -r ../requirements.txt` from the repository root. Finish by running the checker again inside the environment; the SDK line should now pass.

## Common failures

- **Installing the newest SDK and then following the lessons.** The lessons pin v1 on purpose. An unpinned install can land on v2, where `mcp.server.fastmcp` no longer exists, and every SDK file in the course fails at import. Use the requirements file.
- **Python older than 3.10.** The SDK itself needs 3.10 or newer and this course asks for 3.11 or newer, matching the house standard of Courses 1 and 2. The checker flags anything older.
- **Skipping the checker because the twin runs.** The twin proves your Python works. It does not prove the SDK line is right, and Lesson 06 is a bad place to discover that.

## Recap checklist

- [ ] My Python is 3.11 or newer and the checker passes inside the course environment.
- [ ] I can state which SDK line this course pins and why.
- [ ] I know every lesson has an offline path that needs no SDK and no keys.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Course 1, Lesson 14: MCP standard tools](https://github.com/techaurah/agentic-ai-for-beginners)
