# Exercise for Lesson 02: The protocol on the wire: JSON-RPC, lifecycle, and capabilities

Add a `ping` round trip to the client script's main flow (the server already handles it), printing the empty result, and add one deliberate mistake: call `tools/call` before `initialize` in a scratch copy and observe what a stricter server would need in order to reject it. Write two sentences on what the twin currently does with that early call and what production servers commonly do.
