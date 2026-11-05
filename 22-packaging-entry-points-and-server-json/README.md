# Lesson 22: Packaging: project layout, entry points, and server.json

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 06 and 13 · **You need:** Just the lesson files. Packaging metadata validates offline.

A server that runs from your shell is a script. A server other people can install is a package: a project file that declares it, an entry point that starts it, and metadata the registries and directories can read. This lesson packages LeadDesk the way LeadPipe is packaged: a `pyproject.toml`, a console entry point, and a `server.json` manifest following the MCP registry schema, so the same artefact serves a laptop install and a directory listing.

## The project file carries the product

`pyproject.toml` declares the package name, version, Python floor (3.11 here, matching the course), the SDK dependency with the same pin discipline as Lesson 00, and the script entry point that turns the installed package into a command (`leaddesk = "leaddesk.server:main"` in spirit). It also carries the description and keywords directories display. Version it semantically and keep a changelog: a server's version is part of its contract with every saved client config pointing at it.

## server.json: the registry manifest

The official MCP Registry describes servers with a `server.json`: a reverse domain style name (`io.github.techaurah/leaddesk` in the pattern LeadPipe uses), a description within the registry's length discipline, repository and website links, and package entries saying how to obtain and run the server (registry type, identifier, transport, and the runtime arguments and environment variables it needs). Directories beyond the official registry (Glama, M8ven, and others, next lesson) read overlapping subsets of the same facts, which is why one accurate manifest, kept in the repo root, pays off repeatedly.

## Layout that survives growth

Keep the server package importable without side effects (the `__main__` guard again), the logic layer separate (Lesson 06), examples and a demo entry point in the repo, and tests that run from a clean clone with the documented commands only. If a step lives only in your head or your shell history, it does not exist for the next installer, which on a popular server is a stranger at midnight.

## Run it

Run `python3 check_packaging.py`, which parses this lesson's `server.json` and `pyproject.toml` example and checks the manifest fields the registries require. Compare each field with LeadPipe's real manifest shape as described in the lesson.

## Common failures

- **A name that collides or lies.** Registry names are namespaced for a reason. Claim only namespaces you control (your GitHub organisation's reverse domain), and never name a teaching clone after the production server it imitates.
- **Manifest drift.** server.json saying version 0.1.0 while the package ships 0.3.0 is how directories end up installing history. Update the manifest in the same commit as the version bump; better, generate it.
- **Environment variables undocumented in the manifest.** If the server needs a variable, the manifest's environment declaration is where installers learn it. A server that fails at first run for an unnamed variable reads as broken, not secure.

## Recap checklist

- [ ] My package installs from a clean clone with documented commands only.
- [ ] My server.json parses, names a namespace I control, and matches the package version.
- [ ] Every required environment variable is declared in the manifest.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP Registry](https://registry.modelcontextprotocol.io)
