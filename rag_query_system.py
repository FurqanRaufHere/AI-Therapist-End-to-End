import os
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import requests

# Constants
CHUNK_FILE = "./ProcessedData/chunks.json"
EMBEDDING_FILE = "./ProcessedData/embeddings.npy"
INDEX_FILE = "./VectorStore/vector_store.index"

# Replace with your actual Groq API key
API_KEY = "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"

TOP_K = 5  # number of chunks to retrieve

# Load model and data
model = SentenceTransformer("all-MiniLM-L6-v2")
with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Load FAISS index
index = faiss.read_index(INDEX_FILE)

def get_query_embedding(query):
    return model.encode([query])[0]

def retrieve_relevant_chunks(query, k=TOP_K):
    query_embedding = get_query_embedding(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, k)
    relevant_chunks = [chunks[i]['text'] for i in indices[0]]
    return relevant_chunks

def augment_prompt(query, context_chunks):
    context = "\n\n".join(context_chunks)
    augmented_prompt = f"""You are a super chill, friendly therapist assistant who talks like a supportive Gen Z buddy.
Keep your answers:

- Warm, positive, and encouraging
- Casual, slangy, with a fun vibe (but still respectful and empathetic)
- Start with a catchy, upbeat hook or phrase to grab attention
- Use simple, relatable language — like you're chatting with a close friend
- Help the user feel understood, hopeful, and motivated

Use the info below to answer the user's question in this style.

Context:
{context}

User Question:
{query}

Answer:"""
    return augmented_prompt

# def call_llm(prompt):
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "llama-3.3-70b",  # Groq model name
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0.7,
#         "max_tokens": 500
#     }

#     # Groq API endpoint for chat completions
#     GROQ_API_URL = "https://api.groq.com/v1/chat/completions"

#     response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(data))

#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"[!] Error {response.status_code}: {response.text}"


def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    # Groq OpenAI-compatible endpoint
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"[!] Error {response.status_code}: {response.text}"



def rag_query_pipeline(user_query):
    context = retrieve_relevant_chunks(user_query)
    prompt = augment_prompt(user_query, context)
    response = call_llm(prompt)
    return response

def generate_response(user_query):
    """
    Returns (answer, sources) tuple as expected by Streamlit app.
    """
    answer = rag_query_pipeline(user_query)
    sources = []  # Implement if you want to return sources
    return answer, sources


if __name__ == "__main__":
    user_input = input("Ask a question: ")
    result = rag_query_pipeline(user_input)
    print("\n[✓] Response from RAG System:\n")
    print(result)
