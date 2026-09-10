# Course map: 24 lessons

This map records Sviatoslav Omelchuk's self-declared review and connects selected concepts to artifacts created on 2026-09-09 after that review. Notes paraphrase the curriculum and should be read with the [learning statement](provenance/LEARNING_STATEMENT.md). A project link demonstrates selected application, not completion of the lesson's official assignment.

## Lesson 01 — Introduction and History of AI

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/1-Intro/README.md) · **Project:** [Symbolic Legal Triage](projects/01-symbolic-legal-triage/README.md) · **Evidence:** learner declaration + artifact · **Status:** reviewed; artifact_created_post_course · **Created:** 2026-09-09

The review covered changing definitions of artificial intelligence, the contrast between symbolic and data-driven approaches, and the importance of matching a technique to a problem rather than treating AI as one uniform product. For legal work, that history matters because a transparent rule system may be preferable to a learned model when a reviewer needs to see why an intake route fired. Project 01 therefore begins with explicit facts and rules. It demonstrates one practical selection decision, not mastery of AI history. The link to the project verifies the later application; the fact that the lesson itself was reviewed remains Sviatoslav's declaration.

## Lesson 02 — Knowledge Representation and Expert Systems

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/2-Symbolic/README.md) · **Project:** [Symbolic Legal Triage](projects/01-symbolic-legal-triage/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The reviewed material addressed symbolic facts, rules, ontologies, inference, and the explainability of expert systems. In a legal intake setting, those ideas become a small vocabulary for requests and review queues plus rules for deadlines, personal data, contracts, and employment matters. Project 01 records every rule that fires and returns a plain-language explanation, making the route auditable. Its legal ontology is a new interpretation informed by an earlier home-room ontology exercise, with provenance disclosed. Six synthetic cases test combinations and missing facts. The narrow vocabulary cannot capture jurisdiction, privilege, conflicts, or substantive advice, so every route remains an administrative suggestion for human review.

## Lesson 03 — Perceptron

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/3-NeuralNetworks/03-Perceptron/README.md) · **Project:** [Neural Model Basics](projects/02-neural-model-basics/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered a perceptron as a weighted linear decision rule, the role of inputs and bias, and iterative weight updates after classification errors. Project 02 applies that mechanism to bag-of-words features from synthetic legal-intake phrases. It trains one weight vector per class with a fixed shuffle seed and compares the learned classifier against a transparent keyword baseline. The saved results show training and test metrics as well as each test prediction. This is a direct, inspectable implementation of a basic learning rule. The dataset is intentionally tiny, multiclass handling is simplified, and no claim is made that the model can classify real legal communications reliably.

## Lesson 04 — Multi-Layered Perceptron and Creating Our Own Framework

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/3-NeuralNetworks/04-OwnFramework/README.md) · **Project:** [Neural Model Basics](projects/02-neural-model-basics/README.md) · **Evidence:** artifact · **Status:** artifact_created_post_course; not_separately_assessed · **Created:** 2026-09-09

The reviewed lesson develops the idea that layers, activations, losses, and optimization can be assembled into a small neural framework. The portfolio deliberately stops at a single linear layer so its mechanics remain readable without numerical libraries. That boundary is itself relevant to legal technology: model complexity should follow the evidence and operational need. Project 02 exposes feature counts, weights, bias updates, epochs, and predictions, providing a bridge from a perceptron to deeper networks without pretending to implement backpropagation through multiple layers. The artifact therefore supports conceptual application only for this lesson. Multi-layer training, nonlinear activations, gradient checking, and framework design were not separately assessed here.

## Lesson 05 — Intro to Frameworks and Overfitting

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/3-NeuralNetworks/05-Frameworks/README.md) · **Project:** [Neural Model Basics](projects/02-neural-model-basics/README.md) · **Evidence:** test · **Status:** tested · **Created:** 2026-09-09

The review covered why ML frameworks provide reusable tensors, layers, optimization, and evaluation tools, and why fitting training data does not prove generalization. Project 02 uses no third-party framework, but it makes the evaluation distinction concrete: fifteen training phrases and six held-out phrases are fixed in the dataset, and training accuracy is reported separately from test accuracy. The recorded gap and two test errors illustrate overfitting and vocabulary sensitivity. A deterministic seed makes repetition meaningful but does not make the estimate statistically strong. The project tests the evaluation pipeline rather than framework fluency, and its tiny authored dataset cannot justify selecting a production model or reporting a general legal-text accuracy rate.

