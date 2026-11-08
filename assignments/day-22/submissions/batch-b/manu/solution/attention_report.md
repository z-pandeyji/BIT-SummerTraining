\# Transformer Attention From Paper to Experiment



\## Research Question



> How does self-attention help a transformer use context, and where can attention-based explanations become misleading?



\---



\## 1. Introduction



Transformer models have become one of the most important architectures in modern natural language processing. Unlike traditional recurrent neural networks, Transformers can process relationships between tokens using attention mechanisms.



The central idea of self-attention is that every token in a sequence can compare itself with other tokens and selectively combine information from them. As a result, the representation of a word can depend on the complete sentence context.



For example, the meaning of a word can change depending on the words surrounding it. In:



> The movie was good.



the word "good" has a positive context. However, in:



> The movie was not good.



the word "not" changes the meaning of the sentence.



Self-attention provides a mechanism through which tokens can interact with other tokens. This report explains the mathematical operation of self-attention, implements scaled dot-product attention from scratch, and compares the toy implementation with attention behavior observed in a pretrained Transformer model.



\---



\# 2. Query, Key, and Value



Self-attention uses three representations:



\* Query (Q)

\* Key (K)

\* Value (V)



For an input representation matrix X, the Transformer computes:



```text

Q = XW\_Q

K = XW\_K

V = XW\_V

```



where:



\* `W\_Q` is the Query projection matrix;

\* `W\_K` is the Key projection matrix;

\* `W\_V` is the Value projection matrix.



\## Query



A Query represents the information that a token is looking for.



For example, when processing a pronoun such as "it", the model may need information from other tokens to construct its contextual representation.



\## Key



A Key represents information used for matching.



A Query is compared with Keys to calculate how relevant different tokens are to one another.



\## Value



A Value contains the information that is actually aggregated after attention scores have been calculated.



Therefore, the simplified process is:



```text

Query asks:

"What information is relevant?"



Key provides:

"How relevant am I to this query?"



Value provides:

"The information that should be passed forward."

```



\---



\# 3. Scaled Dot-Product Attention



The core equation of Transformer attention is:



```text

Attention(Q, K, V)

=

softmax(QKᵀ / √dₖ)V

```



The calculation occurs in several steps.



\## Step 1: Calculate Query-Key Similarity



The matrix multiplication:



```text

QKᵀ

```



computes the similarity between every Query and every Key.



If the Query of one token is similar to the Key of another token, the corresponding score becomes relatively large.



This creates a score matrix in which:



\* rows correspond to Query tokens;

\* columns correspond to Key tokens.



\---



\## Step 2: Scale the Scores



The similarity scores are divided by:



```text

√dₖ

```



where `dₖ` is the dimension of the Key vectors.



The scaling step prevents the dot products from becoming excessively large as the vector dimension increases.



Without scaling, the softmax function could become extremely concentrated on a small number of values.



\---



\## Step 3: Apply Softmax



The softmax function converts the scores into normalized attention weights:



```text

softmax(xᵢ)

=

exp(xᵢ) / Σ exp(xⱼ)

```



The values in each attention row are non-negative and sum to approximately 1.



For example, a token might distribute its attention as:



```text

Token A: 0.10

Token B: 0.50

Token C: 0.25

Token D: 0.15

```



This means that the Value representations are combined using these weights.



\---



\## Step 4: Weighted Sum of Values



Finally:



```text

softmax(QKᵀ / √dₖ)V

```



produces a new contextual representation.



This representation contains information from other tokens, weighted according to their relevance.



\---



\# 4. From-Scratch Single-Head Attention Implementation



The experiment implemented scaled dot-product attention using NumPy.



The toy sentence was:



> The cat sat on the mat.



The implementation uses small manually created vector representations.



The main computation is:



```python

scores = Q @ K.T / sqrt(d\_k)



attention\_weights = softmax(scores)



output = attention\_weights @ V

```



The experiment produced the following attention matrix:



| Query |   The |   cat |   sat |    on |   the |   mat |

| ----- | ----: | ----: | ----: | ----: | ----: | ----: |

| The   | 0.197 | 0.200 | 0.139 | 0.131 | 0.197 | 0.138 |

| cat   | 0.175 | 0.215 | 0.155 | 0.131 | 0.175 | 0.149 |

| sat   | 0.138 | 0.176 | 0.208 | 0.146 | 0.138 | 0.194 |

