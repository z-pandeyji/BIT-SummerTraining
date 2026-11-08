from pathlib import Path
import json

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

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
# Load Embedding Model
# -----------------------------
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
embeddings = model.encode(texts, convert_to_numpy=True)

# -----------------------------
# Build FAISS Index
# -----------------------------
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def search(query, top_k=3):
    """
    Search top-k chunks using FAISS embeddings.
    """

    query_embedding = model.encode([query], convert_to_numpy=True)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for score, idx in zip(distances[0], indices[0]):
        results.append(
            {
                "score": float(score),
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
        print(f"Distance : {item['score']:.4f}")
        print(f"Document : {item['document']}")
        print()
        print(item["text"])
        print()