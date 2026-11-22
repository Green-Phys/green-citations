#!/usr/bin/env python3
"""Validate authorities, mappings, and generated outputs."""

from pathlib import Path
import subprocess
import sys

import json
import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    policy = yaml.safe_load((ROOT / "CITATIONS.yaml").read_text())
    schema = json.loads((ROOT / "schema/citations.schema.json").read_text())
    jsonschema.validate(policy, schema)

    cff = yaml.safe_load((ROOT / "CITATION.cff").read_text())
    dois: set[str] = set()
    for paper in cff.get("references", []):
        doi = paper["doi"].lower()
        if doi in dois:
            raise ValueError(f"duplicate DOI: {doi}")
        dois.add(doi)

    subprocess.run(
        [sys.executable, str(ROOT / "scripts/generate_citations.py"), "--check"],
        check=True,
    )


if __name__ == "__main__":
    main()