## Lesson 06 — Intro to Computer Vision and OpenCV

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/06-IntroCV/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The reviewed material introduced images as numeric arrays and common operations such as thresholding, color or intensity transformations, and region processing. Project 03 reduces that idea to an ASCII PGM page whose pixels can be inspected in a text editor. A fixed threshold separates dark synthetic fields from the background, and connected components form candidate regions. The approach is CPU-only and uses the Python standard library rather than OpenCV, making every step reproducible in a clean environment. It demonstrates image representation and basic processing, not practical document vision. Noise, skew, compression, handwriting, page structure, and OCR are absent, so the result cannot be generalized to scanned legal documents.

## Lesson 07 — Convolutional Neural Networks

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/07-ConvNets/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** artifact · **Status:** artifact_created_post_course; not_separately_assessed · **Created:** 2026-09-09

The review covered local filters, shared weights, feature maps, pooling, and the way convolutional networks learn spatial patterns. Project 03 does not train or run a CNN. Its connected-component search nevertheless makes spatial locality visible: each dark pixel is joined only to four neighboring pixels, and local regions become bounding boxes. This provides a simple contrast between a hand-defined neighborhood operation and learned convolutional filters. For legal document automation, the lesson informs why layout models can detect signatures, stamps, tables, or fields despite position changes. The portfolio link is therefore conceptual evidence only. CNN architecture selection, training, augmentation, and evaluation on natural images were not separately tested by this artifact.

## Lesson 08 — Pre-trained Networks and Transfer Learning

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/08-TransferLearning/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** learner declaration + artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed lesson explained how features learned on a broad dataset may be reused or fine-tuned for a narrower task, reducing data and compute requirements. In legal document work, transfer learning can be attractive because labeled pages are scarce, but the source domain, license, privacy, and validation population matter. Project 03 intentionally avoids a pretrained model so its core check has no download, license uncertainty, or hidden behavior. That design demonstrates a responsible baseline before adding complexity. It does not demonstrate transfer learning itself. Any future upgrade would need a named model, verified license, version pin, representative document set, subgroup and failure analysis, and comparison against the current deterministic baseline.

## Lesson 09 — Autoencoders and VAEs

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/09-Autoencoders/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** learner declaration · **Status:** not_separately_assessed · **Created:** 2026-09-09

The review covered encoder-decoder structures, compressed latent representations, reconstruction loss, and the probabilistic extension used by variational autoencoders. Potential document uses include denoising, compression, anomaly screening, and representation learning, but reconstruction can also erase legally meaningful marks or create plausible-looking artifacts. Project 03 supplies a document-shaped context and explicit ground truth, yet it contains no encoder, decoder, latent space, or learned reconstruction. Its link records professional relevance rather than practical implementation. A credible legal experiment would require paired corrupt and clean pages, a task-specific quality measure, preservation tests for signatures and annotations, and human review. Those steps were not separately assessed in this portfolio.

## Lesson 10 — Generative Adversarial Networks and Artistic Style Transfer

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/10-GANs/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** learner declaration · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed material introduced adversarial training between generator and discriminator networks and showed how style can be transferred between images. For legal operations, synthetic documents might expand test coverage, but generated pages may reproduce training data, distort evidence, or create deceptive artifacts. Project 03 uses a hand-authored synthetic PGM page instead of a generative model, so the origin and expected regions are fully known. This is a deliberate data-provenance baseline, not a GAN demonstration. The lesson's relevance appears in the choice to label synthetic content and avoid realism claims. Adversarial loss, training stability, mode collapse, style objectives, and privacy leakage were not separately implemented or assessed.

## Lesson 11 — Object Detection

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/11-ObjectDetection/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered locating and classifying multiple objects with bounding boxes, confidence, and overlap-based evaluation. Project 03 implements the localization part on two predefined synthetic fields. Connected dark components become boxes, expected coordinates are stored separately, and intersection over union measures geometric agreement. The saved result reports predicted and expected boxes rather than only a success label. This makes the evidence inspectable and connects detection metrics to a document-redaction scenario. The method does not classify semantic field types, output confidence, handle overlapping regions, or test multiple pages. Perfect IoU on one constructed fixture proves deterministic recovery of those rectangles only; it is not production document-detection accuracy.

