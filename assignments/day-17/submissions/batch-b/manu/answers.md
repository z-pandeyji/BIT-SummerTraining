# Day 17 Answers

## Question 1: Traditional Machine Learning and Deep Learning

Traditional machine learning usually requires people to select and prepare useful features from the raw data before training the model. For example, in house-price prediction, people may select features such as area, number of rooms, and location.

Deep learning can learn useful features automatically from raw data using multiple layers of neural networks. For example, a deep-learning image model can learn features such as edges, shapes, and objects directly from raw images.

---

## Question 2: LLMs, Tokens, and Context Windows

### 1. What is a Large Language Model?

A Large Language Model (LLM) is an AI model trained on a large amount of text to understand and generate human-like language.

### 2. What is a Token?

A token is a small unit of text processed by a language model. A token may be a complete word, part of a word, punctuation mark, or sometimes a space-related unit.

### 3. What does a Context Window Limit?

A context window limits how much text and information an AI model can process and consider at one time.

### Simple Classroom Approximation of Tokens

Sentence:

```text
Artificial intelligence is changing the world.
```

Simple word-based tokens:

```text
["Artificial", "intelligence", "is", "changing", "the", "world", "."]
```

A real tokenizer may split words into smaller subword pieces or process punctuation differently, so real tokens may not be exactly the same as words.

---

## Question 3: Compare Vague and Specific Prompts

### Prompt 1

```text
Explain machine learning.
```

### Short Summary of Response

The response would usually give a general definition of machine learning and may explain common types such as supervised, unsupervised, and reinforcement learning.

### Prompt 2

```text
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

### Short Summary of Response

The response would explain machine learning in simple language and use a cricket example to make the concept easier to understand.

### More Useful Response

The response to the second prompt would be more useful because the prompt gives specific instructions about the audience, length, and example. Specific prompts usually help produce more focused and relevant answers.

---

## Question 4: Write Two Effective Prompts

### 1. Review Classification Prompt

```text
Classify the following review as Positive, Negative, or Neutral. Explain the classification in exactly one sentence. Return the answer in this format: "Sentiment: [label] | Reason: [one-sentence explanation]". Keep the explanation concise and do not add extra information.

Review: "Service bahut slow thi, dobara nahi aaunga."
```

### 2. Hinglish Instagram Caption Prompt

```text
Write a short Hinglish Instagram caption promoting a professional home-cleaning service. Use a friendly and trustworthy tone, include one clear benefit of the service, and keep the caption under 25 words. Return only the caption and do not add hashtags.
```

---

## Question 5: Detect and Verify a Possible Hallucination

The claim about "Gorakhpur scientist Dr. Rakesh Chaturvedi Meelan" should not be accepted without verification.

### 1. What should be verified?

Before answering, I should verify:

* whether the person actually exists;
* whether the person is genuinely a scientist from Gorakhpur;
* whether the person's identity and professional background are documented;
* whether the claimed inventions are supported by reliable evidence;
* whether the name has been confused with another person.

### 2. Reliable sources or source types

I would search:

1. Official university, government, research institution, or patent-office records.
2. Reputable news organisations, academic publications, or recognised research databases.

### 3. If the claim cannot be verified

I would say:

> I could not reliably verify the identity of Dr. Rakesh Chaturvedi Meelan or the claim about three inventions from trustworthy sources, so I should not list inventions as established facts.

### 4. Why confident AI wording is not proof

An AI can generate a confident-sounding answer even when information is incorrect, incomplete, or invented. Confidence in the wording is not evidence that a claim is true, so important claims must be verified using reliable sources.

---

## Question 6: Embeddings, Vector Databases, and RAG

The connection can be understood as:

```text
Text -> Embeddings -> Vector Database -> Relevant Results -> LLM Answer
```

### Embeddings

Embeddings convert text into numerical vectors that represent the meaning of the text. Similar meanings usually produce vectors that are closer to each other.

### Vector Database

A vector database stores these embeddings and allows the system to search for text that is semantically similar to a user's question.

### Relevant Results

When a user asks a question, the question is converted into an embedding. The vector database then finds the most relevant stored information.

### LLM Answer

The relevant information is provided to the LLM as context. The LLM uses that information to generate an answer.

### Example: Training Institute

A training institute could convert its class notes, syllabus, assignments, and study material into embeddings and store them in a vector database.

When a student asks:

```text
What is supervised learning?
```

The system would:

1. convert the question into an embedding;
2. search the vector database;
3. retrieve the most relevant class notes;
4. provide those notes as context to the LLM;
5. generate an answer based on the institute's own study material.

This is called Retrieval-Augmented Generation (RAG).

---

## Question 7: AI Agents and MCP

### 1. AI Agent vs Text-Only Chatbot

A chatbot that only returns text mainly responds to the user's message. An AI agent can reason about a task, decide what actions are needed, use tools, observe results, and continue working toward a goal.

### 2. What is a Tool?

A tool is an external capability that an AI agent can use to perform an action or access information. Examples include a calculator, database, search system, calendar, file system, or API.

### 3. How MCP Can Help

MCP can provide a standard way for an AI system to connect with tools and data sources. This can help an AI system discover and use available capabilities in a more structured way.

### Example Agent Task

**Task:** Find the best available date for a training institute meeting and create a calendar event.

Possible steps:

1. Understand the user's request.
2. Check the calendar for available dates.
3. Compare the available time slots.
4. Select a suitable slot according to the user's requirements.
5. Create the calendar event using a calendar tool.
6. Confirm the result with the user.

---

## Question 8: Responsible AI Checklist

### Responsible AI Checklist

* [ ] Verify important facts using reliable sources.
* [ ] Do not share unnecessary private or sensitive information with AI systems.
* [ ] Check for possible bias or unfair assumptions in the output.
* [ ] Perform human review before using important AI-generated content.
* [ ] Acknowledge sources when information comes from external sources.
* [ ] Check whether the output follows the requested format and instructions.
* [ ] Review the output for errors, misleading claims, or missing context.
* [ ] Do not blindly trust confident-sounding AI answers.
* [ ] Consider the possible consequences before using AI-generated content.
* [ ] Protect confidential information and personal data.

### Reflection

I should not rely on an AI answer by itself when the information is important, high-stakes, or could cause harm if it is wrong. I should verify important facts using reliable sources and use human judgment. I should also be especially careful when dealing with medical, legal, financial, personal, or safety-related decisions.
