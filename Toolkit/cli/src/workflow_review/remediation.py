from __future__ import annotations

from pathlib import Path
from typing import Any

from workflow_review.enumerate import enumerate_workflows


REMEDIATION_MODES = {
    "fix-all": "Apply all approved findings that are safe to fix now.",
    "fix-high-and-medium": "Apply approved high and medium findings.",
    "fix-high-only": "Apply only approved high-severity findings.",
    "fix-low-only": "Apply low-risk cleanup and readability fixes only.",
    "proposal-only": "Plan the work without editing files.",
    "improve-workflow-readability": "Improve user-facing descriptions across the workflow without changing workflow logic.",
    "improve-workflow-description": "Improve the main workflow description only.",
}

SAFETY_MODES = {
    "update-in-place": "Edit the current file directly.",
    "propose-copy": "Create a sibling proposed file and keep the original unchanged.",
    "ask-before-major-change": "Apply safe fixes, but stop before structural changes.",
}

LOW_RISK_MODES = {
    "fix-low-only",
    "proposal-only",
    "improve-workflow-readability",
    "improve-workflow-description",
}


def list_remediation_modes() -> dict[str, str]:
    return dict(REMEDIATION_MODES)


def list_safety_modes() -> dict[str, str]:
    return dict(SAFETY_MODES)


def major_change_risk(remediation_mode: str) -> bool:
    return remediation_mode not in LOW_RISK_MODES


def plan_remediation(
    workflow_path: str,
    remediation_mode: str,
    safety_mode: str,
    findings_path: str | None = None,
    priority_focus: str | None = None,
) -> dict[str, Any]:
    if remediation_mode not in REMEDIATION_MODES:
        raise ValueError(f"Unsupported remediation mode: {remediation_mode}")
    if safety_mode not in SAFETY_MODES:
        raise ValueError(f"Unsupported safety mode: {safety_mode}")

    workflow_path = str(Path(workflow_path).expanduser().resolve())
    findings_path = (
        str(Path(findings_path).expanduser().resolve()) if findings_path else None
    )
    enumeration = enumerate_workflows(workflow_path)
    requires_major_change_review = major_change_risk(remediation_mode)

    if remediation_mode == "improve-workflow-readability":
        planned_fixes = [
            "Limit changes to user-facing readability improvements across workflow descriptions, activity descriptions, group and loop descriptions, and input/output variable descriptions where present.",
            "Keep each edited description within the platform length limit of 1024 characters.",
            "Preserve workflow logic, control flow, target behavior, categories, and output semantics.",
        ]
    elif remediation_mode == "improve-workflow-description":
        planned_fixes = [
            "Limit changes to the main workflow description only.",
            "Keep the edited workflow description within the platform length limit of 1024 characters.",
            "Preserve workflow logic, activity text, variables, outputs, categories, and targets.",
        ]
    elif remediation_mode == "proposal-only":
        planned_fixes = ["Generate a remediation plan only. No file edits should be applied."]
    else:
        planned_fixes = [
            "Review approved findings against the selected severity scope.",
            "Patch the current workflow incrementally rather than rewriting it.",
            "Re-run review after changes and report fixed, remaining, and new issues.",
        ]

    approval_required = safety_mode == "ask-before-major-change" and requires_major_change_review

    return {
        "workflow_path": workflow_path,
        "findings_path": findings_path,
        "priority_focus": priority_focus,
        "remediation_mode": remediation_mode,
        "remediation_mode_description": REMEDIATION_MODES[remediation_mode],
        "safety_mode": safety_mode,
        "safety_mode_description": SAFETY_MODES[safety_mode],
        "major_change_possible": requires_major_change_review,
        "approval_required": approval_required,
        "enumeration": enumeration,
        "planned_fixes": planned_fixes,
        "deferred": [
            "Do not apply unrelated cleanup outside the selected remediation scope.",
            "Do not change workflow identity fields unless explicitly approved.",
        ],
    }
