# Workflow Review MCP

This directory documents the primary stdio MCP path for the public toolkit.

The MCP server is intentionally thin. It wraps the same core package used by the CLI instead of re-implementing workflow review logic.

## Recommended path

For VS Code and Cursor, this is the primary integration surface. MCP is the recommended default because it can be configured once at the user level and then used across all workspaces.

## Current tools

- `review`
- `load_checklist`
- `plan_remediation`
- `inspect_export` (advanced helper, optional)

These tools are read-only planning helpers in the first public slice.

## Run the stdio server

```bash
workflow-review-mcp
```

## One-time install

For the easiest setup, run:

```bash
bash Toolkit/mcp/install_mcp.sh
```

That installs the package and prints the exact `workflow-review-mcp` path you can use in Cursor, VS Code, or any stdio MCP client.

## Start here

Use one of these simple prompts to kick off the review:

- "Review this workflow export."
- "Review this export and tell me what needs improvement."
- "Review this file against the internal review standard."
- "Review this export and include remediation suggestions."

### Cursor

Use `review` as the starting action. Cursor will enumerate the export first, then return findings and remediation suggestions. Prefer this MCP path over workspace-local skill wrappers when you want the toolkit available everywhere.

See `cursor.example.json`. It includes both:

- an installed-package configuration that uses `workflow-review-mcp`
- a dev-only fallback that still uses `python3 -m workflow_review.mcp_server`

### VS Code

If your MCP client supports stdio servers, use the installed command directly and start with `review`:

```json
{
  "mcpServers": {
    "cisco-workflow-review": {
      "command": "/path/to/installed/workflow-review-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

If your VS Code setup uses a different Python environment, point `command` at that environment’s installed `workflow-review-mcp` binary instead. The install helper prints the exact path for you.

### Generic MCP client

Any stdio-capable MCP client can use the same installed binary and start with `review`:

```json
{
  "mcpServers": {
    "cisco-workflow-review": {
      "command": "workflow-review-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

If the command is not on `PATH`, replace it with the full path to the installed script.

## Design intent

- User-level editor integration first
- Local stdio transport first
- Shared core with the CLI
- Narrow tools with explicit scope
- No file-writing remediation in the initial public scaffold
