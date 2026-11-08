# Day 17 Answers

## Question 1

### Difference between Traditional Machine Learning and Deep Learning

**Traditional Machine Learning:**
In traditional machine learning, people usually choose the important features from the data before training the model. The model learns using those selected features.

**Example:**
A spam email detector where features such as the number of links, special characters, and certain keywords are selected manually.

**Deep Learning:**
In deep learning, the model automatically learns useful features from raw data without requiring people to select them manually.

**Example:**
A face recognition system that learns facial features directly from images.

---

## Question 2

### 1. What is a Large Language Model?

A Large Language Model (LLM) is an AI model trained on a huge amount of text to understand and generate human-like language.

### 2. What is a Token?

A token is a small piece of text that an AI model processes. It can be a word, part of a word, or punctuation.

### 3. What does a Context Window limit?

The context window limits how much text the model can read and remember at one time while generating a response.

### Sentence split into words (classroom approximation of tokens)

Artificial | intelligence | is | changing | the | world.

### Why can a real tokenizer split text differently?

A real tokenizer may split words into smaller parts or combine punctuation differently, so its tokens are not always the same as words.

---

## Question 3

### Prompt 1

**Prompt:**
```
Explain machine learning.
```

**Short Summary of Response:**
The response gave a general explanation of machine learning, what it is, and where it is used.

---

### Prompt 2

**Prompt:**
```
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

**Short Summary of Response:**
The response explained machine learning in simple language and used a cricket example, making it easy for a child to understand.

---

### Which response was more useful and why?

The second response was more useful because it clearly defined the audience, limited the length, and requested a cricket example, making the explanation easier to understand.

---

## Question 4

### Prompt 1

```
Task: Classify the following review as Positive, Negative, or Neutral.
Review: "Service bahut slow thi, dobara nahi aaunga."

Output Format:
- Sentiment:
- Reason:

Tone: Professional
Constraint: Give only one sentiment label and explain the reason in one sentence.
```

---

### Prompt 2

```
Task: Create a short Hinglish Instagram caption for a home-cleaning service.

Output Format:
Caption:
Hashtags:

Tone: Friendly and attractive
Constraint: Caption should be under 20 words and include exactly 3 hashtags.
```

---

## Question 5

### 1. What should be verified before answering?

First, verify whether Dr. Rakesh Chaturvedi Meelan is a real scientist and whether the claimed inventions actually exist.

### 2. Two reliable sources or source types

- Google Scholar (https://scholar.google.com/)
- Official government or university websites

### 3. What would you say if you could not verify the claim?

"I could not find reliable evidence to confirm this person or these inventions, so I cannot provide a verified answer."

### 4. Why is confident wording from an AI not proof?

AI can produce convincing text even when the information is incorrect. Facts should always be verified using reliable sources.

**Access Date:** 25 July 2026

---

## Question 6

### Connection between Embeddings, Vector Databases, and RAG

```
Text
   ↓
Embeddings
   ↓
Vector Database
   ↓
Relevant Results
   ↓
LLM Answer
```

**Explanation:**

- Text is converted into numerical vectors called embeddings.
- These embeddings are stored in a vector database.
- When a user asks a question, the database finds the most similar information.
- The relevant information is sent to the LLM.
- The LLM uses this information to generate a more accurate answer.

### Example of RAG in a Training Institute

A training institute can store class notes, assignments, and study materials in a vector database. When students ask questions, the system retrieves the relevant notes and the LLM generates answers based on those notes instead of only relying on its general knowledge.

---

## Question 7

### 1. Difference between an AI Agent and a Chatbot

A chatbot mainly answers questions with text. An AI agent can also perform actions, make decisions, and use tools to complete tasks.

### 2. What is a Tool in an Agent System?

A tool is an external resource, such as a calculator, database, web search, or calendar, that an AI agent can use to complete tasks.

### 3. How MCP Helps

Model Context Protocol (MCP) provides a standard way for AI systems to connect with external tools and data sources safely and efficiently.

### Example Agent Task

**Task:** Book a meeting.

**Steps:**

1. Read the user's request.
2. Check the calendar.
3. Find a free time slot.
4. Create the meeting.
5. Send invitations.
6. Confirm the booking to the user.

---

## Question 8

### Responsible AI Checklist

- ✅ Verify important facts before using AI-generated information.
- ✅ Protect personal and private information.
- ✅ Check for bias or unfair content.
- ✅ Review the output manually before submitting or publishing.
- ✅ Acknowledge and verify sources whenever possible.
- ✅ Confirm that the output follows the requested format.
- ✅ Correct any grammar or factual mistakes.
- ✅ Use AI as a helper, not as the only source of information.

### Reflection

AI can make mistakes or provide outdated information. I should not rely only on AI for important decisions or factual claims. I will always verify important information using trusted sources and apply my own judgment before using it.