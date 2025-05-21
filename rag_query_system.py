import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
# For now, just leave GEMINI_API_KEY None or placeholder
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

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

def generate_response(query, top_k=3):
    retrieved_chunks = retrieve_similar_chunks(query, top_k)
    context = "\n\n".join([chunk['text'] for chunk in retrieved_chunks])

    # For now, we’ll return a dummy answer including the retrieved context
    answer = f"This is a stub answer. Retrieved context:\n{context}"

    return answer, retrieved_chunks

if __name__ == "__main__":
    test_query = "What are some effective cognitive behavioral therapy techniques?"
    answer, sources = generate_response(test_query)
    print("Answer:", answer)
    print("\nSources:")
    for s in sources:
        print("-", s['source'])
