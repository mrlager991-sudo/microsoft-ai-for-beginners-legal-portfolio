# Symbolic Legal Triage

This transparent intake demonstrator routes synthetic requests to review queues. It applies lessons 1–2: knowledge representation, explicit rules, and inspectable explanations. Run `python triage.py` from this directory; the measured output is in [results.json](results.json), and `python -m unittest test_triage.py` exercises positive, combined, unknown, and missing-field cases.

The legal scenario, rule priorities, expected outcomes, and ontology vocabulary were selected for this portfolio. A technical AI agent drafted code, synthetic cases, tests, and documentation under review. The ontology is an original legal reinterpretation informed by an earlier learner-created home-room ontology; no triples were copied. See [AUTHORSHIP.md](AUTHORSHIP.md).

The system achieved the measured exact-match result on six designed cases. This tiny, synthetic test set cannot establish legal correctness or production performance. Rules omit jurisdiction, conflicts, privilege, and factual ambiguity. Every route is administrative guidance for a qualified human, never legal advice or an automated legal decision.
