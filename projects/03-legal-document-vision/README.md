# Legal Document Vision Demonstrator

This pure-Python demonstrator localizes two predefined dark fields on a tiny synthetic document page, compares bounding boxes with gold coordinates using intersection over union (IoU), and replaces located pixels with a neutral redaction value. It applies lessons 6–12 through image representation, local neighborhoods, localization, segmentation, and explicit evaluation. Run `python vision.py`; inspect [results.json](results.json); run `python -m unittest test_vision.py`.

The input is an openly inspectable ASCII PGM file created for this portfolio. Connected components are detected by a fixed intensity threshold; no OCR, neural network, pretrained component, or third-party dependency is used. Perfect IoU here means only that deterministic rectangles were recovered from one constructed image. It is not an accuracy claim for scans, handwriting, photographs, or real documents.

Real redaction requires OCR/layout evaluation, adversarial review, secure removal of underlying content and metadata, and human confirmation. See [AUTHORSHIP.md](AUTHORSHIP.md).
