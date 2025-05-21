import streamlit as st
from rag_query_system import generate_response

st.title("Mind Matters - Therapy RAG Chatbot")

user_query = st.text_input("Ask a question about therapy or mental health:")

if st.button("Get Answer") and user_query:
    with st.spinner("Retrieving answer..."):
        answer, sources = generate_response(user_query)
        st.markdown("### Answer:")
        st.write(answer)
        st.markdown("### Sources:")
        for s in sources:
            st.write(f"- {s['source']}")
    