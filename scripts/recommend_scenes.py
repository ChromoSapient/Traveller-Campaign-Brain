from __future__ import annotations

from graphlib import scenes

def score(scene: dict) -> int:
    score = 0
    purposes = set(scene.get("purpose", []))
    if "advance_mysteries_arc" in purposes:
        score += 4
    if "character_interaction" in purposes:
        score += 2
    if scene.get("complication"):
        score += 2
    if scene.get("location") == "ship.garnette":
        score += 3
    return score

def main() -> None:
    ranked = sorted(scenes(), key=score, reverse=True)
    for scene in ranked[:5]:
        print(f"{score(scene):02d} | {scene['title']} | {scene['complication']}")

if __name__ == "__main__":
    main()
