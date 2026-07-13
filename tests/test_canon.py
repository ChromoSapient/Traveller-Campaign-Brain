import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphlib import find_fact

class CanonTests(unittest.TestCase):
    def test_ship_name(self):
        fact = find_fact("ship.garnette", "name")
        self.assertIsNotNone(fact)
        self.assertEqual(fact["object"], "Garnette")

    def test_roamer_self_ownership(self):
        fact = find_fact("robot.roamer", "actual_owner")
        self.assertEqual(fact["object"], "robot.roamer")

if __name__ == "__main__":
    unittest.main()
