# Repository tools

- `validate_servers.py`: checks every JSON file in the repo
  (parses; host configs carry absolute commands and paths;
  server.json manifests carry the registry fields). CI runs it
  on every push.
- `check_links.py`: checks that relative Markdown links resolve
  to files on disk. Run it before a release; external URLs are
  reviewed by humans, not by this script.

Run either from anywhere: `python3 tools/validate_servers.py`.
