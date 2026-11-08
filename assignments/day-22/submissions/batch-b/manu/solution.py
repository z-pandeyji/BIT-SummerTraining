"""
Day 22: Transformer Attention From Paper to Experiment

This script:
1. Implements single-head scaled dot-product attention from scratch.
2. Visualizes attention weights for a toy sentence.
3. Uses a pretrained BERT model to inspect attention and hidden states.
4. Tests five carefully chosen sentences.
5. Includes an ambiguity/pronoun reference experiment.
6. Saves plots and CSV results in the output/ directory.

Run:
    python attention_experiment.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# PART 1: FROM-SCRATCH SCALED DOT-PRODUCT ATTENTION
# ============================================================

def softmax(x):
    """
    Numerically stable softmax.
    """
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(Q, K, V):
    """
    Scaled dot-product attention:

        Attention(Q, K, V)
        = softmax(QK^T / sqrt(d_k))V

    Parameters:
        Q: Query matrix
        K: Key matrix
        V: Value matrix

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


def run_toy_attention_experiment():
    """
    Toy self-attention experiment using a small sentence.
    """

    tokens = ["The", "cat", "sat", "on", "the", "mat"]

    # Small manually designed vectors.
    # Similar semantic/contextual dimensions are intentionally represented.
    X = np.array(
        [
            [1.0, 0.2, 0.1, 0.0],  # The
            [1.0, 0.9, 0.1, 0.0],  # cat
            [0.1, 0.1, 1.0, 0.2],  # sat
            [0.0, 0.1, 0.8, 0.5],  # on
            [1.0, 0.2, 0.1, 0.0],  # the
            [0.8, 0.7, 0.1, 0.0],  # mat
        ],
        dtype=np.float32,
    )

    # For this toy demonstration, use the same matrix as Q, K, and V.
    Q = X
    K = X
    V = X

    output, weights = scaled_dot_product_attention(Q, K, V)

    print("\n" + "=" * 70)
    print("FROM-SCRATCH SCALED DOT-PRODUCT ATTENTION")
    print("=" * 70)

    print("\nTokens:")
    print(tokens)

    print("\nAttention matrix shape:")
    print(weights.shape)

    print("\nAttention weights:")
    attention_df = pd.DataFrame(
        weights,
        index=tokens,
        columns=tokens,
    )
    print(attention_df.round(3))

    print("\nContextualized output:")
    output_df = pd.DataFrame(
        output,
        index=tokens,
    )
    print(output_df.round(3))

    # Plot full attention matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(weights, aspect="auto")
    plt.colorbar(label="Attention weight")
    plt.xticks(range(len(tokens)), tokens)
    plt.yticks(range(len(tokens)), tokens)
    plt.xlabel("Key / attended-to token")
    plt.ylabel("Query token")
    plt.title("Toy Sentence: Single-Head Self-Attention")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "toy_attention_heatmap.png", dpi=150)
    plt.close()

    # Plot at least three token attention distributions
    selected_tokens = ["cat", "sat", "mat"]

    fig, axes = plt.subplots(
        nrows=len(selected_tokens),
        ncols=1,
        figsize=(9, 8),
    )

    for ax, token in zip(axes, selected_tokens):
        index = tokens.index(token)

        ax.bar(tokens, weights[index])
        ax.set_ylim(0, 1)
        ax.set_ylabel("Weight")
        ax.set_title(f"Attention distribution for query token: '{token}'")

    axes[-1].set_xlabel("Tokens being attended to")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "toy_selected_token_attention.png", dpi=150)
    plt.close()

    attention_df.to_csv(
        OUTPUT_DIR / "toy_attention_weights.csv"
    )

    return tokens, weights


# ============================================================
# PART 2: PRETRAINED TRANSFORMER EXPERIMENT
# ============================================================

def load_pretrained_model():
    """
    Load pretrained BERT tokenizer and model.
    """

    model_name = "bert-base-uncased"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModel.from_pretrained(
        model_name,
        output_attentions=True,
        output_hidden_states=True,
        attn_implementation="eager",
    )

    model.eval()

    return tokenizer, model