| on    | 0.149 | 0.170 | 0.167 | 0.195 | 0.149 | 0.170 |

| the   | 0.197 | 0.200 | 0.139 | 0.131 | 0.197 | 0.138 |

| mat   | 0.141 | 0.175 | 0.200 | 0.153 | 0.141 | 0.190 |



The rows represent Query tokens and the columns represent Key tokens.



For example, the attention distribution for `cat` was:



```text

cat: 0.215

the: 0.175

The: 0.175

```



The highest attention value was directed toward `cat` itself.



For `sat`, the strongest attention values were:



```text

sat: 0.208

mat: 0.194

cat: 0.176

```



For `mat`, the strongest attention values were:



```text

sat: 0.200

mat: 0.190

cat: 0.175

```



These values demonstrate that each token can distribute its attention across the complete sentence.



The generated heatmaps are:



```text

diagrams/toy\_attention\_heatmap.png

diagrams/three\_token\_attention.png

```



\---



\# 5. Multi-Head Attention



A Transformer does not usually rely on only one attention mechanism.



Instead, it uses multiple attention heads.



For each head:



```text

headᵢ =

Attention(QWᵢᴽ, KWᵢᴷ, VWᵢⱽ)

```



The outputs of the heads are concatenated:



```text

MultiHead(Q,K,V)

=

Concat(head₁, head₂, ..., headₕ)Wᴼ

```



Different attention heads can potentially capture different relationships.



For example, different heads may focus on:



\* local word relationships;

\* grammatical relationships;

\* subject-verb dependencies;

\* pronoun relationships;

\* long-distance dependencies.



Multi-head attention allows the model to process several types of relationships simultaneously.



However, the interpretation of individual heads is not always straightforward. A high attention value in one head does not automatically mean that the head has a simple human-interpretable function.



\---



\# 6. Pretrained Transformer Experiment



A pretrained `distilbert-base-uncased` Transformer model was used for the experimental analysis.



The model was tested on multiple carefully selected sentences.



The experiment included:



1\. Basic contextual sentence:



&#x20;  > The cat sat on the mat.



2\. Pronoun and context examples:



&#x20;  > The dog chased the ball because it was excited.



&#x20;  > The dog chased the ball because it was tired.



3\. Word-order and grammatical-role example:



&#x20;  > The teacher gave the student a book.



4\. Scientific context:



&#x20;  > The scientist studied the virus in the laboratory.



5\. Long-distance grammatical dependency:



&#x20;  > The keys to the cabinet are on the table.



&#x20;  > The keys to the cabinet is on the table.



6\. Negation:



&#x20;  > The movie was not good.



&#x20;  > The movie was good.



7\. Relative-clause structure:



&#x20;  > The boy who the girl saw was smiling.



The model produced tokenized representations and attention matrices for these sentences.



The attention matrices were saved in:



```text

outputs/pretrained\_attention\_results.csv

```



The ambiguity visualization was saved in:



```text

diagrams/pretrained\_ambiguity\_attention.png

```



\---



\# 7. Ambiguity Test: Pronoun and Context



The following sentences were compared:



> The dog chased the ball because it was excited.



> The dog chased the ball because it was tired.



The pronoun `it` requires contextual interpretation.



The sentence contains two possible noun candidates:



\* dog;

\* ball.



The surrounding context can influence the contextual representation of the pronoun.



The experiment inspected the attention matrix of the Transformer for both sentences.



The important observation is that changing the surrounding context can change the internal representations and attention patterns.



However, the result should not be interpreted as proof that the model has explicitly performed human-like pronoun resolution.



The attention matrix only shows the distribution of attention values within the model.



\---



\# 8. Ambiguity Test: Negation



The following pair was compared:



> The movie was good.



> The movie was not good.



The addition of the word `not` changes the meaning of the sentence.



The tokenization changed from:



```text

\[CLS] the movie was good . \[SEP]

```



to:



```text

\[CLS] the movie was not good . \[SEP]

```



The model therefore processes a different sequence and produces different contextual representations.



This demonstrates how the presence of a small but semantically important token can affect the contextual processing of the sentence.



The important limitation is that an attention visualization alone cannot establish exactly how the model internally represents negation or whether a particular attention edge is responsible for the final semantic interpretation.



\---



\# 9. Long-Distance Dependency and Agreement



The following sentences were compared:



> The keys to the cabinet are on the table.



> The keys to the cabinet is on the table.



The grammatical subject is:



```text

keys

```



The phrase:



