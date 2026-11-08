from pathlib import Path
import csv
import math

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Day 22: Transformer Attention From Paper to Experiment
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
DIAGRAM_DIR = BASE_DIR / "diagrams"

OUTPUT_DIR.mkdir(exist_ok=True)
DIAGRAM_DIR.mkdir(exist_ok=True)


# ============================================================
# PART 1: FROM-SCRATCH SCALED DOT-PRODUCT ATTENTION
# ============================================================

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(Q, K, V):
    """
    Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
    """
    d_k = Q.shape[-1]

    scores = (Q @ K.T) / math.sqrt(d_k)

    weights = softmax(scores)

    output = weights @ V

    return scores, weights, output


print("=" * 70)
print("PART 1: FROM-SCRATCH SCALED DOT-PRODUCT ATTENTION")
print("=" * 70)


# Toy sentence
tokens = ["The", "cat", "sat", "on", "the", "mat"]

# Small manually designed embeddings.
# These are toy representations for demonstration.
embeddings = np.array([
    [1.0, 0.0, 0.2, 0.1],
    [0.9, 0.1, 0.8, 0.2],
    [0.2, 0.8, 0.7, 0.1],
    [0.1, 0.2, 0.3, 0.8],
    [1.0, 0.0, 0.2, 0.1],
    [0.2, 0.7, 0.6, 0.2],
], dtype=float)


# For a simple demonstration, use the embeddings as Q, K and V.
Q = embeddings
K = embeddings
V = embeddings

scores, attention_weights, attention_output = (
    scaled_dot_product_attention(Q, K, V)
)


print("\nTokens:")
print(tokens)

print("\nAttention Weight Matrix:")
print(np.round(attention_weights, 3))

print("\nAttention weights for selected tokens:")

selected_tokens = ["cat", "sat", "mat"]

for token in selected_tokens:
    index = tokens.index(token)

    print(f"\nToken: {token}")

    ranked_indices = np.argsort(attention_weights[index])[::-1]

    for j in ranked_indices[:3]:
        print(
            f"  attends to '{tokens[j]}': "
            f"{attention_weights[index][j]:.3f}"
        )


# Save attention weights to CSV
attention_csv = OUTPUT_DIR / "attention_weights.csv"

with open(attention_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["query_token"] + tokens)

    for token, row in zip(tokens, attention_weights):
        writer.writerow([token] + [round(float(x), 6) for x in row])


# Plot attention heatmap
plt.figure(figsize=(8, 6))

plt.imshow(attention_weights, aspect="auto")

plt.xticks(range(len(tokens)), tokens)
plt.yticks(range(len(tokens)), tokens)

plt.xlabel("Key tokens")
plt.ylabel("Query tokens")
plt.title("Toy Scaled Dot-Product Attention Weights")

plt.colorbar(label="Attention Weight")

plt.tight_layout()

toy_plot_path = DIAGRAM_DIR / "toy_attention_heatmap.png"

plt.savefig(toy_plot_path, dpi=150)

plt.close()


# Plot attention weights for at least three tokens
plt.figure(figsize=(10, 6))

for token in selected_tokens:
    index = tokens.index(token)

    plt.plot(
        tokens,
        attention_weights[index],
        marker="o",
        label=token
    )

plt.xlabel("Tokens being attended to")
plt.ylabel("Attention Weight")

plt.title("Attention Distribution for Three Tokens")

plt.legend()

plt.xticks(rotation=30)

plt.tight_layout()

three_token_plot_path = DIAGRAM_DIR / "three_token_attention.png"

plt.savefig(three_token_plot_path, dpi=150)

plt.close()


# ============================================================
# PART 2: PRE-TRAINED TRANSFORMER EXPERIMENT
# ============================================================

print("\n")
print("=" * 70)
print("PART 2: PRE-TRAINED TRANSFORMER EXPERIMENT")
print("=" * 70)


sentences = [
    "The cat sat on the mat.",
    "The dog chased the ball because it was excited.",
    "The dog chased the ball because it was tired.",
    "The teacher gave the student a book.",
    "The scientist studied the virus in the laboratory.",
    "The keys to the cabinet are on the table.",
    "The keys to the cabinet is on the table.",
    "The movie was not good.",
    "The movie was good.",
    "The boy who the girl saw was smiling.",
]


