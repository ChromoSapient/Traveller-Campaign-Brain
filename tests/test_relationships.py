import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphlib import relationships

class RelationshipTests(unittest.TestCase):
    def test_dralan_life_debt(self):
        rows = [r for r in relationships() if r.get("subject") == "char.dralan" and r.get("relation") == "owes_life_debt_to"]
        self.assertEqual(rows[0]["object"], "char.ruuk")

if __name__ == "__main__":
    unittest.main()