```text

to the cabinet

```



is an intervening phrase.



The correct grammatical agreement is:



```text

keys ... are

```



rather than:



```text

keys ... is

```



This type of example tests whether the model can represent relationships across intervening words.



The sentences contain similar tokens but differ in the verb:



```text

are

```



versus:



```text

is

```



The experiment demonstrates that Transformers can process relationships between tokens that are not necessarily adjacent.



However, attention patterns alone cannot prove that the model has learned a symbolic grammar rule identical to a human grammatical rule.



\---



\# 10. Sentence-Level Hidden-State Behavior



The experiment also measured the mean norm of hidden-state representations for different sentences.



Examples included:



```text

The cat sat on the mat.

Mean hidden-state norm: 12.4149

```



```text

The movie was not good.

Mean hidden-state norm: 12.6595

```



```text

The movie was good.

Mean hidden-state norm: 12.6673

```



These values demonstrate that the model produces different internal numerical representations for different input sentences.



However, the magnitude of a hidden-state vector by itself does not provide a complete semantic explanation.



A larger hidden-state norm does not necessarily mean that a sentence is more important, more meaningful, or better understood by the model.



\---



\# 11. Comparison Between Toy and Pretrained Attention



| Feature               | Toy Implementation                 | Pretrained Transformer                   |

| --------------------- | ---------------------------------- | ---------------------------------------- |

| Input representations | Manually designed vectors          | Learned model representations            |

| Attention type        | Single-head                        | Multi-layer Transformer attention        |

| Query, Key, Value     | Directly supplied                  | Produced through learned transformations |

| Training              | No training                        | Pretrained on large text corpora         |

| Vocabulary            | Six toy tokens                     | Natural language tokenizer               |

| Context               | Small controlled example           | Real linguistic sentences                |

| Interpretability      | Relatively simple                  | Much more complex                        |

| Purpose               | Demonstrate mathematical mechanism | Study learned model behavior             |



The toy experiment is useful for understanding the mathematical operation of attention.



For example:



```text

QKᵀ

```



creates similarity scores.



Then:



```text

softmax(...)

```



creates attention weights.



Finally:



```text

attention\_weights @ V

```



creates contextualized representations.



The pretrained model is more complex.



It contains:



\* learned embeddings;

\* multiple Transformer layers;

\* multiple attention heads;

\* residual connections;

\* feed-forward neural networks;

\* layer normalization.



Therefore, the toy experiment explains the mechanism clearly, while the pretrained experiment demonstrates how the mechanism appears inside a real language model.



\---



\# 12. How Self-Attention Helps Transformers Use Context



Self-attention helps a Transformer use context by allowing every token to interact with other tokens in the sequence.



A token does not have to depend only on its immediate neighbors.



For example, in:



> The keys to the cabinet are on the table.



the subject `keys` and the verb `are` are separated by several tokens.



Self-attention provides a direct mechanism through which information from different positions can interact.



This allows the model to build contextual representations.



The same word can therefore receive different representations in different contexts.



For example:



```text

The movie was good.

```



and:



```text

The movie was not good.

```



contain overlapping words but have different meanings.



Self-attention allows the model to combine information from the surrounding sequence.



This is one of the fundamental reasons why Transformers are effective at language processing.



\---



\# 13. What Attention Visualizations Can Show



Attention visualizations can be useful for studying:



\* which tokens receive relatively high attention weights;

\* whether attention is concentrated locally or distributed across a sentence;

\* how attention patterns change when context changes;

\* how different sentences produce different attention matrices;

\* whether tokens at distant positions can interact;

\* how different attention heads may behave differently.



Attention visualizations are particularly useful as diagnostic tools.



They can help researchers generate hypotheses about how information may be flowing through a model.



For example, if a pronoun attends strongly to a noun in a particular layer or head, this may suggest that the model is using information related to that noun.



\---



\# 14. What Attention Visualizations Cannot Prove



Attention visualizations should not automatically be considered complete explanations of model decisions.



A high attention value does not necessarily prove that:



\* the attended token caused the final output;

\* the token was the most important feature;

\* the model consciously selected the token;

\* the model understood the human meaning of the sentence;

\* the model performed explicit symbolic reasoning;

\* the attention pattern is a causal explanation.



Attention is only one part of a Transformer computation.



The final representation may also depend on:



\* other attention heads;

\* other Transformer layers;

\* residual connections;

\* feed-forward networks;

\* layer normalization;

\* learned embeddings;

