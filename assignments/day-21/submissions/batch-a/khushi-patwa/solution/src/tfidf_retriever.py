from pathlib import Path
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CHUNK_FILE = BASE_DIR / "results" / "chunks" / "chunks.json"

# -----------------------------
# Load Chunks
# -----------------------------
with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = [chunk["text"] for chunk in chunks]

# -----------------------------
# Build TF-IDF Index
# -----------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)


def search(query, top_k=3):
    """
    Search top-k relevant chunks using TF-IDF.
    """

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, tfidf_matrix)[0]

    ranked = similarity.argsort()[::-1]

    results = []

    for idx in ranked[:top_k]:
        results.append(
            {
                "score": float(similarity[idx]),
                "document": chunks[idx]["document"],
                "text": chunks[idx]["text"],
            }
        )

    return results


if __name__ == "__main__":
    question = input("Enter your question: ")

    answers = search(question)

    print("\nTop Results\n")

    for i, item in enumerate(answers, start=1):
        print("=" * 70)
        print(f"Rank : {i}")
        print(f"Score : {item['score']:.4f}")
        print(f"Document : {item['document']}")
        print()
        print(item["text"])
        print()