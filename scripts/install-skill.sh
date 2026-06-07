#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="agent-capability-router"
RUNTIME=""
MODE="copy"
DRY_RUN="0"
CONFIRM="0"
REPLACE="0"
DEV_SYMLINK="0"
HOME_DIR="${HOME:-}"

usage() {
  cat <<'EOF'
Usage: scripts/install-skill.sh [options]

Options:
  --runtime codex|claude|both   Target runtime. Required.
  --mode copy|symlink           Install mode. Default: copy.
  --home PATH                   Home directory override for tests.
  --dry-run                     Print actions without writing.
  --confirm                     Required for writes.
  --replace                     Replace an existing install after backup.
  --dev-symlink                 Allow --mode symlink for local development.
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
    --confirm)
      CONFIRM="1"
      shift
      ;;
    --replace)
      REPLACE="1"
      shift
      ;;
    --dev-symlink)
      DEV_SYMLINK="1"
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

if [ -z "$RUNTIME" ]; then
  echo "--runtime is required; use codex, claude, or both" >&2
  exit 2
fi

case "$MODE" in
  copy|symlink) ;;
  *)
    echo "--mode must be copy or symlink" >&2
    exit 2
    ;;
esac

if [ "$DRY_RUN" != "1" ] && [ "$CONFIRM" != "1" ]; then
  echo "Refusing to write without --confirm. Use --dry-run to preview." >&2
  exit 2
fi

if [ "$MODE" = "symlink" ] && [ "$DEV_SYMLINK" != "1" ]; then
  echo "Symlink installs are development-only; pass --dev-symlink to allow them." >&2
  exit 2
fi

if [ -z "$HOME_DIR" ]; then
  echo "HOME is not set; pass --home PATH" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ ! -f "$ROOT_DIR/SKILL.md" ]; then
  echo "Skill source not found: $ROOT_DIR/SKILL.md" >&2
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
    if [ "$REPLACE" != "1" ]; then
      echo "Existing $label install found at $dest; pass --replace to back it up and replace it." >&2
      exit 1
    fi
    local backup_dir="$base/.agent-capability-router-backups"
    local backup="$backup_dir/$SKILL_NAME.$stamp"
    mkdir -p "$backup_dir"
    mv "$dest" "$backup"
    echo "Backed up existing $label install to $backup"
  fi

  if [ "$MODE" = "symlink" ]; then
    ln -s "$ROOT_DIR" "$dest"
  else
    mkdir -p "$dest/scripts"
    cp "$ROOT_DIR/SKILL.md" "$dest/SKILL.md"
    cp -R "$ROOT_DIR/agents" "$dest/agents"
    cp -R "$ROOT_DIR/references" "$dest/references"
    cp "$ROOT_DIR/scripts/route-task.py" "$dest/scripts/route-task.py"
  fi

  echo "Installed $SKILL_NAME for $label at $dest"
}

if [ "$RUNTIME" = "codex" ] || [ "$RUNTIME" = "both" ]; then
  install_one "Codex" "$HOME_DIR/.codex/skills"
fi

if [ "$RUNTIME" = "claude" ] || [ "$RUNTIME" = "both" ]; then
  install_one "Claude" "$HOME_DIR/.claude/skills"
fi
