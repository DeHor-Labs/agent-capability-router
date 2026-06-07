# Agent Capability Router

Runtime-neutral skill that helps AI coding agents choose the right capability for the task: local tools, plugins/connectors, skills, subagents, browser/docs lookup, completion goals, automations, hooks, and verification depth.

The included skill is `agent-capability-router`. It watches work for routing signals that users often do not name directly: "use your team", "open the local app", "which plugin handles this?", "keep going until tests pass", "remember this workflow", "make sure this is safe", or "check this every week".

This project is a cleaned and runtime-neutral derivative of Matt Hulme's `claude-power-tools`, published under the MIT license.

## Why this exists

Good agents have force multipliers, but users should not need to know every command, plugin, connector, skill, or runtime-specific feature name before they benefit from them. The router turns task shape into a concise route:

- what capability fits
- why it fits now
- what it would cost
- what should still require explicit approval
- what evidence will prove the route worked

The skill is intentionally conservative. It should not nag, stack proposals, invent unsupported runtime actions, or treat enthusiasm as permission. For proactive routing, it requires strong signals instead of firing on every "maybe this could be better" moment.

## Included skill

```text
skills/
  agent-capability-router/
    SKILL.md
    agents/openai.yaml
    references/
```

## What it routes

- Local shell/tools for workspace facts, tests, builds, git state, and deterministic edits
- Plugins/connectors/MCP tools for service-backed account state and native operations
- Skills for reusable procedural knowledge and stable workflows
- Subagents/workflows for parallel slices, independent review, and whole-repo sweeps
- Browser/docs/research for visual proof, current docs, and live/public state
- Completion goals and checklists for long missions with drift risk
- Automations/hooks for repeated future behavior, with explicit approval boundaries
- Verification routes matched to the mistake cost

## Install

Install into both Codex and Claude skill folders:

```bash
./scripts/install-skill.sh --runtime both --mode copy --confirm
```

Install only for Codex:

```bash
./scripts/install-skill.sh --runtime codex --confirm
```

Install only for Claude:

```bash
./scripts/install-skill.sh --runtime claude --confirm
```

For local development, use symlinks:

```bash
./scripts/install-skill.sh --runtime both --mode symlink --dev-symlink --confirm
```

The default destinations are:

- Codex: `~/.codex/skills/agent-capability-router`
- Claude: `~/.claude/skills/agent-capability-router`

Existing installs are not replaced unless `--replace` is passed. When replacement is allowed, the previous install is moved to a timestamped backup under the target skills directory.

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

Preview a route classification:

```bash
./scripts/route-task.py "Audit all API routes with your team and verify CI findings"
```

## Attribution

This repository includes adapted material from:

- `Matt-Hulme/claude-power-tools`
- original skill: `suggest-power-tools`
- license: MIT

See `NOTICE.md` and `LICENSE`.
