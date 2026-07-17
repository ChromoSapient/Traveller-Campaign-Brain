from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative_path):
    return yaml.safe_load((ROOT / relative_path).read_text(encoding="utf-8"))


class TimelineKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy = load_yaml(
            "Universe/Timeline/Knowledge_Visibility_Taxonomy.yaml"
        )
        cls.pilot = load_yaml("Universe/Timeline/Ancient_Era_Pilot.yaml")
        cls.events = cls.pilot["events"]

    def test_all_visibility_levels_exist(self):
        self.assertEqual(
            set(self.taxonomy["levels"]),
            {"public", "specialist", "limited", "secret", "referee_only", "lost", "disputed"},
        )

    def test_every_event_has_required_fields(self):
        required = {"id", "date", "event", "truth_status", "knowledge", "sources"}
        for event in self.events:
            self.assertTrue(required.issubset(event), event["id"])

    def test_limited_and_secret_entries_identify_known_to(self):
        for event in self.events:
            if event["knowledge"]["visibility"] in {"limited", "secret"}:
                self.assertTrue(event["knowledge"]["known_to"], event["id"])

    def test_vargr_higher_purpose_remains_restricted(self):
        event = self.event("ancient.proto_vargr_transplanted_to_lair")
        restricted = event["knowledge"]["restricted_details"]
        self.assertIn("intended_higher_purpose", restricted)
        self.assertEqual(
            event["campaign_overlays"][0]["answer_status"],
            "unresolved_do_not_answer_in_this_patch",
        )

    def test_church_uplift_date_is_disputed_and_attributed(self):
        event = self.event("chosen_ones.first_vargr_uplift_teaching")
        self.assertEqual(event["date"]["value"], -312463)
        self.assertEqual(event["truth_status"], "disputed")
        self.assertIn("Church_of_the_Chosen_Ones", event["knowledge"]["believed_by"])

    def test_cx_entries_preserve_compiler_inference(self):
        cx_events = [
            event
            for event in self.events
            if "X" in (event["date"]["source_date_code"] or "")
        ]
        self.assertTrue(cx_events)
        for event in cx_events:
            self.assertTrue(event["date"]["inferred"], event["id"])

    def event(self, event_id):
        return next(event for event in self.events if event["id"] == event_id)


if __name__ == "__main__":
    unittest.main()
