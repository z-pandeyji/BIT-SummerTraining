# Day 18 Assignment

## Topic: How Transformers Understand Text

## Question 1

A language model trained **from scratch** requires a very large amount of high-quality training data. It also requires significant computing resources, expensive hardware, and a long training time because the model must learn language patterns from the beginning.

A **pre-trained model** has already learned general language patterns from a large dataset. It usually requires less data, lower computing cost, and less training time for a specific task.

One reason to choose a pre-trained model is that it saves time and resources because we can adapt an already trained model instead of building one from zero.

---

## Question 2

The sequence is:

```text
I -> love -> machine -> learning
```

### RNN or LSTM

An RNN processes the sequence one token at a time:

```text
I -> hidden state 1
love -> hidden state 2
machine -> hidden state 3
learning -> hidden state 4
```

The hidden state carries information from previous tokens to the next step. For example, when processing `machine`, the model can use information about `I` and `love`.

An LSTM is a type of RNN that uses special gates to decide what information to remember and what information to forget. This helps it handle longer sequences better than a basic RNN.

### Transformer

A transformer can examine relationships between many tokens at the same time using self-attention:

```text
I <-> love <-> machine <-> learning
```

Instead of processing every token strictly one after another, the transformer can calculate many token relationships in parallel. This makes training more efficient and helps the model understand relationships between words in a sentence.

---

## Question 3

The process is:

```text
Text -> Tokens -> Embeddings -> Transformer layers -> Output
```

### 1. Text

The original human-readable sentence is:

```text
I love AI
```

### 2. Tokens

The sentence is divided into smaller units called tokens.

A simple classroom token list could be:

```text
["I", "love", "AI"]
```

A real tokenizer may divide text differently and may split some words into smaller pieces.

### 3. Embeddings

Each token is converted into a numerical vector called an embedding.

For example:

```text
"I"    -> vector representing information about the token
"love" -> vector representing its meaning and relationships
"AI"   -> vector representing its meaning and relationships
```

These vectors are not just simple dictionary definitions. They represent useful semantic and contextual information that the model can process mathematically.

### 4. Transformer Layers

The embeddings pass through transformer layers. Self-attention helps the model examine relationships between tokens, while other layers transform and refine the information.

### 5. Output

The final processed representation can be used to produce an output, such as the next token, an answer, a classification, or another generated result.

---

## Question 4

Compare:

```text
Dog bites man.
Man bites dog.
```

Both sentences contain the same words, but their meanings are different because the word order changes.

In:

```text
Dog bites man.
```

the dog is performing the action and the man is receiving the action.

In:

```text
Man bites dog.
```

the man is performing the action and the dog is receiving the action.

A transformer uses positional information to understand where each token appears in the sequence. Without positional information, the model could know which words are present but would have more difficulty understanding their order.

```text
Word meaning + Position information = Better understanding of the sentence
```

---

## Question 5

The sentence is:

```text
The animal did not cross the road because it was tired.
```

The word `it` most likely refers to **the animal** because an animal can be tired and this explanation makes sense in the context of the sentence.

The surrounding words help the model understand this reference:

```text
The animal -> did not cross -> the road -> because -> it was tired
```

Attention is useful because it allows the model to compare `it` with earlier words in the sentence. It can give more attention to words that are relevant to understanding the meaning of `it`.

---

## Question 6

The sentence is:

```text
The cat sat on the mat because it was tired.
```

### Query: What am I looking for?

When the model processes `it`, the Query represents what information is needed to understand the meaning of `it`.

The model may be looking for a possible subject or noun that `it` refers to.

### Key: What information is available?

The Keys represent information about the other tokens:

```text
cat
mat
sat
tired
```

The model compares the Query for `it` with the Keys of these words.

### Value: What information should be passed forward?

The Values contain the information that can be passed forward after the model decides which tokens are relevant.

A simple representation is:

```text
Query -> What am I looking for?
Key   -> What information is available?
Value -> What information should be passed forward?
```

The word `cat` should receive more attention than `mat` when interpreting `it` because `cat` is a living subject that can naturally be tired. The word `mat` is an object and is much less likely to be the thing that is tired in this sentence.

Therefore:

```text
it -> more attention to cat
it -> less attention to mat
```

---

## Question 7

The simplified attention formula is:

```text
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

### High Attention Score

A high attention score means that two tokens are considered strongly related for the current context.

For example, when interpreting a pronoun, a high score may indicate that a particular noun is a strong possible reference.

### Low Attention Score

A low attention score means that the token is considered less relevant to the current token or task.

### Why is Softmax Useful?

Softmax converts the attention scores into normalized weights. These weights make it easier for the model to determine how much attention should be given to each token.

For example:

```text
Token A -> high weight
Token B -> medium weight
Token C -> low weight
```

### Why Apply the Scores to the Values?

The attention weights are applied to the Values so that the model can create a weighted combination of the most useful information.

In simple terms:

```text
Find relevant information
        ↓
Give important information higher weight
        ↓
Combine the useful information
```

---

## Question 8

The sentence is:

```text
The student solved the problem because he understood the concept.
```

Different attention heads can focus on different relationships.

### Head 1: Grammar

This head could examine grammatical relationships such as:

```text
student -> solved
he -> understood
```

It may help identify the subject and action in the sentence.

### Head 2: Subject-Object Relationships

This head could examine:

```text
student -> problem
```

The student is the person who solved the problem.

### Head 3: Meaning

This head could connect:

```text
understood the concept -> solved the problem
```

Understanding the concept provides a meaningful reason for successfully solving the problem.

### Head 4: Pronoun Reference

This head could examine:

```text
he -> student
```

It helps determine that `he` most likely refers to the student.

### Why Multiple Heads Are Useful

Several attention heads can examine different relationships at the same time. One head may focus on grammar, another on meaning, and another on pronoun references.

Together, these different perspectives can help the transformer build a richer understanding of the sentence than a single attention mechanism might provide.

---

## Question 9

A simplified transformer block can be represented as:

```text
+--------------------------------------+
| Embeddings + Positional Encoding    |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
| Multi-Head Self-Attention            |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
| Add & Norm                           |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
| Feed-Forward Network                 |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
| Add & Norm                           |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
| Output to the next layer             |
+--------------------------------------+
```

### Purpose of the Attention Part

Multi-Head Self-Attention allows each token to examine other tokens and identify important relationships within the sequence. Different attention heads can focus on different types of relationships.

### Purpose of the Feed-Forward Part

The Feed-Forward Network processes and transforms the information for each token after attention has combined contextual information. It helps the model learn more complex patterns and representations.

---

## Question 10

Transformers enabled modern Large Language Models because of several important advantages.

### 1. Considering Many Words Together

Self-attention allows a transformer to examine relationships between many tokens in a sequence. This helps the model understand the context of words based on other words around them.

### 2. Capturing Long-Range Relationships

Transformers can connect words that are far apart in a sentence or document. This helps with tasks such as understanding pronouns, topics, and relationships across long passages of text.

### 3. Parallel Training

Unlike traditional sequential models that process tokens one step at a time, transformers can process many token relationships in parallel during training. This makes better use of modern hardware and can speed up training.

### 4. Scaling

Transformers can improve their capabilities when trained with more data, more computing power, and more model parameters. This scalability helped make very large language models possible.

### Limitation or Cost

Large transformer models require enormous computing resources, electricity, storage, and financial cost for training and operation. They can also be difficult to interpret and may sometimes produce incorrect information.
