# Topic: Using Pre-Trained Models With Hugging Face

import torch
from transformers import pipeline, set_seed

# (Ques 1) Select CPU or GPU

device = 0 if torch.cuda.is_available() else -1
print("CUDA Available:", torch.cuda.is_available())
print("Device:", "GPU" if device == 0 else "CPU")

# This program still works even if GPU is unavailable because
# Hugging Face pipelines automatically run on CPU when device = -1.

print("-" * 60)

# (Ques 2) Create a Sentiment Pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

sample_sentences = [
    "This course is absolutely amazing!",
    "The service was terrible and slow."
]

analysis = sentiment(sample_sentences)

for sentence, prediction in zip(sample_sentences, analysis):
    print(sentence)
    print(prediction)
    print()

print("-" * 60)

# (Ques 3) Analyze a Batch of Reviews

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

batch_results = sentiment(reviews)

for review, result in zip(reviews, batch_results):
    print(
        f"{review} -> {result['label']} | score {result['score']:.3f}"
    )

print("-" * 60)

# (Ques 4) Examine an Unclear Input

unclear = "Blah blah lorem ipsum."

result = sentiment(unclear)[0]

print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))

# A high confidence score does not guarantee that the model
# truly understood meaningless or out-of-domain text.
# The model always predicts one of its learned labels even
# for unfamiliar or nonsensical inputs.

print("-" * 60)

# (Ques 5) Create a Text-Generation Pipeline

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

print("-" * 60)

# (Ques 6) Generate  From Several Prompts

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    print("=" * 60)
    print("Prompt:")
    print(prompt)
    print()

    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("Generated:")
    print(output[0]["generated_text"])

# Generated text may contain inaccurate information.
# It should not be treated as verified fact.

print("-" * 60)

# (Ques 7) Compare Temperature Settings

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

# Lower temperature generally produces more predictable output.
# Higher temperature usually produces more diverse and creative output.

print("-" * 60)

# (Ques 8) Compare Sampling With Greedy Generation

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always selects the highest probability token.
# Therefore it is usually more repeatable than sampled generation.

print("-" * 60)

# (Ques 9) Write a Limitations Reflection

# 1. Generated facts should always be verified because AI can
#    produce incorrect or outdated information.
#
# 2. Bias in training data can influence outputs and may
#    produce unfair or unbalanced responses.
#
# 3. Model downloads may be difficult on slow connections
#    because pretrained models are often hundreds of MBs.
#
# 4. CPU generation is slower because CPUs have fewer parallel
#    processing cores compared to GPUs.
#
# 5. Private information should never be entered into an
#    unapproved AI system because it could expose sensitive data.

print("Pre-trained model output should always be reviewed and verified by humans.")