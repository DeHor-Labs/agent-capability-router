#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "agent-capability-router"
SKILL_DIR = ROOT / "skills" / SKILL_NAME
SKILL_MD = SKILL_DIR / "SKILL.md"

EXPECTED_REFS = {
    "references/capability-map.md",
    "references/tool-plugin-skill-routing.md",
    "references/orchestration.md",
    "references/research-browser-docs.md",
    "references/completion-goals.md",
    "references/recurring-work.md",
    "references/skill-capture.md",
    "references/automation-hooks.md",
    "references/decision-memory.md",
    "references/effort-calibration.md",
    "references/verification-routing.md",
    "references/runtime-adapters.md",
}

KNOWN_ROUTES = {
    "none",
    "orchestration",
    "tool-plugin-skill-routing",
    "research-browser-docs",
    "completion-goals",
    "recurring-work",
    "automation-hooks",
    "skill-capture",
    "decision-memory",
    "effort-calibration",
    "verification-routing",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    fields = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    if not SKILL_DIR.is_dir():
        fail(f"Missing skill directory: {SKILL_DIR}")
    if not SKILL_MD.is_file():
        fail("Missing SKILL.md")

    text = SKILL_MD.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)

    if fields.get("name") != SKILL_NAME:
        fail(f"Frontmatter name must be {SKILL_NAME}")
    description = fields.get("description", "")
    if len(description) < 80:
        fail("Frontmatter description is too short for reliable triggering")
    if "ANY" in description or "any substantive" in description.lower():
        fail("Frontmatter description is too broad")

    line_count = len(text.splitlines())
    if line_count > 180:
        fail(f"SKILL.md is too long for the main context: {line_count} lines")

    linked_refs = set(re.findall(r"`(references/[^`]+\.md)`", text))
    missing_links = EXPECTED_REFS - linked_refs
    if missing_links:
        fail(f"SKILL.md does not link expected refs: {sorted(missing_links)}")

    for ref in EXPECTED_REFS:
        path = SKILL_DIR / ref
        if not path.is_file():
            fail(f"Missing reference: {ref}")
        if len(path.read_text(encoding="utf-8").splitlines()) > 220:
            fail(f"Reference is too long: {ref}")

    openai_yaml = SKILL_DIR / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        fail("Missing agents/openai.yaml")
    yaml_text = openai_yaml.read_text(encoding="utf-8")
    if "$agent-capability-router" not in yaml_text:
        fail("agents/openai.yaml default prompt must mention $agent-capability-router")

    for script in ("install-skill.sh", "validate-skill.py", "check-agent-neutrality.py", "route-task.py"):
        if not (ROOT / "scripts" / script).is_file():
            fail(f"Missing script: scripts/{script}")

    fixture_dir = ROOT / "tests" / "fixtures"
    if not fixture_dir.is_dir():
        fail("Missing tests/fixtures")
    for fixture in fixture_dir.glob("*.md"):
        fixture_text = fixture.read_text(encoding="utf-8")
        expected_lines = [line for line in fixture_text.splitlines() if line.startswith("Expected route: ")]
        if len(expected_lines) != 1:
            fail(f"Fixture must declare exactly one Expected route: {fixture.name}")
        route = expected_lines[0].removeprefix("Expected route: ").strip()
        if route not in KNOWN_ROUTES:
            fail(f"Unknown route in {fixture.name}: {route}")

    print("OK: skill structure is valid")


if __name__ == "__main__":
    main()
