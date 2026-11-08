# Day 22 Research Report

## Transformer Attention From Paper to Experiment

### Research Question

> **How does self-attention help a transformer use context, and where can attention-based explanations become misleading?**

---

# 1. Introduction

Transformers are neural network architectures that process sequences using attention mechanisms. Unlike traditional sequential models that process tokens one at a time, Transformers can directly compare different tokens in a sequence.

Self-attention is one of the central mechanisms behind Transformer models. It allows each token to assign different importance to other tokens while constructing its contextual representation.

For example, in the sentence:

```text
The cat sat quietly.
```

the representation of `cat` can incorporate information from `The`, `sat`, and `quietly`.

This project studies self-attention at two levels:

1. A small from-scratch implementation using NumPy.
2. An experiment using a pre-trained Transformer model.

The goal is to connect the mathematical definition of attention with observable model behavior.

---

# 2. Query, Key, and Value

Self-attention uses three representations:

## Query (Q)

A Query represents what information a token is looking for.

For example, a token can use its Query representation to determine which other tokens are relevant to its current context.

## Key (K)

A Key represents information that can be matched against a Query.

The Query and Key are compared using a dot product.

A larger similarity score indicates that the corresponding token may receive greater attention.

## Value (V)

The Value contains the information that is actually combined to produce the output representation.

The attention weights are used to calculate a weighted combination of the Value vectors.

Therefore:

```text
Query → What am I looking for?
Key   → What information do I contain?
Value → What information should I provide?
```

---

# 3. Scaled Dot-Product Attention

The core attention operation is:

```text
Attention(Q,K,V) = softmax(QKᵀ / √dₖ)V
```

where:

* `Q` = Query matrix
* `K` = Key matrix
* `V` = Value matrix
* `dₖ` = dimensionality of the Key vectors

The calculation occurs in several stages.

### Step 1: Calculate QKᵀ

The Query and Key matrices are multiplied.

This produces similarity scores between tokens.

### Step 2: Scale the scores

The scores are divided by:

```text
√dₖ
```

Scaling helps keep the values in a suitable range before applying softmax.

### Step 3: Apply Softmax

Softmax converts the scores into probabilities or normalized weights.

For each query token, the attention weights approximately sum to 1.

### Step 4: Multiply by V

The normalized attention weights are multiplied by the Value matrix.

This produces a context-aware output representation.

---

# 4. Softmax

Softmax converts a group of numerical scores into normalized values.

For a vector of scores:

```text
softmax(xᵢ) = exp(xᵢ) / Σ exp(xⱼ)
```

The output values are between 0 and 1 and sum to approximately 1.

In self-attention, these values act as weights showing how strongly a query token attends to different key tokens.

---

# 5. Multi-Head Attention

Real Transformer models generally use multi-head attention instead of only one attention mechanism.

Different attention heads can learn different relationships.

For example, one head may focus strongly on:

* syntactic relationships,
* nearby words,
* pronoun references,
* long-distance relationships,
* or other contextual patterns.

The outputs of the attention heads are combined and transformed.

A simplified representation is:

```text
MultiHead(Q,K,V)
=
Concat(head₁, head₂, ..., headₕ)Wᴼ
```

where each head performs an attention operation using its own learned projections.

This allows the model to represent multiple types of relationships simultaneously.

---

# 6. From-Scratch Experiment

The first experiment implements single-head scaled dot-product attention using NumPy.

The toy sentence is:

```text
The cat sat quietly
```

The four tokens are:

```text
The
cat
sat
quietly
```

Small manually created Query, Key, and Value vectors are used.

These vectors are intentionally simple so that the mathematical operations can be inspected easily.

They are not learned representations from a real Transformer.

---

# 7. Toy Attention Results

The program calculated the following attention weights:

```text
Attention Weights:

[[0.334 0.203 0.203 0.260]
 [0.157 0.427 0.259 0.157]
 [0.150 0.248 0.409 0.193]
 [0.265 0.206 0.265 0.265]]
```

