# CampusCare: A RAG-Based AI Therapist for University Students

**CampusCare** is an AI-powered chatbot built using a **Retrieval-Augmented Generation (RAG)** pipeline designed specifically to support the mental well-being of college and university students. It retrieves contextually relevant information from a curated dataset of student mental health concerns and generates empathetic, human-like responses using large language models.

---

## Project Overview

Many university students face challenges like academic stress, burnout, loneliness, and anxiety. CampusCare provides an accessible support system by combining **Information Retrieval** techniques with **Language Generation**, helping students receive supportive and relevant guidance instantly.

This project serves both as a meaningful real-world application and an academic demonstration of IR principles like semantic search, vector indexing, and language model integration.

---

## Key Features

- Retrieval-Augmented Generation (RAG) architecture
- Context-aware responses powered by GPT-3.5 (or LLaMA2)
- Custom-curated dataset of ~250 mental health Q&A pairs
- Semantic similarity search using SentenceTransformers and FAISS
- Streamlit-based interactive chat interface
- Ready for local deployment

---

## Tech Stack

| Component | Tool |
|----------|------|
| Embeddings | `sentence-transformers` (all-MiniLM-L6-v2) |
| Vector Store | `FAISS` |
| Language Model | `OpenAI GPT-3.5` or `LLaMA2` (optional) |
| Backend | `Python`, `LangChain` |
| Frontend | `Streamlit` |
| Dataset Format | `CSV` / `JSON` |

---

