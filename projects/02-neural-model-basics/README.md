# Neural Model Basics for Legal Classification

This experiment compares a fixed keyword bag-of-words baseline with a multiclass single-layer perceptron on 21 synthetic legal-intake phrases. It applies lessons 3–5: perceptrons, learning weights from examples, fixed train/test evaluation, and overfitting awareness. Run `python classifier.py`; inspect [results.json](results.json); run `python -m unittest test_classifier.py`.

The split is fixed in the dataset, training shuffle uses seed 17, and both models receive lowercased word tokens. The baseline encodes hand-picked keywords. The perceptron updates one weight vector per class for 12 epochs. This makes the comparison small enough to inspect but also highly unstable: six test examples are not evidence of generalization, and training performance may exceed test performance because rare words and paraphrases are poorly covered.

This is a learning demonstration, not a deployable classifier or a claim of ML-engineering proficiency. A human must classify ambiguous or consequential requests. See [AUTHORSHIP.md](AUTHORSHIP.md).
