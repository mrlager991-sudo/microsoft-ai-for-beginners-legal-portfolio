import importlib.util, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("router",HERE/"router.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class RouterTests(unittest.TestCase):
    def test_cases(self):
        r=mod.evaluate(HERE/"data"/"requests.json"); self.assertEqual(r["exact_route_accuracy"],1.0); self.assertTrue(r["all_require_human_review"])
    def test_sensitive_block(self): self.assertEqual(mod.route({"text":"Use this passport"})["status"],"blocked")
    def test_static_legal_workflow_specification(self):
        w=mod.static_workflow_specification({"text":"Review a contract clause"}); self.assertEqual([x["role"] for x in w["steps"]],["document-facts","evidence-brief","legal-workbench"]); self.assertIn("human",w["final_gate"])
    def test_external_action_gate(self): self.assertIn("explicit-authorization-required",mod.route({"text":"research sources","external_action":True})["flags"])
if __name__=="__main__": unittest.main()
