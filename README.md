# CampusCare: A RAG-Based AI Therapist for University Students

**CampusCare** is an AI-powered chatbot built using a **Retrieval-Augmented Generation (RAG)** pipeline, specifically designed to support the mental well-being of university students. It retrieves contextually relevant information from a large, curated dataset of student mental health topics and generates empathetic responses using **Google Gemini 2.0 Flash**.

---

## Project Overview

University students face increasing psychological challenges including exam anxiety, burnout, loneliness, imposter syndrome, and adjustment stress. CampusCare provides an accessible support system using **Information Retrieval (IR)** techniques like semantic search and vector similarity, paired with large language model generation. It is both a meaningful real-world support tool and a complete academic demonstration of IR methodologies.

---

## Key Features

- Retrieval-Augmented Generation (RAG) architecture
- Context-aware and empathetic responses powered by **Gemini 2.0 Flash**
- Massive custom-curated dataset (~10,000+ Q&A entries)
- Combines PDF therapy books and structured JSON content
- Semantic search via **SentenceTransformers + FAISS**
- Responsive Streamlit-based chat interface
- Fully local and deployable pipeline

---

## Tech Stack

| Component         | Tool                                      |
|------------------|-------------------------------------------|
| Embeddings        | `sentence-transformers` (MiniLM-L6-v2)    |
| Vector Index      | `FAISS`                                   |
| Language Model    | `Google Gemini 2.0 Flash`                 |
| Backend Logic     | `Python`, `LangChain`    |
| Frontend Interface| `Streamlit`                               |
| Data Sources      | `Mental health PDFs` + `TherapyData.json`   |

---

## Project Pipeline

1. **Data Ingestion**  
   Extract text from PDFs and load TherapyData Q&A from JSON.

2. **Text Chunking & Embedding**  
   Clean and chunk the text, then embed with `sentence-transformers`.

3. **Vector Indexing**  
   Build FAISS index from chunk embeddings for fast retrieval.

4. **RAG Retrieval + Generation**  
   On each query: embed → retrieve top chunks → generate Gemini response.

5. **Streamlit Interface**  
   Frontend that enables interactive chat in a conversational layout.

---

## How to Run Locally

1. **Clone this repository**
```bash
git clone https://github.com/FurqanRaufHere/AI-Therapist-End-to-End.git
cd CampusCare
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set Gemini API key**
Create a `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

4. **Run the pipeline**
```bash
python extract_pdf.py
python prepare_embeddings.py
python build_vectorstore.py
```

5. **Launch the app**
```bash
streamlit run app.py
```

---

## Authors
- Muhammad Furqan Rauf (231185)
- Syeda Sara Batool (231173)
- Syed Faraz Kashif (231163)

---

## License
Built as part of an academic project under the Department of Creative Technologies, AIR University. Not a replacement for professional mental health care.
