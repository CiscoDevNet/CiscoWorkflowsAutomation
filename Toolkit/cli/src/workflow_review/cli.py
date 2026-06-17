from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from workflow_review.checklist import read_checklist, resolve_checklist_path
from workflow_review.enumerate import enumerate_workflows, render_enumeration_text
from workflow_review.remediation import (
    list_remediation_modes,
    list_safety_modes,
    plan_remediation,
)
from workflow_review.review import prepare_review


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Workflow review and remediation helpers for Cisco workflow exports."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser(
        "inspect-workflow-export",
        help="Inspect a workflow export and list the parent and embedded workflows it contains.",
    )
    inspect_parser.add_argument("workflow_json")
    inspect_parser.add_argument("--json", action="store_true", dest="json_output")

    enumerate_parser = subparsers.add_parser(
        "enumerate",
        help="Alias for inspect-workflow-export.",
    )
    enumerate_parser.add_argument("workflow_json")
    enumerate_parser.add_argument("--json", action="store_true", dest="json_output")

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate that a workflow export can be parsed and enumerated.",
    )
    validate_parser.add_argument("workflow_json")

    checklist_parser = subparsers.add_parser(
        "checklist",
        help="Resolve or show the canonical workflow review checklist.",
    )
    checklist_parser.add_argument("--checklist")
    checklist_parser.add_argument("--show", action="store_true")

    review_parser = subparsers.add_parser(
        "prepare-review",
        help="Prepare a structured review brief for a workflow export.",
    )
    review_parser.add_argument("workflow_json")
    review_parser.add_argument("--checklist")
    review_parser.add_argument("--priority-focus")
    review_parser.add_argument("--severity-threshold")
    review_parser.add_argument("--json", action="store_true", dest="json_output")

    remediation_parser = subparsers.add_parser(
        "plan-remediation",
        help="Prepare a structured remediation plan without applying edits.",
    )
    remediation_parser.add_argument("workflow_json")
    remediation_parser.add_argument("--mode", required=True, choices=sorted(list_remediation_modes()))
    remediation_parser.add_argument("--safety", required=True, choices=sorted(list_safety_modes()))
    remediation_parser.add_argument("--findings")
    remediation_parser.add_argument("--priority-focus")
    remediation_parser.add_argument("--json", action="store_true", dest="json_output")

    return parser


def _print_payload(payload: Any, json_output: bool) -> int:
    if json_output:
        print(json.dumps(payload, indent=2))
    elif isinstance(payload, str):
        print(payload)
    else:
        print(json.dumps(payload, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command in {"inspect-workflow-export", "enumerate"}:
            result = enumerate_workflows(args.workflow_json)
            if args.json_output:
                return _print_payload(result, json_output=True)
            return _print_payload(render_enumeration_text(result), json_output=False)

        if args.command == "validate":
            result = enumerate_workflows(args.workflow_json)
            print(
                f"Validated {result['workflow_count']} workflows in {result['file']}"
            )
            return 0

        if args.command == "checklist":
            checklist_path = resolve_checklist_path(args.checklist)
            if args.show:
                _, checklist_text = read_checklist(args.checklist)
                print(checklist_text)
            else:
                print(checklist_path)
            return 0

        if args.command == "prepare-review":
            result = prepare_review(
                workflow_path=args.workflow_json,
                checklist_path=args.checklist,
                priority_focus=args.priority_focus,
                severity_threshold=args.severity_threshold,
            )
            return _print_payload(result, json_output=args.json_output)

        if args.command == "plan-remediation":
            result = plan_remediation(
                workflow_path=args.workflow_json,
                remediation_mode=args.mode,
                safety_mode=args.safety,
                findings_path=args.findings,
                priority_focus=args.priority_focus,
            )
            return _print_payload(result, json_output=args.json_output)

    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    parser.print_help()
    return 1
