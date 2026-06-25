# Workflow Skills

This directory contains the public skill wrappers for the toolkit.

The skills intentionally delegate deterministic work to the shared CLI in `../cli/` and keep only the agent-facing orchestration in `SKILL.md`.

## Position in the toolkit

These skills are the primary agent-facing integration surface for the public toolkit right now. They are designed to work in both Cursor and Codex while sharing the same CLI-backed behavior.

## Install

From the repository root:

### Cursor

```bash
bash Toolkit/skills/install_cursor_skills.sh
```

This installs the public `exchange-review` and `exchange-remediation` skills into `~/.cursor/skills`.

### Codex

```bash
bash Toolkit/skills/install_codex_skills.sh
```

This installs the same public skills into `~/.codex/skills`.

## Skills At A Glance

| Skill | Purpose |
| --- | --- |
| `exchange-review` | Review a workflow export against the canonical checklist, enumerate parent and embedded workflows first, and return severity-ranked findings with an overall assessment. |
| `exchange-remediation` | Plan or apply scoped follow-up fixes after review, including severity-based cleanup and description-only improvement paths. |

## What Each Skill Does

### `exchange-review`

Use this when you want to understand the current state of a workflow export before changing it.

Example prompts:

- `Review this workflow export.`
- `Review this export and include remediation suggestions.`
- `Review this export workflow-by-workflow, and call out high-priority issues first.`

Review modes:

- `standard-review`: Run the default review flow and return findings by severity.
- `review-with-remediation-suggestions`: Return findings plus next-step fixes in the same pass.
- `workflow-by-workflow-review`: Make the scope explicit when the export contains embedded subworkflows.

What this skill always does:

- enumerates the parent workflow and embedded workflows first
- reviews against the canonical checklist
- returns findings in severity order
- includes an overall assessment

### `exchange-remediation`

Use this when you already know you want to act on findings instead of only reading review output.

Each remediation run combines:

- exactly one remediation mode
- exactly one safety mode

Example prompts:

- `Fix only the high-severity issues in this workflow export, but stop before major changes.`
- `Build a remediation proposal for high and medium issues first, without editing the original file.`
- `Improve only the main workflow description in this export, keep it under 1024 characters, and leave everything else unchanged.`
- `Improve workflow readability across the main workflow, activities, loops, groups, and variables, with no structural changes.`

Remediation modes:

Findings-based remediation modes:

- `fix-all`: Run the broadest remediation pass.
- `fix-high-and-medium`: Focus cleanup on the most meaningful issues without taking every low-priority polish item.
- `fix-high-only`: Address the most important risks first.
- `fix-low-only`: Target readability, hygiene, and minor cleanup without broader workflow changes.
- `proposal-only`: Produce a plan before any edits happen.

Description-focused remediation modes:

- `improve-workflow-readability`: Improve user-facing descriptions across the main workflow, activities, groups, loops, and variables without changing workflow logic.
- `improve-workflow-description`: Improve the main workflow description while leaving the rest of the workflow untouched.

Safety modes:

- `update-in-place`: Edit the source in place.
- `propose-copy`: Produce a side-by-side proposal without replacing the original.
- `ask-before-major-change`: Apply safe fixes but require approval before structural edits.

What this skill always does:

- enumerates the workflow scope before editing
- builds a remediation plan first
- keeps description edits within the 1024-character platform limit
- keeps workflow identity stable unless explicitly approved otherwise
- re-reviews after edits and reports fixed, remaining, and new issues

## Design rule

If a change can live in the CLI, it should live in the CLI. The skills should stay focused on:

- collecting inputs
- choosing the right CLI calls
- presenting the result in a reviewer-friendly format
