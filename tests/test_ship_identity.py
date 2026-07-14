import sys
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from graphlib import find_entity, find_fact

class ShipIdentityTests(unittest.TestCase):
    def test_garnette_is_type_s(self):
        entity = find_entity("ship.garnette")
        self.assertEqual(entity["displacement_tons"], 100)
        self.assertIn("Type-S", entity["class"])

    def test_garnette_owner(self):
        fact = find_fact("ship.garnette", "legal_owner")
        self.assertEqual(fact["object"], "char.mercedes_taramaka")

    def test_crew_does_not_own_garnette(self):
        fact = find_fact("org.garnette_crew", "owns_garnette")
        self.assertFalse(fact["object"])

    def test_garnette_and_rts_are_separate(self):
        garnette = find_entity("ship.garnette")
        rts = find_entity("ship.restless_tentacle_syndrome")
        self.assertNotEqual(garnette["id"], rts["id"])
        self.assertEqual(garnette["displacement_tons"], 100)
        self.assertEqual(rts["displacement_tons"], 300)

    def test_rts_will_not_return(self):
        fact = find_fact("ship.restless_tentacle_syndrome", "will_return_as_party_asset")
        self.assertFalse(fact["object"])

    def test_tapir_not_rejoined(self):
        fact = find_fact("char.tapir_tracks", "has_rejoined_party")
        self.assertFalse(fact["object"])

    def test_no_air_raft_or_stock_probe_drones(self):
        air_raft = find_fact("ship.garnette", "carries_air_raft")
        probes = find_fact("ship.garnette", "carries_stock_probe_drones")
        self.assertFalse(air_raft["object"])
        self.assertFalse(probes["object"])

    def test_ship_files_repeat_identity(self):
        brain = yaml.safe_load((ROOT / "Ships/Garnette/Garnette_Ship_Brain.yaml").read_text())
        self.assertEqual(brain["identity"]["displacement_tons"], 100)
        self.assertEqual(brain["campaign_role"]["legal_owner"], "char.mercedes_taramaka")

if __name__ == "__main__":
    unittest.main()
