
## Question 1

Training a language model from scratch requires a huge amount of text data, powerful computers, and a long training time. It is expensive and difficult for most people.

A pre-trained model is already trained on a large dataset. It requires less data, lower computing cost, and much less time for fine-tuning. One major advantage is that it can quickly perform many language tasks with good accuracy.

---

## Question 2

RNN/LSTM processes words one by one.

Sequence:

I → love → machine → learning

- Read "I"
- Pass information to "love"
- Then to "machine"
- Finally to "learning"

Each word depends on the previous hidden state.

A Transformer processes all words at the same time using attention. It can understand relationships between every pair of words in parallel, making training much faster.

---

## Question 3

Flow:

Text → Tokens → Embeddings → Transformer Layers → Output

- **Text:** Original sentence.
- **Tokens:** Text is divided into smaller units.
- **Embeddings:** Every token is converted into a vector representing its meaning.
- **Transformer Layers:** The model learns relationships between all tokens.
- **Output:** Final prediction or generated text.

Example:

Sentence:

```
I love AI
```

Tokens:

```
["I", "love", "AI"]
```

Embeddings are numerical vectors that represent the meaning of each token instead of actual words.

---

## Question 4

Sentences:

```
Dog bites man.
Man bites dog.
```

Both sentences contain the same words but in a different order, so their meanings are completely different.

Transformers use **Positional Encoding** to remember the position of each word so the model understands the correct sentence meaning.

---

## Question 5

Sentence:

```
The animal did not cross the road because it was tired.
```

The word **"it"** most likely refers to **the animal**.

Attention helps the transformer focus on nearby and related words, allowing it to correctly identify that "it" refers to the animal rather than the road.

---

## Question 6

Sentence:

```
The cat sat on the mat because it was tired.
```

**Query:** What am I looking for?

**Key:** What information is available?

**Value:** What information should be passed forward?

The word **cat** should receive more attention than **mat** because only a cat can logically be tired. The attention mechanism uses context to make this decision.

---

## Question 7

Formula:

```
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

- A high attention score means two words are strongly related.
- A low attention score means the words are weakly related.
- Softmax converts scores into probabilities that sum to 1.
- These scores are applied to the Values so that more important information contributes more to the final output.

---

## Question 8

Sentence:

```
The student solved the problem because he understood the concept.
```

Different attention heads can focus on different relationships:

1. Grammar between words.
2. Subject-object relationship.
3. Meaning of the sentence.
4. Pronoun reference ("he" refers to "student").

Multiple heads are better because each head learns a different type of relationship, giving the model a deeper understanding.

---

## Question 9

Transformer Block Diagram

```
Embeddings + Positional Encoding
            │
            ▼
Multi-Head Self-Attention
            │
            ▼
       Add & Norm
            │
            ▼
 Feed-Forward Network
            │
            ▼
       Add & Norm
            │
            ▼
 Output to Next Layer
```

The attention layer learns relationships between words and understands context.

The feed-forward network processes the learned information and extracts more useful features before sending the output to the next layer.

---

## Question 10

Advantages of Transformers:

1. They can consider many words together.
2. They capture long-distance relationships between words.
3. They support parallel training, making learning much faster.
4. They improve as more data, computing power, and parameters are added.

One limitation is that large transformer models require high memory, powerful GPUs, and significant computational cost.