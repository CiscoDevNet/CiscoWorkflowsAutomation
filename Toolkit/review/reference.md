# Workflow Review Reference

## Source of truth

The canonical review standard is the root-level `WorkflowReviewChecklist.md` in this repository.

Use that file whenever it is available. This reference is the lightweight companion for tools and wrappers in `Toolkit/`.

## Mandatory sequence

1. Enumerate all workflows in the export first.
2. Present the parent workflow and every embedded workflow before deeper review.
3. Review one workflow at a time across all 7 checklist categories.
4. Lead with findings ordered by severity.
5. End with an overall assessment and next actions.

## Checklist categories

1. Inputs & Parameters
2. Targets & Target Groups
3. Atomics & API Usage
4. Groups & Categories
5. Logic & Flow
6. Error Handling
7. Essential Hygiene & Security

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

## Useful commands

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json"
PYTHONPATH=src python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
```
