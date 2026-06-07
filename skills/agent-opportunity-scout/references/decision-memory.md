# Decision And Memory Scout

## Action Policy

Propose a one-line entry and write it only when the user approves or explicitly asks to save it. Keep the entry small enough that it will be useful later.

## Recognition

- A general rule emerged from a specific debate.
- The user says "let's always", "never do this again", or "from now on" as an operating principle.
- A previously settled decision was deliberately reversed.
- The reasoning behind a tradeoff will not be recoverable from code or git history alone.

## Destination

- Project decision log: for product, architecture, policy, or tradeoff decisions inside a repo.
- Memory: for user preferences, cross-project operating rules, or agent behavior.
- Changelog or issue: for implementation history that belongs with the release surface.

## Stay Quiet When

- The fact already lives in code, tests, config, or git history.
- The statement is tentative.
- It matters only to the current message.

## Proposal Template

```text
That sounds durable enough to record. Draft: "[date] - [decision] - [reason]." Should I save it in [destination]?
```
