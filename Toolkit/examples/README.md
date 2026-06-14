# Toolkit Examples

This directory shows how the public toolkit is intended to be used without requiring a private repo or internal-only tooling.

## Review example

From `Toolkit/cli`:

```bash
PYTHONPATH=src python3 -m workflow_review inspect-workflow-export "../../Meraki/CheckAvailableFirmwareForNetwork__definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF/definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF.json"
PYTHONPATH=src python3 -m workflow_review prepare-review "../../Meraki/CheckAvailableFirmwareForNetwork__definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF/definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF.json" --json
```

## Remediation planning example

```bash
PYTHONPATH=src python3 -m workflow_review plan-remediation "../../Meraki/CheckAvailableFirmwareForNetwork__definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF/definition_workflow_02M30GYJJSYJL0wQPPnkQgIcavBkG6796mF.json" \
  --mode fix-low-only \
  --safety ask-before-major-change \
  --json
```

## Sample output

See `review-output.md` for the intended structure of a reviewer-facing summary. The actual review contract lives in `WorkflowReviewChecklist.md` at the repository root.
