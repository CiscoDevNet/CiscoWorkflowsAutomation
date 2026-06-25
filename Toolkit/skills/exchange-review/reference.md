# Exchange Review Wrapper Reference

Use this wrapper with the shared CLI in `Toolkit/cli/`.

## Minimum command set

```bash
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```

## Common review asks

- Review this workflow export:
  Run the standard review flow and return findings by severity.
- Review this export and include remediation suggestions:
  Return findings plus next-step fixes in the same pass.
- Review this file against the internal review standard:
  Use the canonical checklist as the source of truth and keep the output aligned to that standard.

## What the review always includes

- enumeration before deeper analysis
- parent workflow review first
- embedded subworkflow coverage
- findings ordered by severity
- overall assessment at the end

## How to choose quickly

- Start with the standard review when you need approval-readiness feedback.
- Ask for remediation suggestions in the same pass when you already expect follow-up fixes.
- Emphasize embedded workflow coverage when the export contains multiple workflows and you want the scope made explicit up front.

## Reminder

- Enumerate first.
- Review parent workflow first.
- Cover all embedded workflows.
- Lead with findings.
- Include remediation suggestions in the first pass output.
- Keep `WorkflowReviewChecklist.md` at the repository root canonical, with the packaged checklist as the fallback for installed environments.
