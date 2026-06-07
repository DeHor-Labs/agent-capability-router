# Runtime Adapters

Use capabilities first, runtime commands second. If a runtime does not expose a capability, offer the closest safe fallback and say what cannot be automated.

| Capability | Claude Code | Codex | Fallback |
|---|---|---|---|
| Local tools | Shell commands, file reads, git, project CLIs | Shell commands, file reads, git, project CLIs | Ask for the local command or inspect repo docs |
| Plugins/connectors | MCP/app tools when configured | MCP/app tools discovered in the active tools/plugins surface | Use CLI/API/browser only when safer and authorized |
| Skills | Claude-style skill folder | Codex skill folder and skill metadata | Portable `SKILL.md` directory |
| Orchestration | Workflow, Task, or subagents when available | Subagents, planning tools, or bounded local delegation when available | Phase 0 plan plus manual execution |
| Browser/local app proof | Browser automation available to the runtime | Browser or configured local browser route | Screenshot/manual instructions with caveat |
| Docs/current research | Web/docs tools when available | Web/docs tools when available | Ask user for source content or mark uncertainty |
| Completion goal | Goal command when user can invoke it | Goal tool only when tool instructions and explicit user approval allow it | Verifier checklist with commands |
| Recurring work | Loop or schedule command when available | Automation or reminder tools when available; discover the official tool first | Draft reminder text or checklist |
| Skill install | `~/.claude/skills` | `~/.codex/skills` | User-provided skill directory |
| Hook automation | Runtime settings hooks | Runtime-specific hooks or automations if exposed | Do not pretend support; propose memory or checklist instead |
| Effort calibration | Model, mode, and subagent choices available to that runtime | Model, reasoning, subagent, and validation choices available to that runtime | State the tradeoff and proceed locally |
| Verification | Tests, review, browser, CI, or service checks available to the runtime | Tests, review, browser, CI, or service checks available to the runtime | Explicit checklist and residual risk |

## Adapter Rules

- Never invent a command. If you do not know the runtime-specific surface, ask, inspect available tools, or give a generic proposal.
- Do not activate a high-cost capability from a router proposal unless the user has explicitly authorized it or the active instructions already authorize that class of action.
- Preserve runtime safety rules. For example, if a tool says goal creation requires explicit user request, draft the goal condition instead of creating it.
- Prefer copy installation for users and symlink installation for local development.
- If both Codex and Claude are active consumers, keep the skill directory name and `name:` frontmatter identical.
