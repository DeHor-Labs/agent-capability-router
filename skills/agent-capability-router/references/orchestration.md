# Orchestration Routing

## Action Policy

Propose by default. Act only when the user explicitly asks for subagents/workflows or a standing project instruction already authorizes that class of delegation. Broad orchestration spends real tokens and can touch many files, so the decision must be visible.

## Recognition

- Breadth: the same question or operation across many files, endpoints, repos, claims, or artifacts.
- Panel confidence: review, security, content critique, or product judgment where independent lenses materially increase trust.
- Adversarial verification: plausible findings, root causes, or deletion candidates that deserve a skeptic pass.
- Scale: migrations, renames, and audits that exceed one context window or would force shallow sampling.
- Research sweeps: multi-source questions where a single search mode is likely to miss evidence.
- User language: "systematically", "across the board", "audit", "weed out", "compare all", "use your team".

## Stay Quiet When

- The task is one file, one bug, one answer, or nearly done.
- Dependencies are strictly sequential and fan-out would mostly add coordination overhead.
- One or two local tool calls are enough.

## If You Propose

Use a compact block:

```text
This is a strong orchestration fit because [shape]. Pipeline: [phase 1] -> [phase 2] -> [phase 3]. Output: [durable artifact]. Cost: [rough number of agents / light|moderate|heavy]. Want me to launch it?
```

Name the durable artifact: report, harness, checklist, patch set, or decision list. Keep human-owned decisions explicit.

## If You Act

- Start with a short phase 0: fronts, owners, write scopes, expected outputs, and validation commands.
- Keep the main agent responsible for architecture, integration, product judgment, and final verification.
- Give delegated agents bounded tasks with disjoint write scopes.
- Tell coding agents they are not alone in the codebase and must not revert unrelated changes.
- Close completed agents when their output has been integrated and there is no immediate reuse.
