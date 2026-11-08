from pathlib import Path
import json

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "results" / "chunks"

# Chunk configuration
CHUNK_SIZE = 120
OVERLAP = 20

def read_documents():
    """
    Read all .txt files from the data directory.
    """

    documents = []

    for file_path in sorted(DATA_DIR.glob("*.txt")):

        with open(file_path, "r", encoding="utf-8") as f:

            text = f.read()

        documents.append(
            {
                "document": file_path.name,
                "text": text,
            }
        )

    return documents

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def create_chunks():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    documents = read_documents()

    all_chunks = []

    chunk_id = 1

    for doc in documents:

        chunks = chunk_text(doc["text"])

        for chunk in chunks:

            all_chunks.append(
                {
                    "chunk_id": chunk_id,
                    "document": doc["document"],
                    "text": chunk,
                }
            )

            chunk_id += 1

    with open(
        OUTPUT_DIR / "chunks.json",
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(all_chunks, f, indent=4)

    print("=" * 50)
    print(f"Documents : {len(documents)}")
    print(f"Chunks    : {len(all_chunks)}")
    print("=" * 50)


if __name__ == "__main__":
    create_chunks()