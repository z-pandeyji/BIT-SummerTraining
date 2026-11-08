import csv
import re
import time
from pathlib import Path


# ============================================================
# DAY 26 - AI STUDY ASSISTANT
# End-to-End AI Capstone Prototype
# ============================================================

PROJECT_TITLE = "AI Study Assistant"


# ------------------------------------------------------------
# Knowledge Base
# ------------------------------------------------------------

KNOWLEDGE_BASE = [
    {
        "topic": "machine learning",
        "keywords": ["machine learning", "ml", "supervised", "unsupervised"],
        "answer": (
            "Machine learning is a branch of AI in which systems learn "
            "patterns from data to make predictions or decisions. "
            "Common types include supervised, unsupervised, and reinforcement learning."
        ),
    },
    {
        "topic": "supervised learning",
        "keywords": ["supervised learning", "classification", "regression"],
        "answer": (
            "Supervised learning uses labelled training data. "
            "Classification predicts categories, while regression predicts numerical values."
        ),
    },
    {
        "topic": "unsupervised learning",
        "keywords": ["unsupervised learning", "clustering", "kmeans", "k-means"],
        "answer": (
            "Unsupervised learning works with data without target labels. "
            "Clustering algorithms such as K-Means group similar observations."
        ),
    },
    {
        "topic": "python",
        "keywords": ["python", "python language"],
        "answer": (
            "Python is a high-level programming language widely used in "
            "data analysis, machine learning, automation, and web development."
        ),
    },
    {
        "topic": "pandas",
        "keywords": ["pandas", "dataframe", "data frame"],
        "answer": (
            "Pandas is a Python library for data manipulation and analysis. "
            "Its main structures include Series and DataFrame."
        ),
    },
    {
        "topic": "numpy",
        "keywords": ["numpy", "array", "ndarray"],
        "answer": (
            "NumPy is a Python library for numerical computing. "
            "It provides efficient multidimensional arrays and mathematical operations."
        ),
    },
    {
        "topic": "database",
        "keywords": ["database", "dbms", "sql"],
        "answer": (
            "A database stores and organizes data so that it can be efficiently "
            "accessed and managed. DBMS software provides tools to create and manage databases."
        ),
    },
    {
        "topic": "api",
        "keywords": ["api", "application programming interface"],
        "answer": (
            "An API is an interface that allows different software systems "
            "to communicate using defined requests and responses."
        ),
    },
    {
        "topic": "cybersecurity",
        "keywords": ["cybersecurity", "security", "phishing"],
        "answer": (
            "Cybersecurity protects systems, networks, applications, and data "
            "from unauthorized access, attacks, and misuse."
        ),
    },
    {
        "topic": "artificial intelligence",
        "keywords": ["artificial intelligence", "ai", "artificial intelligence"],
        "answer": (
            "Artificial intelligence refers to systems designed to perform "
            "tasks that normally require human intelligence, such as reasoning, "
            "language processing, prediction, and perception."
        ),
    },
]


# ------------------------------------------------------------
# Safety / Privacy Guardrails
# ------------------------------------------------------------

BLOCKED_TERMS = [
    "password",
    "private key",
    "api key",
    "secret key",
    "credit card",
    "otp",
    "one time password",
]


def safety_check(question):
    """
    Detect requests involving secrets or sensitive information.
    """
    text = question.lower()

    for term in BLOCKED_TERMS:
        if term in text:
            return False, (
                "Request blocked by privacy guardrail. "
                "Do not submit passwords, private keys, API keys, OTPs, "
                "or other sensitive credentials."
            )

    return True, ""


# ------------------------------------------------------------
# Retrieval
# ------------------------------------------------------------

def retrieve_knowledge(question):
    """
    Simple keyword-based retrieval simulation.
    """
    text = question.lower()

    best_item = None
    best_score = 0

    for item in KNOWLEDGE_BASE:
        score = 0

        for keyword in item["keywords"]:
            if re.search(r"\b" + re.escape(keyword) + (r"s?\b" if keyword == "api" else r"\b"), text):
                score += 1

        # Prefer a matching specific concept over broad AI/ML categories.
        priority = int(item["topic"] not in {"machine learning", "artificial intelligence"})
        rank = (priority, score)
        previous_rank = (int(best_item["topic"] not in {"machine learning", "artificial intelligence"}), best_score) if best_item else (-1, 0)
        if score and rank > previous_rank:
            best_score = score
            best_item = item

    return best_item, best_score


