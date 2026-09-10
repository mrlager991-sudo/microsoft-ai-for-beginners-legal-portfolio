import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("validator",ROOT/"scripts"/"validate_portfolio.py"); validator=importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)
class RepositoryTests(unittest.TestCase):
    def test_validator(self): self.assertEqual(validator.validate(),[])
if __name__=="__main__": unittest.main()
