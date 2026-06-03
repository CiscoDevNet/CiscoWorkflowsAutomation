# Cursor Review Wrapper Reference

Use this wrapper with the shared CLI in `Toolkit/cli/`.

## Minimum command set

```bash
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

## Reminder

- Enumerate first.
- Review parent workflow first.
- Cover all embedded workflows.
- Lead with findings.
- Keep the root `WorkflowReviewChecklist.md` canonical.