## Lesson 12 — Semantic Segmentation and U-Net

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/4-ComputerVision/12-Segmentation/README.md) · **Project:** [Document Vision](projects/03-legal-document-vision/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The reviewed lesson addressed pixel-level labeling and encoder-decoder segmentation architectures such as U-Net. Project 03 performs a much simpler binary segmentation: pixels below a fixed intensity become foreground, and located regions are replaced with a neutral value in an in-memory redaction result. Tests verify the expected redacted area and bounding boxes. This demonstrates how a pixel mask can support a legal-document workflow while clearly separating threshold segmentation from a learned U-Net. Real redaction also requires detection of semantic content, removal of underlying text and metadata, secure output handling, and human confirmation. Neural segmentation architecture, loss functions, class imbalance, and real-page evaluation were not separately assessed.

## Lesson 13 — Text Representation: BoW and TF-IDF

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/13-TextRep/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered token-based text representation, bag-of-words counts, TF-IDF weighting, and similarity between sparse vectors. Project 04 implements these operations with counters and logarithmic inverse document frequency, then retrieves the synthetic clause most similar to a payment query using cosine similarity. The dataset, query, expected clause, score, and result are public and deterministic. Project 02 also uses bag-of-words inputs for classification. These artifacts show how representation choices affect downstream legal routing and retrieval. The tokenizer is English-only and simplistic, word order is discarded, and lexical overlap is not legal equivalence. Four clauses cannot support a broad retrieval-quality claim.

## Lesson 14 — Semantic Word Embeddings: Word2Vec and GloVe

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/14-Embeddings/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed lesson explained dense word vectors, distributional similarity, and methods such as Word2Vec and GloVe. In contract review, embeddings can retrieve paraphrases that share little vocabulary, but similarity may also hide legally decisive wording. Project 04 supplies a sparse TF-IDF baseline and explicitly labels it as lexical. That baseline is useful evidence for what an embedding-based extension would need to beat: the expected clause, similarity score, and error analysis are already structured. No dense embedding is trained or downloaded in this repository, so semantic generalization is not tested. Future evaluation would need licensed versioned vectors, multilingual and domain coverage, hard legal negatives, and source-preserving human review.

## Lesson 15 — Language Modeling and Training Embeddings

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/15-LanguageModeling/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The review covered predicting words from context, learning representations during that task, and the relationship between language modeling and generated text. Legal applications include drafting assistance, search, and clause suggestions, but fluent continuation is not evidence of factual or legal correctness. Project 04 avoids generation and instead preserves each source clause alongside extracted outputs. That traceability shows a baseline control that any language-model extension should retain. The artifact does not train embeddings or estimate a language-model loss, and it cannot demonstrate generation quality. A fuller experiment would require a lawful corpus, contamination checks, held-out evaluation, hallucination analysis, and qualified review of both omissions and invented content.

## Lesson 16 — Recurrent Neural Networks

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/16-RNN/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** learner declaration · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed lesson addressed recurrent state, sequence processing, vanishing gradients, and gated variants used to retain longer context. Contract clauses are sequential, and dependencies such as exceptions or defined terms may span many tokens. Project 04 provides a clause-processing setting but intentionally uses order-insensitive TF-IDF and local regular expressions. That limitation makes the need for context-aware sequence models concrete: changing word order or separating a defined term can defeat the current rules. No recurrent network, sequence loss, hidden state, or long-range benchmark is implemented. The lesson mapping is therefore a reviewed concept and professional relevance note, not practical evidence of RNN development or evaluation.

## Lesson 17 — Generative Recurrent Networks

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/17-GenerativeNetworks/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** learner declaration · **Status:** not_separately_assessed · **Created:** 2026-09-09

The review covered recurrent generation, token sampling, and how sequence models can produce text one step at a time. In legal drafting, generated clauses require especially strict controls because plausible text may omit mandatory terms, contradict definitions, or invent authority. Project 04 does not generate text. It focuses on retrieval and extraction from fixed source clauses, preserving a clear evidence path. That design is a risk-control comparison rather than implementation of a generative recurrent network. Temperature, sampling strategy, sequence training, and generated-text metrics were not separately assessed. Any future drafting demonstration should retain the source, mark generated language, compare it against instructions and precedent, and require qualified human approval.

## Lesson 18 — Transformers and BERT

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/18-Transformers/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed material introduced attention, positional information, transformer encoders, pretraining, and BERT-style contextual representations. Those methods can improve clause search and entity recognition because a word's meaning depends on its surroundings. Project 04 establishes a deterministic lexical baseline with a gold set and a visible written-date failure. That structure could later compare a pinned transformer against the same expected outputs, but no transformer is included now. Avoiding a download keeps the core verification fast and removes model-license ambiguity. This lesson is therefore connected through evaluation design and stated relevance only. Contextual representation quality, fine-tuning, tokenization behavior, compute cost, bias, and model provenance were not separately assessed.

## Lesson 19 — Named Entity Recognition

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/19-NER/README.md) · **Project:** [Legal NLP](projects/04-legal-nlp/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered assigning entity types to spans, sequence labeling, and evaluation against annotated text. Project 04 creates a small legal analogue: regular expressions extract dates, amounts, and governing-law jurisdictions from synthetic clauses, then compare each field with a gold value. The saved result reports field-level accuracy and retains the exact error where a written date is missed. Although deterministic extraction is not a learned NER model, it demonstrates labels, expected spans or values, evaluation, and error analysis. Four clauses and three patterns are far too small for production claims. Nested entities, multilingual text, formatting variants, false positives, and legal interpretation all require broader testing and human validation.

## Lesson 20 — Large Language Models, Prompt Programming and Few-Shot Tasks

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/5-NLP/20-LangModels/README.md) · **Project:** [Agentic Workflows](projects/05-agentic-legal-workflows/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered large pretrained language models, prompt-based task specification, few-shot examples, and the difference between fluent output and reliable task performance. Project 05 turns task instructions into four portable skill files with scope, evidence, privacy, authorization, and human-review requirements. A deterministic router tests which skill should receive six synthetic requests; it does not call an LLM. Project 04 supplies a source-linked alternative for bounded extraction. Together they show prompt and workflow design with observable gates while avoiding paid APIs. They do not measure model reasoning, few-shot learning, hallucination, or prompt robustness. Real deployment would require model-specific evaluations, injection defenses, access controls, logging, and qualified review.

## Lesson 21 — Genetic Algorithms

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/6-Other/21-GeneticAlgorithms/README.md) · **Project:** [Agentic Workflows](projects/05-agentic-legal-workflows/README.md) · **Evidence:** learner declaration + artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The reviewed lesson introduced populations, fitness functions, selection, crossover, mutation, and iterative search. Legal operations can frame scheduling, review allocation, or workflow configuration as optimization, but a fitness function inevitably encodes policy choices and may reward shortcuts. Project 05 uses fixed routing rules rather than an evolutionary search. Its explicit gates illustrate constraints that an optimizer would need to respect: privacy blocks, authorization for external action, and human review cannot be traded away for throughput. No population, mutation operator, fitness experiment, or convergence analysis is implemented. The mapping records conceptual relevance and a governance constraint only; it does not claim practical genetic-algorithm experience from this artifact.

