import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphlib import scenes

class SceneTests(unittest.TestCase):
    def test_five_scene_candidates(self):
        self.assertGreaterEqual(len(scenes()), 5)

    def test_every_scene_has_complication(self):
        for scene in scenes():
            self.assertTrue(scene.get("complication"))

if __name__ == "__main__":
    unittest.main()
