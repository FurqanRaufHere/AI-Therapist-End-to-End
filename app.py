# # import streamlit as st
# # from rag_query_system import generate_response

# # st.set_page_config(page_title="Mind Matters - Therapy Chatbot", page_icon="🧠", layout="centered")

# # # Inject custom CSS for better chat UI styling
# # st.markdown(
# #     """
# #     <style>
# #     /* Page background */
# #     body {
# #         background-color: #f5f7fa;
# #         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #     }

# #     /* Container for chat bubbles */
# #     .chat-container {
# #         max-width: 700px;
# #         margin: auto;
# #         padding: 20px 10px;
# #     }

# #     /* User message bubble */
# #     .user-msg {
# #         background-color: #4a90e2;
# #         color: white;
# #         padding: 14px 18px;
# #         border-radius: 18px 18px 0 18px;
# #         max-width: 75%;
# #         margin-left: auto;
# #         margin-bottom: 12px;
# #         font-size: 16px;
# #         box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3);
# #     }

# #     /* Bot message bubble */
# #     .bot-msg {
# #         background-color: #e4e6eb;
# #         color: #242526;
# #         padding: 14px 18px;
# #         border-radius: 18px 18px 18px 0;
# #         max-width: 75%;
# #         margin-right: auto;
# #         margin-bottom: 8px;
# #         font-size: 16px;
# #         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
# #         white-space: pre-wrap;
# #     }

# #     /* Sources expander styling */
# #     .source-expander > div[role="button"] {
# #         font-weight: 600;
# #         color: #4a90e2;
# #         margin-bottom: 6px;
# #     }

# #     /* Source list styling */
# #     .source-list {
# #         margin-left: 12px;
# #         font-size: 14px;
# #         color: #555;
# #     }

# #     /* Input box styling */
# #     div[data-testid="stTextInput"] > div > input {
# #         font-size: 18px;
# #         padding: 12px 15px;
# #         border-radius: 10px;
# #         border: 1.5px solid #ccc;
# #         transition: border-color 0.3s ease;
# #     }

# #     div[data-testid="stTextInput"] > div > input:focus {
# #         border-color: #4a90e2;
# #         outline: none;
# #     }

# #     /* Send button styling */
# #     button[kind="primary"] {
# #         background-color: #4a90e2;
# #         color: white;
# #         font-size: 18px;
# #         padding: 12px 25px;
# #         border-radius: 10px;
# #         border: none;
# #         cursor: pointer;
# #         transition: background-color 0.3s ease;
# #     }
# #     button[kind="primary"]:hover {
# #         background-color: #357ABD;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.title("Mind Matters - Therapy RAG Chatbot")

# # if "history" not in st.session_state:
# #     st.session_state.history = []

# # def add_user_message(message):
# #     st.session_state.history.append({"role": "user", "content": message})

# # def add_bot_message(message, sources):
# #     if not sources or not isinstance(sources, list):
# #         sources = []
# #     st.session_state.history.append({"role": "bot", "content": message, "sources": sources})

# # user_query = st.text_input("Ask a question about therapy or mental health:", key="input")

# # if st.button("Send") and user_query.strip():
# #     add_user_message(user_query.strip())
# #     with st.spinner("Thinking..."):
# #         answer, sources = generate_response(user_query.strip())
# #     add_bot_message(answer, sources)

# # # Chat container div for layout
# # st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # for chat in st.session_state.history:
# #     if chat["role"] == "user":
# #         st.markdown(
# #             f'<div class="user-msg">**You:** {chat["content"]}</div>',
# #             unsafe_allow_html=True,
# #         )
# #     else:
# #         st.markdown(
# #             f'<div class="bot-msg">**Mind Matters:** {chat["content"]}</div>',
# #             unsafe_allow_html=True,
# #         )
# #         with st.expander("Sources", expanded=False, key=f"sources-{chat['content'][:30]}"):
# #             if chat.get("sources") and isinstance(chat["sources"], list):
# #                 for s in chat["sources"]:
# #                     st.markdown(f'<div class="source-list">- {s.get("source", "Unknown source")}</div>', unsafe_allow_html=True)
# #             else:
# #                 st.markdown('<div class="source-list">No sources found.</div>', unsafe_allow_html=True)

# # st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st
# from datetime import datetime
# import random
# from rag_query_system import generate_response

# # Page setup
# st.set_page_config(
#     page_title="MindMatters - Your AI Therapist",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Motivational quotes
# quotes = [
#     "You are stronger than you think.",
#     "This too shall pass.",
#     "Small steps every day.",
#     "Feelings are valid. You matter.",
#     "Be kind to yourself today."
# ]

# # Styling
# st.markdown("""
#     <style>
#     body {
#         background-color: #f0f4f8;
#     }
#     .main-header {
#         text-align: center;
#         padding: 2rem;
#         color: #4a4e69;
#     }
#     .chat-bubble {
#         border-radius: 1rem;
#         padding: 1rem;
#         margin-bottom: 1rem;
#         background-color: #e6eaf0;
#         width: fit-content;
#         max-width: 70%;
#     }
#     .user-bubble {
#         background-color: #929cdb;
#         margin-left: auto;
#         text-align: right;
#     }
#     .bot-bubble {
#         background-color: #8e85b1;
#         margin-right: auto;
#     }
#     .quote-box {
#         font-style: italic;
#         color: #555;
#         text-align: center;
#         margin-top: 1rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Landing page - Login / Signup
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.quote = random.choice(quotes)

