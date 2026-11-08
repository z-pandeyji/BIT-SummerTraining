from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load documents
df = pd.read_csv(Path(__file__).with_name("documents.csv"))

# Clean text
df["text"] = df["text"].fillna("")


# TF-IDF retrieval
vectorizer = TfidfVectorizer(stop_words="english")
document_vectors = vectorizer.fit_transform(df["text"])


def retrieve_tfidf(query, top_k=3):
    """Return the top-k most relevant documents for a query."""
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(query_vector, document_vectors)[0]

    top_indices = scores.argsort()[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "id": int(df.iloc[index]["id"]),
            "text": df.iloc[index]["text"],
            "source": df.iloc[index]["source"],
            "score": float(scores[index]),
        })

    return results


# Example queries
queries = [
    "What is Python?",
    "What is a pandas DataFrame?",
    "What is supervised learning?",
    "What is classification?",
    "What is a decision tree?",
]


print("TF-IDF Retrieval Results")
print("=" * 60)

for query in queries:
    print(f"\nQuery: {query}")

    results = retrieve_tfidf(query, top_k=3)

    for rank, result in enumerate(results, start=1):
        print(
            f"{rank}. Document {result['id']} | "
            f"Score: {result['score']:.3f}"
        )
        print(f"   {result['text']}")
        print(f"   Source: {result['source']}")