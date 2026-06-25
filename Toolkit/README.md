# Workflow Toolkit

This toolkit turns the internal workflow review standard into reusable review and remediation paths for the team.

`WorkflowReviewChecklist.md` at the repository root is the canonical review contract. The CLI ships a packaged fallback copy for installed environments, but everything in `Toolkit/` should reference the root checklist first so the source of truth stays in one place.

## Who It Is For

### Cursor and Codex users

Start with `Toolkit/skills/` for the primary install path. The public skills are the recommended agent integration right now, and they delegate deterministic work to the shared CLI.

### Other LLM users

Use `Toolkit/skills/README.md` for prompt patterns and workflow shape, then run the CLI in `Toolkit/cli/` for deterministic enumeration, review preparation, and remediation planning.

### External contributors

Start with:

1. `WorkflowReviewChecklist.md`
2. `Toolkit/skills/README.md`
3. `Toolkit/cli/README.md`

That path does not require Cursor or Codex.

## Layout

```text
Toolkit/
├── README.md
├── cli/            # Layer 1: shared Python CLI and core helpers
└── skills/         # Layer 2: thin shared skills for Cursor and Codex
```

The canonical checklist itself lives at `WorkflowReviewChecklist.md` in the repository root.

## Layering

- Layer 1: the CLI is the shared core for enumeration, checklist resolution, review preparation with remediation suggestions, and remediation planning.
- Layer 2: the public skills stay thin and delegate deterministic work to the CLI.

## Quick Start

### Install the skills for Cursor

```bash
bash Toolkit/skills/install_cursor_skills.sh
```

### Install the skills for Codex

```bash
bash Toolkit/skills/install_codex_skills.sh
```

### Review a workflow export with the CLI

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH=src python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

The current public toolkit intentionally stops at the skill layer. The CLI remains the stable backend so the team can gather practical feedback before deciding whether another integration layer is worth adding on top.

## Scope

This public toolkit intentionally focuses on shareable workflow review and remediation content. Internal Jira/reporting skills and local scratch exports should remain outside this repo unless they are scrubbed and clearly reusable.
