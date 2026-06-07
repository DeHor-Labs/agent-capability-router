# Agent Leverage Toolkit

Runtime-neutral skills that help AI coding agents notice when a task deserves a higher-leverage execution pattern.

The first included skill is `agent-opportunity-scout`. It watches substantive work for shapes that users often do not name directly: parallel orchestration, verifier-friendly completion goals, recurring checks, reusable skill capture, deterministic hooks, decision or memory logging, and effort recalibration.

This project is a cleaned and runtime-neutral derivative of Matt Hulme's `claude-power-tools`, published under the MIT license.

## Why this exists

Good agents have force multipliers, but users should not need to know every command or runtime-specific feature name before they benefit from them. The scout turns task shape into a concise proposal:

- what capability fits
- why it fits now
- what it would cost
- what should still require explicit approval

The skill is intentionally conservative. It should not nag, stack proposals, invent unsupported runtime actions, or treat enthusiasm as permission.

## Included skill

```text
skills/
  agent-opportunity-scout/
    SKILL.md
    agents/openai.yaml
    references/
```

## Install

Install into both Codex and Claude skill folders:

```bash
./scripts/install-skill.sh --runtime both --mode copy
```

Install only for Codex:

```bash
./scripts/install-skill.sh --runtime codex
```

Install only for Claude:

```bash
./scripts/install-skill.sh --runtime claude
```

For local development, use symlinks:

```bash
./scripts/install-skill.sh --runtime both --mode symlink
```

The default destinations are:

- Codex: `~/.codex/skills/agent-opportunity-scout`
- Claude: `~/.claude/skills/agent-opportunity-scout`

Existing installs are moved to a timestamped backup before a copy or symlink is written.

## Validate

Run all local checks:

```bash
./scripts/validate-skill.py
./scripts/check-agent-neutrality.py
```

Optional Python test runner:

```bash
python3 -m unittest discover -s tests
```

## Attribution

This repository includes adapted material from:

- `Matt-Hulme/claude-power-tools`
- original skill: `suggest-power-tools`
- license: MIT

See `NOTICE.md` and `LICENSE`.
