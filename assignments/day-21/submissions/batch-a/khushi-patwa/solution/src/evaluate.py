import json
from pathlib import Path
import pandas as pd

from tfidf_retriever import search as tfidf_search
from embedding_retriever import search as embedding_search

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

QUESTION_FILE = BASE_DIR / "data" / "questions.json"
RESULT_FILE = BASE_DIR / "results" / "evaluation_results.csv"

# -----------------------------
# Load Questions
# -----------------------------
with open(QUESTION_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

results = []

tfidf_top1 = 0
tfidf_top3 = 0

embedding_top1 = 0
embedding_top3 = 0

for item in questions:

    question = item["question"]
    expected = item["expected_document"]

    # -----------------------------
    # TF-IDF
    # -----------------------------
    tfidf_results = tfidf_search(question, top_k=3)

    tfidf_docs = [r["document"] for r in tfidf_results]

    tfidf_top1_hit = tfidf_docs[0] == expected
    tfidf_top3_hit = expected in tfidf_docs

    if tfidf_top1_hit:
        tfidf_top1 += 1

    if tfidf_top3_hit:
        tfidf_top3 += 1

    # -----------------------------
    # Embedding
    # -----------------------------
    embedding_results = embedding_search(question, top_k=3)

    embedding_docs = [r["document"] for r in embedding_results]

    embedding_top1_hit = embedding_docs[0] == expected
    embedding_top3_hit = expected in embedding_docs

    if embedding_top1_hit:
        embedding_top1 += 1

    if embedding_top3_hit:
        embedding_top3 += 1

    results.append(
        {
            "Question": question,
            "Expected": expected,

            "TFIDF_Top1": tfidf_docs[0],
            "TFIDF_Top1_Hit": tfidf_top1_hit,
            "TFIDF_Top3_Hit": tfidf_top3_hit,

            "Embedding_Top1": embedding_docs[0],
            "Embedding_Top1_Hit": embedding_top1_hit,
            "Embedding_Top3_Hit": embedding_top3_hit,
        }
    )

# -----------------------------
# Save CSV
# -----------------------------
df = pd.DataFrame(results)

df.to_csv(RESULT_FILE, index=False)

# -----------------------------
# Print Summary
# -----------------------------
total = len(questions)

print("=" * 60)

print(f"Questions : {total}")

print("\nTF-IDF")
print(f"Top-1 Accuracy : {tfidf_top1}/{total} = {tfidf_top1/total:.2%}")
print(f"Top-3 Accuracy : {tfidf_top3}/{total} = {tfidf_top3/total:.2%}")

print("\nEmbedding + FAISS")
print(f"Top-1 Accuracy : {embedding_top1}/{total} = {embedding_top1/total:.2%}")
print(f"Top-3 Accuracy : {embedding_top3}/{total} = {embedding_top3/total:.2%}")

print("=" * 60)