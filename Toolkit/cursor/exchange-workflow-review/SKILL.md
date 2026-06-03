---
name: exchange-workflow-review
description: Review exported Cisco workflow JSON against the public Workflow Review Checklist, inspect the export to list parent and embedded subworkflows first, and produce severity-ranked findings plus an overall readiness assessment.
---

# Exchange Workflow Review

## When to use

- The user provides a workflow export JSON file.
- The user wants Exchange review, standards validation, or approval-readiness feedback.
- The user wants findings aligned to the public workflow review checklist.

## Inputs to collect

- Workflow export JSON path
- Optional priority focus: `Security`, `Performance`, or `Maintainability`
- Optional severity threshold: `Critical`, `High`, `Medium`, or `Low`

## Required flow

1. Use the canonical checklist at the repo root when available: `WorkflowReviewChecklist.md`.
2. Resolve the real skill directory and the repo root from this skill's file location. Do not assume the current working directory is the repo.
3. Run the shared CLI first to inspect the workflow export and establish review scope:
   ```bash
   PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
   ```
4. Prepare the review brief:
   ```bash
   PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
   ```
5. Present the enumeration list before deeper review.
6. Review one workflow at a time across all 7 checklist categories.
7. Lead with findings ordered by severity, then finish with the overall assessment and top improvements.

## Review rules

- Do not skip embedded subworkflows.
- Prefer user-facing names over raw internal IDs.
- Use `reference.md` for the local review sequence and severity guidance.
- Keep the checklist as the source of truth if there is any conflict.

## Output sections

- Enumeration
- Critical issues
- High priority issues
- Medium priority issues
- Low priority issues
- Workflow-by-workflow notes
- Overall assessment
