import numpy as np
import matplotlib.pyplot as plt
import torch
from transformers import AutoTokenizer, AutoModel


# =========================================================
# PART 1: FROM-SCRATCH SELF-ATTENTION
# =========================================================

def softmax(x):
    """Convert attention scores into probabilities."""
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(Q, K, V):
    """
    Attention(Q, K, V) =
    softmax(QK^T / sqrt(d_k))V
    """
    d_k = Q.shape[-1]

    scores = Q @ K.T
    scaled_scores = scores / np.sqrt(d_k)

    attention_weights = softmax(scaled_scores)
    output = attention_weights @ V

    return output, attention_weights


tokens = ["The", "cat", "sat", "quietly"]

Q = np.array([
    [1.0, 0.0, 1.0, 0.0],
    [1.0, 1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 0.0]
])

K = np.array([
    [1.0, 0.0, 1.0, 0.0],
    [1.0, 1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 0.0]
])

V = np.array([
    [1.0, 0.0, 0.5, 0.0],
    [0.8, 1.0, 0.0, 0.5],
    [0.2, 0.7, 1.0, 0.9],
    [0.5, 0.4, 0.8, 0.2]
])


output, attention_weights = scaled_dot_product_attention(Q, K, V)


print("=" * 70)
print("PART 1: FROM-SCRATCH SCALED DOT-PRODUCT SELF-ATTENTION")
print("=" * 70)

print("\nTokens:")
print(tokens)

print("\nAttention Weights:")
print(np.round(attention_weights, 3))

print("\nAttention Output:")
print(np.round(output, 3))


print("\nSelected Token Attention:")

for i in range(3):
    print(f"\nToken: {tokens[i]}")

    for j, token in enumerate(tokens):
        print(
            f"  attends to {token}: "
            f"{attention_weights[i][j]:.3f}"
        )


# Save attention visualization
plt.figure(figsize=(8, 6))

plt.imshow(attention_weights)

plt.xticks(range(len(tokens)), tokens)
plt.yticks(range(len(tokens)), tokens)

plt.xlabel("Key / Token Being Attended To")
plt.ylabel("Query / Current Token")
plt.title("Toy Self-Attention Weights")

plt.colorbar(label="Attention Weight")
plt.tight_layout()

plt.savefig(
    "toy_attention_weights.png",
    dpi=150
)

plt.close()

print("\nToy attention plot saved:")
print("toy_attention_weights.png")


# =========================================================
# PART 2: PRE-TRAINED TRANSFORMER
# =========================================================

print("\n" + "=" * 70)
print("PART 2: PRE-TRAINED TRANSFORMER ATTENTION")
print("=" * 70)

print("\nLoading pre-trained model...")

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModel.from_pretrained(
    MODEL_NAME,
    output_attentions=True,
        attn_implementation="eager"
)

model.eval()

print("Model loaded successfully.")
print("Model:", MODEL_NAME)


# =========================================================
# FIVE CAREFULLY CHOSEN SENTENCES
# =========================================================

sentences = [
    "The cat sat on the mat.",
    "The dog chased the ball across the garden.",
    "The student studied hard for the examination.",
    "The scientist explained the complex experiment clearly.",
    "The teacher gave the student a difficult assignment."
]


# =========================================================
# FUNCTION TO INSPECT ATTENTION
# =========================================================

