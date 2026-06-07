# Capability Map

Use this when the user asks "what should we use?", when several agent surfaces could apply, or when the task would benefit from an explicit route before execution.

## Core Rule

Pick the smallest capability that changes the outcome. More machinery is only better when it reduces risk, improves evidence, saves repeated effort, or lets independent work run in parallel.

## Routing Matrix

| Need | Prefer | Why |
|---|---|---|
| Known local command, file search, git state, tests | Local shell/tools | Fast, inspectable, low overhead |
| Specialized procedural knowledge | Skill | Keeps behavior consistent without external calls |
| Current external service state or account operation | Plugin/connector/MCP | Uses the service's real API/context |
| Many independent slices | Subagents/workflow | Parallelism and independent judgment |
| Visual/local browser proof | Browser tool | Confirms rendered state, layout, interaction |
| Current docs or niche API behavior | Docs/web research | Reduces stale model assumptions |
| Repeated future action | Automation/schedule/hook | Removes manual babysitting |
| Long mission with drift risk | Completion goal/checklist | Makes "done" visible |
| High-risk claim or code change | Verification route | Converts confidence into evidence |

## Proposal Shape

```text
Route: [capability]. Why: [signals]. Cost/risk: [brief]. Approval needed: [yes/no and why]. Evidence I will produce: [check].
```

## Quiet Mode

Stay quiet and just use the route when it is obvious, low-risk, and already allowed: searching files, reading docs in a repo, running a standard test, or using a skill explicitly named by the user.
