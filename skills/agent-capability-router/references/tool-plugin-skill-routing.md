# Tool, Plugin, And Skill Routing

## Local Tools

Use local tools first for facts that live in the workspace: file contents, git state, tests, builds, logs, generated artifacts, and deterministic transformations.

Prefer local tools when:

- The answer is in files or command output.
- The task needs a concrete artifact or patch.
- Network state is irrelevant.
- A standard command can prove the result.

## Skills

Use a skill when the task needs reusable procedural knowledge: workflows, domain rules, file-format handling, project conventions, or stable tool sequences.

Prefer skills when:

- The user names a skill.
- The task clearly matches a skill description.
- The same non-obvious procedure would otherwise be rebuilt from scratch.

## Plugins, Connectors, And MCP Tools

Use plugins/connectors when the task depends on current state inside a service, account-specific context, API-backed operations, deployment platforms, payments, databases, design tools, or app-specific actions.

Before using one:

- Confirm the plugin/tool is actually available in the current runtime.
- Prefer official/service tools over browser scraping.
- Treat writes, sends, deploys, purchases, and public publication as approval-gated unless already authorized.

## Shell Versus Connector

Use shell/CLI when the repo already provides a trusted local command. Use connector/API when authentication, account state, or service-native metadata matters.

Example: run local tests through shell; inspect a hosted deployment through the platform connector if available; fall back to browser proof when the user needs visual/public confirmation.
