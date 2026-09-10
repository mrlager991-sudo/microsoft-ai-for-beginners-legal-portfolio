"""Bag-of-words keyword baseline and one-layer perceptron, pure Python."""
from __future__ import annotations
import json, math, random, re
from collections import Counter
from pathlib import Path

LABELS = ["contract", "employment", "privacy"]
KEYWORDS = {
    "contract": {"agreement", "clause", "payment", "termination", "supplier"},
    "employment": {"employee", "salary", "dismissal", "leave", "workplace"},
    "privacy": {"personal", "data", "consent", "controller", "breach"},
}
def tokens(text): return re.findall(r"[a-z]+", text.lower())
def baseline(text):
    counts = {label: sum(t in words for t in tokens(text)) for label, words in KEYWORDS.items()}
    best = max(counts.values())
    return next((label for label in LABELS if counts[label] == best), "contract")

class Perceptron:
    def __init__(self):
        self.weights = {label: Counter() for label in LABELS}; self.bias = Counter()
    def predict(self, text):
        bag = Counter(tokens(text))
        scores = {label: self.bias[label] + sum(self.weights[label][t] * n for t,n in bag.items()) for label in LABELS}
        return max(LABELS, key=lambda label: (scores[label], -LABELS.index(label)))
    def fit(self, rows, epochs=12, seed=17):
        rng = random.Random(seed)
        for _ in range(epochs):
            order = list(rows); rng.shuffle(order)
            for row in order:
                predicted = self.predict(row["text"]); gold = row["label"]
                if predicted != gold:
                    for token, count in Counter(tokens(row["text"])).items():
                        self.weights[gold][token] += count; self.weights[predicted][token] -= count
                    self.bias[gold] += 1; self.bias[predicted] -= 1
        return self

def accuracy(predict, rows): return sum(predict(r["text"]) == r["label"] for r in rows) / len(rows)
def evaluate(path):
    rows = json.loads(path.read_text(encoding="utf-8")); train=[r for r in rows if r["split"]=="train"]; test=[r for r in rows if r["split"]=="test"]
    model=Perceptron().fit(train)
    return {"seed":17,"epochs":12,"train_size":len(train),"test_size":len(test),"baseline_test_accuracy":accuracy(baseline,test),"perceptron_train_accuracy":accuracy(model.predict,train),"perceptron_test_accuracy":accuracy(model.predict,test),"test_predictions":[{"id":r["id"],"gold":r["label"],"baseline":baseline(r["text"]),"perceptron":model.predict(r["text"])} for r in test]}
if __name__ == "__main__": print(json.dumps(evaluate(Path(__file__).with_name("data") / "phrases.json"), indent=2))
