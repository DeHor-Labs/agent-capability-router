# Research, Browser, And Docs Routing

## Browser

Use browser capability when the task needs rendered proof, clicking, typing, screenshots, local app inspection, or visual/interaction validation.

Prefer the user's configured local-browser path for `localhost`, `127.0.0.1`, and `file://` targets when present. Record the fallback reason if a different browser automation route is used.

## Docs Lookup

Use docs lookup or web research when:

- The user asks for latest/current behavior.
- The library, API, product, law, price, schedule, or platform feature may have changed.
- A specific external page, paper, dataset, or docs URL is referenced.
- Stale model knowledge would materially change the answer.

For technical questions, prefer primary sources: official docs, source repos, standards, or papers.

## Web Research

Use web research for current public facts, recommendations involving spend/time, market information, public repo/profile visibility, and source-backed comparisons.

## Proposal Shape

```text
This needs current/rendered evidence. Route: [browser | docs | web]. I will verify [exact thing] and report links/screenshots/commands.
```

## Stay Quiet When

- The answer is already in the local repo.
- The user explicitly says not to browse.
- Browser use would only decorate a result that can be proven by tests or local output.
