from __future__ import annotations

import json
import sys
from typing import Any

from workflow_review.checklist import resolve_checklist_path
from workflow_review.enumerate import enumerate_workflows
from workflow_review.remediation import list_remediation_modes, list_safety_modes, plan_remediation
from workflow_review.review import prepare_review


PROTOCOL_VERSION = "2024-11-05"

CAPABILITIES = {
    "tools": {"listChanged": False},
    "resources": {"subscribe": False, "listChanged": False},
    "prompts": {"listChanged": False},
}


TOOLS = [
    {
        "name": "inspect_export",
        "description": "Advanced helper that lists the parent workflow and any embedded subworkflows in a JSON export.",
        "inputSchema": {
            "type": "object",
            "required": ["workflow_path"],
            "properties": {
                "workflow_path": {"type": "string"},
            },
        },
    },
    {
        "name": "load_checklist",
        "description": "Resolve and load the internal review standard used by the workflow review toolkit.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "checklist_path": {"type": "string"},
            },
        },
    },
    {
        "name": "review",
        "description": "Review a workflow export end to end: enumerate workflows first, then return the review brief that leads into findings, severity, and remediation suggestions.",
        "inputSchema": {
            "type": "object",
            "required": ["workflow_path"],
            "properties": {
                "workflow_path": {"type": "string"},
                "checklist_path": {"type": "string"},
                "priority_focus": {"type": "string"},
                "severity_threshold": {"type": "string"},
            },
        },
    },
    {
        "name": "plan_remediation",
        "description": "Prepare a remediation plan without writing to disk.",
        "inputSchema": {
            "type": "object",
            "required": ["workflow_path", "mode", "safety"],
            "properties": {
                "workflow_path": {"type": "string"},
                "mode": {"type": "string", "enum": sorted(list_remediation_modes())},
                "safety": {"type": "string", "enum": sorted(list_safety_modes())},
                "findings_path": {"type": "string"},
                "priority_focus": {"type": "string"},
            },
        },
    },
]


def _write_message(message: dict[str, Any]) -> None:
    payload = json.dumps(message).encode("utf-8")
    sys.stdout.write(f"Content-Length: {len(payload)}\r\n\r\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()


def _read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line == b"\r\n":
            break
        name, value = line.decode("utf-8").split(":", 1)
        headers[name.strip().lower()] = value.strip()

    content_length = int(headers.get("content-length", "0"))
    if content_length <= 0:
        return None

    payload = sys.stdin.buffer.read(content_length)
    return json.loads(payload.decode("utf-8"))


def _result_content(payload: Any) -> dict[str, Any]:
    return {
        "content": [{"type": "text", "text": json.dumps(payload, indent=2)}],
        "structuredContent": payload,
    }


def _handle_tool_call(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name == "inspect_export":
        return _result_content(enumerate_workflows(arguments["workflow_path"]))
    if name == "load_checklist":
        checklist_path = resolve_checklist_path(arguments.get("checklist_path"))
        return _result_content(
            {
                "checklist_path": str(checklist_path),
                "description": "Internal review standard used by the workflow review toolkit.",
            }
        )
    if name == "review":
        return _result_content(
            prepare_review(
                workflow_path=arguments["workflow_path"],
                checklist_path=arguments.get("checklist_path"),
                priority_focus=arguments.get("priority_focus"),
                severity_threshold=arguments.get("severity_threshold"),
            )
        )
    if name == "plan_remediation":
        return _result_content(
            plan_remediation(
                workflow_path=arguments["workflow_path"],
                remediation_mode=arguments["mode"],
                safety_mode=arguments["safety"],
                findings_path=arguments.get("findings_path"),
                priority_focus=arguments.get("priority_focus"),
            )
        )
    raise ValueError(f"Unknown tool: {name}")


def _success(message_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def _error(message_id: Any, code: int, text: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": code, "message": text},
    }


def handle_message(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    message_id = message.get("id")
    params = message.get("params", {})

    if method == "initialize":
        return _success(
            message_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "serverInfo": {"name": "cisco-workflow-review", "version": "0.1.0"},
                "capabilities": CAPABILITIES,
            },
        )

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return _success(message_id, {"tools": TOOLS})

    if method == "resources/list":
        return _success(message_id, {"resources": []})

    if method == "resources/templates/list":
        return _success(message_id, {"resourceTemplates": []})

    if method == "prompts/list":
        return _success(message_id, {"prompts": []})

    if method == "tools/call":
        try:
            result = _handle_tool_call(params["name"], params.get("arguments", {}))
            return _success(message_id, result)
        except Exception as exc:  # pragma: no cover - best-effort server path
            return _error(message_id, -32000, str(exc))

    if method == "ping":
        return _success(message_id, {})

    if message_id is not None:
        return _error(message_id, -32601, f"Unsupported method: {method}")
    return None


def main() -> int:
    while True:
        message = _read_message()
        if message is None:
            return 0
        response = handle_message(message)
        if response is not None:
            _write_message(response)


if __name__ == "__main__":
    raise SystemExit(main())
