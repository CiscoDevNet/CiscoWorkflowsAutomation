# Exchange Remediation Reference

## Prerequisite

Use exchange review first unless you already have an approved findings list.

## Remediation modes

### `fix-all`
Apply all approved findings that fit the selected safety mode.

### `fix-high-and-medium`
Apply approved `High` and `Medium` findings.

### `fix-high-only`
Apply approved `High` findings only.

### `fix-low-only`
Apply low-risk cleanup and readability fixes only.

### `proposal-only`
Produce a concrete plan without editing files.

### `improve-activity-descriptions`
Improve activity titles and descriptions only. This must remain non-structural.

### `improve-workflow-description`
Improve only the main workflow description. This must remain non-structural.

## Safety modes

### `update-in-place`
Edit the current workflow file directly.

### `propose-copy`
Create a sibling proposed file and leave the original unchanged.

### `ask-before-major-change`
Apply safe fixes directly, but stop before structural changes.

## Major change definition

Treat the remediation as a major change when it would:

- add or remove branches
- add or remove outputs
- add or remove major logic blocks
- materially change target behavior
- materially change categories
- convert a non-atomic workflow into an atomic workflow
- redesign the workflow rather than patching it

## Non-negotiable guardrails

- No rewrite-by-default.
- Preserve workflow identity.
- Stay inside the selected remediation scope.
- Re-review after edits.

## Useful command

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review plan-remediation "/path/to/workflow.json" \
  --mode fix-high-only \
  --safety ask-before-major-change \
  --json
```