def run_pretrained_experiment():
    """
    Inspect attention and hidden-state behavior on five sentences.
    """

    tokenizer, model = load_pretrained_model()

    sentences = [
        "The cat sat on the mat.",
        "The bank approved the customer's loan.",
        "The fisherman sat on the bank of the river.",
        "The movie was not good because the acting was weak.",
        "The scientist who studied the cells published the results.",
    ]

    results = []

    print("\n" + "=" * 70)
    print("PRETRAINED TRANSFORMER EXPERIMENT")
    print("=" * 70)

    for sentence_id, sentence in enumerate(sentences, start=1):

        encoded = tokenizer(
            sentence,
            return_tensors="pt",
        )

        with torch.no_grad():
            outputs = model(
                **encoded,
                output_attentions=True,
                output_hidden_states=True,
            )

        tokens = tokenizer.convert_ids_to_tokens(
            encoded["input_ids"][0]
        )

        # Last layer attention:
        # Shape:
        # (batch_size, number_of_heads, sequence_length, sequence_length)
        last_layer_attention = outputs.attentions[-1][0]

        # Average attention across all heads
        mean_attention = last_layer_attention.mean(dim=0)

        # Average attention received by each token
        average_received_attention = mean_attention.mean(dim=0)

        # Hidden state representation from final layer
        final_hidden_state = outputs.last_hidden_state[0]

        # Mean vector norm as a simple representation statistic
        hidden_state_norm = torch.norm(
            final_hidden_state,
            dim=1,
        ).mean().item()

        print("\n" + "-" * 70)
        print(f"Sentence {sentence_id}: {sentence}")
        print("-" * 70)

        print("Tokens:")
        print(tokens)

        print(
            "Number of attention heads:",
            last_layer_attention.shape[0],
        )

        print(
            "Average hidden-state norm:",
            round(hidden_state_norm, 4),
        )

        print("\nAverage attention received by tokens:")

        token_attention_pairs = list(
            zip(
                tokens,
                average_received_attention.tolist(),
            )
        )

        token_attention_pairs.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        for token, value in token_attention_pairs[:5]:
            print(
                f"{token:15s} {value:.4f}"
            )

        results.append(
            {
                "sentence_id": sentence_id,
                "sentence": sentence,
                "token_count": len(tokens),
                "hidden_state_norm": hidden_state_norm,
                "highest_attention_token": token_attention_pairs[0][0],
                "highest_attention_value": token_attention_pairs[0][1],
            }
        )

        # Save a heatmap for each sentence
        plt.figure(figsize=(10, 8))

        plt.imshow(
            mean_attention.numpy(),
            aspect="auto",
        )

        plt.colorbar(
            label="Mean attention weight"
        )

        plt.xticks(
            range(len(tokens)),
            tokens,
            rotation=45,
            ha="right",
        )

        plt.yticks(
            range(len(tokens)),
            tokens,
        )

        plt.xlabel("Key / attended-to token")
        plt.ylabel("Query token")

        plt.title(
            f"Mean Last-Layer Attention\n{sentence}"
        )

        plt.tight_layout()

        filename = (
            OUTPUT_DIR
            / f"pretrained_attention_sentence_{sentence_id}.png"
        )

        plt.savefig(
            filename,
            dpi=150,
        )

        plt.close()

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        OUTPUT_DIR / "pretrained_sentence_results.csv",
        index=False,
    )

    print("\nSummary:")
    print(results_df.to_string(index=False))

    return tokenizer, model


# ============================================================
# PART 3: AMBIGUITY / PRONOUN REFERENCE TEST
# ============================================================

def run_pronoun_ambiguity_test(tokenizer, model):
    """
    Ambiguity experiment.

    The pronoun 'it' can refer to different nouns depending on context.
    """

    sentences = [
        "The trophy does not fit in the suitcase because it is too large.",
        "The trophy does not fit in the suitcase because it is too small.",
        "The suitcase does not fit in the trophy because it is too large.",
        "The suitcase does not fit in the trophy because it is too small.",
    ]

    print("\n" + "=" * 70)
    print("AMBIGUITY / PRONOUN REFERENCE TEST")
    print("=" * 70)

    rows = []

    for sentence in sentences:

        encoded = tokenizer(
            sentence,
            return_tensors="pt",
        )

        with torch.no_grad():
            outputs = model(
                **encoded,
                output_attentions=True,
                output_hidden_states=True,
            )

        tokens = tokenizer.convert_ids_to_tokens(
            encoded["input_ids"][0]
        )

        # Last layer mean attention over heads
        attention = outputs.attentions[-1][0].mean(dim=0)

        # Find token position of "it"
        it_positions = [
            index
            for index, token in enumerate(tokens)
            if token == "it"
        ]

        if not it_positions:
            continue

        it_index = it_positions[0]

        it_attention = attention[it_index]

        ranked_tokens = sorted(
            zip(tokens, it_attention.tolist()),
            key=lambda item: item[1],
            reverse=True,
        )

        top_context = ranked_tokens[:5]

        print("\nSentence:")
        print(sentence)

        print("\nTokens receiving highest attention from 'it':")

        for token, weight in top_context:
            print(
                f"{token:15s} {weight:.4f}"
            )

        rows.append(
            {
                "sentence": sentence,
                "top_attended_token": top_context[0][0],
                "top_attention_weight": top_context[0][1],
            }
        )

        # Plot attention from pronoun "it"
        plt.figure(figsize=(10, 5))

        plt.bar(
            tokens,
            it_attention.numpy(),
        )

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.ylabel("Attention weight")
        plt.xlabel("Token")
        plt.title(
            f"Attention from pronoun 'it'\n{sentence}"
        )

        plt.tight_layout()

        safe_name = (
            sentence[:30]
            .replace(" ", "_")
            .replace(".", "")
        )

        plt.savefig(
            OUTPUT_DIR
            / f"pronoun_{safe_name}.png",
            dpi=150,
        )

        plt.close()

    ambiguity_df = pd.DataFrame(rows)

    ambiguity_df.to_csv(
        OUTPUT_DIR / "ambiguity_test_results.csv",
        index=False,
    )

    print("\nAmbiguity test summary:")
    print(ambiguity_df.to_string(index=False))


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("DAY 22: TRANSFORMER ATTENTION FROM PAPER TO EXPERIMENT")
    print("=" * 70)

    # 1. Toy attention
    run_toy_attention_experiment()

    # 2. Pretrained transformer
    tokenizer, model = run_pretrained_experiment()

    # 3. Ambiguity test
    run_pronoun_ambiguity_test(
        tokenizer,
        model,
    )

    print("\n" + "=" * 70)
    print("EXPERIMENT COMPLETE")
    print("=" * 70)

    print("\nGenerated files are available in:")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()