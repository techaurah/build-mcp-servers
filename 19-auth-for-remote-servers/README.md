# Lesson 19: Authentication for remote servers: OAuth 2.1, tokens, and least privilege

**Time:** about 60 minutes · **Difficulty:** Advanced · **Prerequisites:** Lesson 18 · **You need:** Just the lesson files. No live identity provider needed.

A remote MCP server is an API with a model's hands on it, and it needs real authentication. The MCP authorisation model is built on OAuth 2.1: the server acts as an OAuth resource server, clients obtain access tokens from an authorisation server and present them as bearer tokens, and protected resource metadata tells clients where to get them. This lesson teaches that flow at design depth, plus the principle that decides whether any of it matters: authorise the action, not just the connection.

## The flow, in roles

The client discovers, from the server's protected resource metadata (served under the well known path defined by RFC 9728), which authorisation server protects it. The client registers or presents its client identity, runs an OAuth 2.1 flow with PKCE, and receives an access token scoped to the resource. Requests then carry `Authorization: Bearer` with the token. Servers validate the token (signature, expiry, audience: a token minted for another service must be rejected, the confused deputy defence) and derive the caller's identity and scopes from it. The SDK and standalone frameworks provide pieces of this; the design decisions (scopes, audience, lifetimes) remain yours.

## Authorisation per action

A valid token proves a caller may talk to the server. It must not prove they may do everything. Map scopes to capability tiers (read, draft, write, admin), check them inside tools, and let resources filter by caller: `list_leads` for a sales rep returns their pipeline, not the company's. This is the server side mirror of Lesson 08's annotations and Lesson 20's threat model: authentication names the caller, authorisation bounds them, and neither replaces the tool level guards (approval modes, idempotency) that protect against a legitimate caller being steered by injected content.

## Local servers and tokens, briefly

Stdio servers inherit the user's own machine security: whoever can run the process is the caller, and per user config env is the usual credential channel. Do not invent token checks inside a stdio server; do keep secrets out of the repository and the config examples, and rotate anything that ever appeared in a screenshot or a commit.

## Run it

Run `python3 auth_flow.py` to walk the OAuth sequence as numbered steps with the artefact each step produces, then run the scope checker in the smoke test, which encodes LeadDesk's tier map and refuses two plausible but wrong requests.

## Common failures

- **Audience blindness.** Accepting any token from your identity provider, including ones minted for other services, rebuilds the confused deputy problem OAuth audience claims exist to close.
- **One scope to rule the demo.** A single `full-access` scope feels simple and removes your ability to give a read only integration to anyone, ever, without a redesign.
- **Tokens in tool arguments.** Credentials travel in headers and env, never as tool parameters a model can see, repeat, and log.

## Recap checklist

- [ ] I can walk the OAuth 2.1 flow for a remote server and name each artefact.
- [ ] My tools check scopes per action and my resources filter per caller.
- [ ] No credential ever appears as a tool argument or in a committed config.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [MCP specification: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
