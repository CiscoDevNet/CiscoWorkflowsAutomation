# Workflow Review MCP

This directory documents the Layer 3 stdio MCP path for the public toolkit.

The MCP server is intentionally thin. It wraps the same core package used by the CLI instead of re-implementing workflow review logic.

## Current tools

- `workflow_inspect_export`
- `workflow_resolve_checklist`
- `workflow_prepare_review`
- `workflow_plan_remediation`

These tools are read-only planning helpers in the first public slice.

## Run the stdio server

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review.mcp_server
```

## Example Cursor MCP config

See `cursor.example.json`.

## Design intent

- Local stdio transport first
- Shared core with the CLI
- Narrow tools with explicit scope
- No file-writing remediation in the initial public scaffold
