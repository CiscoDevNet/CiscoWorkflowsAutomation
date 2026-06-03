# Workflow Remediation Guide

Use this guide after a review has identified accepted findings to fix.

The remediation path in this public toolkit is intentionally conservative:

- review first
- scope fixes explicitly
- preserve workflow identity
- avoid rewrite-by-default
- stop before major structural edits unless the safety mode allows them

## Planning first

The initial public CLI prepares remediation plans without applying edits:

```bash
cd Toolkit/cli
PYTHONPATH=src python3 -m workflow_review plan-remediation "/path/to/workflow.json" \
  --mode fix-high-only \
  --safety ask-before-major-change \
  --json
```

That plan can then drive:

- a human review pass
- a Cursor skill invocation
- or a future automated remediation engine

## Modes

See `reference.md` for:

- remediation modes such as `fix-all` or `improve-workflow-description`
- safety modes such as `update-in-place` or `ask-before-major-change`
- the public definition of a major change

## Guardrails

- Patch existing workflows instead of regenerating them.
- Keep changes inside the approved remediation scope.
- Preserve `name`, `title`, `unique_name`, and core workflow intent unless explicitly approved otherwise.
- Re-review after edits and report fixed, remaining, and new issues.