# ------------------------------------------------------------
# Study Assistant
# ------------------------------------------------------------

def answer_question(question):
    start_time = time.perf_counter()

    safe, safety_message = safety_check(question)

    if not safe:
        latency = time.perf_counter() - start_time

        return {
            "success": False,
            "answer": safety_message,
            "topic": "safety",
            "confidence": 1.0,
            "latency_seconds": round(latency, 6),
            "reason": "privacy_guardrail",
        }

    item, score = retrieve_knowledge(question)

    if item is None:
        latency = time.perf_counter() - start_time

        return {
            "success": False,
            "answer": (
                "I could not find enough information in the study knowledge "
                "base to answer this question reliably."
            ),
            "topic": "unknown",
            "confidence": 0.0,
            "latency_seconds": round(latency, 6),
            "reason": "insufficient_knowledge",
        }

    # Heuristic display score; this is not a calibrated probability.
    confidence = min(0.95, 0.60 + (score * 0.15))

    latency = time.perf_counter() - start_time

    return {
        "success": True,
        "answer": item["answer"],
        "topic": item["topic"],
        "confidence": round(confidence, 2),
        "latency_seconds": round(latency, 6),
        "reason": "knowledge_retrieval",
    }


# ------------------------------------------------------------
# Evaluation
# ------------------------------------------------------------

def evaluate_test_set():
    dataset_path = Path(__file__).with_name("test_scenarios.csv")

    if not dataset_path.exists():
        print("test_scenarios.csv not found.")
        return

    results = []

    with open(dataset_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            question = row["question"]
            expected_topic = row["expected_topic"]

            result = answer_question(question)

            predicted_topic = result["topic"]

            correct = (
                predicted_topic == expected_topic
            )

            results.append({
                "id": row["id"],
                "difficulty": row["difficulty"],
                "question": question,
                "expected_topic": expected_topic,
                "predicted_topic": predicted_topic,
                "success": result["success"],
                "confidence": result["confidence"],
                "latency_seconds": result["latency_seconds"],
                "correct": correct,
                "reason": result["reason"],
            })

    output_path = Path(__file__).with_name("evaluation_results.csv")

    fieldnames = [
        "id",
        "difficulty",
        "question",
        "expected_topic",
        "predicted_topic",
        "success",
        "confidence",
        "latency_seconds",
        "correct",
        "reason",
    ]

    with open(
        output_path,
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    total = len(results)

    if total == 0:
        print("No evaluation examples found.")
        return

    correct_count = sum(
        1 for result in results if result["correct"]
    )

    success_count = sum(
        1 for result in results if result["success"]
    )

    average_latency = sum(
        result["latency_seconds"]
        for result in results
    ) / total

    accuracy = correct_count / total
    success_rate = success_count / total

    print("\n" + "=" * 70)
    print("EVALUATION RESULTS")
    print("=" * 70)

    print(f"Total test scenarios : {total}")
    print(f"Correct predictions  : {correct_count}")
    print(f"Accuracy             : {accuracy:.2%}")
    print(f"Successful responses : {success_count}")
    print(f"Success rate         : {success_rate:.2%}")
    print(f"Average latency      : {average_latency:.6f} seconds")

    print("\nResults saved to:")
    print(output_path)


# ------------------------------------------------------------
# Interactive Mode
# ------------------------------------------------------------

def interactive_mode():
    print("\n" + "=" * 70)
    print("AI STUDY ASSISTANT")
    print("=" * 70)

    print("Ask a study question.")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nStudent: ").strip()

        if question.lower() == "exit":
            print("Study session ended.")
            break

        if not question:
            print("Please enter a question.")
            continue

        result = answer_question(question)

        print("\nAssistant:")
        print(result["answer"])

        print(f"\nTopic: {result['topic']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Latency: {result['latency_seconds']} seconds")


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    print("=" * 70)
    print("DAY 26 - END-TO-END AI CAPSTONE")
    print("=" * 70)
    print("Prototype:", PROJECT_TITLE)

    evaluate_test_set()

    print("\nPrototype evaluation completed.")

    interactive_mode()


if __name__ == "__main__":
    main()