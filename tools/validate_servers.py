#!/usr/bin/env python3
"""Validate every JSON example in this repository.

Three families are checked:
- Any .json file must parse as JSON.
- Host config files (recognised by a top level mcpServers or
  servers key) must give every server a command, and command and
  .py args must be absolute paths (the rule Lesson 15 teaches).
- server.json manifests (recognised by a packages key plus a
  namespaced name) must carry the registry fields Lesson 22
  teaches: name, description (100 chars or fewer), version, and
  packages with registryType, identifier, and transport.
Exits nonzero on any failure, so CI can gate on it.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def iter_json():
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for name in sorted(files):
            if name.endswith(".json"):
                yield os.path.join(dirpath, name)


def check(path, data):
    errors = []
    if isinstance(data, dict) and ("mcpServers" in data or "servers" in data):
        key = "mcpServers" if "mcpServers" in data else "servers"
        for name, cfg in data[key].items():
            if "command" not in cfg:
                errors.append(f"{name}: no command")
            elif not str(cfg["command"]).startswith("/"):
                errors.append(f"{name}: command is not an absolute path")
            for arg in cfg.get("args", []):
                if str(arg).endswith(".py") and not str(arg).startswith("/"):
                    errors.append(f"{name}: script arg is not absolute: {arg}")
    if isinstance(data, dict) and "packages" in data and "name" in data:
        for field in ["name", "description", "version", "packages"]:
            if field not in data:
                errors.append(f"manifest missing {field}")
        if "/" not in str(data.get("name", "")):
            errors.append("manifest name is not namespaced")
        if len(str(data.get("description", ""))) > 100:
            errors.append("manifest description over 100 chars")
        for pkg in data.get("packages", []):
            for field in ["registryType", "identifier", "transport"]:
                if field not in pkg:
                    errors.append(f"manifest package missing {field}")
    return errors


def main():
    total, bad = 0, 0
    for path in iter_json():
        total += 1
        rel = os.path.relpath(path, ROOT)
        try:
            with open(path) as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            bad += 1
            print(f"FAIL {rel}: does not parse: {exc}")
            continue
        errors = check(path, data)
        if errors:
            bad += 1
            for e in errors:
                print(f"FAIL {rel}: {e}")
        else:
            print(f"OK   {rel}")
    print(f"\n{total} JSON files checked, {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
