import importlib.util, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("triage", HERE / "triage.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class TriageTests(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(mod.evaluate(HERE / "data" / "cases.json")["exact_match_accuracy"], 1.0)
    def test_explanation_and_rule_trace(self):
        result = mod.triage({"topic":"contract", "deadline_hours":6, "personal_data":True})
        self.assertEqual(result["rule_ids"], ["R1", "R2", "R3"])
        self.assertEqual(len(result["explanations"]), 3)
    def test_unknown_is_general(self):
        self.assertEqual(mod.triage({"topic":"tax"})["queues"], ["general-intake"])

if __name__ == "__main__": unittest.main()
