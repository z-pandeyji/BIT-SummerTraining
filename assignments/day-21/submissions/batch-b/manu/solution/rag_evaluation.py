from pathlib import Path
import csv
import math
import re
from collections import Counter


BASE_DIR = Path(__file__).parent
DOCUMENTS_FILE = BASE_DIR / "documents" / "documents.csv"


def tokenize(text):
    """Convert text into lowercase word tokens."""
    return re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())


def load_documents():
    """Load documents from the CSV file."""
    documents = []

    with open(DOCUMENTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            documents.append(row)

    return documents


def build_chunks(documents, chunk_size=80):
    """
    Split documents into clean word-based chunks.

    Chunking rules:
    - Each document is split independently.
    - A chunk contains at most 80 words.
    - Chunks do not cross document boundaries.
    - Every chunk keeps its document ID and source.
    """

    chunks = []

    for document in documents:
        words = document["text"].split()

        for start in range(0, len(words), chunk_size):
            chunk_words = words[start:start + chunk_size]

            chunks.append(
                {
                    "chunk_id": (
                        f"{document['document_id']}_"
                        f"{start // chunk_size + 1}"
                    ),
                    "document_id": document["document_id"],
                    "title": document["title"],
                    "source": document["source"],
                    "text": " ".join(chunk_words),
                }
            )

    return chunks


def bm25_retrieve(query, chunks, top_k=3):
    """Retrieve chunks using BM25."""

    query_terms = tokenize(query)

    tokenized_chunks = [
        tokenize(chunk["text"])
        for chunk in chunks
    ]

    document_count = len(chunks)

    average_length = (
        sum(len(tokens) for tokens in tokenized_chunks)
        / document_count
    )

    document_frequency = Counter()

    for tokens in tokenized_chunks:
        for term in set(tokens):
            document_frequency[term] += 1

    k1 = 1.5
    b = 0.75

    scores = []

    for index, tokens in enumerate(tokenized_chunks):

        term_counts = Counter(tokens)
        document_length = len(tokens)
        score = 0.0

        for term in query_terms:

            if term not in term_counts:
                continue

            df = document_frequency[term]

            idf = math.log(
                1
                + (
                    document_count - df + 0.5
                )
                / (
                    df + 0.5
                )
            )

            term_frequency = term_counts[term]

            denominator = (
                term_frequency
                + k1
                * (
                    1
                    - b
                    + b
                    * document_length
                    / average_length
                )
            )

            score += (
                idf
                * (
                    term_frequency
                    * (k1 + 1)
                    / denominator
                )
            )

        scores.append((score, index))

    ranked = sorted(
        scores,
        key=lambda item: item[0],
        reverse=True
    )

    return [
        chunks[index]
        for score, index in ranked[:top_k]
        if score > 0
    ]


def cosine_similarity(vector_a, vector_b):
    """Calculate cosine similarity between two vectors."""

    all_terms = set(vector_a) | set(vector_b)

    dot_product = sum(
        vector_a.get(term, 0)
        * vector_b.get(term, 0)
        for term in all_terms
    )

    magnitude_a = math.sqrt(
        sum(
            value * value
            for value in vector_a.values()
        )
    )

    magnitude_b = math.sqrt(
        sum(
            value * value
            for value in vector_b.values()
        )
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (
        magnitude_a * magnitude_b
    )


def tfidf_retrieve(query, chunks, top_k=3):
    """Retrieve chunks using TF-IDF cosine similarity."""

    tokenized_chunks = [
        tokenize(chunk["text"])
        for chunk in chunks
    ]

    document_count = len(chunks)

    document_frequency = Counter()

    for tokens in tokenized_chunks:

        for term in set(tokens):
            document_frequency[term] += 1

    def make_tfidf_vector(tokens):

        term_counts = Counter(tokens)
        vector = {}

        for term, count in term_counts.items():

            idf = math.log(
                (
                    document_count + 1
                )
                / (
                    document_frequency[term] + 1
                )
            ) + 1

            vector[term] = count * idf

        return vector

    chunk_vectors = [
        make_tfidf_vector(tokens)
        for tokens in tokenized_chunks
    ]

    query_vector = make_tfidf_vector(
        tokenize(query)
    )

    scored_chunks = []

    for index, vector in enumerate(chunk_vectors):

        score = cosine_similarity(
            query_vector,
            vector
        )

        scored_chunks.append(
            (score, index)
        )

    ranked = sorted(
        scored_chunks,
        key=lambda item: item[0],
        reverse=True
    )

    return [
        chunks[index]
        for score, index in ranked[:top_k]
        if score > 0
    ]


TEST_QUESTIONS = [
    {
        "question": "What is a Python variable?",
        "answer_document": "D01",
    },
    {
        "question": "What are Python data types?",
        "answer_document": "D02",
    },
    {
        "question": "What is a Python list?",
        "answer_document": "D03",
    },
    {
        "question": "What is a tuple in Python?",
        "answer_document": "D04",
    },
    {
        "question": "What is a Python dictionary?",
        "answer_document": "D05",
    },
    {
        "question": "What is a set in Python?",
        "answer_document": "D06",
    },
    {
        "question": "How do conditional statements work?",
        "answer_document": "D07",
    },
    {
        "question": "What is a for loop?",
        "answer_document": "D08",
    },
    {
        "question": "What is a while loop?",
        "answer_document": "D09",
    },
    {
        "question": "What is a Python function?",
        "answer_document": "D10",
    },
    {
        "question": "What is recursion?",
        "answer_document": "D11",
    },
    {
        "question": "What is exception handling?",
        "answer_document": "D12",
    },
]


def evaluate_retriever(
    retriever,
    chunks,
    top_k=3
):
    """Evaluate retrieval accuracy."""

    correct_top_1 = 0
    correct_top_3 = 0

    results = []

    for item in TEST_QUESTIONS:

        retrieved = retriever(
            item["question"],
            chunks,
            top_k=top_k
        )

        retrieved_ids = [
            chunk["document_id"]
            for chunk in retrieved
        ]

        top_1_correct = (
            len(retrieved_ids) > 0
            and retrieved_ids[0]
            == item["answer_document"]
        )

        top_3_correct = (
            item["answer_document"]
            in retrieved_ids[:3]
        )

        if top_1_correct:
            correct_top_1 += 1

        if top_3_correct:
            correct_top_3 += 1

        results.append(
            {
                "question": item["question"],
                "expected": item["answer_document"],
                "retrieved": retrieved_ids,
                "top_1": top_1_correct,
                "top_3": top_3_correct,
            }
        )

    total = len(TEST_QUESTIONS)

    return {
        "top_1_accuracy": (
            correct_top_1 / total
        ),
        "top_3_accuracy": (
            correct_top_3 / total
        ),
        "results": results,
    }


def print_results(
    name,
    evaluation
):
    """Print evaluation results."""

    print(f"\n{name}")
    print("-" * len(name))

    print(
        "Top-1 Accuracy: "
        f"{evaluation['top_1_accuracy']:.2%}"
    )

    print(
        "Top-3 Accuracy: "
        f"{evaluation['top_3_accuracy']:.2%}"
    )

    for result in evaluation["results"]:

        print(
            f"\nQuestion: "
            f"{result['question']}"
        )

        print(
            f"Expected: "
            f"{result['expected']}"
        )

        print(
            f"Retrieved: "
            f"{result['retrieved']}"
        )

        print(
            f"Top-1 Correct: "
            f"{result['top_1']}"
        )

        print(
            f"Top-3 Correct: "
            f"{result['top_3']}"
        )


def generate_grounded_answer(
    question,
    retrieved_chunks
):
    """
    Generate a simple grounded answer
    using the highest-ranked retrieved chunk.
    """

    if not retrieved_chunks:

        return (
            "No relevant chunk was retrieved. "
            "The system should abstain rather than guess."
        )

    best_chunk = retrieved_chunks[0]

    return (
        f"{best_chunk['text']} "
        f"[Citation: "
        f"{best_chunk['chunk_id']}; "
        f"Source: "
        f"{best_chunk['source']}]"
    )


def run_ablation(chunks):

    print("\nAblation Experiment")
    print("-------------------")

    for top_k in [1, 3, 5]:

        bm25_result = evaluate_retriever(
            bm25_retrieve,
            chunks,
            top_k=top_k
        )

        tfidf_result = evaluate_retriever(
            tfidf_retrieve,
            chunks,
            top_k=top_k
        )

        print(
            f"\nRetrieved chunks k = {top_k}"
        )

        print(
            "BM25 Top-1: "
            f"{bm25_result['top_1_accuracy']:.2%}"
        )

        print(
            "BM25 Top-3: "
            f"{bm25_result['top_3_accuracy']:.2%}"
        )

        print(
            "TF-IDF Top-1: "
            f"{tfidf_result['top_1_accuracy']:.2%}"
        )

        print(
            "TF-IDF Top-3: "
            f"{tfidf_result['top_3_accuracy']:.2%}"
        )


def main():

    documents = load_documents()

    chunks = build_chunks(
        documents,
        chunk_size=80
    )

    print(
        f"Loaded documents: "
        f"{len(documents)}"
    )

    print(
        f"Created chunks: "
        f"{len(chunks)}"
    )

    bm25_evaluation = evaluate_retriever(
        bm25_retrieve,
        chunks,
        top_k=3
    )

    tfidf_evaluation = evaluate_retriever(
        tfidf_retrieve,
        chunks,
        top_k=3
    )

    print_results(
        "BM25 Evaluation",
        bm25_evaluation
    )

    print_results(
        "TF-IDF Evaluation",
        tfidf_evaluation
    )

    print(
        "\nGrounded Answer Examples"
    )

    print(
        "========================"
    )

    for item in TEST_QUESTIONS[:3]:

        retrieved = bm25_retrieve(
            item["question"],
            chunks,
            top_k=3
        )

        answer = generate_grounded_answer(
            item["question"],
            retrieved
        )

        print(
            f"\nQuestion: "
            f"{item['question']}"
        )

        print(
            f"Answer: "
            f"{answer}"
        )

    run_ablation(chunks)


if __name__ == "__main__":
    main()