def inspect_attention(sentence):
    """Run the sentence through the transformer and inspect attention."""

    inputs = tokenizer(
        sentence,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    tokens = tokenizer.convert_ids_to_tokens(
        inputs["input_ids"][0]
    )

    # Last transformer layer
    attention = outputs.attentions[-1]

    # Average across attention heads
    average_attention = attention[0].mean(dim=0)

    # Convert to NumPy
    average_attention = average_attention.numpy()

    return tokens, average_attention


# =========================================================
# RUN FIVE SENTENCES
# =========================================================

for number, sentence in enumerate(sentences, start=1):

    print("\n" + "-" * 70)
    print(f"Sentence {number}:")
    print(sentence)

    tokens, weights = inspect_attention(sentence)

    print("\nTokens:")
    print(tokens)

    print("\nAttention matrix shape:")
    print(weights.shape)

    print("\nStrongest attention relationships:")

    # Find strongest relationships
    relationships = []

    for i in range(len(tokens)):
        for j in range(len(tokens)):
            if i != j:
                relationships.append(
                    (
                        weights[i][j],
                        tokens[i],
                        tokens[j]
                    )
                )

    relationships.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    for score, source, target in relationships[:5]:

        print(
            f"{source} -> {target}: "
            f"{score:.3f}"
        )


# =========================================================
# ATTENTION VISUALIZATION FOR FIRST SENTENCE
# =========================================================

tokens, weights = inspect_attention(sentences[0])

plt.figure(figsize=(10, 8))

plt.imshow(weights)

plt.xticks(
    range(len(tokens)),
    tokens,
    rotation=45
)

plt.yticks(
    range(len(tokens)),
    tokens
)

plt.xlabel("Key Token")
plt.ylabel("Query Token")

plt.title(
    "DistilBERT Average Attention - "
    "Sentence 1"
)

plt.colorbar(label="Attention Weight")

plt.tight_layout()

plt.savefig(
    "pretrained_attention_sentence1.png",
    dpi=150
)

plt.close()

print("\nPre-trained attention plot saved:")
print("pretrained_attention_sentence1.png")


# =========================================================
# PART 3: AMBIGUITY TEST
# =========================================================

print("\n" + "=" * 70)
print("PART 3: AMBIGUITY / PRONOUN TEST")
print("=" * 70)


ambiguity_sentences = [
    "The animal did not cross the road because it was tired.",
    "The animal did not cross the road because it was dangerous.",
    "The trophy does not fit in the suitcase because it is too large."
]


for sentence in ambiguity_sentences:

    print("\nSentence:")
    print(sentence)

    tokens, weights = inspect_attention(sentence)

    print("\nTokens:")
    print(tokens)

    # Search for tokens related to pronouns
    pronoun_indices = [
        i for i, token in enumerate(tokens)
        if token in ["it", "##it"]
    ]

    if pronoun_indices:

        for index in pronoun_indices:

            print(
                f"\nAttention from pronoun '{tokens[index]}':"
            )

            scores = []

            for j, token in enumerate(tokens):

                if j != index:

                    scores.append(
                        (
                            weights[index][j],
                            token
                        )
                    )

            scores.sort(
                reverse=True,
                key=lambda x: x[0]
            )

            for score, token in scores[:5]:

                print(
                    f"  {token}: {score:.3f}"
                )

    else:

        print("Pronoun token not found directly.")


# =========================================================
# PART 4: COMPARISON
# =========================================================

print("\n" + "=" * 70)
print("PART 4: TOY MODEL VS PRE-TRAINED TRANSFORMER")
print("=" * 70)

print("""
Toy implementation:
- Uses manually created Q, K, and V vectors.
- Contains only one attention head.
- Demonstrates the mathematical attention process directly.
- Does not learn from data.

Pre-trained Transformer:
- Uses learned representations.
- Contains multiple transformer layers and attention heads.
- Uses contextual token representations.
- Was trained on a large text collection.
- Can capture more complex relationships between words.

The toy experiment is useful for understanding the mathematics,
while the pre-trained model demonstrates how attention operates
inside a real transformer architecture.
""")


# =========================================================
# PART 5: WHAT ATTENTION CAN AND CANNOT PROVE
# =========================================================

print("\n" + "=" * 70)
print("LIMITATIONS OF ATTENTION VISUALIZATION")
print("=" * 70)

print("""
Attention visualization can show which tokens receive relatively
high attention weights for a particular layer and attention head.

However, attention weights alone do not prove that a particular
token caused the model's final prediction or that the model
'understood' the sentence in a human-like way.

Different heads can learn different patterns, and important
information can also be stored in hidden states and residual
connections.

Therefore, attention should be treated as one diagnostic tool
rather than a complete explanation of model reasoning.
""")


# =========================================================
# FINAL SUMMARY
# =========================================================

print("\n" + "=" * 70)
print("EXPERIMENT COMPLETE")
print("=" * 70)

print("1. Single-head attention was implemented from scratch.")
print("2. Attention was inspected for five sentences.")
print("3. A pronoun ambiguity test was performed.")
print("4. Attention visualizations were saved.")
print("5. Toy attention was compared with a pre-trained Transformer.")

print("\nSaved plots:")
print("- toy_attention_weights.png")
print("- pretrained_attention_sentence1.png")