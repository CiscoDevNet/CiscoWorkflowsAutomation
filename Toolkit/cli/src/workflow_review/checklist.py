from __future__ import annotations

import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from importlib import resources


CHECKLIST_ENV_VAR = "WORKFLOW_REVIEW_CHECKLIST"
CHECKLIST_FILENAME = "WorkflowReviewChecklist.md"
PACKAGE_CHECKLIST_RESOURCE = "data/WorkflowReviewChecklist.md"
_PACKAGED_CHECKLIST_PATH: Path | None = None


def _candidate_repo_roots() -> list[Path]:
    current = Path(__file__).resolve()
    return list(current.parents)


def resolve_checklist_path(explicit_path: str | None = None) -> Path:
    candidates: list[Path] = []

    if explicit_path:
        candidates.append(Path(explicit_path).expanduser().resolve())

    env_value = os.getenv(CHECKLIST_ENV_VAR)
    if env_value:
        candidates.append(Path(env_value).expanduser().resolve())

    for parent in _candidate_repo_roots():
        candidates.append(parent / CHECKLIST_FILENAME)

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate

    package_resource = resources.files("workflow_review").joinpath(PACKAGE_CHECKLIST_RESOURCE)
    if package_resource.is_file():
        return _materialize_packaged_checklist(package_resource)

    searched = ", ".join(str(path) for path in candidates[:5])
    raise FileNotFoundError(
        f"Could not resolve {CHECKLIST_FILENAME}. Checked explicit path, "
        f"{CHECKLIST_ENV_VAR}, and repo-relative candidates such as: {searched}"
    )


def read_checklist(explicit_path: str | None = None) -> tuple[Path, str]:
    checklist_path = resolve_checklist_path(explicit_path=explicit_path)
    return checklist_path, checklist_path.read_text(encoding="utf-8")


def _materialize_packaged_checklist(package_resource: resources.abc.Traversable) -> Path:
    global _PACKAGED_CHECKLIST_PATH
    if _PACKAGED_CHECKLIST_PATH and _PACKAGED_CHECKLIST_PATH.exists():
        return _PACKAGED_CHECKLIST_PATH

    with resources.as_file(package_resource) as checklist_path:
        source_path = Path(checklist_path)
        with NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as handle:
            handle.write(source_path.read_text(encoding="utf-8"))
            _PACKAGED_CHECKLIST_PATH = Path(handle.name)

    return _PACKAGED_CHECKLIST_PATH
