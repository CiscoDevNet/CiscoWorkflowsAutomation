# Exchange Review Guide

Use this guide when you want to review a workflow export against the canonical workflow review standard.

## Source of truth

`WorkflowReviewChecklist.md` at the repository root is the canonical review contract. The CLI also ships a packaged copy for installed environments, but this repo should reference the root checklist first.

## Start here prompts

- Review this workflow export.
- Review this file against the internal review standard.
- Review this export and include remediation suggestions.

The recommended flow is:

1. Enumerate the workflow scope first.
2. Review the parent workflow.
3. Review each embedded workflow.
4. Aggregate findings by severity.
5. End with an approval-readiness summary, next actions, and remediation suggestions.

## CLI-first path

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH=src python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

The `prepare-review` output is intentionally structured so it can be handed to another LLM or used by a thin skill wrapper.

## Manual/LLM path

If you are using another LLM directly:

1. Use `WorkflowReviewChecklist.md` from the repository root.
2. Attach the workflow JSON export.
3. Use the reference in `reference.md` to keep the review sequence and output format consistent.

## Expectations

- Do not skip embedded subworkflows.
- Keep the canonical review standard as the source of truth.
- Lead with findings, sorted by severity.
- Include remediation suggestions in the first review output.
- Use user-facing names instead of raw internal IDs whenever possible.
