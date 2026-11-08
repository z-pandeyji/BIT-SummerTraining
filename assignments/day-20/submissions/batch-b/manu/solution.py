import torch
from transformers import pipeline, set_seed


# Question 1: Select CPU or GPU

device = 0 if torch.cuda.is_available() else -1

print("CUDA available:", torch.cuda.is_available())

if device == 0:
    print("Device: GPU")
else:
    print("Device: CPU")

# The same program should work without a GPU so that users with
# normal computers can also run the program using the CPU.


# Question 2: Create a Sentiment Pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

print("\nSentiment Analysis:")

sentences = [
    "This course is absolutely amazing!",
    "The service was terrible and slow.",
]

for sentence in sentences:
    result = sentiment(sentence)
    print(sentence, "->", result)


# Question 3: Analyze a Batch of Reviews

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

print("\nBatch Review Analysis:")

review_results = sentiment(reviews)

for review, result in zip(reviews, review_results):
    label = result["label"]
    score = result["score"]

    print(f"{review} -> {label} | score {score:.3f}")


# Question 4: Examine an Unclear Input

unclear_text = "Blah blah lorem ipsum."

unclear_result = sentiment(unclear_text)[0]

print("\nUnclear Input:")
print(
    f"{unclear_text} -> "
    f"{unclear_result['label']} | "
    f"confidence {unclear_result['score']:.3f}"
)

# A high confidence score does not prove that meaningless or
# out-of-domain text was truly understood correctly. The model
# may still confidently assign a label even when the input has
# no clear meaning.


# Question 5: Create a Text-Generation Pipeline

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

set_seed(42)

prompt = "Artificial Intelligence will"

generated = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nText Generation:")
print(generated[0]["generated_text"])


# Question 6: Generate From Several Prompts

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

print("\nMultiple Prompt Generation:")

for prompt in prompts:
    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("\n" + "=" * 50)
    print("Prompt:", prompt)
    print("Generated:", result[0]["generated_text"])
    print("=" * 50)

# Generated text may contain inaccurate information.
# It should not automatically be treated as verified fact.


# Question 7: Compare Temperature Settings

temperature_prompt = "Artificial Intelligence will"

set_seed(42)

low_temperature_result = generator(
    temperature_prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

set_seed(42)

high_temperature_result = generator(
    temperature_prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nTemperature 0.3:")
print(low_temperature_result[0]["generated_text"])

print("\nTemperature 1.2:")
print(high_temperature_result[0]["generated_text"])

# Lower temperature usually produces more predictable output.
# Higher temperature usually produces more varied and creative output.


# Question 8: Compare Sampling With Greedy Generation

set_seed(42)

greedy_result = generator(
    temperature_prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nGreedy Generation:")
print(greedy_result[0]["generated_text"])

# Greedy generation usually selects the highest-probability next token.
# Therefore, it is generally more repeatable than sampled generation.


# Question 9: Limitations Reflection

# 1. Generated facts should be verified because a language model
# can produce incorrect or outdated information.

# 2. Training-data bias can affect outputs because the model may
# learn and reproduce patterns or biases present in its training data.

# 3. Model downloads can be difficult on a slow connection because
# pre-trained model files can be large.

# 4. CPU generation may be slower than GPU generation because GPUs
# can process many mathematical operations in parallel.

# 5. Private information should not be placed into an unapproved AI
# system because it may create privacy and security risks.

print("\nPre-trained model output still requires human review.")