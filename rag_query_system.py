import os
import json
import numpy as np
import faiss
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# File paths
CHUNK_FILE = "./ProcessedData/chunks.json"
INDEX_FILE = "./VectorStore/vector_store.index"
TOP_K = 5

# Load chunks and FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)
index = faiss.read_index(INDEX_FILE)

# LangChain model setup with Gemini 2.0 Flash
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=API_KEY,
    temperature=0.5,
    max_tokens=500
)

# Prompt template
# PROMPT_TEMPLATE = """You are a super chill, friendly therapist assistant who talks like a supportive Gen Z buddy.
# Keep your answers:
# - Warm, positive, and encouraging
# - Casual, slangy, with a fun vibe (but still respectful and empathetic)
# - Start with a catchy, upbeat hook or phrase to grab attention
# - Use simple, relatable language — like you're chatting with a close friend
# - Help the user feel understood, hopeful, and motivated

# Use the info below to answer the user's question in this style.

# Context:
# {context}

# User Question:
# {question}

# Answer:
# """

PROMPT_TEMPLATE = """
You are an empathetic, supportive therapist assistant specialized in student mental health. Your role is to provide compassionate, clear, and practical guidance, structured neatly in Markdown format, to help students effectively manage emotional and academic challenges.

**Always follow these strict formatting rules**:
- Never start your response with quotes or unnecessary punctuation.
- Always use clear and structured Markdown formatting:
  - Use headings (`####`) to clearly separate main sections.
  - Use bullet points (`-`) or numbered lists for tips, steps, and techniques.
  - Bold important key points to enhance readability.
- Adapt your response to the user's query length:
  - Short queries ("hi", "hello", "hey"): Reply warmly, briefly, and invitingly in one or two sentences.
  - Detailed or complex queries: Provide concise, structured responses with clear headings and no more than 3-5 bullet points or steps per section to ensure readability and brevity.
- Maintain a compassionate, reassuring, and professional tone, making students feel validated and hopeful.
- Provide gentle encouragement, practical strategies, and clearly actionable advice tailored for students.
- Keep responses for complex queries concise yet comprehensive, prioritizing clarity and ease of reading to avoid overwhelming the reader.

Here's the context you should use:

{context}

Here's the user's question:

{question}

**Provide your neatly structured response in Markdown format below**:
"""

prompt = PromptTemplate(input_variables=["context", "question"], template=PROMPT_TEMPLATE)
chain = LLMChain(llm=llm, prompt=prompt)

# tone_prompt_map = {
#     "Empathetic": "Respond in a warm, caring, and deeply understanding manner. Use gentle and validating language.",
#     "Gen Z": "Respond with casual Gen Z slang, emojis, and a chill tone. Keep it short and relatable.",
#     "Motivational": "Respond like a motivational coach, use uplifting, powerful words to encourage the user.",
#     "Professional": "Respond formally and respectfully, with clinical accuracy but human understanding."
# }


def get_query_embedding(query):
    return model.encode([query])[0]

def retrieve_relevant_chunks(query, k=TOP_K):
    query_embedding = get_query_embedding(query).reshape(1, -1)
    faiss.normalize_L2(query_embedding)  # normalize query vector
    distances, indices = index.search(query_embedding, k)
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "chunk": chunks[idx]["text"],
            "score": float(distances[0][i])
        })
    return results



# def rag_query_pipeline(user_query):
#     context = retrieve_relevant_chunks(user_query)
#     result = chain.run({"context": "\n\n".join(context), "question": user_query})
#     return result

def rag_query_pipeline(user_query):
    retrieved = retrieve_relevant_chunks(user_query)
    
    print("\n🔍 Retrieved Chunks with Cosine Similarities:\n")
    for i, item in enumerate(retrieved):
        print(f"[{i+1}] Score: {item['score']:.4f}")
        print(f"Chunk: {item['chunk'][:200]}...\n")

    context_text = "\n\n".join([item["chunk"] for item in retrieved])
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
