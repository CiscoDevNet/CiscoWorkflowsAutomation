# Exchange Remediation Wrapper Reference

Use this wrapper with the shared CLI in `Toolkit/cli/`.

## Minimum command set

```bash
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review inspect-workflow-export "/path/to/workflow.json" --json
PYTHONPATH="<repo-root>/Toolkit/cli/src" python3 -m workflow_review plan-remediation "/path/to/workflow.json" --mode fix-high-only --safety ask-before-major-change --json
```

## Remediation modes

Each remediation run uses exactly one remediation mode and exactly one safety mode.

- `fix-all`:
  Apply all approved findings that are safe to fix now.
- `fix-high-and-medium`:
  Apply approved high and medium findings.
- `fix-high-only`:
  Apply only approved high-severity findings.
- `fix-low-only`:
  Apply low-risk cleanup and readability fixes only.
- `proposal-only`:
  Generate a remediation plan only and do not edit files.
- `improve-workflow-readability`:
  Improve user-facing descriptions across the main workflow, activities, groups, loops, and input/output variables where present. Keep description edits within the 1024-character platform limit.
- `improve-workflow-description`:
  Improve the main workflow description only. Keep the edited description within the 1024-character platform limit.

## Safety modes

- `update-in-place`:
  Edit the current file directly.
- `propose-copy`:
  Create a sibling proposed file and keep the original unchanged.
- `ask-before-major-change`:
  Apply safe fixes, but stop before structural changes.

## How to choose quickly

- Pick `fix-high-only` when you want the fastest risk-reduction pass.
- Pick `fix-high-and-medium` when you want a stronger cleanup pass without chasing every low-priority item.
- Pick `fix-low-only` when you want low-risk polish and readability improvements.
- Pick `proposal-only` when you want a plan before any edits happen.
- Pick `improve-workflow-readability` when you want text-only cleanup across the workflow without structural changes.
- Pick `improve-workflow-description` when you want to tighten only the main workflow description.
- Pair broad remediation modes with `ask-before-major-change` when you want human approval before bigger workflow changes.

## Key rules

- Reuse approved findings when possible.
- Stay inside the chosen remediation scope.
- Treat branch, output, target, and category changes as potentially major.
- Re-review after edits.
- Keep `WorkflowReviewChecklist.md` at the repository root as the canonical source for the checklist, with the packaged copy as the installed fallback.
