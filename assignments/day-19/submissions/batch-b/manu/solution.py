import random
from collections import Counter


text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()


# Question 1: Prepare the Words

words = text.replace(".", "").split()

print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))


# Question 2: Build the Transition Chain

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nComplete Transition Dictionary:")
print(chains)

# One word can have several possible next words because the same word
# may appear in different contexts in the training text.


# Question 3: Inspect Learned Transitions

print("\nPossible next words:")
print("artificial:", chains.get("artificial", []))
print("is:", chains.get("is", []))
print("machine:", chains.get("machine", []))


# Question 4: Create a Safe Generator

def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current_word = start_word

    for _ in range(max_new_words):
        next_words = chains.get(current_word, [])

        if not next_words:
            break

        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word

    return " ".join(result)


print("\nGenerated text starting with artificial:")
print(generate("artificial"))


# Question 5: Make Random Output Reproducible

random.seed(42)
result_one = generate("artificial")

random.seed(42)
result_two = generate("artificial")

print("\nAre both generated results equal?")
print(result_one == result_two)

# A seed makes random output reproducible, which helps in debugging
# and comparing program results.


# Question 6: Compare Starting Words

print("\nGenerated text starting with machine:")
print(generate("machine"))

print("\nGenerated text starting with data:")
print(generate("data"))

print("\nGenerated text starting with world:")
print(generate("world"))


# Question 7: Find the Most Likely Next Word

def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counter = Counter(chains[word])
    return counter.most_common(1)[0]


print("\nMost likely next word:")
print("artificial:", most_likely_next("artificial"))
print("machine:", most_likely_next("machine"))
print("unknown:", most_likely_next("robot"))


# Question 8: Handle an Unknown Start Word

print("\nUnknown start word:")
print(generate("robot"))


# Question 9: Explain the Limitations

# 1. The generator can only use patterns found in its training text
# because it only remembers word transitions that appear in that text.

# 2. The output can become repetitive or grammatically incorrect because
# it chooses the next word based only on one previous word.

# 3. This one-word transition model is different from a transformer because
# a transformer uses attention and can consider much larger context,
# while this model only looks at the current word and its next-word choices.


print("\nThis classroom generator is not a real GPT model.")