from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    rules = yaml.safe_load((ROOT / "KnowledgeGraph" / "validation_rules.yaml").read_text(encoding="utf-8"))
    violations = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".txt"}:
            continue
        if "validation_rules.yaml" in str(path):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rule in rules.get("validation_rules", []):
            for pattern in rule.get("pattern", []):
                if pattern in text:
                    violations.append((rule["severity"], rule["code"], str(path.relative_to(ROOT)), pattern))

    for severity, code, path, pattern in violations:
        print(f"{severity.upper()} {code}: {path}: {pattern}")

    errors = [v for v in violations if v[0] == "error"]
    if errors:
        sys.exit(1)

    print("Campaign validation passed.")

if __name__ == "__main__":
    main()
