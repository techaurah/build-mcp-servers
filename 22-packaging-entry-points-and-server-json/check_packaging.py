"""Lesson 22: check server.json and the pyproject example."""
import json

def check_manifest(path="server.json"):
    with open(path) as f:
        m = json.load(f)
    problems = []
    for field in ["name", "description", "version", "packages"]:
        if field not in m:
            problems.append(f"missing {field}")
    if "name" in m and "/" not in m["name"]:
        problems.append("name is not namespaced (needs owner/name form)")
    if "description" in m and len(m["description"]) > 100:
        problems.append("description over 100 chars: registries truncate or reject")
    for pkg in m.get("packages", []):
        for field in ["registryType", "identifier", "transport"]:
            if field not in pkg:
                problems.append(f"package missing {field}")
    return problems

if __name__ == "__main__":
    problems = check_manifest()
    print("server.json:", "OK" if not problems else "FAIL " + "; ".join(problems))
    text = open("pyproject.toml").read()
    for needle in ["[project]", "requires-python", "[project.scripts]", "mcp[cli]"]:
        print(f"pyproject has {needle}:", needle in text)
