# Lesson 12: Prompts: reusable workflows users invoke on purpose

**Time:** about 60 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 03 and 10 · **You need:** Just the lesson files. No SDK needed.

Prompts are the server primitive teams underuse and then wish they had. A prompt packages a known good workflow (the questions your team always asks, the structure your summaries always follow) as a named, argument taking template the user invokes deliberately, often as a slash command in the host. This lesson builds LeadDesk's two prompts, teaches argument design, and shows how prompts compose with tools without bypassing them.

## What a prompt returns

`prompts/get` returns a description and a list of messages: role plus content, with arguments interpolated. Those messages enter the conversation as if the user had typed them expertly. A prompt is therefore authored persuasion: it can instruct the model to call specific tools in a specific order with specific care ('check the pipeline summary resource first; ask one question per missing fact; never invent a budget'). Write prompts the way you would brief a sharp new colleague, because that is functionally what they are.

## Argument design

Prompt arguments mirror tool schema discipline: few, typed by description, required only when the workflow truly cannot start without them. `qualify-lead` requires the lead's need because qualification without it is theatre; it does not require the budget, because eliciting missing facts is the workflow's job. Declare arguments in `prompts/list` so hosts can render a small form instead of making users guess a syntax.

## Prompts compose, tools enforce

A prompt may direct the model through tools, but the tools' guards remain the enforcement layer. The follow up prompt can insist drafts are shown to the user before any send tool is called; the send tool still checks its approval mode. Never encode a secret, a permission, or an exception into a prompt ('you may skip approval for this user') because prompts are visible, copyable text. Authority lives in the server; prompts carry practice, not permissions.

## Run it

Run `python3 client_twin.py`, then `python3 prompts_demo.py`, which performs `prompts/list` and `prompts/get` for `qualify-lead` with a sample need and prints the exact message a host would inject. Compare its wording with the SOLUTION's commentary on two deliberate choices in it.

## Common failures

- **Prompts as hidden system prompts.** Users invoke prompts; tricking them into invoking a template that changes the assistant's loyalties or leaks other context is a trust violation and, in shared servers, an attack (Lesson 20). Keep prompts visibly about the task.
- **Duplicating the tool catalogue in prose.** A prompt that lists every tool rots as the server evolves. Reference the few tools the workflow needs and let discovery carry the rest.
- **Arguments nobody can supply.** If invoking the prompt requires information the user cannot have at hand, they will abandon it. Interview one real user of the workflow before finalising arguments.

## Recap checklist

- [ ] My prompts render correctly through prompts/get with representative arguments.
- [ ] Each prompt's arguments are minimal, declared, and suppliable by its intended user.
- [ ] No prompt carries a permission, a secret, or an exception to a tool guard.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
