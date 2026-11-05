# Exercise for Lesson 09: Testing without a model: Inspector, scripted clients, and smoke tests

Extend the smoke test with two negative assertions of your own: a `tools/call` whose arguments fail logic validation (capture with a bad email) must return isError true, and a `resources/read` for an unknown URI must return a protocol error. Run it and confirm both pass against the twin.
