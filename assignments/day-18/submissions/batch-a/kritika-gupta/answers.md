# Day 18 Answers

## Question 1

### Training a Language Model from Scratch vs Using a Pre-Trained Model

| Training from Scratch | Pre-Trained Model |
|------------------------|-------------------|
| Requires a very large amount of data. | Uses an already trained model. |
| Needs expensive computing resources such as GPUs or TPUs. | Requires much less computing power. |
| Takes weeks or months to train. | Can be fine-tuned or used immediately in a short time. |
| Suitable for creating a completely new model. | Suitable for solving tasks quickly with good performance. |

**One reason to choose a pre-trained model:**

A pre-trained model saves time and computing cost because it has already learned general language patterns.

---

## Question 2

### How an RNN/LSTM Processes a Sequence

Sequence:

```text
I → love → machine → learning
```

An RNN or LSTM processes one word at a time.

1. Read **I**.
2. Store its information.
3. Read **love** while remembering **I**.
4. Read **machine** while remembering the previous words.
5. Read **learning** using information from all previous words.

The information flows step by step through the sequence.

### How a Transformer Works

A transformer processes all the words at the same time instead of one by one. It uses an attention mechanism to learn relationships between all words in parallel, making training much faster.

---

## Question 3

### Text → Tokens → Embeddings → Transformer Layers → Output

**Text**

```
I love AI
```

↓

**Tokens**

```
["I", "love", "AI"]
```

↓

**Embeddings**

Each token is converted into a vector (a list of numbers) that represents its meaning and relationship with other words. The actual values are learned by the model and are not manually created.

↓

**Transformer Layers**

The transformer studies how the words relate to one another using attention and updates their representations.

↓

**Output**

The final output is used for tasks such as text generation, translation, question answering, or classification.

---

## Question 4

Consider these sentences:

```
Dog bites man.
```

```
Man bites dog.
```

Although both sentences contain the same words, their meanings are completely different because the word order changes.

Transformers use **positional encoding** to remember the position of every word. This helps the model understand that "dog" is the subject in the first sentence but "man" is the subject in the second sentence.

---

## Question 5

Sentence:

```
The animal did not cross the road because it was tired.
```

The word **it** most likely refers to **the animal** because an animal can become tired, while a road cannot.

Attention helps the transformer connect the pronoun **it** with the earlier word **animal** by considering the surrounding context instead of only nearby words.

---

## Question 6

Sentence:

```
The cat sat on the mat because it was tired.
```

### Query

**What am I looking for?**

The model wants to know what **it** refers to.

### Key

**What information is available?**

The words **cat**, **sat**, **mat**, and **tired** provide useful information.

### Value

**What information should be passed forward?**

The important information about the correct meaning of **it** is passed to the next layer.

The word **cat** should receive more attention than **mat** because living things become tired, while a mat cannot.

---

## Question 7

### Attention Formula

```text
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

- A **high attention score** means two words are strongly related.
- A **low attention score** means the words have little relationship.
- **Softmax** converts the scores into probabilities so they are easy to compare and together sum to 1.
- The scores are multiplied with the **Value** vectors so that more important information contributes more to the final representation.

---

## Question 8

Sentence:

```
The student solved the problem because he understood the concept.
```

Different attention heads may focus on different relationships.

### Head 1: Grammar

Identifies that **student** is the subject.

### Head 2: Subject-Object Relationship

Connects **student** with **solved** and **problem**.

### Head 3: Meaning

Understands that solving the problem happened because the student understood the concept.

### Head 4: Pronoun Reference

Determines that **he** refers to **student**.

Using several attention heads allows the transformer to learn different types of relationships at the same time, making it more accurate than using only one attention head.

---

## Question 9

### Transformer Block Diagram

```text
           Input
             │
             ▼
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

### Purpose of Multi-Head Self-Attention

The attention layer helps the transformer understand how different words in a sentence are related and which words are most important for understanding the context.

### Purpose of Feed-Forward Network

The feed-forward network processes the updated word representations and learns more complex patterns before passing them to the next transformer layer.

---

## Question 10

### Why Transformers Enabled Modern LLMs

**1. Considering Many Words Together**

Transformers can examine relationships between many words simultaneously, helping them understand the full context.

**2. Capturing Long-Range Relationships**

They can connect words that are far apart in a sentence, improving language understanding.

**3. Parallel Training**

Unlike RNNs, transformers process many tokens at the same time, making training much faster.

**4. Scaling with More Data, Computing Power, and Model Parameters**

Transformers generally perform better when trained with larger datasets, more powerful hardware, and more model parameters. This scalability has enabled the development of modern large language models.

### Limitation

Large transformer models require significant computing resources, memory, and electricity, making them expensive to train and run.