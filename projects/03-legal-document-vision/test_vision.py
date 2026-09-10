import importlib.util, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("vision",HERE/"vision.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class VisionTests(unittest.TestCase):
    def test_expected_boxes(self):
        r=mod.evaluate(HERE/"data"/"synthetic-page.pgm",HERE/"data"/"expected.json"); self.assertEqual(r["predicted_boxes"],r["expected_boxes"]); self.assertEqual(r["mean_best_iou"],1.0)
    def test_redaction_area(self): self.assertEqual(mod.redact(HERE/"data"/"synthetic-page.pgm",[[2,2,5,2]])["redacted_pixels"],10)
    def test_disjoint_iou(self): self.assertEqual(mod.iou([0,0,1,1],[2,2,1,1]),0.0)
if __name__=="__main__": unittest.main()
