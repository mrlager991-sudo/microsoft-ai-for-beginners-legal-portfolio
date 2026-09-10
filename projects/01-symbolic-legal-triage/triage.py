"""Transparent rules-based triage for synthetic legal requests."""
from __future__ import annotations
import json
from pathlib import Path

RULES = [
    {"id": "R1", "when": {"deadline_hours_max": 24}, "queue": "urgent-human-review", "reason": "A stated deadline is within 24 hours."},
    {"id": "R2", "when": {"personal_data": True}, "queue": "privacy-review", "reason": "The request contains personal data."},
    {"id": "R3", "when": {"topic": "contract"}, "queue": "contract-review", "reason": "The request concerns contract terms."},
    {"id": "R4", "when": {"topic": "employment"}, "queue": "employment-review", "reason": "The request concerns employment law."},
]

def _matches(facts: dict, conditions: dict) -> bool:
    for key, expected in conditions.items():
        if key.endswith("_max"):
            value = facts.get(key[:-4])
            if value is None or value > expected:
                return False
        elif facts.get(key) != expected:
            return False
    return True

def triage(facts: dict) -> dict:
    fired = [r for r in RULES if _matches(facts, r["when"])]
    if not fired:
        return {"queues": ["general-intake"], "explanations": ["No specialist rule matched."], "rule_ids": []}
    return {
        "queues": sorted({r["queue"] for r in fired}),
        "explanations": [r["reason"] for r in fired],
        "rule_ids": [r["id"] for r in fired],
    }

def evaluate(path: Path) -> dict:
    cases = json.loads(path.read_text(encoding="utf-8"))
    outcomes, correct = [], 0
    for case in cases:
        prediction = triage(case["facts"])
        ok = prediction["queues"] == sorted(case["expected_queues"])
        correct += int(ok)
        outcomes.append({"id": case["id"], "predicted": prediction, "expected_queues": case["expected_queues"], "correct": ok})
    return {"cases": len(cases), "exact_match_accuracy": correct / len(cases), "outcomes": outcomes}

if __name__ == "__main__":
    print(json.dumps(evaluate(Path(__file__).with_name("data") / "cases.json"), indent=2))
