import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# -----------------------------
# Question 1: Prepare the Words
# -----------------------------
text = text.replace(".", "")
words = text.split()

print("Number of words:", len(words))
print("First 10 words:", words[:10])
print("Unique words:", len(set(words)))

# -----------------------------
# Question 2: Build the Transition Chain
# -----------------------------
chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nTransition Dictionary:")
print(chains)

# One word can have multiple possible next words depending on different
# sentences in the training text.

# -----------------------------
# Question 3: Inspect Learned Transitions
# -----------------------------
print("\nNext words:")
print("artificial ->", chains.get("artificial", []))
print("is ->", chains.get("is", []))
print("machine ->", chains.get("machine", []))

# -----------------------------
# Question 4: Safe Generator
# -----------------------------
def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current = start_word

    for _ in range(max_new_words):
        next_words = chains.get(current, [])

        if not next_words:
            break

        current = random.choice(next_words)
        result.append(current)

    return " ".join(result)


print("\nGenerated from 'artificial':")
print(generate("artificial"))

# -----------------------------
# Question 5: Random Seed
# -----------------------------
random.seed(42)
text1 = generate("artificial")

random.seed(42)
text2 = generate("artificial")

print("\nSeed Test")
print(text1)
print(text2)
print("Equal:", text1 == text2)

# A random seed produces the same random output every time,
# making debugging and comparison easier.

# -----------------------------
# Question 6: Compare Starting Words
# -----------------------------
print("\nStarting with machine:")
print(generate("machine"))

print("\nStarting with data:")
print(generate("data"))

print("\nStarting with world:")
print(generate("world"))

# -----------------------------
# Question 7: Most Likely Next Word
# -----------------------------
def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    count = Counter(chains[word])
    return count.most_common(1)[0]


print("\nMost Likely Next Word")
print("artificial:", most_likely_next("artificial"))
print("machine:", most_likely_next("machine"))
print("robot:", most_likely_next("robot"))

# -----------------------------
# Question 8: Unknown Start Word
# -----------------------------
print("\nUnknown Start Word")
print(generate("robot"))
print("Program handled the unknown word safely without an exception.")

# -----------------------------
# Question 9: Limitations
# -----------------------------

# This generator only learns patterns that already exist in the training text.
# It may produce repetitive or grammatically incorrect sentences because it
# only predicts one word at a time.
# Unlike transformers, this model does not understand long-range context or
# use attention mechanisms.

print("\nThis classroom generator is not a real GPT model.")