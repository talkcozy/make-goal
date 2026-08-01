#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${CODEX_HOME:-$HOME/.codex}/skills/make-goal"

mkdir -p "$(dirname "$TARGET")"

if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo "make-goal already exists at $TARGET"
  echo "Remove it first if you want to reinstall."
  exit 1
fi

ln -s "$ROOT/packages/codex/skills/make-goal" "$TARGET"
echo "Installed make-goal Codex skill at $TARGET"

