"""Deterministic TF-IDF retrieval, clause routing, and regex entity extraction."""
from __future__ import annotations
import json, math, re
from collections import Counter
from pathlib import Path

def words(text): return re.findall(r"[a-z0-9€$,.]+",text.lower())
def tfidf_vectors(texts):
    docs=[Counter(words(t)) for t in texts]; n=len(docs); df=Counter(w for d in docs for w in d)
    return [{w:c*(math.log((n+1)/(df[w]+1))+1) for w,c in d.items()} for d in docs]
def cosine(a,b):
    dot=sum(v*b.get(w,0) for w,v in a.items()); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0.0
def most_similar(query,candidates):
    vectors=tfidf_vectors([query]+candidates); scores=[cosine(vectors[0],v) for v in vectors[1:]]; i=max(range(len(scores)),key=scores.__getitem__)
    return i,scores[i]
def classify(text):
    t=text.lower()
    for label,keys in [("governing-law",("governed","jurisdiction")),("payment",("payment","invoice","€","$")),("termination",("terminate","termination","notice"))]:
        if any(k in t for k in keys): return label
    return "other"
def entities(text):
    patterns={"date":r"\b\d{4}-\d{2}-\d{2}\b","amount":r"(?:€|\$)\s?\d[\d,]*","jurisdiction":r"laws of ([A-Z][A-Za-z ]+)"}
    out={}
    for key,pattern in patterns.items():
        m=re.search(pattern,text); out[key]=(m.group(1) if key=="jurisdiction" and m else m.group(0) if m else None)
    return out
def evaluate(path):
    data=json.loads(path.read_text(encoding="utf-8")); clauses=data["clauses"]
    class_correct=sum(classify(c["text"])==c["gold_class"] for c in clauses); fields=correct=0; errors=[]
    for c in clauses:
        got=entities(c["text"])
        for field,gold in c["gold_entities"].items():
            fields+=1; correct+=got.get(field)==gold
            if got.get(field)!=gold: errors.append({"id":c["id"],"field":field,"expected":gold,"predicted":got.get(field)})
    idx,score=most_similar(data["retrieval_query"],[c["text"] for c in clauses])
    return {"clause_count":len(clauses),"classification_accuracy":class_correct/len(clauses),"entity_field_accuracy":correct/fields,"retrieval":{"query":data["retrieval_query"],"predicted_clause_id":clauses[idx]["id"],"expected_clause_id":data["expected_retrieval_id"],"cosine":round(score,6),"correct":clauses[idx]["id"]==data["expected_retrieval_id"]},"errors":errors}
if __name__=="__main__": print(json.dumps(evaluate(Path(__file__).with_name("data")/"clauses.json"),indent=2))
