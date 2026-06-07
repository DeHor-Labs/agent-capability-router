# Effort Calibration Routing

## Action Policy

Split effort levers into agent-controlled and user-controlled.

- Agent-controlled: act directly and mention it briefly when useful.
- User-controlled: propose the exact toggle or preference change and ask.

## Agent-Controlled Levers

- Delegation shape: local work, one sidecar, parallel agents, or adversarial review.
- Verification depth: smoke check, focused test, full suite, independent re-derivation.
- Search breadth: direct lookup, repo-wide search, multi-source research.
- Implementation style: quick patch, conservative refactor, or architecture pass.

## User-Controlled Levers

- Session model or effort mode.
- Budget directives.
- Long-running goal or automation setup.
- External spend, deployment, publication, or broad write permissions.

## Recognition

Underkill:

- Auth, payment, migration, concurrency, security, release, or public API changes getting a casual skim.
- User language: "make sure", "audit", "this has to be right", "thoroughly".

Overkill:

- Premium reasoning spent on mechanical renames, simple lint fixes, or one-line docs.
- User language: "quick", "rough", "do not overthink", "just get it working".

## Stay Quiet When

- The current effort already matches the mistake cost.
- The user explicitly chose the effort for this turn and the choice is not dangerous.

## Proposal Template

```text
Effort note: [mismatch]. Worth switching [exact user-controlled lever] for this stretch? It buys [benefit] and costs [cost].
```
