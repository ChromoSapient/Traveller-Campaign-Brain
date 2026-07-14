# v1.2 Upload Manifest

## Full replacements

- `KnowledgeGraph/campaign_state.yaml`
- `KnowledgeGraph/validation_rules.yaml`
- `Instructions/PROJECT_ROUTER.yaml`
- `ROADMAP.md`

## New files

- `Chronology/Campaign_Chronology.yaml`
- `Instructions/BRANCH_AND_DRAFT_POLICY.yaml`
- `tests/test_live_edge.py`
- `Reference/Extraction_Log_v1.2.md`

## Package documentation

- `PATCH_README.md`
- `UPLOAD_MANIFEST.md`

After upload, run:

```bash
python -m unittest tests.test_live_edge
```
