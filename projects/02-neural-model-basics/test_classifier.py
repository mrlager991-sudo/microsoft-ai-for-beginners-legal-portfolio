import importlib.util, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("classifier",HERE/"classifier.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class ClassifierTests(unittest.TestCase):
    def test_deterministic(self):
        a=mod.evaluate(HERE/"data"/"phrases.json"); b=mod.evaluate(HERE/"data"/"phrases.json"); self.assertEqual(a,b)
    def test_expected_shape(self):
        r=mod.evaluate(HERE/"data"/"phrases.json"); self.assertEqual((r["train_size"],r["test_size"]),(15,6)); self.assertEqual(len(r["test_predictions"]),6)
    def test_perceptron_learns_training_set(self):
        self.assertGreaterEqual(mod.evaluate(HERE/"data"/"phrases.json")["perceptron_train_accuracy"],0.9)
if __name__=="__main__": unittest.main()
