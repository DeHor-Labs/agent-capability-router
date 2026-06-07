#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="agent-opportunity-scout"
RUNTIME="both"
MODE="copy"
DRY_RUN="0"
HOME_DIR="${HOME:-}"

usage() {
  cat <<'EOF'
Usage: scripts/install-skill.sh [options]

Options:
  --runtime codex|claude|both   Target runtime. Default: both.
  --mode copy|symlink           Install mode. Default: copy.
  --home PATH                   Home directory override for tests.
  --dry-run                     Print actions without writing.
  -h, --help                    Show this help.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --runtime)
      RUNTIME="${2:-}"
      shift 2
      ;;
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --home)
      HOME_DIR="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN="1"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$RUNTIME" in
  codex|claude|both) ;;
  *)
    echo "--runtime must be codex, claude, or both" >&2
    exit 2
    ;;
esac

case "$MODE" in
  copy|symlink) ;;
  *)
    echo "--mode must be copy or symlink" >&2
    exit 2
    ;;
esac

if [ -z "$HOME_DIR" ]; then
  echo "HOME is not set; pass --home PATH" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILL_SRC="$ROOT_DIR/skills/$SKILL_NAME"

if [ ! -d "$SKILL_SRC" ]; then
  echo "Skill source not found: $SKILL_SRC" >&2
  exit 1
fi

timestamp() {
  date +"%Y%m%d%H%M%S"
}

install_one() {
  local label="$1"
  local base="$2"
  local dest="$base/$SKILL_NAME"
  local stamp
  stamp="$(timestamp)"

  if [ "$DRY_RUN" = "1" ]; then
    echo "Would install $SKILL_NAME for $label at $dest using $MODE"
    return 0
  fi

  mkdir -p "$base"

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    local backup="$dest.backup.$stamp"
    mv "$dest" "$backup"
    echo "Backed up existing $label install to $backup"
  fi

  if [ "$MODE" = "symlink" ]; then
    ln -s "$SKILL_SRC" "$dest"
  else
    cp -R "$SKILL_SRC" "$dest"
  fi

  echo "Installed $SKILL_NAME for $label at $dest"
}

if [ "$RUNTIME" = "codex" ] || [ "$RUNTIME" = "both" ]; then
  install_one "Codex" "$HOME_DIR/.codex/skills"
fi

if [ "$RUNTIME" = "claude" ] || [ "$RUNTIME" = "both" ]; then
  install_one "Claude" "$HOME_DIR/.claude/skills"
fi
