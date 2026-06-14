# Cursor Wrappers

This directory contains thin Cursor wrappers for the public toolkit.

The wrappers intentionally delegate deterministic work to the shared CLI in `../cli/` and keep only the agent-facing orchestration in `SKILL.md`.

## Position in the toolkit

These wrappers are a secondary convenience layer. They are not the canonical install path and they are not the source of truth for the toolkit. For VS Code and Cursor, prefer the MCP setup in `../mcp/` first when you want the toolkit available in all workspaces.

## Install

From the repository root:

```bash
bash Toolkit/cursor/install_cursor_skills.sh
```

This installs the public `exchange-review` and `exchange-remediation` skills into `~/.cursor/skills`.

## Included wrappers

- `exchange-review`
- `exchange-remediation`

## When to use this

Use these wrappers when you want skill-style prompting in Cursor after the MCP path is already available or when you specifically want a lightweight prompt wrapper around the shared CLI.

## Design rule

If a change can live in the CLI, it should live in the CLI. The Cursor wrappers should stay focused on:

- collecting inputs
- choosing the right CLI calls
- presenting the result in a reviewer-friendly format
