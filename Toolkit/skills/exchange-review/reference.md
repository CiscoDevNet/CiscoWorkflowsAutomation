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

## Reporting rules

- Use user-facing labels whenever possible.
- Avoid raw internal IDs in reviewer-facing comments.
- For each issue include:
  - location
  - problem
  - recommended fix
  - severity
- Reviews are incomplete until embedded workflows are covered too.

## Severity guidance

- `High`: correctness, hidden failure, security, or likely approval blocker
- `Medium`: meaningfully important but not a blocker
- `Low`: cleanup, readability, consistency, and maintainability

## Review output shape

Suggested sections:

- Enumeration
- Critical issues
- High priority issues
- Medium priority issues
- Low priority issues
- Workflow-by-workflow notes
- Overall assessment
- Remediation suggestions

Example summary shape:

```markdown
## Exchange Review Results

### Enumeration
- Workflow 1: Parent Workflow
- Workflow 2: Embedded Workflow

### High priority issues
- Activity "Submit API Request" does not surface failure details in the workflow outputs.

### Low priority issues
- The main workflow description is too thin for Exchange reviewers.

### Workflow-by-workflow notes
#### Parent Workflow
- Logic & Flow: Add explicit success and failure output updates.

#### Embedded Workflow
- Essential Hygiene & Security: Replace a real org ID default with a placeholder.

### Overall assessment
- Score: 7/10
- Approval readiness: approve with suggestions

### Remediation suggestions
- Improve output handling.
- Remove production-like defaults.
- Strengthen reviewer-facing descriptions.
```

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
