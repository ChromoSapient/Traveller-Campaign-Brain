import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphlib import knowledge

class KnowledgeTests(unittest.TestCase):
    def test_ruuk_has_partial_omicron_knowledge(self):
        rows = [k for k in knowledge() if k.get("knower") == "char.ruuk" and k.get("fact") == "fact.omicron.partial_knowledge"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["certainty"], "partial")

if __name__ == "__main__":
    unittest.main()