# if not st.session_state.logged_in:
#     st.markdown("<div class='main-header'><h1>Welcome to MindMatters</h1><p>Your AI therapy space to feel heard and healed.</p></div>", unsafe_allow_html=True)
#     st.selectbox("Choose your tone:", ["Empathetic", "Gen-Z", "Motivational"], key="tone")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         st.session_state.logged_in = True
#     st.markdown(f"<div class='quote-box'>\"{st.session_state.quote}\"</div>", unsafe_allow_html=True)
#     st.stop()

# # Sidebar: Mood tracker and tools
# st.sidebar.header("🧘 Mood & Tools")
# st.sidebar.radio("How are you feeling today?", ["😊 Good", "😐 Okay", "😢 Down", "😠 Stressed"])
# st.sidebar.markdown("---")
# st.sidebar.subheader("Quick Tools")
# st.sidebar.button("🫁 Breathing Exercise")
# st.sidebar.button("📓 Journal Now")
# st.sidebar.button("🧘 Guided Meditation")
# st.sidebar.selectbox("Switch tone style:", ["Empathetic", "Gen-Z", "Motivational"], key="tone_toggle")

# # Main Chat User Interface
# st.markdown("<div class='main-header'><h2>MindMatters Chat</h2></div>", unsafe_allow_html=True)
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# user_input = st.text_input("What's on your mind?")
# if st.button("Send") and user_input:
#     st.session_state.chat_history.append({"role": "user", "content": user_input})

#     # Get RAG-based response from Gemini 2.0 Flash
#     with st.spinner("Thinking..."):
#         bot_response, _ = generate_response(user_input)

#     st.session_state.chat_history.append({"role": "bot", "content": bot_response})

# # Chat Display
# for msg in st.session_state.chat_history:
#     bubble_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
#     st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# # Post-session summary
# if len(st.session_state.chat_history) >= 4:
#     st.markdown("---")
#     st.subheader("📝 Session Summary")
#     st.markdown("- You expressed emotions around stress or anxiety\n- A moment of calm was encouraged\n- Stay consistent with your check-ins 💜")
#     st.markdown("**Tip:** Try a guided breathing tool from the sidebar before your next session.")

import streamlit as st
from rag_query_system import generate_response

# Page config
st.set_page_config(
    page_title="MindMatters - AI Therapist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark mode CSS styling
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .chat-container {
        max-width: 700px;
        height: 550px;
        overflow-y: auto;
        margin: 1rem auto;
        padding: 1rem;
        background-color: #1e1e1e;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.7);
        display: flex;
        flex-direction: column;
    }
    .chat-container::-webkit-scrollbar {
        width: 8px;
    }
    .chat-container::-webkit-scrollbar-track {
        background: #1e1e1e;
        border-radius: 12px;
    }
    .chat-container::-webkit-scrollbar-thumb {
        background-color: #555;
        border-radius: 12px;
    }
    .user-bubble {
        background-color: #4a90e2;
        color: white;
        align-self: flex-end;
        padding: 12px 18px;
        margin: 6px 0;
        border-radius: 18px 18px 0 18px;
        max-width: 75%;
        font-size: 16px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.6);
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    .bot-bubble {
        background-color: #333744;
        color: #d0d0d0;
        align-self: flex-start;
        padding: 12px 18px;
        margin: 6px 0;
        border-radius: 18px 18px 18px 0;
        max-width: 75%;
        font-size: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.7);
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    .input-row {
        max-width: 700px;
        margin: 0 auto 1rem;
        display: flex;
        gap: 0.5rem;
    }
    textarea[data-testid="stTextArea"] {
        flex-grow: 1;
        background-color: #1e1e1e !important;
        color: #eee !important;
        border: 1.5px solid #444;
        border-radius: 10px;
        padding: 12px 15px;
        font-size: 16px;
        resize: none;
    }
    textarea[data-testid="stTextArea"]:focus {
        border-color: #4a90e2 !important;
        outline: none !important;
    }
    button[kind="primary"] {
        background-color: #4a90e2;
        color: white;
        font-size: 16px;
        padding: 12px 24px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        user-select: none;
    }
    button[kind="primary"]:hover {
        background-color: #357ABD;
    }
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# To hold input temporarily
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def send_message():
    msg = st.session_state.user_input.strip()
    if not msg:
        return
    st.session_state.chat_history.append({"role": "user", "content": msg})
    st.session_state.user_input = ""

    with st.spinner("Thinking..."):
        bot_reply, _ = generate_response(msg)
    st.session_state.chat_history.append({"role": "bot", "content": bot_reply})

# Title
st.title("🧠 MindMatters - AI Therapist Chat")

# Chat box container
chat_box = st.container()
with chat_box:
    st.markdown('<div class="chat-container" id="chat-box">', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        css_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
        st.markdown(f'<div class="{css_class}">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Input row with textarea and send button
st.markdown('<div class="input-row">', unsafe_allow_html=True)
user_text = st.text_area(
    "",
    key="user_input",
    height=70,
    placeholder="Type your message here...",
    label_visibility="collapsed",
)

send_clicked = st.button("Send")

st.markdown("</div>", unsafe_allow_html=True)

# Send if button clicked
if send_clicked and st.session_state.user_input.strip():
    send_message()

# Send on Enter key press in textarea (workaround using form submit)
# Streamlit does not support direct enter to submit on textarea without JS hacks,
# so we rely on user pressing send or hitting enter + shift for new lines.

# Auto scroll chat to bottom after update (JS)
st.markdown(
    """
    <script>
    const chatBox = window.parent.document.getElementById('chat-box');
    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    </script>
    """,
    unsafe_allow_html=True,
)
