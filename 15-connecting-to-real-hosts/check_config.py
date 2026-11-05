"""Lesson 15: validate host config files against the lesson rules.

Checks JSON parses, the expected top level key exists, every
server has a command, and command and script args are absolute
(the placeholders in the shipped examples count, since they
begin with /ABSOLUTE). Run: python3 check_config.py
"""
import json
import os

FILES = [("claude_desktop_config.json", "mcpServers"),
         ("vscode_mcp.json", "servers")]

def check(path, key):
    with open(path) as f:
        data = json.load(f)
    problems = []
    if key not in data:
        return [f"missing top level key {key}"]
    for name, cfg in data[key].items():
        if "command" not in cfg:
            problems.append(f"{name}: no command")
        elif not (cfg["command"].startswith("/") or cfg["command"].startswith("ABSOLUTE")):
            problems.append(f"{name}: command is not an absolute path")
        for arg in cfg.get("args", []):
            if arg.endswith(".py") and not arg.startswith("/"):
                problems.append(f"{name}: script arg is not absolute: {arg}")
    return problems

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    bad = 0
    for name, key in FILES:
        problems = check(os.path.join(here, name), key)
        print(f"{name}: {'OK' if not problems else 'FAIL ' + '; '.join(problems)}")
        bad += bool(problems)
    print(f"{len(FILES)} configs checked, {bad} failing")
