import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def softmax(x):
    """
    Compute numerically stable softmax.
    """
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(Q, K, V):
    """
    Scaled Dot-Product Attention

    Attention(Q, K, V) =
        softmax(QK^T / sqrt(d_k)) V

    Returns:
        output: contextualized representations
        weights: attention weights
    """

    d_k = Q.shape[-1]

    scores = Q @ K.T
    scaled_scores = scores / np.sqrt(d_k)

    attention_weights = softmax(scaled_scores)

    output = attention_weights @ V

    return output, attention_weights


def main():
    # ---------------------------------------------------------
    # Toy sentence
    # ---------------------------------------------------------

    tokens = [
        "The",
        "cat",
        "sat",
        "on",
        "the",
        "mat"
    ]

    print("=" * 60)
    print("FROM-SCRATCH SCALED DOT-PRODUCT SELF-ATTENTION")
    print("=" * 60)

    print("\nToy sentence:")
    print(" ".join(tokens))

    # ---------------------------------------------------------
    # Toy embeddings
    #
    # Each token is represented by a small vector.
    # In a real Transformer these representations are learned.
    # ---------------------------------------------------------

    embeddings = np.array([
        [1.0, 0.0, 0.2, 0.1],
        [0.9, 0.8, 0.1, 0.2],
        [0.2, 0.7, 0.9, 0.1],
        [0.1, 0.2, 0.8, 0.9],
        [0.8, 0.1, 0.2, 0.1],
        [0.7, 0.2, 0.3, 0.8]
    ])

    # For this educational experiment we use the embeddings
    # directly as Q, K and V.
    Q = embeddings
    K = embeddings
    V = embeddings

    output, attention_weights = scaled_dot_product_attention(Q, K, V)

    # ---------------------------------------------------------
    # Print attention weights
    # ---------------------------------------------------------

    print("\nAttention weights:")
    print()

    header = "Query".ljust(10)
    for token in tokens:
        header += token.rjust(10)

    print(header)
    print("-" * len(header))

    for i, token in enumerate(tokens):
        row = token.ljust(10)

        for weight in attention_weights[i]:
            row += f"{weight:10.3f}"

        print(row)

    # ---------------------------------------------------------
    # Display attention for at least three tokens
    # ---------------------------------------------------------

    print("\nSelected token attention:")
    
    selected_indices = [0, 1, 2]

    for index in selected_indices:
        print(f"\nQuery token: '{tokens[index]}'")

        ranked = np.argsort(attention_weights[index])[::-1]

        for j in ranked:
            print(
                f"  attends to '{tokens[j]}': "
                f"{attention_weights[index][j]:.4f}"
            )

    # ---------------------------------------------------------
    # Save heatmap
    # ---------------------------------------------------------

    output_dir = Path(__file__).resolve().parent.parent / "results/plots"
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 7))

    plt.imshow(
        attention_weights,
        interpolation="nearest",
        aspect="auto"
    )

    plt.colorbar(label="Attention Weight")

    plt.xticks(
        range(len(tokens)),
        tokens
    )

    plt.yticks(
        range(len(tokens)),
        tokens
    )

    plt.xlabel("Key Tokens")
    plt.ylabel("Query Tokens")
    plt.title("Toy Sentence: Scaled Dot-Product Self-Attention")

    plt.tight_layout()

    output_path = output_dir / "toy_attention.png"

    plt.savefig(output_path, dpi=200)
    plt.close()

    print(f"\nPlot saved to: {output_path}")

    # ---------------------------------------------------------
    # Print output representations
    # ---------------------------------------------------------

    print("\nContextualized output representations:")
    print(output)

    print("\n" + "=" * 60)
    print("Toy attention experiment completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()