The rows represent query tokens and the columns represent tokens being attended to.

For example, the `cat` token produced approximately:

```text
The      → 0.157
cat      → 0.427
sat      → 0.259
quietly  → 0.157
```

The largest weight is assigned to `cat` itself in this manually constructed example.

For `sat`:

```text
The      → 0.150
cat      → 0.248
sat      → 0.409
quietly  → 0.193
```

Again, the largest weight is assigned to the current token.

These values demonstrate how the mathematical attention mechanism produces a different weighted context for each token.

---

# 8. Toy Attention Visualization

The script saves the attention matrix as:

```text
toy_attention_weights.png
```

The visualization represents:

* rows = query/current tokens
* columns = key tokens being attended to
* cell intensity = attention weight

The visualization makes the attention distribution easier to compare than the numerical matrix alone.

---

# 9. Pre-trained Transformer Experiment

The second experiment uses a pre-trained Transformer model.

The purpose is to observe attention behavior on real model representations rather than manually created toy vectors.

Five carefully selected sentences were used.

The sentences were designed to include contextual relationships and different linguistic structures.

The experiment inspects attention values produced by the pre-trained model and saves a visualization.

The generated output includes:

```text
pretrained_attention_sentence1.png
```

---

# 10. Five-Sentence Experiment

The five sentences were selected to test different contextual situations.

The experiment demonstrates that attention distributions can change depending on the words surrounding a token.

This is important because the meaning or role of a token can depend heavily on its context.

For example, a word such as:

```text
bank
```

can refer to a financial institution or the side of a river depending on the surrounding words.

A contextual model can use surrounding tokens to represent such differences.

---

# 11. Ambiguity Test: Pronoun Reference

A pronoun-reference experiment was included.

Consider examples where a pronoun can refer to different entities depending on the surrounding context.

For example:

```text
The trophy did not fit in the suitcase because it was too large.
```

and:

```text
The trophy did not fit in the suitcase because it was too small.
```

The surrounding context changes the likely interpretation of the pronoun.

The experiment examines whether attention patterns change when the context changes.

This demonstrates that Transformer representations are contextual rather than completely independent for each word.

However, an attention pattern alone does not prove that the model has correctly resolved the pronoun.

---

# 12. Toy Implementation vs Pre-trained Transformer

The two experiments demonstrate different aspects of self-attention.

| Aspect          | Toy Implementation      | Pre-trained Transformer       |
| --------------- | ----------------------- | ----------------------------- |
| Vectors         | Manually created        | Learned model representations |
| Number of heads | Single head             | Multiple attention heads      |
| Purpose         | Understand mathematics  | Study real model behavior     |
| Complexity      | Very small              | Large and distributed         |
| Interpretation  | Easy to inspect         | More difficult                |
| Learning        | No training             | Pre-trained model             |
| Visualization   | Direct attention matrix | Model attention patterns      |

The toy implementation is useful for understanding the mathematical calculation.

The pre-trained experiment is more realistic because the representations and attention projections were learned during model training.

---

# 13. What Attention Helps a Transformer Do

Self-attention helps a Transformer use context by allowing token representations to incorporate information from other tokens.

Instead of treating every token independently, the model can calculate relationships between tokens.

This is especially useful for:

* contextual word representations,
* syntactic relationships,
* pronoun references,
* long-distance dependencies,
* word-order effects,
* and relationships between different parts of a sentence.

Because every token can potentially interact with other tokens in the sequence, the model can build context-aware representations.

---

# 14. What Attention Visualizations Can Show

Attention visualizations can provide useful information about model behavior.

They can show:

1. Which tokens receive relatively high attention weights.
2. How attention differs between tokens.
3. How attention patterns change across sentences.
4. How different attention heads may behave differently.
5. Whether contextual changes are associated with changes in attention patterns.

