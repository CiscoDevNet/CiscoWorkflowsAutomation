from __future__ import annotations

from pathlib import Path
from typing import Any

from workflow_review.checklist import resolve_checklist_path
from workflow_review.enumerate import enumerate_workflows


def prepare_review(
    workflow_path: str,
    checklist_path: str | None = None,
    priority_focus: str | None = None,
    severity_threshold: str | None = None,
) -> dict[str, Any]:
    workflow_path = str(Path(workflow_path).expanduser().resolve())
    enumeration = enumerate_workflows(workflow_path)

    resolved_checklist = None
    checklist_error = None
    try:
        resolved_checklist = str(resolve_checklist_path(checklist_path))
    except FileNotFoundError as exc:
        checklist_error = str(exc)

    return {
        "workflow_path": workflow_path,
        "checklist_path": resolved_checklist,
        "checklist_error": checklist_error,
        "priority_focus": priority_focus,
        "severity_threshold": severity_threshold,
        "enumeration": enumeration,
        "review_contract": {
            "sequence": [
                "Enumerate all workflows before review.",
                "Review the parent workflow first.",
                "Review each embedded workflow across all 7 checklist categories.",
                "Lead with findings ordered by severity.",
                "Finish with an overall assessment and next steps.",
            ],
            "categories": [
                "Inputs & Parameters",
                "Targets & Target Groups",
                "Atomics & API Usage",
                "Groups & Categories",
                "Logic & Flow",
                "Error Handling",
                "Essential Hygiene & Security",
            ],
        },
    }
