#!/usr/bin/env python3
import argparse
import json
import re
import sys


ROUTES = [
    {
        "route": "orchestration",
        "risk_class": "multi_agent_spend",
        "approval_required": True,
        "patterns": [
            ("explicit team", r"\b(use your team|with your team|multi.?agent|subagent|parallel)\b", 2),
            ("broad sweep", r"\b(across the board|audit all|whole repo|review all)\b", 1),
            ("systematic breadth", r"\b(systematic|sweep|fan.?out|many files|compare all)\b", 1),
        ],
    },
    {
        "route": "tool-plugin-skill-routing",
        "risk_class": "authenticated_read",
        "approval_required": True,
        "patterns": [
            ("explicit capability choice", r"\b(which plugin|which connector|which mcp|which tool|what should we use)\b", 2),
            ("named capability", r"\b(plugin|connector|mcp|skill)\b", 1),
            ("service surface", r"\b(Canva|Figma|GitHub|Netlify|Vercel|Supabase|Stripe|OpenAI)\b", 1),
        ],
    },
    {
        "route": "research-browser-docs",
        "risk_class": "public_web_or_browser_read",
        "approval_required": False,
        "patterns": [
            ("local browser target", r"\b(localhost|127\.0\.0\.1|file://)\b", 2),
            ("visual proof", r"\b(screenshot|browser|click|rendered|visual)\b", 1),
            ("current docs", r"\b(latest official docs|current official docs|official docs|documentation)\b", 2),
            ("web request", r"\b(browse the web|web research|search the web|public page|verify live)\b", 2),
        ],
    },
    {
        "route": "completion-goals",
        "risk_class": "session_control",
        "approval_required": True,
        "patterns": [
            ("explicit until", r"\b(keep going until|do not stop until|done when)\b", 2),
            ("pass condition", r"\b(until .* pass|tests pass|build is clean|finish line)\b", 1),
        ],
    },
    {
        "route": "recurring-work",
        "risk_class": "persistent_automation",
        "approval_required": True,
        "patterns": [
            ("recurrence", r"\b(remind|schedule|check back|every day|weekly|poll|watch)\b", 2),
            ("notify state", r"\b(let me know when|report only on state change)\b", 1),
        ],
    },
    {
        "route": "automation-hooks",
        "risk_class": "persistent_automation",
        "approval_required": True,
        "patterns": [
            ("every time policy", r"\b(from now on|always run|whenever|every time|hook)\b", 2),
        ],
    },
    {
        "route": "skill-capture",
        "risk_class": "local_write",
        "approval_required": True,
        "patterns": [
            ("explicit skill capture", r"\b(make this a skill|save this approach|remember this workflow|reusable technique)\b", 2),
        ],
    },
    {
        "route": "decision-memory",
        "risk_class": "memory_write",
        "approval_required": True,
        "patterns": [
            ("explicit memory", r"\b(decision log|save in memory|remember this preference)\b", 2),
            ("standing decision", r"\b(let's always|never do this again)\b", 1),
        ],
    },
    {
        "route": "effort-calibration",
        "risk_class": "session_effort",
        "approval_required": False,
        "patterns": [
            ("explicit effort", r"\b(thoroughly|quick pass|don't overthink|cheap model|faster)\b", 2),
            ("risk language", r"\b(high risk|security critical|payment|auth|migration)\b", 1),
        ],
    },
    {
        "route": "verification-routing",
        "risk_class": "local_validation",
        "approval_required": False,
        "patterns": [
            ("explicit verify", r"\b(verify|validate|prove)\b", 2),
            ("pipeline evidence", r"\b(tests|ci|checks|security review|scanner|review findings)\b", 1),
            ("merge gate", r"\b(before merge|before merging|merge gate)\b", 1),
        ],
    },
]


def classify(text: str) -> list[dict]:
    matches = []
    for route in ROUTES:
        score = 0
        signals = []
        for label, pattern, weight in route["patterns"]:
            if re.search(pattern, text, re.IGNORECASE):
                score += weight
                signals.append(label)
        if score >= 2:
            matches.append(
                {
                    "route": route["route"],
                    "score": score,
                    "signals": signals,
                    "risk_class": route["risk_class"],
                    "approval_required": route["approval_required"],
                }
            )
    matches.sort(key=lambda item: (-item["score"], item["route"]))
    return matches


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify a task into agent capability routes.")
    parser.add_argument("text", nargs="*", help="Task text. Reads stdin when omitted.")
    args = parser.parse_args()

    text = " ".join(args.text).strip()
    if not text:
        text = sys.stdin.read().strip()
    if not text:
        parser.error("provide task text or stdin")

    routes = classify(text)
    print(
        json.dumps(
            {
                "routes": routes,
                "primary": routes[0]["route"] if routes else None,
                "approval_required": routes[0]["approval_required"] if routes else False,
                "risk_class": routes[0]["risk_class"] if routes else None,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
