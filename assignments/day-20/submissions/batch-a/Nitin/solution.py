import torch
from transformers import pipeline, set_seed

# -----------------------------
# Question 1: Select CPU or GPU
# -----------------------------

device = 0 if torch.cuda.is_available() else -1

print("Question 1")
print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Using Device: GPU")
else:
    print("Using Device: CPU")

# The same program works on CPU if a GPU is not available.

# ------------------------------------
# Question 2: Sentiment Analysis
# ------------------------------------

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

texts = [
    "This course is absolutely amazing!",
    "The service was terrible and slow."
]

print("\nQuestion 2")

results = sentiment(texts)

for text, result in zip(texts, results):
    print(f"\nText: {text}")
    print(result)

# ------------------------------------
# Question 3: Batch Review Analysis
# ------------------------------------

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

batch_results = sentiment(reviews)

print("\nQuestion 3")

for review, result in zip(reviews, batch_results):
    print(
        f"{review} -> {result['label']} | score {result['score']:.3f}"
    )
    
    # ------------------------------------
# Question 4: Examine an Unclear Input
# ------------------------------------

print("\nQuestion 4")

unclear_text = "Blah blah lorem ipsum."

result = sentiment(unclear_text)[0]

print("Text:", unclear_text)
print("Label:", result["label"])
print("Confidence Score:", round(result["score"], 3))

# A high confidence score does not guarantee that the model truly
# understood meaningless or out-of-domain text.

# ------------------------------------
# Question 5: Text Generation
# ------------------------------------

print("\nQuestion 5")

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

set_seed(42)

generated = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(generated[0]["generated_text"])

# ------------------------------------
# Question 6: Generate From Several Prompts
# ------------------------------------

print("\nQuestion 6")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    print("\n----------------------------")
    print("Prompt:", prompt)

    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("Generated Text:")
    print(output[0]["generated_text"])

# Generated text may contain incorrect information and should be verified.

# ------------------------------------
# Question 7: Compare Temperature
# ------------------------------------

print("\nQuestion 7")

prompt = "Artificial Intelligence will"

set_seed(42)
low_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

set_seed(42)
high_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nTemperature = 0.3")
print(low_temp[0]["generated_text"])

print("\nTemperature = 1.2")
print(high_temp[0]["generated_text"])

# Lower temperature usually produces more predictable output.
# Higher temperature usually produces more creative and varied output.

# ------------------------------------
# Question 8: Greedy Generation
# ------------------------------------

print("\nQuestion 8")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("Greedy Output:")
print(greedy[0]["generated_text"])

# Greedy generation always selects the most probable next token,
# making the output more repeatable than sampled generation.

# ------------------------------------
# Question 9: Reflection
# ------------------------------------

# Generated facts should always be verified because AI can produce
# incorrect or outdated information.
#
# Training-data bias can influence the responses produced by the model.
#
# Large models require downloading many files, which can take time
# on slow internet connections.
#
# CPU generation is usually slower because GPUs are optimized for
# parallel computations used in deep learning.
#
# Private or sensitive information should never be shared with
# unapproved AI systems to protect privacy and security.

print("\nQuestion 9")
print("Pre-trained model output should always be reviewed and verified by a human before it is trusted or used.")