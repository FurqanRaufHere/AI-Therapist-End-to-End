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
    model="gemini-2.0-flash",  # use "gemini-pro" or "gemini-1.5-flash" depending on your model
    google_api_key=API_KEY,
    temperature=0.7,
    max_tokens=500
)

# Prompt template
PROMPT_TEMPLATE = """You are a super chill, friendly therapist assistant who talks like a supportive Gen Z buddy.
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
{question}

Answer:
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
    distances, indices = index.search(query_embedding, k)
    return [chunks[i]['text'] for i in indices[0]]

def rag_query_pipeline(user_query):
    context = retrieve_relevant_chunks(user_query)
    result = chain.run({"context": "\n\n".join(context), "question": user_query})
    return result

def generate_response(user_query):
    answer = rag_query_pipeline(user_query)
    return answer, []  # Can add source tracking later

if __name__ == "__main__":
    user_input = input("Ask a question: ")
    response = rag_query_pipeline(user_input)
    print("\n[✓] Response from RAG System:\n")
    print(response)
