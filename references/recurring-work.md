# Recurring Work Routing

## Action Policy

Propose the smallest recurring or deferred mechanism that matches the need. Use runtime-specific automation only after confirming the runtime supports it and the user opts in.

## Recognition

- Polling external state: CI, deploys, queues, background jobs, long exports.
- Deferred one-shots: "remind me tomorrow", "check after launch", "follow up next week".
- Recurring chores: weekly audits, morning log checks, PR babysitting, release status scans.
- User language: "let me know when", "check back", "keep watching", "schedule this".

## Choose The Shape

- Session-local polling: use when the open session has needed context and the work ends soon.
- Durable automation: use when the task should run after this session, on a clock, or after a date.
- Plain checklist: use when the need is really just two or three immediate repeats.

## Stay Quiet When

- The tool or background process already notifies on completion.
- A completion goal fits better than recurring polling.
- The recurring need would require judgment that the automation cannot safely provide.

## Proposal Template

```text
This is babysitting work: [state being watched]. The safe shape is [session loop | durable schedule | checklist]. Cost/risk: [note]. Want me to set it up or just keep it manual?
```
