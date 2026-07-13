from __future__ import annotations

from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
KG = ROOT / "KnowledgeGraph"

def load_yaml(name: str) -> dict[str, Any]:
    path = KG / name
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}

def entities() -> list[dict[str, Any]]:
    return load_yaml("entities.yaml").get("entities", [])

def facts() -> list[dict[str, Any]]:
    return load_yaml("facts.yaml").get("facts", [])

def relationships() -> list[dict[str, Any]]:
    return load_yaml("relationships.yaml").get("relationships", [])

def knowledge() -> list[dict[str, Any]]:
    return load_yaml("knowledge_states.yaml").get("knowledge", [])

def scenes() -> list[dict[str, Any]]:
    return load_yaml("scene_candidates.yaml").get("scenes", [])

def find_entity(entity_id: str) -> dict[str, Any] | None:
    return next((e for e in entities() if e.get("id") == entity_id), None)

def find_fact(subject: str, predicate: str) -> dict[str, Any] | None:
    matches = [f for f in facts() if f.get("subject") == subject and f.get("predicate") == predicate]
    if not matches:
        return None
    order = {
        "explicit_referee_ruling": 1,
        "current_campaign_chronology": 2,
        "campaign_canon_file": 3,
        "campaign_narrative": 3,
        "campaign_state": 3,
        "current_edition_primary_source": 4,
        "current_edition_regional_source": 5,
        "legacy_source": 6,
        "JTAS_supporting_material": 7,
        "adopted_interpretation": 8,
        "repository_rule": 8,
        "hypothesis": 9,
        "speculation": 10,
    }
    return sorted(matches, key=lambda f: order.get(f.get("authority", ""), 99))[0]
