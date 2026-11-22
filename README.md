# GREEN citation policy

This repository is the independent source of truth for scientific credit in
the [GREEN software ecosystem](https://green-phys.org/). It separates:

- bibliographic facts, maintained in `CITATION.cff`;
- component-to-publication policy, maintained in `CITATIONS.yaml`; and
- generated guidance, including `CITATION.md` and `references.bib`.

Do not edit generated files. Run `python3 scripts/generate_citations.py` after
changing either authority file, then run `cffconvert --validate`,
`python3 scripts/check.py`, and the unit tests.

## Current scope

The initial catalog contains the two established GREEN software publications.
The component policy is deliberately marked `draft`: method-specific mappings
must be reviewed by the scientific collaborators before they become normative.

The non-normative first-pass inventory is in
`proposals/method-citations.yaml`. It records candidate mappings and open
questions but is deliberately excluded from generated citation guidance until
collaborators approve individual decisions.

Downstream repositories and AI agents should link to this repository rather
than maintain their own publication metadata. They may present the generated
guidance, but must not infer that a software citation replaces citations for
the scientific methods used in a calculation.

## Policy changes

Publication metadata corrections and changes to scientific citation policy are
reviewed changes. See `CONTRIBUTING.md`.

