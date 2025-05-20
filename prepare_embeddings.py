# prepare_embeddings.py

import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

INPUT_FILE = "./ProcessedData/extracted_texts.json"
CHUNK_FILE = "./ProcessedData/chunks.json"
EMBEDDING_FILE = "./ProcessedData/embeddings.npy"

os.makedirs("ProcessedData", exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=300):
    paragraphs = text.split('\n')
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current += para + " "
        else:
            chunks.append(current.strip())
            current = para + " "
    if current.strip():
        chunks.append(current.strip())
    return chunks

def prepare_chunks_and_embeddings():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        documents = json.load(f)

    all_chunks = []
    for doc in tqdm(documents, desc="Chunking documents"):
        chunks = chunk_text(doc['content'])
        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": doc['source']
            })

    with open(CHUNK_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=4, ensure_ascii=False)

    texts = [item["text"] for item in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    np.save(EMBEDDING_FILE, embeddings)

    print(f"[✓] Created {len(all_chunks)} chunks")
    print(f"[✓] Saved chunks to {CHUNK_FILE}")
    print(f"[✓] Saved embeddings to {EMBEDDING_FILE}")

if __name__ == "__main__":
    prepare_chunks_and_embeddings()
