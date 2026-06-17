# Exchange Remediation Wrapper Reference

Use this wrapper with the shared CLI in `Toolkit/cli/`.

## Minimum command set

```bash
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json" --json
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review plan-remediation "/path/to/workflow.json" --mode fix-high-only --safety ask-before-major-change --json
```

## Key rules

- Reuse approved findings when possible.
- Stay inside the chosen remediation scope.
- Treat branch, output, target, and category changes as potentially major.
- Re-review after edits.
- Keep `WorkflowReviewChecklist.md` at the repository root as the canonical source for the checklist, with the packaged copy as the installed fallback.
