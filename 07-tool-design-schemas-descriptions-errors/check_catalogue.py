"""Lesson 07: audit a tool catalogue against the design rules.

Rules: verb phrase snake case names; descriptions of at least
12 words that are not the name restated; every property typed;
required fields all present in properties. Run: python3 check_catalogue.py
"""
import re
from catalogue import CATALOGUE

def check(tool):
    problems = []
    if not re.fullmatch(r"[a-z]+(_[a-z]+)+", tool["name"]):
        problems.append("name is not a snake case verb phrase")
    desc = tool["description"]
    if len(desc.split()) < 12:
        problems.append("description under 12 words: too thin to guide a model")
    schema = tool["inputSchema"]
    for field, spec in schema["properties"].items():
        if "type" not in spec:
            problems.append(f"property {field} has no type")
    for req in schema.get("required", []):
        if req not in schema["properties"]:
            problems.append(f"required field {req} missing from properties")
    return problems

if __name__ == "__main__":
    bad = 0
    for tool in CATALOGUE:
        problems = check(tool)
        print(f"{tool['name']}: {'OK' if not problems else 'FAIL ' + '; '.join(problems)}")
        bad += bool(problems)
    print(f"{len(CATALOGUE)} tools checked, {bad} failing")
