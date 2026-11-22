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

    proposal = yaml.safe_load(
        (ROOT / "proposals/method-citations.yaml").read_text()
    )
    proposal_schema = json.loads(
        (ROOT / "schema/method-citation-proposal.schema.json").read_text()
    )
    jsonschema.validate(proposal, proposal_schema)
    candidates = proposal["candidate-publications"]
    locators = [candidate["locator"].lower() for candidate in candidates.values()]
    if len(locators) != len(set(locators)):
        raise ValueError("method citation proposal contains duplicate locators")
    for component in proposal["components"].values():
        for method in component["methods"].values():
            for mapping in method["proposed"]:
                if mapping["publication"] not in candidates:
                    raise ValueError(
                        "method citation proposal uses unknown candidate: "
                        + mapping["publication"]
                    )

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

