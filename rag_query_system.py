import os
import json
import faiss
import numpy as np
import requests
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google.oauth2 import service_account
import google.auth.transport.requests

# Load environment variables
load_dotenv()

# --- Google Gemini Setup ---
def get_access_token():
    key_path = os.path.join("secrets", "ai-therapist-5517-94f11d5b590b.json")
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    credentials = service_account.Credentials.from_service_account_file(key_path, scopes=scopes)
    credentials.refresh(google.auth.transport.requests.Request())
    return credentials.token

PROJECT_ID = "ai-therapist-5517"  # Replace with your actual project ID
LOCATION = "us-central1"            # Default location for Gemini models

# --- FAISS + Embedding Model Setup ---
INDEX_FILE = "./VectorStore/vector_store.index"
CHUNK_FILE = "./ProcessedData/chunks.json"

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_FILE)

with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

def retrieve_similar_chunks(query, top_k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[idx] for idx in indices[0]]

# --- Gemini 2.0 Flash Direct API Call ---
def call_gemini_flash(prompt_text):
    access_token = get_access_token()

    url = f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-1.5-flash:generateContent"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt_text}]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print("Gemini API error:", response.status_code, response.text)
        return "Sorry, I couldn't fetch a response."

# --- Generate Response Function ---
def generate_response(query, top_k=3):
    retrieved_chunks = retrieve_similar_chunks(query, top_k)
    context = "\n\n".join([chunk['text'] for chunk in retrieved_chunks])

    prompt = f"""You are a compassionate AI assistant trained to support university students with mental health concerns.
Use the following context to answer the question empathetically and informatively.

Context:
{context}

User Question:
{query}

Answer:"""

    answer = call_gemini_flash(prompt)
    return answer, retrieved_chunks

# --- Test Block ---
if __name__ == "__main__":
    test_query = "What are effective cognitive behavioral therapy techniques?"
    answer, sources = generate_response(test_query)
    print("Answer:", answer)
    print("\nSources:")
    for s in sources:
        print("-", s['source'])
