# Lesson 11: Resource templates, subscriptions, and change notifications

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lesson 10 · **You need:** Just the lesson files. No SDK needed.

Two resource refinements separate shelf servers from live ones. Templates let one pattern (`leaddesk://leads/{lead_id}`) address every lead without listing thousands. Subscriptions let a client ask to be told when a specific resource changes, through `resources/subscribe` and `notifications/resources/updated`, with `notifications/resources/list_changed` announcing catalogue changes. This lesson adds both to the LeadDesk design and teaches the restraint they need: templates are not an excuse to expose everything, and subscriptions are a cost you should grant deliberately.

## Templates: one pattern, many items

A template is listed through `resources/templates/list` with a `uriTemplate` following RFC 6570: variables in braces, expanded per item. The read path parses the concrete URI back into variables and serves that item. Design templates around the identifier your users already think in (the lead id printed everywhere), validate the expanded values as strictly as tool arguments (a template variable is still untrusted input), and return the same -32602 style error for ids that do not exist rather than an empty document that looks like a real, blank lead.

## Subscriptions and update notifications

A client subscribes to a URI; when that resource's content changes, the server sends `notifications/resources/updated` with the URI, and the client re reads if it cares. The server advertises `resources.subscribe` in capabilities only if it truly implements this, and `resources.listChanged` if it emits catalogue change notifications. The honest engineering questions: how do you know the content changed (compute on write paths, not polling theatre), and what does a notification cost at your scale? For LeadDesk, captures and stage moves are the write paths, and they are exactly where the twin design hooks notification emission.

## Dynamic catalogues and list_changed

When resources appear or disappear at runtime (a summary that exists only after the first lead, per user workspaces in a remote server), `notifications/resources/list_changed` tells clients to re list. Use it when the catalogue genuinely moves; a static server emitting it habitually trains clients to ignore it. In the SDK, list changed behaviour ties to how you register resources, so design the catalogue's dynamics on paper first, as this lesson does, before wiring decorators.

## Run it

Run `python3 templates_demo.py`, which expands the lead template for two ids, shows the parse back into variables, and simulates the subscribe then capture then notify sequence as printed messages. Finish with the smoke test.

## Common failures

- **Template variables as a skeleton key.** `leaddesk://leads/{anything}` must still check that the id exists and that this client may see it. A template widens addressing, never authority.
- **Subscribing clients to everything.** Notifications are per URI for a reason. A server that blasts updates for resources nobody subscribed to is spamming its hosts and will be muted or dropped.
- **list_changed without a change.** Clients respond by re listing and diffing; crying wolf costs them work and costs you trust. Emit on real catalogue changes only.

## Recap checklist

- [ ] I can write a URI template for my items and parse a concrete URI back safely.
- [ ] I know which capability flags subscriptions and list changed require.
- [ ] My server notifies subscribers on real write paths, and nobody else.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
