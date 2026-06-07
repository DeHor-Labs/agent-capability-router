---
name: agent-opportunity-scout
description: "Proactively spot when an AI coding agent should propose higher-leverage execution patterns: parallel workflows, verifiable completion goals, recurring checks, reusable skill capture, automation hooks, decision or memory logging, or effort calibration. Use when a task has clear leverage signals such as multi-file audits, long completion loops, recurring checks, repeated procedures, automation policies, durable decisions, or explicit requests for systematic, thorough, or faster agent work."
---

# Agent Opportunity Scout

Users think in terms of their work: "audit these modules", "keep going until this passes", "we keep repeating this", "make sure this is right". The scout translates those task shapes into a small, honest proposal for a higher-leverage agent capability.

## Shared Etiquette

- Make at most one proposal per opportunity. If the user declines or ignores it, continue the task normally.
- Do not stack proposals. If several scouts fit, pick the strongest one.
- Propose at a natural seam, when the task shape is clear enough to sketch concretely.
- Be explicit about cost: setup time, token spend, risk, and maintenance burden.
- Do not treat enthusiasm as approval. Costly actions, broad automation, and external state changes need explicit confirmation unless the user already authorized that class of action.
- If the active runtime does not support a capability, propose the safest equivalent instead of pretending it exists.
- In credential, personal-data, or sensitive-production contexts, prefer a quiet local check unless the user asks for broader automation.

## Runtime First

Before suggesting a command or tool, identify the active runtime and read `references/runtime-adapters.md` if the mapping is not obvious. Prefer capability names in the main proposal and runtime-specific commands only in the final handoff.

## Recognition Routing

When the current work matches a row, read the reference for recognition signals, action policy, and proposal shape.

| Task shape | Capability | Reference |
|---|---|---|
| Same operation across many units; audits; adversarial verification; repo-wide sweeps; "systematically", "across the board", "weed out" | Orchestration | `references/orchestration.md` |
| A multi-turn mission with a blurry finish line; "keep going until..." | Completion goal | `references/completion-goals.md` |
| Waiting, polling, reminders, recurring chores, deferred one-shots | Recurring work | `references/recurring-work.md` |
| A hard-won repeatable technique was just invented | Skill capture | `references/skill-capture.md` |
| "From now on..." or a repeated ritual that should happen every time | Automation hook | `references/automation-hooks.md` |
| A durable project or user operating principle crystallized | Decision or memory logging | `references/decision-memory.md` |
| Task gravity does not match model, budget, or verification depth | Effort calibration | `references/effort-calibration.md` |

The strongest opportunities are often compositional, such as orchestration plus a verifier-friendly completion goal. Name the composition only when it helps the user decide.
