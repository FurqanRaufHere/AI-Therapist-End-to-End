import streamlit as st
from rag_query_system import generate_response

st.set_page_config(page_title="Mind Matters - Therapy Chatbot", page_icon="🧠")

st.title("Mind Matters - Therapy RAG Chatbot")

# Initialize session state to keep chat history
if "history" not in st.session_state:
    st.session_state.history = []

def add_user_message(message):
    st.session_state.history.append({"role": "user", "content": message})

def add_bot_message(message, sources):
    st.session_state.history.append({"role": "bot", "content": message, "sources": sources})

# Input box for user query
user_query = st.text_input("Ask a question about therapy or mental health:", key="input")

# When user submits query
if st.button("Send") and user_query.strip():
    add_user_message(user_query.strip())
    with st.spinner("Thinking..."):
        answer, sources = generate_response(user_query.strip())
    add_bot_message(answer, sources)
    st.experimental_rerun()

# Display conversation history in chat bubbles
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f'<div style="background-color:#DCF8C6; padding:10px; border-radius:10px; max-width:70%; margin-left:auto; margin-bottom:8px;">**You:** {chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color:#E8E8E8; padding:10px; border-radius:10px; max-width:70%; margin-bottom:4px;">**Mind Matters:** {chat["content"]}</div>', unsafe_allow_html=True)
        with st.expander("Sources", expanded=False):
            for s in chat["sources"]:
                st.write(f"- {s['source']}")
