import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from index import models_from_text
class TestModels(unittest.TestCase):
    def test_duplicates(self): self.assertEqual(models_from_text('AB-123 ab-123'),['AB-123'])
if __name__=='__main__':unittest.main()
