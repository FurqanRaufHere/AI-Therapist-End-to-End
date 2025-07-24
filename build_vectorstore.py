# build_vectorstore.py

import faiss #vector store
import numpy as np
import os

EMBEDDING_FILE = "./ProcessedData/embeddings.npy"
INDEX_FILE = "./VectorStore/vector_store.index"

os.makedirs("VectorStore", exist_ok=True)

def build_faiss_index():
    embeddings = np.load(EMBEDDING_FILE)
    dimension = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dimension)  # L2 distance
    index.add(embeddings)
    
    faiss.write_index(index, INDEX_FILE)
    print(f"[✓] FAISS index built and saved to {INDEX_FILE}")

if __name__ == "__main__":
    build_faiss_index()
