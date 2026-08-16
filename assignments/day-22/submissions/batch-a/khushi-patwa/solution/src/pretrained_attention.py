import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel


MODEL_NAME = "bert-base-uncased"


def load_sentences():
    """Load the experiment sentences from data/test_sentences.json."""

    data_path = Path("data/test_sentences.json")

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["sentences"]


def main():
    print("=" * 70)
    print("PRETRAINED TRANSFORMER ATTENTION EXPERIMENT")
    print("=" * 70)

    print(f"\nLoading pretrained model: {MODEL_NAME}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModel.from_pretrained(
        MODEL_NAME,
        output_attentions=True
    )

    model.eval()

    print("Model loaded successfully.")

    sentences = load_sentences()

    print(f"\nNumber of test sentences: {len(sentences)}")

    # We need at least five carefully chosen sentences.
    if len(sentences) < 5:
        raise ValueError(
            "The experiment requires at least five test sentences."
        )

    # Use the first five sentences from the experiment dataset.
    selected_sentences = sentences

    all_attention = []

    for index, sentence_item in enumerate(
        selected_sentences,
        start=1
    ):

        # Support either:
        # {"text": "..."}
        # or simply:
        # "..."
        if isinstance(sentence_item, dict):
            sentence = sentence_item["text"]
        else:
            sentence = sentence_item

        print("\n" + "-" * 70)
        print(f"Sentence {index}")
        print(sentence)

        inputs = tokenizer(
            sentence,
            return_tensors="pt"
        )

        tokens = tokenizer.convert_ids_to_tokens(
            inputs["input_ids"][0]
        )

        print("\nTokens:")
        print(tokens)

        with torch.no_grad():
            outputs = model(
                **inputs,
                output_attentions=True
            )

        attentions = outputs.attentions

        if attentions is None:
            raise RuntimeError(
                "The model did not return attention weights."
            )

        # Last Transformer layer
        last_layer_attention = attentions[-1]

        # Shape:
        # [batch, heads, tokens, tokens]
        #
        # Average across attention heads.
        mean_attention = (
            last_layer_attention
            .mean(dim=1)[0]
            .cpu()
            .numpy()
        )

        all_attention.append(
            {
                "sentence": sentence,
                "tokens": tokens,
                "attention": mean_attention
            }
        )

        # --------------------------------------------------
        # Print strongest attention connections
        # --------------------------------------------------

        print("\nStrongest attention connections:")

        connections = []

        for query_index in range(len(tokens)):
            for key_index in range(len(tokens)):

                if query_index == key_index:
                    continue

                connections.append(
                    (
                        mean_attention[
                            query_index,
                            key_index
                        ],
                        tokens[query_index],
                        tokens[key_index]
                    )
                )

        connections.sort(
            key=lambda item: item[0],
            reverse=True
        )

        for weight, query_token, key_token in connections[:5]:
            print(
                f"  {query_token:>12} -> "
                f"{key_token:<12} "
                f"{weight:.4f}"
            )

    # ------------------------------------------------------
    # Create visualization for the first sentence
    # ------------------------------------------------------

    first_result = all_attention[0]

    tokens = first_result["tokens"]
    attention = first_result["attention"]

    output_dir = Path("results/plots")

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.figure(
        figsize=(12, 9)
    )

    plt.imshow(
        attention,
        interpolation="nearest",
        aspect="auto"
    )

    plt.colorbar(
        label="Mean Attention Weight"
    )

    plt.xticks(
        range(len(tokens)),
        tokens,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(len(tokens)),
        tokens
    )

    plt.xlabel("Key Tokens")
    plt.ylabel("Query Tokens")

    plt.title(
        "Pretrained BERT: Mean Attention "
        "from Final Layer Across Heads"
    )

    plt.tight_layout()

    output_path = (
        output_dir / "pretrained_attention.png"
    )

    plt.savefig(
        output_path,
        dpi=200
    )

    plt.close()

    print("\n" + "=" * 70)
    print("PRETRAINED TRANSFORMER EXPERIMENT COMPLETED")
    print("=" * 70)

    print("\nAttention plot saved to:")
    print(output_path)

    print(
        "\nImportant interpretation note:"
        "\nAttention weights show token-to-token interaction patterns,"
        "\nbut they should not automatically be treated as causal"
        "\nor faithful explanations of model decisions."
    )


if __name__ == "__main__":
    main()