# Workflow Review Guide

Use this guide when you want to review a workflow export against the canonical `WorkflowReviewChecklist.md`.

The recommended flow is:

1. Enumerate the workflow scope first.
2. Review the parent workflow.
3. Review each embedded workflow.
4. Aggregate findings by severity.
5. End with an approval-readiness summary and next actions.

## CLI-first path

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH=src python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

The `prepare-review` output is intentionally structured so it can be handed to another LLM or used by a thin Cursor or MCP wrapper.

## Manual/LLM path

If you are using another LLM directly:

1. Attach `WorkflowReviewChecklist.md`
2. Attach the workflow JSON export
3. Use the reference in `reference.md` to keep the review sequence and output format consistent

## Expectations

- Do not skip embedded subworkflows.
- Keep the public checklist as the source of truth.
- Lead with findings, sorted by severity.
- Use user-facing names instead of raw internal IDs whenever possible.
