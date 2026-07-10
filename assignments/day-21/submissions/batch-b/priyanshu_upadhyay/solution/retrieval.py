# retrieval.py - BM25 and TF-IDF Retrieval Methods

from documents import documents
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
import numpy as np

corpus = [doc["text"] for doc in documents]
tokenized_corpus = [text.lower().split() for text in corpus]

# BM25 Retrieval
bm25 = BM25Okapi(tokenized_corpus)

def retrieve_bm25(query, top_k=3):
    tokenized_query = query.lower().split()
    scores = bm25.get_scores(tokenized_query)
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [documents[i] for i in top_indices]

# TF-IDF Retrieval
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

def retrieve_tfidf(query, top_k=3):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [documents[i] for i in top_indices]