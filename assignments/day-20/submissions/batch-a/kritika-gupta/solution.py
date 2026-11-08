import torch
from transformers import pipeline, set_seed

# ==========================================================
# Question 1: Select CPU or GPU
# ==========================================================

device = 0 if torch.cuda.is_available() else -1

print("Question 1")
print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Using Device: GPU")
else:
    print("Using Device: CPU")

# The same program works even without a GPU because the
# Hugging Face pipeline automatically runs on the CPU when
# CUDA is unavailable.

# ==========================================================
# Question 2: Create a Sentiment Pipeline
# ==========================================================

print("\nQuestion 2")

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

texts = [
    "This course is absolutely amazing!",
    "The service was terrible and slow.",
]

results = sentiment(texts)

for text, result in zip(texts, results):
    print(f"\nInput: {text}")
    print(result)

# ==========================================================
# Question 3: Analyze a Batch of Reviews
# ==========================================================

print("\nQuestion 3")

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

batch_results = sentiment(reviews)

for review, result in zip(reviews, batch_results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")

# ==========================================================
# Question 4: Examine an Unclear Input
# ==========================================================

print("\nQuestion 4")

unclear = "Blah blah lorem ipsum."

result = sentiment(unclear)[0]

print("Input:", unclear)
print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))

# A high confidence score does not guarantee correctness.
# The model may confidently classify meaningless or
# out-of-domain text because it always predicts one of
# the available labels.

# ==========================================================
# Question 5: Create a Text Generation Pipeline
# ==========================================================

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

# ==========================================================
# Question 6: Generate From Several Prompts
# ==========================================================

print("\nQuestion 6")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    print("-" * 50)
    print("Prompt:", prompt)

    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print(output[0]["generated_text"])

# Generated text may contain inaccurate information.
# It should not be treated as verified fact.

# ==========================================================
# Question 7: Compare Temperature Settings
# ==========================================================

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

# Lower temperature usually produces more predictable
# and focused output.
#
# Higher temperature usually produces more diverse and
# creative output.

# ==========================================================
# Question 8: Compare Sampling With Greedy Generation
# ==========================================================

print("\nQuestion 8")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always chooses the highest-probability
# next token, making the output more repeatable than
# random sampling.

# ==========================================================
# Question 9: Limitations Reflection
# ==========================================================

# 1. Generated facts should always be verified because
#    language models can produce incorrect or outdated
#    information.
#
# 2. Bias in the training data can influence the model's
#    responses and may lead to unfair or inaccurate outputs.
#
# 3. Model downloads can be slow because pre-trained models
#    are often hundreds of megabytes or even several gigabytes.
#
# 4. CPU generation is slower because CPUs perform fewer
#    parallel computations than GPUs.
#
# 5. Private or sensitive information should never be entered
#    into an unapproved AI system because it may create
#    privacy and security risks.

print("\nQuestion 9")
print("Pre-trained model output should always be reviewed and verified by a human before it is trusted or used.")