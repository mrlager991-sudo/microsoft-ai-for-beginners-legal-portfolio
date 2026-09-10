import importlib.util, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("pipeline",HERE/"pipeline.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class PipelineTests(unittest.TestCase):
    def test_metrics_and_recorded_error(self):
        r=mod.evaluate(HERE/"data"/"clauses.json"); self.assertEqual(r["classification_accuracy"],1.0); self.assertEqual(len(r["errors"]),1); self.assertTrue(r["retrieval"]["correct"])
    def test_entities(self): self.assertEqual(mod.entities("laws of Poland; fee € 50 on 2026-01-02"),{"date":"2026-01-02","amount":"€ 50","jurisdiction":"Poland"})
    def test_unknown_clause(self): self.assertEqual(mod.classify("Definitions appear below."),"other")
if __name__=="__main__": unittest.main()