\* nonlinear transformations.



Therefore, an attention map should be interpreted as evidence about one aspect of information interaction rather than as a complete explanation of the model's reasoning process.



\---



\# 15. Why Attention-Based Explanations Can Be Misleading



There are several reasons attention explanations can be misleading.



\## 15.1 Attention Is Not Necessarily Causal



A token can receive high attention without being the actual cause of the final prediction.



The model may use information from multiple pathways.



Therefore, correlation between attention weight and output importance does not automatically establish causality.



\---



\## 15.2 Averaging Can Hide Important Behavior



In the experiment, attention from multiple heads may be averaged for visualization.



However, averaging can hide differences between individual heads.



One head may focus on a particular grammatical relationship while another focuses on local context.



The average may therefore produce a pattern that no individual head actually represents.



\---



\## 15.3 Multiple Layers Contribute



A Transformer contains multiple layers.



A relationship that appears in one layer may be transformed by later layers.



Therefore, inspecting only the final layer does not provide a complete picture of the model's computation.



\---



\## 15.4 High Attention Does Not Mean Human-Like Understanding



A model may produce a high attention weight for a token because of learned statistical patterns.



This does not prove that the model understands the sentence in the same way as a human.



Attention values are numerical components of a neural computation.



They should not automatically be interpreted as conscious focus or human reasoning.



\---



\# 16. Limitations of This Experiment



This experiment has several limitations.



\### 1. Toy Representations



The from-scratch experiment uses manually designed vectors.



These vectors are useful for demonstrating the mathematics but do not represent real learned language embeddings.



\### 2. Limited Number of Sentences



Although the experiment uses more than the required five sentences, it is still a small dataset.



The results should not be generalized to all language.



\### 3. Model Architecture



The pretrained experiment uses DistilBERT.



Results may differ for other Transformer architectures and models.



\### 4. Attention Interpretation



Attention weights are difficult to interpret directly.



A visualization can show numerical relationships but cannot by itself prove a complete reasoning process.



\### 5. Tokenization



The Transformer works with tokens produced by a tokenizer.



A single natural-language word may sometimes be represented as multiple subword tokens.



Therefore, interpretation at the word level may not always exactly match the model's actual token-level computation.



\---



\# 17. Conclusion



Self-attention helps Transformers use context by allowing each token to compare its Query with the Keys of other tokens and combine their Values.



The fundamental operation is:



```text

Attention(Q, K, V)

=

softmax(QKᵀ / √dₖ)V

```



The from-scratch NumPy implementation demonstrated this operation on the sentence:



> The cat sat on the mat.



The attention matrix showed how each token distributed weights across other tokens.



The pretrained Transformer experiment demonstrated attention and hidden-state behavior on multiple natural-language sentences involving:



\* pronoun ambiguity;

\* negation;

\* grammatical agreement;

\* word relationships;

\* long-distance dependencies.



The experiments show that contextual information can affect the internal representations produced by a Transformer.



However, attention visualizations must be interpreted carefully.



Attention weights can provide useful information about token interactions and information routing, but they are not automatically complete causal explanations of model predictions.



The answer to the research question is therefore:



> Self-attention helps a Transformer use context by allowing tokens to dynamically exchange information with other tokens in the sequence. This creates contextual representations that can reflect relationships across both nearby and distant positions. However, attention-based explanations can become misleading when attention weights are treated as direct evidence of importance, causality, reasoning, or human-like understanding. Attention should therefore be used as a diagnostic signal rather than as a complete explanation of a model's behavior.



\---



\# References



1\. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. (2017).

&#x20;  \*\*Attention Is All You Need.\*\*

&#x20;  arXiv:1706.03762.



2\. Google Research.

&#x20;  \*\*Attention Is All You Need.\*\*

&#x20;  Transformer architecture and self-attention research.



3\. Hugging Face.

&#x20;  \*\*Transformers Documentation.\*\*

&#x20;  Documentation for pretrained Transformer models, tokenizers, hidden states, and attention outputs.



4\. Jain, S. and Wallace, B. C. (2019).

&#x20;  \*\*Attention is not Explanation.\*\*

&#x20;  arXiv:1902.10186.



5\. Clark, K., Khandelwal, U., Levy, O., and Manning, C. D. (2019).

&#x20;  \*\*What Does BERT Look At? An Analysis of BERT's Attention.\*\*

&#x20;  Proceedings of the Third BlackboxNLP Workshop.



