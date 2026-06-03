# Workflow Toolkit

This toolkit turns the public workflow review checklist in this repository into reusable review and remediation paths for multiple audiences.

The canonical review contract remains the root-level `WorkflowReviewChecklist.md`. Everything in `Toolkit/` is designed to help contributors apply that checklist more consistently.

## Who It Is For

### Cursor and VS Code users

Use `Toolkit/cursor/` to install thin Cursor skill wrappers that call the shared CLI.

### Other LLM users

Use `Toolkit/review/` and `Toolkit/remediation/` as copyable playbooks, then run the CLI in `Toolkit/cli/` for deterministic enumeration and checklist resolution.

### External contributors

Start with:

1. `WorkflowReviewChecklist.md`
2. `Toolkit/review/README.md`
3. `Toolkit/cli/README.md`

That path does not require Cursor.

## Layout

```text
Toolkit/
├── README.md
├── cli/            # Layer 1: shared Python CLI and core helpers
├── cursor/         # Layer 2: thin Cursor skill wrappers
├── examples/       # Example commands and sample output
├── mcp/            # Layer 3: stdio MCP guidance
├── remediation/    # Public remediation guidance and mode reference
└── review/         # Public review guidance and checklist companion
```

## Layering

- Layer 1: the CLI is the shared core for enumeration, checklist resolution, review preparation, and remediation planning.
- Layer 2: Cursor skills stay thin and delegate deterministic work to the CLI.
- Layer 3: the MCP server wraps the same core instead of re-implementing logic.

## Quick Start

### Review a workflow export with the CLI

```bash
cd Toolkit/cli
python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

### Install the public Cursor wrappers

```bash
bash Toolkit/cursor/install_cursor_skills.sh
```

### Run the stdio MCP scaffold

```bash
cd Toolkit/cli
python3 -m workflow_review.mcp_server
```

## Scope

This public toolkit intentionally focuses on shareable workflow review and remediation content. Internal Jira/reporting skills and local scratch exports should remain outside this repo unless they are scrubbed and clearly reusable.
