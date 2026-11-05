# Lesson 15: Connecting to real hosts: config files, Claude Desktop, VS Code, and friends

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06 and 14 · **You need:** A host application if you want the live pass (Claude Desktop, VS Code, or another MCP host). The config files in this lesson validate offline.

A server is finished only when a host can launch it. Hosts discover local servers through configuration: a JSON file naming each server, the command that starts it, its arguments, and its environment. This lesson teaches the shared shape, the per host locations and dialects, and the three config bugs that account for nearly every 'my server does not appear' report in the ecosystem.

## The mcpServers shape

Claude Desktop's `claude_desktop_config.json` set the pattern most hosts follow: a top level `mcpServers` object; each key is a server name the user will see; each value gives `command`, `args`, and optionally `env` and `cwd`. The host spawns the command per session, speaks stdio, and kills the process at exit. VS Code uses the same idea in `.vscode/mcp.json` with a `servers` key and adds input prompts for secrets. Other hosts (Cursor, Claude Code's `claude mcp add` command and `.mcp.json`, ChatGPT's connector settings for remote servers) vary the file and the key names, never the underlying model: name, launch, environment.

## Absolute paths, always

Hosts launch servers from their own working directory, not yours, often with a minimal environment. Relative paths in `args` therefore resolve against a directory you do not control, and bare `python` may not be the Python with your packages. Use the absolute interpreter path from your environment (the checker in Lesson 00 prints the pattern), absolute script paths, and an explicit `cwd` when the server expects one. Half of all connection failures are this paragraph.

## Environment and secrets in config

The `env` block is where a server's API keys and mode flags come from in local setups. Treat config files as secrets bearing documents: they sit in user directories, get pasted into bug reports, and are committed to dotfiles repositories with depressing regularity. Prefer the smallest env that works, prefer host secret prompts or OS keychains where offered, and design servers (Lesson 13) whose demo mode needs no env at all, so the first run never asks a stranger for a credential.

## Run it

Validate this lesson's two example configs with `python3 check_config.py`. Then, if you have a host installed, register the Lesson 06 server using `claude_desktop_config.json` (or your host's equivalent) with absolute paths, restart the host, and make one real tool call. The debugging split from Lesson 09 applies: works in Inspector plus fails in host equals config.

## Common failures

- **Relative paths everywhere.** Command, script, and data file paths all resolve against the host's context. Absolutes, and a server that locates its data relative to its own file, not the cwd.
- **Editing config while the host runs.** Most hosts read config at startup. Restart fully (tray and all, on desktop apps) before concluding the server is broken.
- **One server, five names.** The config key is the name users and models see. Name servers by what they do (`leaddesk`), not by the file or the experiment of the week.

## Recap checklist

- [ ] My example configs pass the checker, including absolute path rules.
- [ ] A real host lists my server and completes one call.
- [ ] My config contains no secret I would mind seeing in a screenshot, or I know exactly why it does.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
