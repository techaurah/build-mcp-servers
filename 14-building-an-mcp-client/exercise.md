# Exercise for Lesson 14: Building an MCP client in Python

The twin client's `request` method raises on any protocol error. Improve its contract for product use: distinguish the unknown tool case so a caller can react differently (refresh the catalogue and retry once) from a parse error (never retry). Write the design in prose: what the method returns or raises in each case, and why the distinction belongs in the client rather than in every caller.
