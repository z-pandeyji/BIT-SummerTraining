from embedding_retriever import search


def generate_answer(question):
    """
    Generate a grounded answer using the top retrieved chunk.
    """

    results = search(question, top_k=1)

    if not results:
        print("No relevant information found.")
        return

    best = results[0]

    print("\n" + "=" * 70)
    print("QUESTION")
    print("=" * 70)
    print(question)

    print("\n" + "=" * 70)
    print("GENERATED ANSWER")
    print("=" * 70)
    print(best["text"])

    print("\n" + "=" * 70)
    print("CITATION")
    print("=" * 70)
    print(best["document"])


if __name__ == "__main__":

    question = input("Enter your question: ")

    generate_answer(question)