from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def load_json_file(path: Path) -> tuple[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Workflow export not found: {path}")
    if not path.is_file():
        raise ValueError(f"Workflow export is not a file: {path}")

    text = path.read_text(encoding="utf-8")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    return text, data


def iter_workflows(node: Any, path: list[Any] | None = None) -> list[dict[str, Any]]:
    if path is None:
        path = []

    workflows: list[dict[str, Any]] = []

    if isinstance(node, dict):
        if node.get("object_type") == "definition_workflow":
            workflows.append({"path": list(path), "workflow": node})

        for key, value in node.items():
            workflows.extend(iter_workflows(value, [*path, key]))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            workflows.extend(iter_workflows(value, [*path, index]))

    return workflows


def is_simple_identifier(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value))


def format_path(path: list[Any]) -> str:
    result = "$"
    for part in path:
        if isinstance(part, int):
            result += f"[{part}]"
        elif is_simple_identifier(part):
            result += f".{part}"
        else:
            escaped = str(part).replace("\\", "\\\\").replace('"', '\\"')
            result += f'["{escaped}"]'
    return result


def find_start_line(text_lines: list[str], unique_name: str | None) -> int | None:
    if not unique_name:
        return None

    needle = f'"unique_name": "{unique_name}"'
    for index, line in enumerate(text_lines, start=1):
        if needle in line:
            return index
    return None


def classify_workflows(workflows: list[dict[str, Any]]) -> None:
    parent_assigned = False

    for item in workflows:
        path = item["path"]
        if path == ["workflow"] and not parent_assigned:
            item["workflow_type"] = "parent"
            parent_assigned = True
        else:
            item["workflow_type"] = "embedded"

    if not parent_assigned and workflows:
        workflows[0]["workflow_type"] = "parent"


def enrich_line_ranges(text: str, workflows: list[dict[str, Any]]) -> None:
    text_lines = text.splitlines()
    total_lines = len(text_lines)

    for item in workflows:
        workflow = item["workflow"]
        item["start_line"] = find_start_line(text_lines, workflow.get("unique_name"))
        item["end_line"] = None

    indexed = sorted(
        (
            (item["start_line"], index)
            for index, item in enumerate(workflows)
            if item["start_line"] is not None
        ),
        key=lambda pair: pair[0],
    )

    for position, (_, index) in enumerate(indexed):
        next_start = indexed[position + 1][0] if position + 1 < len(indexed) else None
        workflows[index]["end_line"] = (next_start - 1) if next_start else total_lines


def summarize_workflows(workflows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []

    for item in workflows:
        workflow = item["workflow"]
        properties = workflow.get("properties", {})
        name = (
            workflow.get("title")
            or properties.get("display_name")
            or workflow.get("name")
            or workflow.get("unique_name")
            or "Unnamed Workflow"
        )
        summary.append(
            {
                "name": name,
                "unique_name": workflow.get("unique_name"),
                "workflow_type": item["workflow_type"],
                "path": format_path(item["path"]),
                "start_line": item["start_line"],
                "end_line": item["end_line"],
            }
        )

    return summary


def enumerate_workflows(path: str | Path) -> dict[str, Any]:
    workflow_path = Path(path).expanduser().resolve()
    text, data = load_json_file(workflow_path)
    workflows = iter_workflows(data)
    if not workflows:
        raise ValueError("No definition_workflow objects found in the supplied JSON export.")

    classify_workflows(workflows)
    enrich_line_ranges(text, workflows)
    summary = summarize_workflows(workflows)
    parent_count = sum(1 for item in summary if item["workflow_type"] == "parent")
    embedded_count = sum(1 for item in summary if item["workflow_type"] == "embedded")

    return {
        "file": str(workflow_path),
        "workflow_count": len(summary),
        "parent_count": parent_count,
        "embedded_count": embedded_count,
        "workflows": summary,
    }


def render_enumeration_text(result: dict[str, Any]) -> str:
    lines = [
        "## Workflow Enumeration",
        f"File: {result['file']}",
        (
            f"Count: {result['workflow_count']} workflows found "
            f"({result['parent_count']} parent + {result['embedded_count']} embedded)"
        ),
        "",
    ]

    for index, item in enumerate(result["workflows"], start=1):
        if item["start_line"] and item["end_line"]:
            line_range = f"L{item['start_line']}-L{item['end_line']}"
        else:
            line_range = "unavailable"

        lines.extend(
            [
                f"{index}. {item['name']}",
                f"   Type: {item['workflow_type']}",
                f"   Unique name: {item['unique_name'] or 'missing'}",
                f"   Path: {item['path']}",
                f"   Line range: {line_range}",
                "",
            ]
        )

    return "\n".join(lines).rstrip()
