#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CLI_DIR="$REPO_ROOT/Toolkit/cli"

printf 'Installing workflow review MCP package...\n'
python3 -m pip install -e "$CLI_DIR"

SCRIPT_PATH="$(python3 - <<'PY'
import site
from pathlib import Path

user_base = Path(site.getuserbase())
print(user_base / "bin" / "workflow-review-mcp")
PY
)"

cat <<EOF

Install complete.

Use this command in Cursor, VS Code, or any stdio MCP client:
  ${SCRIPT_PATH}

If that directory is not on PATH, either add it or point your MCP client at the full path above.

Suggested first prompt:
  Review this workflow export.
EOF
