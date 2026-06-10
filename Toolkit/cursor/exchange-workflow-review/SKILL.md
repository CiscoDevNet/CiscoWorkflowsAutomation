---
name: exchange-workflow-review
description: Review exported Cisco workflow JSON against the internal workflow review standard, enumerate the export first, and produce severity-ranked findings plus remediation suggestions and an overall readiness assessment.
---

# Exchange Workflow Review

## When to use

- The user provides a workflow export JSON file.
- The user wants Exchange review, standards validation, or approval-readiness feedback.
- The user wants findings aligned to the internal workflow review standard.

## Start here prompts

- Review this workflow export.
- Review this file against the internal review standard.
- Review this export and include remediation suggestions.

## Inputs to collect

- Workflow export JSON path

## Required flow

1. Use the packaged internal review standard when available. Fall back to the repo-root `WorkflowReviewChecklist.md` only for team development overrides.
2. Resolve the real skill directory and the repo root from this skill's file location. Do not assume the current working directory is the repo.
3. Run the shared CLI first to review the export and establish scope:
   - The review flow should enumerate first and return remediation suggestions in the first pass.
   ```bash
   PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review prepare-review "/path/to/workflow.json" --json
   ```
4. Present the enumeration list before deeper review.
5. Review one workflow at a time across all 7 checklist categories.
6. Lead with findings ordered by severity, then finish with the overall assessment, top improvements, and remediation suggestions.

## Review rules

- Do not skip embedded subworkflows.
- Prefer user-facing names over raw internal IDs.
- Use `reference.md` for the local review sequence and severity guidance.
- Keep the internal review standard as the source of truth if there is any conflict.

## Output sections

- Enumeration
- Critical issues
- High priority issues
- Medium priority issues
- Low priority issues
- Workflow-by-workflow notes
- Overall assessment
