from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative_path):
    path = ROOT / relative_path
    return yaml.safe_load(path.read_text(encoding="utf-8"))


class LiveEdgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = load_yaml("KnowledgeGraph/campaign_state.yaml")["campaign_state"]
        cls.chronology = load_yaml("Chronology/Campaign_Chronology.yaml")
        cls.policy = load_yaml("Instructions/BRANCH_AND_DRAFT_POLICY.yaml")

    def test_live_edge_date_is_resolved(self):
        self.assertEqual(self.state["date"], "056-1107")
        self.assertNotIn("unresolved", self.state["date"])

    def test_live_edge_location_is_pagaton(self):
        location = self.state["current_location"]
        self.assertEqual(location["system"], "Pagaton")
        self.assertEqual(location["area"], "just_outside_respis")
        self.assertEqual(location["aboard"], "ship.garnette")

    def test_active_branch(self):
        self.assertEqual(self.state["branch"], "mainline_pagaton_departure")
        self.assertEqual(
            self.policy["active_branch"]["id"],
            "mainline_pagaton_departure",
        )

    def test_active_cast(self):
        expected = {
            "char.ruuk",
            "char.dralan",
            "robot.roamer",
            "char.ardric",
            "char.solveig",
            "char.corbin",
        }
        self.assertEqual(set(self.state["active_crew"]), expected)

    def test_tapir_is_absent(self):
        tapir = self.state["absent_characters"][0]
        self.assertEqual(tapir["character"], "char.tapir_tracks")
        self.assertFalse(tapir["escape_confirmed_in_play"])
        self.assertFalse(tapir["rejoined"])
        self.assertFalse(tapir["aboard_garnette"])

    def test_rts_is_unavailable(self):
        rts = self.state["unavailable_assets"][0]
        self.assertEqual(rts["asset"], "ship.restless_tentacle_syndrome")
        self.assertFalse(rts["return_expected"])

    def test_route_is_planned_not_completed(self):
        plan = self.state["travel_plan"]
        self.assertFalse(plan["has_departed_pagaton"])
        self.assertEqual(plan["next_destination"], "Binges")
        self.assertEqual(plan["eventual_destination"], "Lydia")
        self.assertEqual(plan["next_destination_status"], "discussed_not_departed")
        self.assertEqual(plan["eventual_destination_status"], "intended_not_departed")

    def test_chronology_matches_campaign_state(self):
        live = self.chronology["live_edge"]
        self.assertEqual(live["date"], self.state["date"])
        self.assertEqual(live["branch"], self.state["branch"])
        self.assertEqual(
            live["location"]["system"],
            self.state["current_location"]["system"],
        )
        self.assertEqual(
            live["location"]["aboard"],
            self.state["current_location"]["aboard"],
        )

    def test_canon_records_do_not_contain_draft_material(self):
        canonical_files = [
            ROOT / "KnowledgeGraph/campaign_state.yaml",
            ROOT / "Chronology/Campaign_Chronology.yaml",
        ]
        forbidden = [
            "alternate_branch_unplayed_draft",
            "previous_lydia_scenes",
            "lydia_jump_draft",
        ]
        for path in canonical_files:
            text = path.read_text(encoding="utf-8").lower()
            for term in forbidden:
                self.assertNotIn(term, text, f"{term} found in {path}")

    def test_no_unresolved_live_edge_placeholders(self):
        canonical_files = [
            ROOT / "KnowledgeGraph/campaign_state.yaml",
            ROOT / "Chronology/Campaign_Chronology.yaml",
        ]
        forbidden = [
            "unresolved_current_live_edge",
            "unresolved_in_this_correction",
        ]
        for path in canonical_files:
            text = path.read_text(encoding="utf-8")
            for term in forbidden:
                self.assertNotIn(term, text, f"{term} found in {path}")


if __name__ == "__main__":
    unittest.main()
