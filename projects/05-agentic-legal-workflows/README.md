# Agentic Legal Workflows and Responsible AI

This English-portable adaptation of the user-directed AI Practice Kit demonstrates deterministic routing across four bounded skills, privacy minimization, external-action authorization, mandatory human review, and a static three-role legal workflow specification. The three core capabilities are evidence synthesis, document fact extraction, and legal work; affiliate analysis is a supplemental cross-functional example. Run `python router.py`; inspect [results.json](results.json); run `python -m unittest test_router.py`.

For a legal request, the static specification defines three bounded roles in order: source-linked extraction, evidence comparison, then legal drafting. It describes the artifact each role would pass to the next, while the final gate remains human acceptance. It does not launch agents or execute an LLM. Requests marked as containing personal data are blocked before routing; external actions receive an authorization flag. These controls are executable examples, not a security boundary or a deployed agent platform.

The local source kit had no license or Git metadata. These concise English files are a new AI-assisted adaptation made at the user's direction; independent provenance is not claimed. See [AUTHORSHIP.md](AUTHORSHIP.md) and the repository source register.
