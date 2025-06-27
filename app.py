import warnings
import streamlit as st
from datetime import datetime
import random
from rag_query_system import generate_response
import nest_asyncio


# # Page setup
# st.set_page_config(
#     page_title="MindMatters - Your AI Therapist",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

warnings.filterwarnings("ignore", message="Tried to instantiate class '__path__._path'")
nest_asyncio.apply()

st.set_page_config(
    page_title=" MindMatters - Your AI Therapist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.mindmatters.ai/help',
        'Report a bug': 'https://www.mindmatters.ai/bug-report',
        'About': '# MindMatters is your AI-powered mental wellness companion.'
    }
)



# Motivational quotes
quotes = [
    "You are stronger than you think.",
    "This too shall pass.",
    "Small steps every day.",
    "Feelings are valid. You matter.",
    "Be kind to yourself today."
]

# Styling with improved color scheme and layout

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0f7fa, #f3e5f5); /* Soothing blue to purple gradient */
        color: #2d2d5e;
        font-family: 'Arial', sans-serif;
    }
            


    /* Header */
    .main-header {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        padding: 2rem;
        color: white;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="25" cy="75" r="1" fill="white" opacity="0.05"/><circle cx="75" cy="25" r="1" fill="white" opacity="0.05"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        pointer-events: none;
    }
    
    .header-content {
        position: relative;
        z-index: 1;
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        font-weight: 400;
    }
    
    .header-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
    }





    
    # .main-header {
    #     text-align: center;
    #     padding: 2rem;
    #     margin-bottom: 1rem;
    # }
    # .main-header h1 {
    #     font-size: 3rem;
    #     font-weight: bold;
    #     background: linear-gradient(90deg, #4a90e2, #9b59b6); /* Gradient text for title */
    #     -webkit-background-clip: text;
    #     -webkit-text-fill-color: transparent;
    #     text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    # }
    # .main-header p {
    #     font-size: 1.2rem;
    #     color: #4a4e69;
    # }
            


    .chat-bubble {
        border-radius: 1rem;
        padding: 1rem;
        margin-bottom: 1rem;
        width: fit-content;
        max-width: 70%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for bubbles */
    }
    .user-bubble {
        background-color: #a3bffa; /* Light blue for user */
        color: #2d2d5e;
        margin-left: auto;
        text-align: right;
    }
    .bot-bubble {
        background-color: #d1c4e9; /* Softer purple for bot */
        color: #2d2d5e;
        margin-right: auto;
    }
    .quote-box {
        font-style: italic;
        color: #4a4e69;
        text-align: center;
        margin-top: 1rem;
    }
    .stSidebar {
        background: linear-gradient(135deg, #c6d9ff, #d9c6ff); /* Sidebar gradient */
    }
    .stButton>button {
        background-color: #7f9cf5; /* Button color */
        color: #ffffff;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #9f7aea; /* Hover color */
    }
    .stTextInput {
        width: 100%;
        margin-top: 1rem;
        background: #e0f7fa; /* Match background gradient */
    }
    .stTextInput>div>input {
        background-color: #e6e6ff;
        color: #2d2d5e;
        border-radius: 0.5rem;
        width: 80%;
        margin: 0 auto;
        display: block;
    }
    .stSelectbox>div>div {
        background-color: #e6e6ff;
        color: #2d2d5e;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Landing page - Login / Signup (Restored to Original)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.quote = random.choice(quotes)

if not st.session_state.logged_in:
    st.markdown("<div class='main-header'><h1>Welcome to MindMatters</h1><p>Your AI therapy space to feel heard and healed.</p></div>", unsafe_allow_html=True)
    st.selectbox("Choose your tone:", ["Empathetic", "Gen-Z", "Motivational"], key="tone")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.logged_in = True
    st.markdown(f"<div class='quote-box'>\"{st.session_state.quote}\"</div>", unsafe_allow_html=True)
    st.stop()

# Sidebar: Mood tracker and tools
st.sidebar.header("🧘 Mood & Tools")
st.sidebar.radio("How are you feeling today?", ["😊 Good", "😐 Okay", "😢 Down", "😠 Stressed"])
st.sidebar.markdown("---")
st.sidebar.subheader("Quick Tools")
st.sidebar.button("🫁 Breathing Exercise")
st.sidebar.button("📓 Journal Now")
st.sidebar.button("🧘 Guided Meditation")
st.sidebar.selectbox("Switch tone style:", ["Empathetic", "Gen-Z", "Motivational"], key="tone_toggle")

# Main Chat User Interface
st.markdown("<div class='main-header'><h1>🧠 MindMatters Chat</h1></div>", unsafe_allow_html=True)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Display
for msg in st.session_state.chat_history:
    bubble_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# User Input (at Bottom)
user_input = st.text_input("What's on your mind?")
if st.button("Send") and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get RAG-based response from Gemini 2.0 Flash
    with st.spinner("Thinking..."):
        bot_response, _ = generate_response(user_input)

    st.session_state.chat_history.append({"role": "bot", "content": bot_response})

# Post-session summary
if len(st.session_state.chat_history) >= 10:
    st.markdown("---")
    st.subheader("📝 Session Summary")
    st.markdown("- You expressed emotions around stress or anxiety\n- A moment of calm was encouraged\n- Stay consistent with your check-ins 💜")
    st.markdown("**Tip:** Try a guided breathing tool from the sidebar before your next session.")