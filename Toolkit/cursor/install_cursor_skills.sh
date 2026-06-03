#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SKILLS_SRC_DIR="$REPO_ROOT/Toolkit/cursor"
CURSOR_SKILLS_DIR="${HOME}/.cursor/skills"

mkdir -p "$CURSOR_SKILLS_DIR"

installed=0

for skill_dir in "$SKILLS_SRC_DIR"/*; do
  [ -d "$skill_dir" ] || continue
  [ -f "$skill_dir/SKILL.md" ] || continue

  skill_name="$(basename "$skill_dir")"
  target_link="$CURSOR_SKILLS_DIR/$skill_name"

  if [ -L "$target_link" ] || [ -e "$target_link" ]; then
    rm -rf "$target_link"
  fi

  ln -s "$skill_dir" "$target_link"
  printf 'Installed skill: %s -> %s\n' "$skill_name" "$target_link"
  installed=$((installed + 1))
done

if [ "$installed" -eq 0 ]; then
  printf 'No skill directories with SKILL.md were found under %s\n' "$SKILLS_SRC_DIR" >&2
  exit 1
fi

printf '\nInstalled %d skill(s) into %s\n' "$installed" "$CURSOR_SKILLS_DIR"
