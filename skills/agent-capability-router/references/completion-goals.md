# Completion Goal Routing

## Action Policy

Draft a verifier-friendly completion condition. Create or activate a runtime goal only when the active runtime supports it and the user has explicitly requested or approved it. Otherwise, hand over the condition as a checklist or command.

## Recognition

- Multi-turn missions where the finish line can drift.
- "Keep going until..." or "do not stop until..." phrasing.
- Test/build/debug loops that need a clear exit condition.
- Long unattended work where the transcript must prove completion.

## Condition Craft

Write conditions that can be verified from visible evidence:

- Good: "`python3 -m unittest discover -s tests` exits 0 and the final checklist has no open items."
- Good: "Each endpoint in `docs/api-audit.md` has exactly one verdict: pass, fail, or not applicable."
- Bad: "The code is correct."
- Bad: "Everything is done."

If the success condition cannot be made visible, ask one clarifying question: "What output would prove this is done?"

## Stay Quiet When

- The task is short enough to finish in the current turn.
- The user is actively steering every step.
- The desired state is vague and cannot yet be verified.
- Another active goal already governs the session.

## Proposal Template

```text
This is completion-goal shaped because [drift risk]. Verifiable condition: [condition]. Want me to use that as the finish line, or should I tweak it?
```
