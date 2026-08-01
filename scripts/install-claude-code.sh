#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${1:-.claude/commands}"

mkdir -p "$TARGET_DIR"
cp "$ROOT/packages/claude-code/commands/make-goal.md" "$TARGET_DIR/make-goal.md"
cp "$ROOT/packages/claude-code/commands/make-goal.zh-CN.md" "$TARGET_DIR/make-goal.zh-CN.md"

echo "Installed Claude Code make-goal commands into $TARGET_DIR"

