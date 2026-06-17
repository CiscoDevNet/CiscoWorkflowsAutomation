---
name: exchange-remediation
description: Apply approved workflow review fixes safely by building a remediation plan, honoring remediation and safety modes, and preserving workflow identity unless the user explicitly approves structural changes.
disable-model-invocation: true
---

# Exchange Remediation

## When to use

- The user wants to apply workflow review feedback instead of only reading findings.
- The user asks to fix checklist issues by severity.
- The user wants description-only cleanup or a guarded remediation plan.

## Inputs to collect

- Workflow export JSON path
- Remediation mode
- Safety mode
- Optional findings source
- Optional priority focus

## Required flow

1. Reuse an approved findings set when available. Otherwise run the review wrapper first.
2. Resolve the real skill directory and repo root from this skill's file location. Do not assume the current working directory is the repo.
3. Enumerate the workflow scope before editing:
   ```bash
   PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json" --json
   ```
4. Build the remediation plan first:
   ```bash
   PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review plan-remediation "/path/to/workflow.json" --mode fix-high-only --safety ask-before-major-change --json
   ```
5. Apply the selected safety mode exactly.
6. Re-review after edits and report fixed, remaining, and new issues.

## Guardrails

- No rewrite-by-default.
- Preserve `name`, `title`, `unique_name`, and core intent unless the user explicitly approves otherwise.
- Keep changes inside the selected remediation mode.
- Stop if JSON validity or post-edit review fails.
- Description-only modes must remain non-structural.

## Additional reference

Use `reference.md` for mode definitions and the major-change rules.
