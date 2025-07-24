#rag_query_system.py
import os
import json
import numpy as np
import faiss # for vector search
from dotenv import load_dotenv


model_cache = {}
index_cache = {}
chain_cache = {}


def get_model():
    if "sbert" not in model_cache:
        from sentence_transformers import SentenceTransformer
        model_cache["sbert"] = SentenceTransformer("all-MiniLM-L6-v2")
    return model_cache["sbert"]

def get_index():
    if "faiss_index" not in index_cache:
        import faiss
        index_cache["faiss_index"] = faiss.read_index(INDEX_FILE)
    return index_cache["faiss_index"]

def get_chain():
    if "chain" not in chain_cache:
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain.chains import LLMChain
        from langchain.prompts import PromptTemplate
        from langchain.memory import ConversationBufferMemory

        prompt = PromptTemplate(input_variables=["context", "question"], template=PROMPT_TEMPLATE)

        memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", return_messages=True)

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=API_KEY,
            temperature=0.5,
            max_tokens=500
        )

        chain_cache["chain"] = LLMChain(llm=llm, prompt=prompt, memory=memory)
    return chain_cache["chain"]



# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# File paths
CHUNK_FILE = "./ProcessedData/chunks.json"
INDEX_FILE = "./VectorStore/vector_store.index"
TOP_K = 5
with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)


PROMPT_TEMPLATE = """
You are a warm, friendly, and supportive therapist assistant who specializes in student mental health. Your job is to help students feel heard and supported while offering simple, clear, and practical guidance they can act on. Your tone should be kind, conversational, and emotionally intelligent — like a calm, caring friend who knows how to help.

-For short greetings (like "hi", "hello", "hey"):
  - Respond with only **1 or 2 sentences**.
  - Be warm and inviting — like a friendly check-in.
  - **Do not** give advice, paraphrase, or suggest steps unless the user shares more.
  - End with a **light, friendly question** to keep the door open, like:
    - "How is your day going?"
    - "What is on your mind today?"
    - "Wanna talk about anything specific?"

- If user responds to a text like (how are you doing?):
  - Keep it short and supportive.

- Speak with emotional maturity, like a thoughtful therapist or mentor.
- Acknowledge and validate the user's feelings before offering any suggestions.
- Use headings that feel natural and conversational, not robotic or like a manual.
- Avoid overusing bullet points. Use them only when needed — short lists, not instructions.
- Blend empathy and strategy: comfort first, then practical steps — but never rush into advice.
- Always end with an emotionally aware follow-up question. Let it feel like a human conversation, not an automated next step.


**Important formatting guidelines**:
- Do not start with quotes, disclaimers, or punctuation.
- Always respond using clean and simple **Markdown formatting**:
  - Use `####` for section headers
  - Use bullet points (`-`) or numbered lists for steps, suggestions, or tips
  - **Bold important ideas** for clarity and readability
- Keep it short and supportive:
  - For small talk or casual greetings (e.g. “hi”, “hello”), reply in 1-2 warm and welcoming sentences
  - For emotional or complex queries, give helpful advice in no more than **3-4 bullets per section** — don't overwhelm
- End with a **gentle follow-up question** to keep the conversation flowing (e.g., “Would you like to talk more about that?”, “How have you been coping with this lately?”, etc.)

Always prioritize clarity, kindness, and helpfulness. You're here to listen, guide, and make students feel a little better — one message at a time.


Chat History:
{chat_history}

Here's the context you should use:

{context}

Here's the user's question:

{question}

**Provide your neatly structured response in Markdown format below**:
"""


def get_query_embedding(query):
    model = get_model()  # ✅ Lazy-loads when needed
    return model.encode([query])[0]

def retrieve_relevant_chunks(query, k=TOP_K):
    query_embedding = get_query_embedding(query).reshape(1, -1)
    faiss.normalize_L2(query_embedding)  # normalize query vector
    index = get_index()  # ✅ Lazy-loads when needed
    distances, indices = index.search(query_embedding, k)
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "chunk": chunks[idx]["text"],
            "score": float(distances[0][i])
        })
    return results


def rag_query_pipeline(user_query):
    retrieved = retrieve_relevant_chunks(user_query)
    
    print("\nRetrieved Chunks with Cosine Similarities:\n")
    for i, item in enumerate(retrieved):
        print(f"[{i+1}] Score: {item['score']:.4f}")
        print(f"Chunk: {item['chunk'][:200]}...\n")

    context_text = "\n\n".join([item["chunk"] for item in retrieved])
    chain = get_chain() # ✅ Lazy-loads when needed
    result = chain.run({"context": context_text, "question": user_query})
    return result




def generate_response(user_query):

    answer = rag_query_pipeline(user_query)
    return answer, []  # Can add source tracking later

if __name__ == "__main__":
    user_input = input("Ask a question: ")
    response = rag_query_pipeline(user_input)
    print("\n[✓] Response from the RAG System:\n")
    print(response)
