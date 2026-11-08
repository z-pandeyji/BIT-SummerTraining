# Self-attention: context and interpretation

This report was completed during maintainer review because the submitted report file was empty. The accompanying code and sentence dataset are retained from the student's submission.

## Research question

How does self-attention help a transformer use context, and where can attention-based explanations become misleading?

Self-attention constructs each token's representation using information from other positions in the sequence. The amount contributed by each position depends on a compatibility score between learned Query and Key vectors. The resulting weights combine Value vectors. This mechanism can connect nearby and distant tokens without a recurrent step for every relationship. It supports contextual representations, but a bright square in a heatmap is not by itself a causal explanation of a model's answer.

## Mathematics

For an input matrix X, learned projections produce Q = XWq, K = XWk, and V = XWv. The scaled attention calculation is `A = softmax(QKᵀ / sqrt(d_k))`, followed by `O = AV`. Each row of A corresponds to a query position and each column to a key position. Softmax acts separately on each query row, producing nonnegative weights whose sum is one. Scaling the dot products limits their growth as the key dimension increases. In the toy implementation, subtracting the largest score in a row before exponentiation improves numerical stability.

Query describes the information being sought, Key describes what can be matched, and Value is the representation to combine. These descriptions are teaching analogies: the actual vectors are numerical quantities, not explicit English questions. Multi-head attention repeats the operation with different learned projections, concatenates the results, and projects them again. Heads can represent different relationships, but their roles are learned and need not have simple linguistic names.

## Toy experiment

Run `python src/attention_numpy.py`. The sentence is `The cat sat on the mat`. Each token has a manually chosen four-dimensional vector. For this demonstration the same matrix is used directly for Q, K, and V, so the example isolates the matrix operations rather than learning the projections. The script prints the complete attention table, ranks weights for three selected query tokens, prints the combined representations, and saves `results/plots/toy_attention.png`.

The toy weights depend entirely on the supplied vectors. They illustrate similarity weighting and row normalization; they do not establish that the program understands the sentence. Changing the vectors changes the pattern even though the visible words remain the same. This is a useful contrast with a trained model.

## Pretrained experiment

Run `python src/pretrained_attention.py`. The script loads `bert-base-uncased`, uses evaluation mode with gradients disabled, and requests materialized attention matrices with the eager attention implementation. This avoids relying on an optimized backend that may not return the matrices required for inspection.

The dataset contains eight sentences: a cat on a mat, a scientist explaining an experiment, children playing football, a trophy/suitcase pronoun example, a negated movie review, a long-distance book/teacher dependency, and a pair that exchanges the dog and boy as subject and object. This includes more than five sentences and several controlled linguistic contrasts. The script prints tokenizer output and strong connections for each input. It saves a heatmap for the first sentence by averaging the final layer across heads.

These outputs must be read with the script's tokenization. BERT adds special tokens and can split words into subword pieces. The axes therefore do not necessarily align one-to-one with whitespace-delimited words. Averaging heads simplifies the picture but can hide specialized patterns. Inspecting other layers or individual heads can produce a different-looking plot.

## Ambiguity and comparison

In `The trophy did not fit in the suitcase because it was too large`, ordinary world knowledge suggests that `it` refers to the trophy. This experiment checks whether contextual interactions change around that sentence; it does not use a labelled coreference head or score a pronoun-resolution prediction. A strong weight to one noun cannot certify the intended reference. The dog/boy pair offers a complementary test because it holds most vocabulary constant while changing word order.

The NumPy example has no training, learned projections, positional representation, residual paths, or feed-forward layers. BERT uses learned contextual transformations in a stack of transformer layers. Both contain the same scaled dot-product weighting operation, but the pretrained representations reflect training and the surrounding architecture. Their heatmaps should be compared as demonstrations of mechanism, rather than as directly comparable measures of language ability.

## What the visualizations can and cannot show

A heatmap records how one attention operation distributes its weights for a particular input, layer, head selection, model checkpoint, and implementation. It can reveal patterns worth investigating, including special-token concentration or changing interactions after a controlled edit. It cannot alone prove understanding, truthfulness, fairness, or why a final prediction occurred. Information also travels through values, residual connections, and feed-forward components. Different attention distributions can be consistent with similar predictions, as the cited explanation study demonstrates in its investigated settings.

Stronger interpretation would combine controlled input changes, task-level measurements, comparisons across layers and heads, and intervention or attribution experiments. None of those additional causal tests is claimed here. The present scripts are an inspection experiment, not a validated explanation system.

## Reproduction and limitations

Install the declared requirements, run both scripts from the solution directory, and keep the printed output with the generated plots. The pretrained checkpoint requires an initial network download and substantially more memory than the toy example. Evaluation mode removes dropout randomness; versions and the downloaded checkpoint should still be recorded for strict reproducibility. CPU execution is supported. The small, hand-selected sentence set does not establish general performance, and the report does not invent numerical pretrained results or claim a student's unrecorded experiment.

## Sources

1. Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762): transformer attention, scaling, and multiple heads.
2. Devlin et al., [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805): pretrained bidirectional contextual representations.
3. Jain and Wallace, [Attention is not Explanation](https://aclanthology.org/N19-1357/): limitations of treating attention distributions as prediction explanations.

Source pages checked during maintainer review on 8 November 2026.
