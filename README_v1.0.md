# Traveller Campaign Brain v1.0

## Purpose

v1.0 provides a minimal but operational knowledge graph for campaign use.

It can answer:

- Who knows this fact?
- What source supports it?
- Which claim wins when sources conflict?
- Is a fact branch-specific?
- Which NPCs and organizations care?
- What contradictions remain unresolved?
- What scenes are valid next steps?
- Does a proposed scene violate campaign canon?

## Quick Start

```bash
python scripts/query_graph.py canon ship.garnette name
python scripts/query_graph.py knowledge char.ruuk org.omicron
python scripts/validate_campaign.py
python scripts/recommend_scenes.py
python -m unittest discover -s tests
```

## File Groups

- `KnowledgeGraph/` contains campaign data and rules.
- `scripts/` contains small command-line tools.
- `tests/` contains regression checks.
- Existing character and culture files remain authoritative source material.

## Design Principle

The graph is deliberately readable YAML rather than a database requiring a priesthood.
