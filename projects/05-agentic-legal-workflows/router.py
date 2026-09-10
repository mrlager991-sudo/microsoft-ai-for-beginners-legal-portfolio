"""Deterministic skill router with privacy and human-review gates."""
from __future__ import annotations
import json
from pathlib import Path

ROUTES = [
    ("legal-workbench", ("contract", "legal", "clause", "law")),
    ("document-facts", ("extract", "compare", "table", "document")),
    ("evidence-brief", ("research", "explain", "sources", "options")),
    ("affiliate-lab", ("affiliate", "campaign", "offer", "advert")),
]
SENSITIVE = ("client secret", "passport", "medical record", "nda document")

def route(request):
    text=request["text"].lower(); flags=[]
    if request.get("contains_personal_data") or any(term in text for term in SENSITIVE):
        return {"status":"blocked","skill":None,"flags":["privacy-minimization-required"],"human_review":True}
    skill="evidence-brief"
    for name,terms in ROUTES:
        if any(term in text for term in terms): skill=name; break
    if skill=="legal-workbench": flags.append("qualified-legal-review-required")
    if request.get("external_action"): flags.append("explicit-authorization-required")
    return {"status":"routed","skill":skill,"flags":flags,"human_review":True}

def static_workflow_specification(request):
    decision=route(request)
    if decision["status"]=="blocked": return {"route":decision,"steps":[]}
    steps=[
        {"role":"document-facts","scope":"Extract supplied facts with source pointers."},
        {"role":"evidence-brief","scope":"Compare evidence and identify uncertainty."},
        {"role":"legal-workbench","scope":"Draft legal analysis for qualified human review."},
    ] if decision["skill"]=="legal-workbench" else [{"role":decision["skill"],"scope":"Handle only the routed bounded task."}]
    return {"route":decision,"steps":steps,"final_gate":"human acceptance required"}

def evaluate(path):
    cases=json.loads(path.read_text(encoding="utf-8")); outcomes=[]; correct=0
    for case in cases:
        got=route(case); ok=got["status"]==case["expected_status"] and got["skill"]==case["expected_skill"] and got["human_review"]
        correct+=ok; outcomes.append({"id":case["id"],"result":got,"correct":ok})
    return {"cases":len(cases),"exact_route_accuracy":correct/len(cases),"all_require_human_review":all(x["result"]["human_review"] for x in outcomes),"outcomes":outcomes}
if __name__=="__main__": print(json.dumps(evaluate(Path(__file__).with_name("data")/"requests.json"),indent=2))
