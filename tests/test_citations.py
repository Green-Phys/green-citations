import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_citations


class CitationPolicyTests(unittest.TestCase):
    def test_all_catalog_entries_are_used(self):
        policy, papers = generate_citations.load()
        self.assertEqual(generate_citations.cited_keys(policy), set(papers))

    def test_unapproved_methods_are_not_mapped(self):
        policy, _ = generate_citations.load()
        for component in policy["components"].values():
            if component["method-mapping-status"] == "review-required":
                self.assertEqual(component["methods"], {})

    def test_dois_are_unique(self):
        _, papers = generate_citations.load()
        dois = [paper["doi"].lower() for paper in papers.values()]
        self.assertEqual(len(dois), len(set(dois)))


if __name__ == "__main__":
    unittest.main()

