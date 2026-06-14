# Workflow Toolkit

This toolkit turns the internal workflow review standard into reusable review and remediation paths for the team.

`WorkflowReviewChecklist.md` at the repository root is the canonical review contract. The CLI ships a packaged fallback copy for installed environments, but everything in `Toolkit/` should reference the root checklist first so the source of truth stays in one place.

## Who It Is For

### VS Code and Cursor users

Start with `Toolkit/mcp/` for the primary cross-workspace install path. The MCP server is the recommended integration for VS Code and Cursor because one user-level configuration can make it available in every workspace.

Use `Toolkit/cursor/` only if you also want optional thin skill wrappers that call the shared CLI.

### Other LLM users

Use `Toolkit/exchange-review/` and `Toolkit/exchange-remediation/` as copyable playbooks, then run the CLI in `Toolkit/cli/` for deterministic enumeration and checklist resolution.

### External contributors

Start with:

1. `WorkflowReviewChecklist.md`
2. `Toolkit/exchange-review/README.md`
3. `Toolkit/cli/README.md`

That path does not require Cursor.

## Layout

```text
Toolkit/
├── README.md
├── cli/            # Layer 1: shared Python CLI and core helpers
├── mcp/            # Layer 2: primary stdio MCP integration for editors
├── cursor/         # Layer 3: optional thin Cursor skill wrappers
├── examples/       # Example commands and sample output
├── exchange-remediation/ # Public remediation guidance and mode reference
└── exchange-review/      # Public review guidance and checklist companion
```

## Layering

- Layer 1: the CLI is the shared core for enumeration, checklist resolution, review preparation with remediation suggestions, and remediation planning.
- Layer 2: the MCP server wraps the same core instead of re-implementing logic and is the recommended editor integration.
- Layer 3: Cursor skills stay thin, optional, and delegate deterministic work to the CLI.

## Quick Start

### Review a workflow export with the CLI

```bash
cd Toolkit/cli
python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

### Install the workflow review MCP

```bash
bash Toolkit/mcp/install_mcp.sh
```

This is the recommended setup for VS Code and Cursor because it is configured at the user level rather than tied to a single workspace.

### Install the optional Cursor wrappers

```bash
bash Toolkit/cursor/install_cursor_skills.sh
```

### Run the stdio MCP scaffold

```bash
cd Toolkit/cli
python3 -m workflow_review.mcp_server
```

For installed-client usage, see `Toolkit/mcp/README.md` for Cursor, VS Code, and generic stdio MCP examples that point at `workflow-review-mcp` directly and start with `review`; `inspect_export` is available as an advanced helper. Treat `Toolkit/cursor/` as an optional convenience layer rather than the primary install surface.

## Scope

This public toolkit intentionally focuses on shareable workflow review and remediation content. Internal Jira/reporting skills and local scratch exports should remain outside this repo unless they are scrubbed and clearly reusable.