## Lesson 22 — Deep Reinforcement Learning

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/6-Other/22-DeepRL/README.md) · **Project:** [Agentic Workflows](projects/05-agentic-legal-workflows/README.md) · **Evidence:** learner declaration + artifact · **Status:** not_separately_assessed · **Created:** 2026-09-09

The review covered agents, environments, states, actions, rewards, policies, and learning from delayed outcomes. A legal workflow could use feedback to improve routing, but poorly designed rewards might favor speed over accuracy, confidentiality, or procedural fairness. Project 05 does not learn a policy. It uses deterministic routes and non-negotiable gates, providing an inspectable baseline against which any adaptive system should be evaluated. The always-on human-review flag also prevents a synthetic routing score from becoming permission to act. No environment, reward function, value estimate, exploration strategy, or deep reinforcement learner is implemented. This lesson is mapped as reviewed theory with governance relevance and was not separately assessed.

## Lesson 23 — Multi-Agent Systems

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/6-Other/23-MultiagentSystems/README.md) · **Project:** [Agentic Workflows](projects/05-agentic-legal-workflows/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The reviewed lesson addressed multiple agents, local roles, coordination, cooperation, and emergent system behavior. Project 05 represents a bounded legal sequence with three roles: document facts preserves source-linked inputs, evidence brief compares support and uncertainty, and legal workbench drafts analysis for a qualified human. Tests verify the ordered handoff and final human gate. The workflow makes responsibilities visible and limits each stage rather than treating an agent team as automatically reliable. It is a static orchestration demonstration, not a distributed simulation or live multi-agent runtime. Concurrency, conflicting goals, message failure, shared memory, prompt injection, and emergent behavior remain outside the tested scope.

## Lesson 24 — AI Ethics and Responsible AI

**Source:** [Microsoft lesson](https://github.com/microsoft/AI-For-Beginners/blob/392d0df1b2647cbee104942390551f1ed9e072c8/lessons/7-Ethics/README.md) · **Project:** [Agentic Workflows](projects/05-agentic-legal-workflows/README.md) · **Evidence:** artifact + test · **Status:** tested · **Created:** 2026-09-09

The review covered fairness, reliability, safety, privacy, security, inclusiveness, transparency, and accountability. These concerns appear throughout the portfolio as operational requirements: synthetic data, explicit provenance, bounded claims, visible errors, source links, privacy blocking, authorization flags, and mandatory human review. Project 05 tests that every route requires a human and that marked personal data is blocked. The repository validator also checks for secrets, local paths, large binaries, missing evidence, and misleading credential language. These checks show concrete responsible-AI controls within a small demonstration. They do not constitute a complete impact assessment, security audit, legal compliance review, or proof of fairness across real populations.
