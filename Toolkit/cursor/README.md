# Cursor Wrappers

This directory contains thin Cursor wrappers for the public toolkit.

The wrappers intentionally delegate deterministic work to the shared CLI in `../cli/` and keep only the agent-facing orchestration in `SKILL.md`.

## Install

From the repository root:

```bash
bash Toolkit/cursor/install_cursor_skills.sh
```

This installs the public `exchange-review` and `exchange-remediation` skills into `~/.cursor/skills`.

## Included wrappers

- `exchange-review`
- `exchange-remediation`

## Design rule

If a change can live in the CLI, it should live in the CLI. The Cursor wrappers should stay focused on:

- collecting inputs
- choosing the right CLI calls
- presenting the result in a reviewer-friendly format
