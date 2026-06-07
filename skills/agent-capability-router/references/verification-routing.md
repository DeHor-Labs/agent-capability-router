# Verification Routing

## Action Policy

Verification is not one thing. Match proof depth to mistake cost, and report the exact evidence.

## Routes

| Risk | Verification |
|---|---|
| Text/doc only | Read changed files, grep stale terms, validate links |
| Small code patch | Focused tests or typecheck touching the changed surface |
| Shared behavior | Broader unit/integration suite and regression review |
| UI change | Browser screenshot/interaction checks across relevant viewports |
| Security/auth/payments/data | Dedicated security review plus tests and config inspection |
| Public/deploy/store state | CLI/API/browser confirmation of live state |
| Review/scanner findings | Classify each as fixed, not applicable, or accepted backlog |

## Proposal Shape

```text
Verification route: [checks]. This matches the risk because [reason]. I will consider it done only when [visible evidence].
```

## Evidence Rules

- Prefer command output, links, screenshots, file paths, or exact checklist rows over vague confidence.
- Separate local truth, remote truth, CI truth, and runtime/public truth.
- If a check cannot be run, say why and name the residual risk.
