# Day 22 – Transformer Attention From Paper to Experiment

## Topic

**Transformer Attention From Paper to Experiment**

This project explains the self-attention mechanism used by Transformer models and demonstrates it through both a from-scratch NumPy implementation and an experiment using a pre-trained Transformer model.

---

## Research Question

> **How does self-attention help a transformer use context, and where can attention-based explanations become misleading?**

---

## Project Structure

```text
solution/
├── attention_experiment.py
├── README.md
├── report.md
├── toy_attention_weights.png
└── pretrained_attention_sentence1.png
```

---

## Requirements

Python 3.10+ is recommended.

Install the required libraries:

```bash
python -m pip install numpy pandas matplotlib torch transformers
```

The experiment was tested with:

* NumPy
* Matplotlib
* PyTorch
* Hugging Face Transformers

---

## How to Run

Open a terminal inside this `solution` folder and run:

```bash
python attention_experiment.py
```

The program performs the following experiments:

1. Implements single-head scaled dot-product attention from scratch.
2. Calculates attention weights for a toy sentence.
3. Prints attention weights for multiple tokens.
4. Creates a visualization of the toy attention matrix.
5. Loads a pre-trained Transformer model.
6. Inspects attention behavior on five sentences.
7. Performs a pronoun ambiguity experiment.
8. Compares the toy implementation with the pre-trained model.
9. Saves attention visualizations.

---

## From-Scratch Attention

The toy experiment uses the sentence:

```text
The cat sat quietly
```

Query, Key, and Value vectors are manually created to demonstrate the attention mechanism.

The implementation calculates:

```text
Attention(Q,K,V) = softmax(QKᵀ / √dₖ)V
```

The resulting attention weights are printed and visualized.

---

## Pre-trained Transformer Experiment

A pre-trained Transformer model is used to inspect attention behavior on carefully selected sentences.

The experiment includes five sentences designed to test contextual relationships and ambiguity.

The experiment also includes a pronoun-reference test to examine how attention changes when the surrounding context changes.

---

## Output Files

The experiment generates attention visualizations such as:

```text
toy_attention_weights.png
pretrained_attention_sentence1.png
```

These plots show attention weights between tokens.

---

## Important Interpretation Note

Attention weights should not automatically be treated as direct explanations of model reasoning.

A high attention value means that a particular attention head assigned relatively high weight to another token during that computation. It does not by itself prove that the model "understood" the token in a human-like way.

Therefore, the visualizations in this project are treated as evidence about model behavior rather than complete explanations of model reasoning.

---

## Reproducibility

To reproduce the experiment:

```bash
cd assignments/day-22/submissions/Nitin/solution
python attention_experiment.py
```

The first execution may require an internet connection if the pre-trained model has not already been downloaded.

---

## Conclusion

The experiment demonstrates that self-attention allows Transformer models to combine information from different tokens and use contextual relationships when processing a sequence. The toy implementation makes the mathematical mechanism easy to inspect, while the pre-trained model experiment demonstrates that real Transformer attention is more complex and distributed across multiple layers and heads.

Attention visualization is useful for studying model behavior, but it should not be treated as a complete or definitive explanation of model decisions.
