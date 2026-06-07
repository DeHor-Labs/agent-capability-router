#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "agent-opportunity-scout"

FORBIDDEN_IN_MAIN = [
    "Claude",
    "Codex",
    "/goal",
    "/loop",
    "/schedule",
    "Workflow tool",
    "suggest-power-tools",
    "Claude Power Tools",
]

FORBIDDEN_STALE = [
    "suggest-power-tools",
    "Claude Power Tools",
]


def scan_file(path: Path, forbidden: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    hits = []
    for term in forbidden:
        if term in text:
            hits.append(term)
    return hits


def main() -> None:
    skill_md = SKILL_DIR / "SKILL.md"
    hits = scan_file(skill_md, FORBIDDEN_IN_MAIN)
    if hits:
        print(f"FAIL: SKILL.md has runtime-coupled terms: {hits}", file=sys.stderr)
        sys.exit(1)

    for path in (SKILL_DIR / "references").glob("*.md"):
        if path.name == "runtime-adapters.md":
            continue
        hits = scan_file(path, FORBIDDEN_STALE)
        if hits:
            print(f"FAIL: {path.relative_to(ROOT)} has stale upstream terms: {hits}", file=sys.stderr)
            sys.exit(1)

    print("OK: main skill is runtime-neutral")


if __name__ == "__main__":
    main()
