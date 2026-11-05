# Lesson 03: Tools, resources, prompts: the three server primitives

**Time:** about 60 minutes · **Difficulty:** Beginner · **Prerequisites:** Lesson 02 · **You need:** Just the lesson files. No SDK needed.

A server offers three kinds of things, and the specification is deliberate about who controls each. **Tools** are model controlled: functions the model chooses to call, each with a name, a description, and a JSON Schema for its inputs. **Resources** are application controlled: readable data identified by a URI, which the host decides to include as context. **Prompts** are user controlled: named, parameterised templates a person invokes on purpose, often surfaced as slash commands. Choosing the wrong primitive is a design error no amount of code fixes, so this lesson is mostly judgment, practised on the twin.

## Tools: actions and lookups the model drives

If the model should decide when it happens, it is a tool. Searching, calculating, creating, booking: tools. A tool's description is part of its interface, because the model chooses from descriptions; Lesson 07 is devoted to writing them. Tools can have side effects, which is why the course's servers mark write shaped tools clearly, gate them behind approval modes, and compute anything safety critical (like a lead score) server side rather than accepting it from the caller.

## Resources: data the application offers

If the host or user should decide what context goes in, it is a resource. A resource has a URI (`leaddesk://pipeline/summary`, `file:///logs/today.txt`), a name, a description, and a MIME type. Clients list them with `resources/list` and read them with `resources/read`. URI templates (`leaddesk://leads/{id}`) let one pattern address many items. Resources are for reading; a resource that changes the world is a tool wearing the wrong uniform.

## Prompts: workflows the user invokes

If a person should trigger a known good workflow, it is a prompt. `prompts/list` describes them with their arguments; `prompts/get` returns the message sequence with arguments filled in. The LeadDesk `qualify-lead` prompt is the running example: it encodes how your team qualifies a lead, once, in the server, instead of in every user's head or chat history. Prompts are the least used primitive and, for team consistency, often the most valuable.

## Run it

Run `python3 client_twin.py`, then run `python3 classify.py`, which presents eight capabilities and asks you to classify each as tool, resource, or prompt before revealing the course's answer and reasoning. Finish by listing the twin's resources and prompts through the smoke test's pattern.

## Common failures

- **Making everything a tool.** A daily summary the user always wants in context is a resource; burying it as a tool means the model may simply never call it. Match the primitive to who should decide.
- **Resources with side effects.** Reading must be safe to repeat. If `resources/read` changes state, caching, prefetching, and innocent retries all become dangerous.
- **Prompts that are secretly tools.** A prompt returns messages, not actions. If invoking it must change a system, the prompt should instruct the model to call the proper tool, with the tool's own guards intact.

## Recap checklist

- [ ] I can classify a new capability as tool, resource, or prompt and defend the choice by who decides.
- [ ] I can name the list and get or read method for each primitive.
- [ ] I can give a URI and a URI template example for resources.

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
