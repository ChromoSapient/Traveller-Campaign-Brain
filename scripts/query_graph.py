from __future__ import annotations

import argparse
import json
from graphlib import find_fact, knowledge, facts, relationships

def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    canon = sub.add_parser("canon")
    canon.add_argument("subject")
    canon.add_argument("predicate")

    know = sub.add_parser("knowledge")
    know.add_argument("knower")
    know.add_argument("subject")

    rel = sub.add_parser("relationships")
    rel.add_argument("entity")

    args = parser.parse_args()

    if args.command == "canon":
        result = find_fact(args.subject, args.predicate)
    elif args.command == "knowledge":
        known_ids = {k["fact"] for k in knowledge() if k.get("knower") == args.knower}
        result = [f for f in facts() if f.get("id") in known_ids and f.get("subject") == args.subject]
    else:
        result = [r for r in relationships() if r.get("subject") == args.entity or r.get("object") == args.entity]

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