try:
    import torch
    from transformers import AutoTokenizer, AutoModel

    print("\nLoading pretrained transformer model...")

    model_name = "distilbert-base-uncased"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModel.from_pretrained(
        model_name,
        output_attentions=True,
        attn_implementation="eager"
    )

    model.eval()

    print("Model loaded:", model_name)

    pretrained_results = []

    print("\nSentence-level hidden-state analysis:")

    for sentence in sentences:

        inputs = tokenizer(
            sentence,
            return_tensors="pt"
        )

        with torch.no_grad():

            outputs = model(
                **inputs,
                output_attentions=True
            )

        hidden_states = outputs.last_hidden_state

        attention = outputs.attentions

        # Average the final-layer attention across heads
        final_layer_attention = attention[-1][0]

        average_attention = final_layer_attention.mean(dim=0)

        # Exclude special tokens for a simple summary
        token_ids = inputs["input_ids"][0]

        wordpieces = tokenizer.convert_ids_to_tokens(
            token_ids
        )

        # Mean attention received by each token
        attention_received = average_attention.mean(dim=0)

        max_index = torch.argmax(
            attention_received
        ).item()

        most_attended_token = wordpieces[max_index]

        mean_hidden_norm = torch.norm(
            hidden_states[0],
            dim=1
        ).mean().item()

        pretrained_results.append({
            "sentence": sentence,
            "token_count": len(wordpieces),
            "most_attended_token": most_attended_token,
            "mean_hidden_state_norm": round(
                mean_hidden_norm,
                6
            )
        })

        print("\nSentence:", sentence)

        print("Tokens:", wordpieces)

        print(
            "Most attended token:",
            most_attended_token
        )

        print(
            "Mean hidden-state norm:",
            round(mean_hidden_norm, 4)
        )


    # Save pretrained results
    pretrained_csv = OUTPUT_DIR / "pretrained_attention_results.csv"

    with open(
        pretrained_csv,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "sentence",
            "token_count",
            "most_attended_token",
            "mean_hidden_state_norm"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(pretrained_results)


    # ========================================================
    # PART 3: AMBIGUITY TEST
    # ========================================================

    print("\n")
    print("=" * 70)
    print("PART 3: AMBIGUITY TEST")
    print("=" * 70)

    ambiguity_sentences = [
        "The dog chased the ball because it was excited.",
        "The dog chased the ball because it was tired.",
        "The movie was not good.",
        "The movie was good.",
        "The keys to the cabinet are on the table.",
        "The keys to the cabinet is on the table.",
    ]

    print(
        "\nThe ambiguity test compares sentences that differ "
        "in pronoun reference, negation, or grammatical agreement."
    )

    for sentence in ambiguity_sentences:

        inputs = tokenizer(
            sentence,
            return_tensors="pt"
        )

        with torch.no_grad():

            outputs = model(
                **inputs,
                output_attentions=True
            )

        tokens_for_sentence = tokenizer.convert_ids_to_tokens(
            inputs["input_ids"][0]
        )

        final_attention = outputs.attentions[-1][0]

        average_attention = final_attention.mean(dim=0)

        print("\nSentence:", sentence)

        print("Tokens:", tokens_for_sentence)

        print(
            "Attention matrix shape:",
            tuple(average_attention.shape)
        )


    # ========================================================
    # ATTENTION VISUALIZATION FOR AN AMBIGUITY SENTENCE
    # ========================================================

    sentence = ambiguity_sentences[0]

    inputs = tokenizer(
        sentence,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model(
            **inputs,
            output_attentions=True
        )

    tokens_for_plot = tokenizer.convert_ids_to_tokens(
        inputs["input_ids"][0]
    )

    final_attention = outputs.attentions[-1][0]

    average_attention = final_attention.mean(dim=0).numpy()

    plt.figure(figsize=(10, 8))

    plt.imshow(
        average_attention,
        aspect="auto"
    )

    plt.xticks(
        range(len(tokens_for_plot)),
        tokens_for_plot,
        rotation=45
    )

    plt.yticks(
        range(len(tokens_for_plot)),
        tokens_for_plot
    )

    plt.xlabel("Key tokens")

    plt.ylabel("Query tokens")

    plt.title(
        "Pretrained Transformer Attention: Ambiguity Example"
    )

    plt.colorbar(
        label="Average Attention Weight"
    )

    plt.tight_layout()

    pretrained_plot_path = (
        DIAGRAM_DIR /
        "pretrained_ambiguity_attention.png"
    )

    plt.savefig(
        pretrained_plot_path,
        dpi=150
    )

    plt.close()


except ImportError:

    print("\nPretrained experiment could not run.")

    print(
        "Install required packages with:"
    )

    print(
        "pip install torch transformers"
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("EXPERIMENT COMPLETE")
print("=" * 70)

print("\nGenerated files:")

print(
    "1.",
    attention_csv
)

print(
    "2.",
    toy_plot_path
)

print(
    "3.",
    three_token_plot_path
)

print(
    "4.",
    OUTPUT_DIR / "pretrained_attention_results.csv"
)

print(
    "5.",
    DIAGRAM_DIR / "pretrained_ambiguity_attention.png"
)

print("\nThe experiment demonstrates:")

print(
    "- Query, Key and Value interaction"
)

print(
    "- Scaled dot-product attention"
)

print(
    "- Attention distributions across tokens"
)

print(
    "- Pretrained transformer attention behavior"
)

print(
    "- Ambiguity and context sensitivity"
)

print(
    "- The difference between toy attention and pretrained attention"
)