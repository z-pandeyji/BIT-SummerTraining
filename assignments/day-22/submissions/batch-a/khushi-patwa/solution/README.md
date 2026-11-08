# Day 22 — Transformer Attention From Paper to Experiment

## Overview

This project studies self-attention in Transformer models from both a mathematical and experimental perspective.

It contains:

1. A from-scratch NumPy implementation of scaled dot-product self-attention.
2. Attention weights for a small toy sentence.
3. A pretrained BERT experiment using `bert-base-uncased`.
4. Attention visualization for the pretrained Transformer.
5. Test sentences covering normal context, pronoun reference, negation, and other linguistic cases.
6. A technical research report and attention mechanism diagram.

## Project Structure

```text
solution/
├── README.md
├── requirements.txt
├── data/
│   └── test_sentences.json
├── diagrams/
│   └── attention_mechanism.md
├── report/
│   └── report.md
├── results/
│   └── plots/
│       ├── toy_attention.png
│       └── pretrained_attention.png
└── src/
    ├── attention_numpy.py
    ├── pretrained_attention.py
    └── utils.py
```

Run from this solution directory:

```bash
python -m pip install -r requirements.txt
python src/attention_numpy.py
python src/pretrained_attention.py
```

The pretrained experiment downloads BERT on its first run. See report/report.md for interpretation and limitations.
