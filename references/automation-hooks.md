# Automation Hook Routing

## Action Policy

Propose, then use the runtime-specific configuration path only after explicit approval. Hooks are sharp because they run deterministically, often without judgment.

## The Key Distinction

Memory and preferences influence an agent when it is invoked. A hook or automation runs because the harness or runtime fires it. When the user expects something to happen every time, storing it as memory is not enough.

## Recognition

- Explicit: "from now on", "always run X after Y", "whenever I do Y, also do Z".
- Implicit: the same manual ritual repeats after the same trigger.
- Friction: "why do I always need to remind you to..." or "I keep having to..."

## Stay Quiet When

- The behavior needs judgment per occurrence.
- It happened once.
- The hook could mutate files, spend money, or send external messages without a safe guardrail.
- The runtime has no hook mechanism and no safe fallback.

## Proposal Template

```text
This is hook-shaped: [trigger] -> [action]. A hook would make the runtime do it every time. Caveat: it would also fire on [annoying or risky edge case]. Want me to configure it?
```
