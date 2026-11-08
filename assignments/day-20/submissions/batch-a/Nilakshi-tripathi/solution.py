import torch
from transformers import pipeline, set_seed

# ==========================================================
# Question 1: Select CPU or GPU
# ==========================================================

device = 0 if torch.cuda.is_available() else -1

print("Question 1")
print("CUDA Available:", torch.cuda.is_available())
print("Device:", "GPU" if device == 0 else "CPU")
print()

# The same program still works without a GPU because Hugging Face
# pipelines automatically run on the CPU when device = -1.
# Execution is slower, but the code does not need to change.


# ==========================================================
# Question 2: Create a Sentiment Pipeline
# ==========================================================

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

print("Question 2")

texts = [
    "This course is absolutely amazing!",
    "The service was terrible and slow.",
]

for text in texts:
    result = sentiment(text)
    print(f"Input: {text}")
    print(result)

print()


# ==========================================================
# Question 3: Analyze a Batch of Reviews
# ==========================================================

print("Question 3")

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

results = sentiment(reviews)

for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")

print()


# ==========================================================
# Question 4: Examine an Unclear Input
# ==========================================================

print("Question 4")

unclear = "Blah blah lorem ipsum."
result = sentiment(unclear)[0]

print("Text:", unclear)
print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))
print()

# A high confidence score does not prove the model understood the text.
# The model always predicts one of its learned labels, even for meaningless
# or out-of-domain inputs. Confidence reflects the model's certainty in its
# prediction, not whether the input actually makes sense.


# ==========================================================
# Question 5: Create a Text Generation Pipeline
# ==========================================================

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

print("Question 5")

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
print()


# ==========================================================
# Question 6: Generate From Several Prompts
# ==========================================================

print("Question 6")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("=" * 60)
    print("Prompt:")
    print(prompt)
    print()
    print("Generated:")
    print(output[0]["generated_text"])
    print()

# Generated text may contain inaccurate information and should not
# be treated as verified fact.


# ==========================================================
# Question 7: Compare Temperature Settings
# ==========================================================

print("Question 7")

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

print("Temperature = 0.3")
print(low_temp[0]["generated_text"])
print()

print("Temperature = 1.2")
print(high_temp[0]["generated_text"])
print()

# Lower temperature usually produces more predictable and focused text.
# Higher temperature usually produces more varied and creative text.


# ==========================================================
# Question 8: Compare Sampling With Greedy Generation
# ==========================================================

print("Question 8")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])
print()

# Greedy generation always selects the most likely next token.
# Because no randomness is involved, the same prompt usually
# produces the same output each time.


# ==========================================================
# Question 9: Limitations Reflection
# ==========================================================

# 1. Generated facts should be verified because language models can
#    produce incorrect or outdated information.
#
# 2. Training-data bias can affect outputs by reflecting biases that
#    existed in the data used to train the model.
#
# 3. Model downloads can be difficult on a slow connection because
#    pretrained models are often hundreds of megabytes in size.
#
# 4. CPU generation is slower because CPUs have fewer parallel processing
#    capabilities than GPUs for deep learning workloads.
#
# 5. Private information should not be entered into an unapproved AI
#    system because it may create security or privacy risks.

print("Pre-trained model output should always be reviewed and verified by humans.")