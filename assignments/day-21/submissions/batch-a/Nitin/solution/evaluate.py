from pathlib import Path

import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi


# Load documents
documents = []

with open(Path(__file__).with_name("documents.csv"), "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        documents.append(row)


texts = [doc["text"] for doc in documents]
document_ids = [doc["id"] for doc in documents]


# TF-IDF setup
vectorizer = TfidfVectorizer(stop_words="english")
document_vectors = vectorizer.fit_transform(texts)


# BM25 setup
tokenized_documents = [
    text.lower().split()
    for text in texts
]

bm25 = BM25Okapi(tokenized_documents)


# 12 questions.
# expected_id is the document containing the answer.
questions = [
    ("What is Python?", "1"),
    ("What are Python lists?", "2"),
    ("What are Python tuples?", "3"),
    ("What are Python dictionaries?", "4"),
    ("What is supervised learning?", "14"),
    ("What is classification?", "15"),
    ("What is regression?", "16"),
    ("What is a decision tree?", "18"),
    ("What is a random forest?", "19"),
    ("Why split data into training and testing sets?", "20"),
    ("What is machine learning?", "13"),
    ("What is Matplotlib?", "12"),
]


def tfidf_search(query, top_k=3):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    indices = scores.argsort()[::-1][:top_k]

    return [document_ids[i] for i in indices]


def bm25_search(query, top_k=3):
    query_tokens = query.lower().split()
    scores = bm25.get_scores(query_tokens)

    indices = scores.argsort()[::-1][:top_k]

    return [document_ids[i] for i in indices]


def evaluate(method_name, search_function):
    top1_correct = 0
    top3_correct = 0
    errors = []

    print("\n" + "=" * 70)
    print(method_name)
    print("=" * 70)

    for question, expected_id in questions:

        results = search_function(question, 3)

        top1 = results[0]
        top3 = results

        if top1 == expected_id:
            top1_correct += 1

        if expected_id in top3:
            top3_correct += 1

        print(f"\nQuestion: {question}")
        print(f"Expected Document: {expected_id}")
        print(f"Retrieved Top-3: {results}")

        if expected_id not in top3:
            errors.append({
                "question": question,
                "expected": expected_id,
                "retrieved": results
            })

    top1_accuracy = top1_correct / len(questions)
    top3_accuracy = top3_correct / len(questions)

    print("\nResults:")
    print(f"Top-1 Accuracy: {top1_accuracy:.3f}")
    print(f"Top-3 Accuracy: {top3_accuracy:.3f}")

    print("\nError Analysis:")

    if errors:
        for error in errors:
            print(
                f"- {error['question']} | "
                f"Expected: {error['expected']} | "
                f"Retrieved: {error['retrieved']}"
            )
    else:
        print("No retrieval errors in the test set.")

    return top1_accuracy, top3_accuracy


# Evaluate both retrieval methods
tfidf_results = evaluate(
    "TF-IDF Evaluation",
    tfidf_search
)

bm25_results = evaluate(
    "BM25 Evaluation",
    bm25_search
)


# Comparison
print("\n" + "=" * 70)
print("RETRIEVAL COMPARISON")
print("=" * 70)

print(
    f"TF-IDF  -> Top-1: {tfidf_results[0]:.3f}, "
    f"Top-3: {tfidf_results[1]:.3f}"
)

print(
    f"BM25    -> Top-1: {bm25_results[0]:.3f}, "
    f"Top-3: {bm25_results[1]:.3f}"
)

if bm25_results[1] > tfidf_results[1]:
    print("\nBM25 performed better based on Top-3 accuracy.")
elif tfidf_results[1] > bm25_results[1]:
    print("\nTF-IDF performed better based on Top-3 accuracy.")
else:
    print("\nBoth methods achieved the same Top-3 accuracy.")