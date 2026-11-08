import csv
import time
from pathlib import Path

from transformers import pipeline


DATASET = Path(__file__).with_name("evaluation_dataset.csv")
RESULTS = Path(__file__).with_name("comparison_results.csv")


def load_dataset():
    examples = []

    with open(DATASET, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            examples.append({
                "text": row["text"],
                "label": row["label"]
            })

    return examples


def normalize_label(text):
    text = text.lower()

    if "positive" in text:
        return "positive"

    if "negative" in text:
        return "negative"

    return "unknown"


def calculate_accuracy(predictions, labels):
    correct = sum(
        prediction == label
        for prediction, label in zip(predictions, labels)
    )

    return correct / len(labels)


def zero_shot_experiment(classifier, examples):
    predictions = []
    latencies = []

    print("\n" + "=" * 70)
    print("ZERO-SHOT SENTIMENT CLASSIFICATION")
    print("=" * 70)

    for i, example in enumerate(examples, start=1):
        start = time.perf_counter()

        result = classifier(
            example["text"],
            candidate_labels=["positive", "negative"]
        )

        latency = time.perf_counter() - start
        latencies.append(latency)

        prediction = normalize_label(result["labels"][0])
        predictions.append(prediction)

        print(
            f"{i:02d}. Expected={example['label']:8s} "
            f"Predicted={prediction:8s} "
            f"Score={result['scores'][0]:.3f}"
        )

    accuracy = calculate_accuracy(
        predictions,
        [x["label"] for x in examples]
    )

    average_latency = sum(latencies) / len(latencies)

    return accuracy, average_latency, predictions


def few_shot_experiment(classifier, examples):
    predictions = []
    latencies = []

    demonstrations = [
        (
            "I absolutely loved this product. It works perfectly.",
            "positive"
        ),
        (
            "The service was terrible and very disappointing.",
            "negative"
        ),
        (
            "The application is fast and easy to use.",
            "positive"
        ),
        (
            "The product stopped working and I regret buying it.",
            "negative"
        )
    ]

    print("\n" + "=" * 70)
    print("FEW-SHOT PROMPTING")
    print("=" * 70)

    demo_text = "\n".join(
        f"Example: {text}\nLabel: {label}"
        for text, label in demonstrations
    )

    for i, example in enumerate(examples, start=1):

        prompt = f"""
Classify the sentiment of the following text as positive or negative.

{demo_text}

Text: {example['text']}
Label:
"""

        start = time.perf_counter()

        result = classifier(
            prompt,
            candidate_labels=["positive", "negative"]
        )

        latency = time.perf_counter() - start
        latencies.append(latency)

        prediction = normalize_label(result["labels"][0])
        predictions.append(prediction)

        print(
            f"{i:02d}. Expected={example['label']:8s} "
            f"Predicted={prediction:8s} "
            f"Score={result['scores'][0]:.3f}"
        )

    accuracy = calculate_accuracy(
        predictions,
        [x["label"] for x in examples]
    )

    average_latency = sum(latencies) / len(latencies)

    return accuracy, average_latency, predictions


def save_results(results):
    with open(RESULTS, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "approach",
                "accuracy",
                "average_latency_seconds",
                "cost",
                "privacy",
                "maintainability",
                "reproducibility"
            ]
        )

        writer.writeheader()

        for result in results:
            writer.writerow(result)


def error_analysis(examples, predictions, approach):
    print("\n" + "=" * 70)
    print(f"ERROR ANALYSIS: {approach}")
    print("=" * 70)

    errors = []

    for example, prediction in zip(examples, predictions):
        if prediction != example["label"]:
            errors.append((example, prediction))

    if not errors:
        print("No classification errors found.")
        return

    for i, (example, prediction) in enumerate(errors[:10], start=1):
        print(f"\nError {i}")
        print(f"Text     : {example['text']}")
        print(f"Expected : {example['label']}")
        print(f"Predicted: {prediction}")


def main():

    print("=" * 70)
    print("PROMPTING VS MODEL ADAPTATION EXPERIMENT")
    print("=" * 70)

    examples = load_dataset()

    print(f"\nLoaded examples: {len(examples)}")

    print("\nLoading zero-shot classification model...")

    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

    zero_accuracy, zero_latency, zero_predictions = (
        zero_shot_experiment(classifier, examples)
    )

    few_accuracy, few_latency, few_predictions = (
        few_shot_experiment(classifier, examples)
    )

    error_analysis(
        examples,
        few_predictions,
        "Few-shot Prompting"
    )

    results = [
        {
            "approach": "Zero-shot prompting",
            "accuracy": round(zero_accuracy, 4),
            "average_latency_seconds": round(zero_latency, 4),
            "cost": "Low",
            "privacy": "Medium",
            "maintainability": "High",
            "reproducibility": "High"
        },
        {
            "approach": "Few-shot prompting",
            "accuracy": round(few_accuracy, 4),
            "average_latency_seconds": round(few_latency, 4),
            "cost": "Low-Medium",
            "privacy": "Medium",
            "maintainability": "Medium-High",
            "reproducibility": "High"
        },
        {
            "approach": "Parameter-efficient fine-tuning",
            "accuracy": "Planned",
            "average_latency_seconds": "Planned",
            "cost": "Medium",
            "privacy": "High if locally trained",
            "maintainability": "Medium",
            "reproducibility": "Medium-High"
        }
    ]

    save_results(results)

    print("\n" + "=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)

    print(f"Zero-shot accuracy : {zero_accuracy:.3f}")
    print(f"Few-shot accuracy  : {few_accuracy:.3f}")

    print("\nResults saved to:")
    print("comparison_results.csv")

    print("\nAdaptation plan:")
    print(
        "Parameter-efficient fine-tuning such as LoRA is proposed "
        "as the third approach."
    )

    print("\n" + "=" * 70)
    print("EXPERIMENT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()