These observations can help researchers formulate hypotheses about what a model is doing.

---

# 15. What Attention Visualizations Cannot Prove

Attention should not automatically be treated as a complete explanation of model reasoning.

A high attention weight does not necessarily mean:

```text
"The model used this token as the reason for its final prediction."
```

Attention is only one component of the Transformer computation.

Other factors include:

* value representations,
* output projections,
* feed-forward layers,
* residual connections,
* layer normalization,
* multiple layers,
* and interactions between multiple attention heads.

Therefore, attention visualization should be interpreted as evidence about model computation rather than a definitive explanation of model reasoning.

---

# 16. Limitations

## 16.1 Toy Vectors

The from-scratch experiment uses manually created vectors.

They do not represent learned linguistic features.

Therefore, the toy experiment demonstrates the attention calculation but does not reproduce the behavior of a trained Transformer.

## 16.2 Small Sample Size

Only five sentences were used in the pre-trained experiment.

This is not enough to make broad claims about Transformer behavior.

A larger evaluation set would provide stronger evidence.

## 16.3 Attention Is Not a Complete Explanation

Attention weights alone cannot fully explain a model's output.

Other layers and computations also influence the final representation and prediction.

## 16.4 Model-Specific Behavior

Different Transformer architectures and models can produce different attention patterns.

Therefore, results from one model should not automatically be generalized to all Transformer models.

## 16.5 Visualization Limitations

Heatmaps simplify complex numerical computations into visual patterns.

A visually strong relationship does not necessarily imply a causal relationship.

---

# 17. Research Question Answer

### How does self-attention help a transformer use context, and where can attention-based explanations become misleading?

Self-attention helps a Transformer use context by allowing every token to compare its Query representation with the Key representations of other tokens. The resulting attention weights are used to combine Value representations, producing context-aware representations.

The toy experiment demonstrates this mechanism directly through the scaled dot-product attention equation.

The pre-trained Transformer experiment demonstrates that real models use learned representations and multiple attention operations to process contextual relationships.

However, attention-based explanations can become misleading when attention weights are interpreted as direct evidence of model reasoning. A high attention value indicates a computational relationship within an attention layer, but it does not by itself prove why the model produced a particular output or that the model understood a linguistic relationship correctly.

Therefore, attention visualization is a useful diagnostic tool, but it should be combined with other experiments and evaluation methods before making strong claims about model reasoning.

---

# 18. Conclusion

This project connected the mathematical definition of self-attention with a practical experiment.

The from-scratch NumPy implementation demonstrated:

```text
QKᵀ → Scaling → Softmax → Weighted Values
```

The pre-trained Transformer experiment demonstrated how attention patterns can be inspected on real sentences.

The ambiguity experiment showed why context matters when interpreting language.

Overall, self-attention provides Transformers with an effective mechanism for combining information across a sequence. At the same time, attention visualizations should be interpreted carefully because they provide only a partial view of the computations occurring inside a Transformer.

---

# 19. References

1. Vaswani, A. et al. (2017). **Attention Is All You Need.** Advances in Neural Information Processing Systems.

   https://arxiv.org/abs/1706.03762

2. Hugging Face Transformers Documentation.

   https://huggingface.co/docs/transformers/

3. PyTorch Documentation – MultiheadAttention.

   https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html

4. Google Research – Transformer Architecture.

   https://research.google/pubs/attention-is-all-you-need/

5. Lilian Weng. **Attention? Attention!**

   https://lilianweng.github.io/posts/2018-06-24-attention/

---

# 20. Reproducibility

From the project directory, run:

```bash
python attention_experiment.py
```

The script performs the toy attention experiment and the pre-trained Transformer experiment.

Expected generated visualizations include:

```text
toy_attention_weights.png
pretrained_attention_sentence1.png
```

The exact numerical attention values can vary depending on the selected model, tokenizer, implementation details, and execution environment.
