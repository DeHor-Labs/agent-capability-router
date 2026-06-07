---
name: agent-capability-router
description: "Route task shape to the right AI agent capability: local tools, plugins or connectors, skills, subagents, browser or docs lookup, completion goals, recurring automations, hooks, decision or memory logging, and verification depth. Use when a task has clear routing signals such as multi-file audits, explicit tool/plugin/skill questions, long completion loops, external-state checks, repeated procedures, runtime-specific capabilities, or requests for systematic, thorough, faster, or safer agent work."
---

# Agent Capability Router

Users think in terms of their work: "audit these modules", "open the local app", "which plugin should handle this?", "keep going until this passes", "we keep repeating this", "make sure this is right". The router translates task shape into the smallest useful capability path.

## Routing Protocol

1. Classify the task shape and risk.
2. Pick the minimum adequate capability: tool, plugin, skill, subagent, automation, browser/docs lookup, goal, or verification plan.
3. Check the active runtime before naming commands. Read `references/runtime-adapters.md` when the mapping is not obvious.
4. Act directly only for low-risk capability choices already allowed by the user and runtime instructions.
5. Propose for costly, persistent, external, broad, or high-autonomy actions. Include cost and approval boundary.
6. Verify the route worked with visible evidence.

## Guardrails

- Prefer quiet routing for simple tasks. Do not turn a one-file fix into a strategy meeting.
- For proactive proposals, require at least two strong signals such as breadth, risk, repetition, external state, runtime-specific tooling, or explicit user language.
- Make at most one recommendation per opportunity. If the user declines or ignores it, continue normally.
- Do not stack proposals. If several routes fit, choose the strongest path and mention optional follow-ups only when useful.
- Never invent tools, plugins, hooks, or commands. Inspect the available surface or give a safe fallback.
- In credential, personal-data, or sensitive-production contexts, prefer local/read-only checks unless the user asks for broader automation.

## Recognition Routing

When the current work matches a row, read the reference for recognition signals, action policy, and proposal shape.

| Task shape | Capability | Reference |
|---|---|---|
| User asks what capability to use; task spans tools, plugins, skills, or runtimes | Capability map | `references/capability-map.md` |
| Need to choose between local tools, plugin/connectors, skills, MCP/app tools, or raw shell | Tool/plugin/skill routing | `references/tool-plugin-skill-routing.md` |
| Same operation across many units; audits; adversarial verification; repo-wide sweeps; "systematically", "across the board", "weed out" | Orchestration | `references/orchestration.md` |
| Local app/browser inspection, current docs, web research, screenshots, or visual proof | Browser/docs/research | `references/research-browser-docs.md` |
| A multi-turn mission with a blurry finish line; "keep going until..." | Completion goal | `references/completion-goals.md` |
| Waiting, polling, reminders, recurring chores, deferred one-shots | Recurring work | `references/recurring-work.md` |
| A hard-won repeatable technique was just invented | Skill capture | `references/skill-capture.md` |
| "From now on..." or a repeated ritual that should happen every time | Automation hook | `references/automation-hooks.md` |
| A durable project or user operating principle crystallized | Decision or memory logging | `references/decision-memory.md` |
| Task gravity does not match model, budget, or verification depth | Effort calibration | `references/effort-calibration.md` |
| Claims need proof; code changed; reviews/scanners/CI must be triaged | Verification routing | `references/verification-routing.md` |

The strongest routes are often compositional: a skill plus a plugin, browser proof plus a verification checklist, or subagents plus a completion goal. Name the composition only when it helps the user decide.
