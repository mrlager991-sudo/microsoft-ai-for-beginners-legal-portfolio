# Legal AI Practice Portfolio

Sviatoslav Omelchuk is a legal professional applying AI to legal workflows; this repository connects a self-directed review of Microsoft's 24-lesson *AI for Beginners* curriculum to five reproducible, post-course legal-AI demonstrations.

## Verification status

The 24-lesson review is a [learner declaration](provenance/LEARNING_STATEMENT.md). Microsoft issued no certificate, completion record, or grade. The practical examples were created on 2026-09-09 after the reported review for this portfolio; they are not presented as official assignments. Repository checks verify files and behavior, not the historical act of reading.

## Evidence snapshot

| Material claim | Classification | Direct evidence |
|---|---|---|
| Self-directed review of 24 lessons | Self-declared | [Learning statement](provenance/LEARNING_STATEMENT.md), [24-lesson map](course-map.md) |
| Five post-course legal-AI demonstrations exist | Artifact/test verified | [Machine-readable evidence graph](portfolio.json), project results below |
| Demonstrations run deterministically with the standard library | Test verified | [Check runner](scripts/run_checks.py), [CI workflow](.github/workflows/validate.yml) |
| Human direction and technical AI assistance are separated | Documented | [Authorship and AI use](provenance/AUTHORSHIP_AND_AI_USE.md) |
| Privacy and human-review controls appear in the workflow | Test verified within the demo | [Agentic workflow result](projects/05-agentic-legal-workflows/results.json) |

## Five applied projects

| Project | Legal task and AI concept | Actual result | Test | Material limit |
|---|---|---|---|---|
| [01 Symbolic triage](projects/01-symbolic-legal-triage/README.md) | Explainable rules and legal ontology | [6/6 exact routes](projects/01-symbolic-legal-triage/results.json) | [Tests](projects/01-symbolic-legal-triage/test_triage.py) | Designed cases do not establish legal correctness |
| [02 Neural basics](projects/02-neural-model-basics/README.md) | Keyword baseline versus perceptron | [33.3% vs 66.7% test accuracy](projects/02-neural-model-basics/results.json) | [Tests](projects/02-neural-model-basics/test_classifier.py) | Six test items; visible overfitting risk |
| [03 Document vision](projects/03-legal-document-vision/README.md) | Field localization and redaction | [1.0 IoU on one synthetic page](projects/03-legal-document-vision/results.json) | [Tests](projects/03-legal-document-vision/test_vision.py) | No OCR or real-document accuracy claim |
| [04 Legal NLP](projects/04-legal-nlp/README.md) | TF-IDF retrieval, routing, regex entities | [91.7% entity-field accuracy; error retained](projects/04-legal-nlp/results.json) | [Tests](projects/04-legal-nlp/test_pipeline.py) | Four synthetic clauses; lexical methods only |
| [05 Agentic workflows](projects/05-agentic-legal-workflows/README.md) | Skill routing, static three-role workflow specification, privacy gates | [6/6 routes and universal human review](projects/05-agentic-legal-workflows/results.json) | [Tests](projects/05-agentic-legal-workflows/test_router.py) | Illustrative controls, not deployed security |

## 24-lesson map

The [course map](course-map.md) gives every lesson label and pinned upstream link, a concise application note, evidence type, status, date, and limitation. The same mapping is available to agents in [portfolio.json](portfolio.json).

## Authorship and AI assistance

Sviatoslav directed the legal scenarios, evaluation and evidence requirements, responsible-use boundaries, and portfolio positioning. A technical AI agent drafted the implementation, synthetic inputs, tests, measured outputs, and documentation under that direction. Read the [full role split](provenance/AUTHORSHIP_AND_AI_USE.md) and each project's concrete `AUTHORSHIP.md`.

## Verify in three minutes and three clicks

1. Read this page and choose any actual result in the project table.
2. Open its linked test or authorship record.
3. Run from the repository root: `python scripts/run_checks.py`.

Independent recruiter-style repository QA returned **PASS / PUBLISH**, a **93/100 portfolio readiness score**, and **zero critical blockers** on 2026-09-09. This score evaluates publication readiness only; it is not a course grade, academic assessment, vendor assessment, legal opinion, security audit, or proof of professional qualification. Read the evidence-linked [QA report](evaluations/recruiter-review/REPORT.md), [machine-readable result](evaluations/recruiter-review/report.json), and [response log](evaluations/recruiter-review/RESPONSE.md). The review used the saved [context-free prompt](evaluations/recruiter-review/REVIEW_PROMPT.md) and [portfolio-readiness rubric](evaluations/RUBRIC.md).

## Responsible use and attribution

All executable examples use synthetic data. No client, employer, personal, internal-template, or NDA material is included. Outputs are educational and require qualified human review before legal use. See the [source register](provenance/SOURCE_REGISTER.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

This is an independent project based on concepts in [Microsoft AI for Beginners at pinned commit `392d0df1…`](https://github.com/microsoft/AI-For-Beginners/tree/392d0df1b2647cbee104942390551f1ed9e072c8). It is not endorsed by Microsoft and does not represent a Microsoft-issued credential or an official grade.
