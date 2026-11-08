@'
# Transformer Self-Attention Mechanism

## 1. Basic Idea

Self-attention allows each token in a sequence to look at other tokens and assign different importance to them.

For example:

"The cat sat on the mat"

Each token can attend to every other token in the sequence.

---

## 2. Query, Key, and Value

Each input token representation is transformed into three vectors:

```text
Input Token Representations
          |
          v
     +---------+
     | Linear  |
     | Layers  |
     +---------+
       /  |  \
      v   v   v
   Query Key Value
     Q    K    V
```
