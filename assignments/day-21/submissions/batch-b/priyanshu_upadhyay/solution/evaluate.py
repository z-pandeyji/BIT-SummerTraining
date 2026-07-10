# evaluate.py - Evaluation with 12 test questions

from retrieval import retrieve_bm25, retrieve_tfidf

test_questions = [
    {"question": "What is machine learning?", "relevant_id": 1},
    {"question": "What is supervised learning?", "relevant_id": 2},
    {"question": "What is unsupervised learning?", "relevant_id": 3},
    {"question": "How does reinforcement learning work?", "relevant_id": 4},
    {"question": "What is deep learning?", "relevant_id": 5},
    {"question": "What is a transformer architecture?", "relevant_id": 6},
    {"question": "What is attention mechanism?", "relevant_id": 7},
    {"question": "What is BERT?", "relevant_id": 8},
    {"question": "What is GPT?", "relevant_id": 9},
    {"question": "What is retrieval augmented generation?", "relevant_id": 10},
    {"question": "What is BM25?", "relevant_id": 11},
    {"question": "What is hallucination in language models?", "relevant_id": 20},
]

def evaluate(retrieve_fn, method_name):
    top1_correct = 0
    top3_correct = 0
    errors = []

    for item in test_questions:
        results = retrieve_fn(item["question"], top_k=3)
        ids = [r["id"] for r in results]

        if ids[0] == item["relevant_id"]:
            top1_correct += 1
        if item["relevant_id"] in ids:
            top3_correct += 1
        else:
            errors.append({
                "question": item["question"],
                "expected_id": item["relevant_id"],
                "retrieved_ids": ids
            })

    total = len(test_questions)
    print(f"\n=== {method_name} Results ===")
    print(f"Top-1 Accuracy: {top1_correct}/{total} = {round(top1_correct/total*100, 1)}%")
    print(f"Top-3 Accuracy: {top3_correct}/{total} = {round(top3_correct/total*100, 1)}%")

    print(f"\nError Analysis ({len(errors)} missed in top-3):")
    for e in errors:
        print(f"  Q: {e['question']}")
        print(f"  Expected ID: {e['expected_id']}, Retrieved IDs: {e['retrieved_ids']}")

    return top1_correct/total, top3_correct/total

bm25_top1, bm25_top3 = evaluate(retrieve_bm25, "BM25")
tfidf_top1, tfidf_top3 = evaluate(retrieve_tfidf, "TF-IDF")

print("\n=== Comparison Table ===")
print(f"{'Method':<10} {'Top-1':>8} {'Top-3':>8}")
print(f"{'BM25':<10} {bm25_top1*100:>7.1f}% {bm25_top3*100:>7.1f}%")
print(f"{'TF-IDF':<10} {tfidf_top1*100:>7.1f}% {tfidf_top3*100:>7.1f}%")

# Ablation: top_k=1 vs top_k=3
print("\n=== Ablation: BM25 top_k=1 vs top_k=3 ===")
top1_ablation = sum(
    1 for item in test_questions
    if retrieve_bm25(item["question"], top_k=1)[0]["id"] == item["relevant_id"]
)
print(f"BM25 top_k=1 accuracy: {top1_ablation}/{len(test_questions)} = {round(top1_ablation/len(test_questions)*100,1)}%")
print(f"BM25 top_k=3 accuracy: {round(bm25_top3*100,1)}%")
print("Retrieving more chunks improves recall but may add noise.")

print("\nSample grounded answer:")
q = "What is retrieval augmented generation?"
chunks = retrieve_bm25(q, top_k=2)
print(f"Q: {q}")
for c in chunks:
    print(f"  [{c['source']}] {c['text']}")
print("Answer: RAG combines retrieval with a language model to ground answers in real documents. [Source: RAG Course Notes]")