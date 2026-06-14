# Workflow Review CLI

This directory contains the Layer 1 core for the public toolkit.

The initial CLI focuses on deterministic tasks that are useful across Cursor, other LLMs, and MCP-capable clients:

- inspect a workflow export and list its parent and embedded workflows
- validate that an export can be parsed
- resolve the canonical checklist path
- prepare a structured review brief
- prepare a structured remediation plan

## Install

From this directory:

```bash
python3 -m pip install -e .
```

If you do not want to install the package, you can run it in-place:

```bash
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
```

## Commands

### Enumerate workflows

```bash
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json" --json
```

The legacy `enumerate` subcommand still works as an alias, but `inspect-workflow-export` is the clearer public-facing name.

### Validate exports

```bash
PYTHONPATH=src python3 -m workflow_review validate "/path/to/workflow.json"
```

### Resolve the checklist

```bash
PYTHONPATH=src python3 -m workflow_review checklist
PYTHONPATH=src python3 -m workflow_review checklist --show
```

When run from this repository, the CLI resolves `WorkflowReviewChecklist.md` at the repo root first. If the repo-root file is not available, it falls back to the packaged checklist that ships with the installed package.

### Prepare a review run

```bash
PYTHONPATH=src python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

### Prepare a remediation plan

```bash
PYTHONPATH=src python3 -m workflow_review plan-remediation "/path/to/workflow.json" \
  --mode fix-high-only \
  --safety ask-before-major-change \
  --json
```

## Checklist Resolution

The CLI resolves the checklist in this order:

1. `--checklist /path/to/file.md`
2. `WORKFLOW_REVIEW_CHECKLIST=/path/to/file.md`
3. the repo-root `WorkflowReviewChecklist.md`
4. the packaged internal review standard

That keeps the repository copy canonical while still allowing the team to point at another checklist during development or use the packaged fallback when installed elsewhere.

## MCP

The stdio MCP scaffold is implemented in the same package and exposed through:

```bash
workflow-review-mcp
```

For the easiest MCP setup, run `bash Toolkit/mcp/install_mcp.sh` from the repo root. It installs the package and prints the exact command path to use.

See `../mcp/README.md` for client configuration examples.
