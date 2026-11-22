# Contributing

`CITATION.cff` is the only authority for titles, authors, venues, years, DOIs,
and other bibliographic metadata. `CITATIONS.yaml` is the only authority for
which GREEN component, version, feature, or method requires which publication.
Generated files must not become a second editable source.

For a change:

1. Edit the appropriate authority file.
2. Run `python3 scripts/generate_citations.py`.
3. Run `cffconvert --validate`, `python3 scripts/check.py`, and
   `python3 -m unittest discover -s tests`.
4. Explain the scientific basis for policy changes in the pull request.

Method mappings require review by collaborators with responsibility for the
method or implementation. A DOI's presence in the catalog does not by itself
make that publication mandatory for any component.

