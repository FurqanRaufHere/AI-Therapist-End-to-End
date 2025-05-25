# import streamlit as st
# from rag_query_system import generate_response

# st.set_page_config(page_title="Mind Matters - Therapy Chatbot", page_icon="🧠", layout="centered")

# # Inject custom CSS for better chat UI styling
# st.markdown(
#     """
#     <style>
#     /* Page background */
#     body {
#         background-color: #f5f7fa;
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }

#     /* Container for chat bubbles */
#     .chat-container {
#         max-width: 700px;
#         margin: auto;
#         padding: 20px 10px;
#     }

#     /* User message bubble */
#     .user-msg {
#         background-color: #4a90e2;
#         color: white;
#         padding: 14px 18px;
#         border-radius: 18px 18px 0 18px;
#         max-width: 75%;
#         margin-left: auto;
#         margin-bottom: 12px;
#         font-size: 16px;
#         box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3);
#     }

#     /* Bot message bubble */
#     .bot-msg {
#         background-color: #e4e6eb;
#         color: #242526;
#         padding: 14px 18px;
#         border-radius: 18px 18px 18px 0;
#         max-width: 75%;
#         margin-right: auto;
#         margin-bottom: 8px;
#         font-size: 16px;
#         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
#         white-space: pre-wrap;
#     }

#     /* Sources expander styling */
#     .source-expander > div[role="button"] {
#         font-weight: 600;
#         color: #4a90e2;
#         margin-bottom: 6px;
#     }

#     /* Source list styling */
#     .source-list {
#         margin-left: 12px;
#         font-size: 14px;
#         color: #555;
#     }

#     /* Input box styling */
#     div[data-testid="stTextInput"] > div > input {
#         font-size: 18px;
#         padding: 12px 15px;
#         border-radius: 10px;
#         border: 1.5px solid #ccc;
#         transition: border-color 0.3s ease;
#     }

#     div[data-testid="stTextInput"] > div > input:focus {
#         border-color: #4a90e2;
#         outline: none;
#     }

#     /* Send button styling */
#     button[kind="primary"] {
#         background-color: #4a90e2;
#         color: white;
#         font-size: 18px;
#         padding: 12px 25px;
#         border-radius: 10px;
#         border: none;
#         cursor: pointer;
#         transition: background-color 0.3s ease;
#     }
#     button[kind="primary"]:hover {
#         background-color: #357ABD;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("Mind Matters - Therapy RAG Chatbot")

# if "history" not in st.session_state:
#     st.session_state.history = []

# def add_user_message(message):
#     st.session_state.history.append({"role": "user", "content": message})

# def add_bot_message(message, sources):
#     if not sources or not isinstance(sources, list):
#         sources = []
#     st.session_state.history.append({"role": "bot", "content": message, "sources": sources})

# user_query = st.text_input("Ask a question about therapy or mental health:", key="input")

# if st.button("Send") and user_query.strip():
#     add_user_message(user_query.strip())
#     with st.spinner("Thinking..."):
#         answer, sources = generate_response(user_query.strip())
#     add_bot_message(answer, sources)

# # Chat container div for layout
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# for chat in st.session_state.history:
#     if chat["role"] == "user":
#         st.markdown(
#             f'<div class="user-msg">**You:** {chat["content"]}</div>',
#             unsafe_allow_html=True,
#         )
#     else:
#         st.markdown(
#             f'<div class="bot-msg">**Mind Matters:** {chat["content"]}</div>',
#             unsafe_allow_html=True,
#         )
#         with st.expander("Sources", expanded=False, key=f"sources-{chat['content'][:30]}"):
#             if chat.get("sources") and isinstance(chat["sources"], list):
#                 for s in chat["sources"]:
#                     st.markdown(f'<div class="source-list">- {s.get("source", "Unknown source")}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown('<div class="source-list">No sources found.</div>', unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)























































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
























































# # Second Code:

# # import streamlit as st
# # from rag_query_system import generate_response

# # # Page config
# # st.set_page_config(
# #     page_title="MindMatters - AI Therapist",
# #     page_icon="🧠",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Dark mode CSS styling
# # st.markdown(
# #     """
# #     <style>
# #     body, .block-container {
# #         background-color: #121212;
# #         color: #e0e0e0;
# #         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #     }
# #     # .chat-container {
# #     #     max-width: 70px;
# #     #     overflow-y: auto;
# #     #     margin: 1rem auto;
# #     #     padding: 1rem;
# #     #     background-color: #1e1e1e;
# #     #     border-radius: 12px;
# #     #     box-shadow: 0 4px 12px rgba(0,0,0,0.7);
# #     #     display: flex;
# #     #     flex-direction: column;
# #     }
# #     .chat-container::-webkit-scrollbar {
# #         width: 8px;
# #     }
# #     .chat-container::-webkit-scrollbar-track {
# #         background: #1e1e1e;
# #         border-radius: 12px;
# #     }
# #     .chat-container::-webkit-scrollbar-thumb {
# #         background-color: #555;
# #         border-radius: 12px;
# #     }
# #     .user-bubble {
# #         background-color: #4a90e2;
# #         color: white;
# #         align-self: flex-end;
# #         padding: 12px 18px;
# #         margin: 6px 0;
# #         border-radius: 18px 18px 0 18px;
# #         max-width: 75%;
# #         font-size: 16px;
# #         box-shadow: 0 2px 8px rgba(74, 144, 226, 0.6);
# #         word-wrap: break-word;
# #         white-space: pre-wrap;
# #     }
# #     .bot-bubble {
# #         background-color: #333744;
# #         color: #d0d0d0;
# #         align-self: flex-start;
# #         padding: 12px 18px;
# #         margin: 6px 0;
# #         border-radius: 18px 18px 18px 0;
# #         max-width: 75%;
# #         font-size: 16px;
# #         box-shadow: 0 2px 8px rgba(0,0,0,0.7);
# #         word-wrap: break-word;
# #         white-space: pre-wrap;
# #     }
# #     .input-row {
# #         max-width: 700px;
# #         margin: 0 auto 1rem;
# #         display: flex;
# #         gap: 0.5rem;
# #     }
# #     textarea[data-testid="stTextArea"] {
# #         flex-grow: 1;
# #         background-color: #1e1e1e !important;
# #         color: #eee !important;
# #         border: 1.5px solid #444;
# #         border-radius: 10px;
# #         padding: 12px 15px;
# #         font-size: 16px;
# #         resize: none;
# #     }
# #     textarea[data-testid="stTextArea"]:focus {
# #         border-color: #4a90e2 !important;
# #         outline: none !important;
# #     }
# #     button[kind="primary"] {
# #         background-color: #4a90e2;
# #         color: white;
# #         font-size: 16px;
# #         padding: 12px 24px;
# #         border-radius: 10px;
# #         border: none;
# #         cursor: pointer;
# #         transition: background-color 0.3s ease;
# #         user-select: none;
# #     }
# #     button[kind="primary"]:hover {
# #         background-color: #357ABD;
# #     }
# #     footer {
# #         visibility: hidden;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )
# # # Initialize session state variables
# # if "logged_in" not in st.session_state:
# #     st.session_state.logged_in = False
# # if "quote" not in st.session_state:
# #     st.session_state.quote = "You are stronger than you think."
# #     if "author" not in st.session_state:
# #         st.session_state.author = "Unknown"
# # if "tone" not in st.session_state:
# #     st.session_state.tone = "Empathetic"
# # if "history" not in st.session_state:
# #     st.session_state.history = []
# #     # Main application

# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # if "user_input" not in st.session_state:
# #     st.session_state.user_input = ""

# # # Flag to indicate input was sent by button click
# # if "send_by_button" not in st.session_state:
# #     st.session_state.send_by_button = False

# # def send_message():
# #     msg = st.session_state.user_input.strip()
# #     if not msg:
# #         return
# #     st.session_state.chat_history.append({"role": "user", "content": msg})
    
# #     # Clear input only if called via textarea on_change (not button)
# #     if not st.session_state.send_by_button:
# #         st.session_state.user_input = ""

# #     with st.spinner("Thinking..."):
# #         bot_reply, _ = generate_response(msg)
# #     st.session_state.chat_history.append({"role": "bot", "content": bot_reply})

# # # Title
# # st.title("🧠 MindMatters - AI Therapist Chat")

# # # Chat box container
# # chat_box = st.container()
# # with chat_box:
# #     st.markdown('<div class="chat-container" id="chat-box">', unsafe_allow_html=True)
# #     for msg in st.session_state.chat_history:
# #         css_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
# #         st.markdown(f'<div class="{css_class}">{msg["content"]}</div>', unsafe_allow_html=True)
# #     st.markdown("</div>", unsafe_allow_html=True)

# # # Input row with textarea and send button
# # st.markdown('<div class="input-row">', unsafe_allow_html=True)
# # user_text = st.text_area(
# #     "",
# #     key="user_input",
# #     height=70,
# #     placeholder="Type your message here...",
# #     label_visibility="collapsed",
# #     on_change=send_message,  # Send message on Enter key press
# # )
# # send_clicked = st.button("Send")
# # st.markdown("</div>", unsafe_allow_html=True)

# # if send_clicked and st.session_state.user_input.strip():
# #     st.session_state.send_by_button = True  # Set flag to prevent clearing input twice
# #     send_message()
# #     st.session_state.user_input = ""  # Now clear input safely after send_message
# #     st.session_state.send_by_button = False  # Reset flag

# # # Footer with motivational quote
# # st.markdown(
# #     f"""
# #     <footer style="text-align: center; margin-top: 2rem; color: #888;">
# #         <p>💬 {st.session_state.quote} - <em>{st.session_state.author}</em></p>
# #     </footer>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # # Third Code:

# # import streamlit as st
# # import requests
# # import json
# # from datetime import datetime
# # import time

# # # Page configuration
# # st.set_page_config(
# #     page_title="University AI Therapist",
# #     page_icon="🧠",
# #     layout="wide",
# #     initial_sidebar_state="collapsed"
# # )

# # # Custom CSS for styling
# # st.markdown("""
# # <style>
# #     .main-header {
# #         background: linear-gradient(90deg, #3B82F6, #6366F1);
# #         padding: 1rem;
# #         border-radius: 10px;
# #         color: white;
# #         margin-bottom: 2rem;
# #     }
    
# #     .chat-container {
# #         max-height: 500px;
# #         overflow-y: auto;
# #         padding: 1rem;
# #         border: 1px solid #E5E7EB;
# #         border-radius: 10px;
# #         background-color: #F8FAFC;
# #     }
    
# #     .user-message {
# #         background: linear-gradient(90deg, #8B5CF6, #EC4899);
# #         color: white;
# #         padding: 0.75rem;
# #         border-radius: 15px;
# #         margin: 0.5rem 0;
# #         margin-left: 20%;
# #         text-align: right;
# #     }
    
# #     .ai-message {
# #         background: white;
# #         color: #374151;
# #         padding: 0.75rem;
# #         border-radius: 15px;
# #         margin: 0.5rem 0;
# #         margin-right: 20%;
# #         border: 1px solid #E5E7EB;
# #         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
# #     }
    
# #     .crisis-footer {
# #         background: #EFF6FF;
# #         padding: 1rem;
# #         border-radius: 10px;
# #         margin-top: 2rem;
# #         border: 1px solid #DBEAFE;
# #     }
    
# #     .timestamp {
# #         font-size: 0.75rem;
# #         opacity: 0.7;
# #         margin-top: 0.25rem;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # Initialize session state
# # if "messages" not in st.session_state:
# #     st.session_state.messages = [
# #         {
# #             "role": "assistant",
# #             "content": "Hello! I'm here to provide a safe space for you to share your thoughts and feelings. How are you doing today?",
# #             "timestamp": datetime.now()
# #         }
# #     ]

# # if "session_id" not in st.session_state:
# #     st.session_state.session_id = str(int(time.time()))

# # # Backend API configuration
# # API_BASE_URL = "http://localhost:8000"  # Replace with your backend URL
# # API_ENDPOINT = f"{API_BASE_URL}/api/chat"

# # def call_backend_api(user_message, session_id):
# #     """Call the backend RAG pipeline API"""
# #     try:
# #         payload = {
# #             "message": user_message,
# #             "session_id": session_id,
# #             # Add any other required parameters for your RAG pipeline
# #             "context": "university_mental_health",
# #             "user_type": "student"
# #         }
        
# #         response = requests.post(
# #             API_ENDPOINT,
# #             json=payload,
# #             headers={
# #                 "Content-Type": "application/json",
# #                 # Add authentication headers if needed
# #                 # "Authorization": f"Bearer {your_token}"
# #             },
# #             timeout=30
# #         )
        
# #         if response.status_code == 200:
# #             data = response.json()
# #             # Adjust based on your backend response format
# #             return data.get("response", data.get("message", "I'm here to help."))
# #         else:
# #             return f"Sorry, I'm having technical difficulties (Error {response.status_code}). Please try again."
            
# #     except requests.exceptions.Timeout:
# #         return "I'm taking a bit longer to respond. Please try again."
# #     except requests.exceptions.ConnectionError:
# #         return "I'm having trouble connecting right now. Please check your connection and try again."
# #     except Exception as e:
# #         st.error(f"API Error: {str(e)}")
# #         return "I'm sorry, I'm having technical difficulties. Please try again in a moment."

# # # Header
# # st.markdown("""
# # <div class="main-header">
# #     <h1>🧠 University AI Therapist</h1>
# #     <p>Confidential Support Chat - Your mental health matters</p>
# # </div>
# # """, unsafe_allow_html=True)

# # # Sidebar with controls
# # with st.sidebar:
# #     st.header("Chat Controls")
# #     if st.button("🔄 New Chat"):
# #         st.session_state.messages = [
# #             {
# #                 "role": "assistant",
# #                 "content": "Hello! I'm here to provide a safe space for you to share your thoughts and feelings. How are you doing today?",
# #                 "timestamp": datetime.now()
# #             }
# #         ]
# #         st.session_state.session_id = str(int(time.time()))
# #         st.rerun()
    
# #     st.markdown("---")
# #     st.markdown("**🔒 Privacy Notice**")
# #     st.markdown("This conversation is confidential and secure.")
    
# #     st.markdown("**💡 Tips**")
# #     st.markdown("- Be honest about your feelings")
# #     st.markdown("- Take your time to respond")
# #     st.markdown("- Remember: seeking help is strength")

# # # Chat display
# # chat_placeholder = st.empty()

# # with chat_placeholder.container():
# #     st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
# #     for message in st.session_state.messages:
# #         timestamp = message["timestamp"].strftime("%H:%M")
        
# #         if message["role"] == "user":
# #             st.markdown(f"""
# #             <div class="user-message">
# #                 <strong>You:</strong> {message["content"]}
# #                 <div class="timestamp">{timestamp}</div>
# #             </div>
# #             """, unsafe_allow_html=True)
# #         else:
# #             st.markdown(f"""
# #             <div class="ai-message">
# #                 <strong>🤖 AI Therapist:</strong> {message["content"]}
# #                 <div class="timestamp">{timestamp}</div>
# #             </div>
# #             """, unsafe_allow_html=True)
    
# #     st.markdown('</div>', unsafe_allow_html=True)

# # # Chat input
# # with st.container():
# #     col1, col2 = st.columns([6, 1])
    
# #     with col1:
# #         user_input = st.text_area(
# #             "Share what's on your mind...",
# #             placeholder="I'm here to listen. Feel free to share your thoughts and feelings.",
# #             height=100,
# #             key="chat_input"
# #         )
    
# #     with col2:
# #         st.write("")  # Spacing
# #         send_button = st.button("Send 📤", type="primary", use_container_width=True)

# # # Handle message sending
# # if send_button and user_input.strip():
# #     # Add user message
# #     user_message = {
# #         "role": "user",
# #         "content": user_input.strip(),
# #         "timestamp": datetime.now()
# #     }
# #     st.session_state.messages.append(user_message)
    
# #     # Show loading indicator
# #     with st.spinner("AI Therapist is thinking..."):
# #         # Call backend API
# #         ai_response = call_backend_api(user_input.strip(), st.session_state.session_id)
    
# #     # Add AI response
# #     ai_message = {
# #         "role": "assistant",
# #         "content": ai_response,
# #         "timestamp": datetime.now()
# #     }
# #     st.session_state.messages.append(ai_message)
    
# #     # Clear input and refresh
# #     st.rerun()

# # # Crisis resources footer
# # st.markdown("""
# # <div class="crisis-footer">
# #     <h4>🚨 Crisis Resources</h4>
# #     <p><strong>If you're experiencing a mental health emergency:</strong></p>
# #     <ul>
# #         <li>Contact Campus Counseling Services immediately</li>
# #         <li>Call 988 (Suicide & Crisis Lifeline)</li>
# #         <li>Go to your nearest emergency room</li>
# #         <li>Text "HELLO" to 741741 (Crisis Text Line)</li>
# #     </ul>
# # </div>
# # """, unsafe_allow_html=True)

# # # Usage instructions in expander
# # with st.expander("ℹ️ How to Use This Chat"):
# #     st.markdown("""
# #     **Getting Started:**
# #     - Type your message in the text area below
# #     - Click "Send" or press Ctrl+Enter to send
# #     - The AI will respond based on your input
    
# #     **This AI can help with:**
# #     - Academic stress and anxiety
# #     - Relationship concerns
# #     - Loneliness and isolation
# #     - General mental health support
# #     - Coping strategies and resources
    
# #     **Remember:**
# #     - This is not a replacement for professional therapy
# #     - All conversations are confidential
# #     - Be honest about your feelings for better support
# #     """)



# # #Fourth Code:
# import streamlit as st
# import requests
# import json
# from datetime import datetime
# import time
# import os
# from typing import List, Dict

# # Page configuration
# st.set_page_config(
#     page_title="University AI Therapist",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Enhanced Custom CSS for better UI/UX
# st.markdown("""
# <style>
#     /* Import Google Fonts */
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
#     /* Global Styles */
#     .main {
#         padding: 0;
#     }
    
#     .stApp {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Hide Streamlit elements */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
    
#     /* Main container */
#     .chat-container {
#         background: rgba(255, 255, 255, 0.95);
#         backdrop-filter: blur(20px);
#         border-radius: 24px;
#         box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
#         margin: 20px;
#         overflow: hidden;
#         border: 1px solid rgba(255, 255, 255, 0.2);
#     }
    
#     /* Header */
#     .main-header {
#         background: linear-gradient(135deg, #4F46E5, #7C3AED);
#         padding: 2rem;
#         color: white;
#         text-align: center;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .main-header::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         bottom: 0;
#         background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="25" cy="75" r="1" fill="white" opacity="0.05"/><circle cx="75" cy="25" r="1" fill="white" opacity="0.05"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
#         pointer-events: none;
#     }
    
#     .header-content {
#         position: relative;
#         z-index: 1;
#     }
    
#     .header-title {
#         font-size: 2.5rem;
#         font-weight: 700;
#         margin-bottom: 0.5rem;
#         text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#     }
    
#     .header-subtitle {
#         font-size: 1.1rem;
#         opacity: 0.9;
#         font-weight: 400;
#     }
    
#     .header-icon {
#         font-size: 3rem;
#         margin-bottom: 1rem;
#         filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
#     }
    
#     /* Chat Messages */
#     .chat-messages {
#         max-height: 500px;
#         overflow-y: auto;
#         padding: 2rem;
#         background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
#         scroll-behavior: smooth;
#     }
    
#     .chat-messages::-webkit-scrollbar {
#         width: 6px;
#     }
    
#     .chat-messages::-webkit-scrollbar-track {
#         background: rgba(0, 0, 0, 0.05);
#         border-radius: 10px;
#     }
    
#     .chat-messages::-webkit-scrollbar-thumb {
#         background: linear-gradient(135deg, #4F46E5, #7C3AED);
#         border-radius: 10px;
#     }
    
#     /* User Message */
#     .user-message {
#         background: linear-gradient(135deg, #4F46E5, #7C3AED);
#         color: white;
#         padding: 1rem 1.5rem;
#         border-radius: 24px 24px 8px 24px;
#         margin: 1rem 0 1rem 20%;
#         box-shadow: 0 8px 16px rgba(79, 70, 229, 0.3);
#         position: relative;
#         animation: slideInRight 0.3s ease-out;
#     }
    
#     .user-message::before {
#         content: '👤';
#         position: absolute;
#         top: -12px;
#         right: 12px;
#         background: white;
#         border-radius: 50%;
#         width: 24px;
#         height: 24px;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 12px;
#         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
#     }
    
#     /* AI Message */
#     .ai-message {
#         background: white;
#         color: #1e293b;
#         padding: 1rem 1.5rem;
#         border-radius: 24px 24px 24px 8px;
#         margin: 1rem 20% 1rem 0;
#         border: 1px solid #e2e8f0;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
#         position: relative;
#         animation: slideInLeft 0.3s ease-out;
#     }
    
#     .ai-message::before {
#         content: '🤖';
#         position: absolute;
#         top: -12px;
#         left: 12px;
#         background: linear-gradient(135deg, #4F46E5, #7C3AED);
#         border-radius: 50%;
#         width: 24px;
#         height: 24px;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 12px;
#         box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
#     }
    
#     .error-message {
#         background: linear-gradient(135deg, #ef4444, #dc2626) !important;
#         color: white !important;
#         border: none !important;
#     }
    
#     .error-message::before {
#         content: '⚠️' !important;
#         background: white !important;
#     }
    
#     /* Animations */
#     @keyframes slideInRight {
#         from {
#             opacity: 0;
#             transform: translateX(30px);
#         }
#         to {
#             opacity: 1;
#             transform: translateX(0);
#         }
#     }
    
#     @keyframes slideInLeft {
#         from {
#             opacity: 0;
#             transform: translateX(-30px);
#         }
#         to {
#             opacity: 1;
#             transform: translateX(0);
#         }
#     }
    
#     @keyframes pulse {
#         0%, 100% {
#             opacity: 1;
#         }
#         50% {
#             opacity: 0.5;
#         }
#     }
    
#     /* Timestamp */
#     .timestamp {
#         font-size: 0.75rem;
#         opacity: 0.7;
#         margin-top: 0.5rem;
#         display: flex;
#         align-items: center;
#         gap: 0.25rem;
#     }
    
#     /* Input Area */
#     .input-section {
#         padding: 2rem;
#         background: white;
#         border-top: 1px solid #e2e8f0;
#     }
    
#     .stTextArea > div > div > textarea {
#         background: linear-gradient(135deg, #f8fafc, #f1f5f9) !important;
#         border: 2px solid #e2e8f0 !important;
#         border-radius: 16px !important;
#         padding: 1rem !important;
#         font-size: 1rem !important;
#         font-family: 'Inter', sans-serif !important;
#         resize: none !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05) !important;
#     }
    
#     .stTextArea > div > div > textarea:focus {
#         border-color: #4F46E5 !important;
#         box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
#         background: white !important;
#     }
    
#     /* Buttons */
#     .stButton > button {
#         background: linear-gradient(135deg, #4F46E5, #7C3AED) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 12px !important;
#         padding: 0.75rem 2rem !important;
#         font-weight: 600 !important;
#         font-size: 1rem !important;
#         transition: all 0.3s ease !important;
#         box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
#         text-transform: none !important;
#         font-family: 'Inter', sans-serif !important;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4) !important;
#     }
    
#     .stButton > button:active {
#         transform: translateY(0) !important;
#     }
    
#     /* Loading Animation */
#     .loading-container {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         gap: 0.5rem;
#         padding: 1rem;
#         background: rgba(79, 70, 229, 0.1);
#         border-radius: 16px;
#         margin: 1rem 20% 1rem 0;
#         animation: pulse 2s infinite;
#     }
    
#     .loading-dots {
#         display: flex;
#         gap: 0.25rem;
#     }
    
#     .loading-dot {
#         width: 8px;
#         height: 8px;
#         background: #4F46E5;
#         border-radius: 50%;
#         animation: bounce 1.4s infinite both;
#     }
    
#     .loading-dot:nth-child(2) {
#         animation-delay: 0.2s;
#     }
    
#     .loading-dot:nth-child(3) {
#         animation-delay: 0.4s;
#     }
    
#     @keyframes bounce {
#         0%, 80%, 100% {
#             transform: scale(0.6);
#             opacity: 0.5;
#         }
#         40% {
#             transform: scale(1);
#             opacity: 1;
#         }
#     }
    
#     /* Crisis Footer */
#     .crisis-footer {
#         background: linear-gradient(135deg, #fee2e2, #fecaca);
#         border: 1px solid #fca5a5;
#         border-radius: 16px;
#         padding: 1.5rem;
#         margin: 2rem;
#         text-align: center;
#     }
    
#     .crisis-title {
#         font-size: 1.25rem;
#         font-weight: 600;
#         color: #dc2626;
#         margin-bottom: 0.5rem;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         gap: 0.5rem;
#     }
    
#     .crisis-content {
#         color: #7f1d1d;
#         line-height: 1.6;
#     }
    
#     /* Sidebar Enhancements */
#     .sidebar-content {
#         background: rgba(255, 255, 255, 0.9) !important;
#         border-radius: 16px !important;
#         padding: 1rem !important;
#         margin: 1rem !important;
#         backdrop-filter: blur(10px) !important;
#         border: 1px solid rgba(255, 255, 255, 0.2) !important;
#     }
    
#     /* Mobile Responsiveness */
#     @media (max-width: 768px) {
#         .user-message, .ai-message {
#             margin-left: 5%;
#             margin-right: 5%;
#         }
        
#         .header-title {
#             font-size: 2rem;
#         }
        
#         .chat-messages {
#             padding: 1rem;
#         }
        
#         .input-section {
#             padding: 1rem;
#         }
#     }
    
#     /* Success Messages */
#     .success-message {
#         background: linear-gradient(135deg, #10b981, #059669);
#         color: white;
#         padding: 1rem;
#         border-radius: 12px;
#         margin: 1rem 0;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#         box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
#     }
    
#     /* Connection Status */
#     .connection-status {
#         position: fixed;
#         top: 20px;
#         right: 20px;
#         z-index: 1000;
#         padding: 0.5rem 1rem;
#         border-radius: 20px;
#         font-size: 0.875rem;
#         font-weight: 500;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }
    
#     .connected {
#         background: linear-gradient(135deg, #10b981, #059669);
#         color: white;
#     }
    
#     .disconnected {
#         background: linear-gradient(135deg, #ef4444, #dc2626);
#         color: white;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Backend Configuration
# API_BASE_URL = "http://localhost:8000"  # Update this to your backend URL
# API_ENDPOINT = f"{API_BASE_URL}/api/chat"

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": "Hello! I'm here to provide a safe space for you to share your thoughts and feelings. How are you doing today? 😊",
#             "timestamp": datetime.now()
#         }
#     ]

# if "session_id" not in st.session_state:
#     st.session_state.session_id = str(int(time.time()))

# if "is_loading" not in st.session_state:
#     st.session_state.is_loading = False

# if "connection_status" not in st.session_state:
#     st.session_state.connection_status = "checking"

# def check_backend_connection():
#     """Check if backend is accessible"""
#     try:
#         response = requests.get(f"{API_BASE_URL}/health", timeout=5)
#         return response.status_code == 200
#     except:
#         return False

# def call_backend_api(user_message: str, session_id: str) -> str:
#     """Call the backend RAG pipeline API"""
#     try:
#         payload = {
#             "message": user_message,
#             "session_id": session_id,
#             "context": "university_mental_health",
#             "user_type": "student",
#             "timestamp": datetime.now().isoformat()
#         }
        
#         response = requests.post(
#             API_ENDPOINT,
#             json=payload,
#             headers={
#                 "Content-Type": "application/json",
#                 "Accept": "application/json"
#             },
#             timeout=30
#         )
        
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("response", data.get("message", data.get("reply", "I'm here to help.")))
#         elif response.status_code == 404:
#             return "I'm still learning and growing. Could you try rephrasing your question? I'm here to support you."
#         else:
#             return f"I'm experiencing some technical difficulties right now. Please try again in a moment."
            
#     except requests.exceptions.Timeout:
#         return "I'm taking a bit longer to respond than usual. Please be patient with me."
#     except requests.exceptions.ConnectionError:
#         st.session_state.connection_status = "disconnected"
#         return "I'm having trouble connecting to my knowledge base right now. Please check your connection and try again."
#     except Exception as e:
#         st.error(f"Unexpected error: {str(e)}")
#         return "I encountered an unexpected issue. Please try again or contact support if this persists."

# def render_message(message: Dict, index: int):
#     """Render a single message with enhanced styling"""
#     timestamp = message["timestamp"].strftime("%H:%M")
    
#     if message["role"] == "user":
#         st.markdown(f"""
#         <div class="user-message">
#             <div style="font-weight: 500; margin-bottom: 0.5rem;">You</div>
#             <div style="line-height: 1.6;">{message["content"]}</div>
#             <div class="timestamp">
#                 🕒 {timestamp}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         error_class = "error-message" if message.get("is_error", False) else ""
#         st.markdown(f"""
#         <div class="ai-message {error_class}">
#             <div style="font-weight: 500; margin-bottom: 0.5rem;">AI Therapist</div>
#             <div style="line-height: 1.6;">{message["content"]}</div>
#             <div class="timestamp">
#                 🕒 {timestamp}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

# def send_message():
#     """Handle sending a message"""
#     user_input = st.session_state.get("chat_input", "").strip()
    
#     if not user_input:
#         return
    
#     # Add user message
#     user_message = {
#         "role": "user",
#         "content": user_input,
#         "timestamp": datetime.now()
#     }
#     st.session_state.messages.append(user_message)
    
#     # Set loading state
#     st.session_state.is_loading = True
    
#     # Clear input
#     st.session_state.chat_input = ""
    
#     # Rerun to show user message and loading state
#     st.rerun()

# # Check backend connection
# connection_ok = check_backend_connection()
# st.session_state.connection_status = "connected" if connection_ok else "disconnected"

# # Connection status indicator
# status_class = "connected" if connection_ok else "disconnected"
# status_text = "🟢 Connected" if connection_ok else "🔴 Disconnected"
# st.markdown(f"""
# <div class="connection-status {status_class}">
#     {status_text}
# </div>
# """, unsafe_allow_html=True)

# # Main container
# with st.container():
#     st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
#     # Header
#     st.markdown("""
#     <div class="main-header">
#         <div class="header-content">
#             <div class="header-icon">🧠</div>
#             <div class="header-title">University AI Therapist</div>
#             <div class="header-subtitle">Your confidential mental health companion</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Chat messages container
#     st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    
#     # Render messages
#     for i, message in enumerate(st.session_state.messages):
#         render_message(message, i)
    
#     # Show loading animation if processing
#     if st.session_state.is_loading:
#         st.markdown("""
#         <div class="loading-container">
#             <div>🤖 AI Therapist is thinking</div>
#             <div class="loading-dots">
#                 <div class="loading-dot"></div>
#                 <div class="loading-dot"></div>
#                 <div class="loading-dot"></div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Get AI response
#         try:
#             last_user_message = st.session_state.messages[-1]["content"]
#             ai_response = call_backend_api(last_user_message, st.session_state.session_id)
            
#             # Add AI response
#             ai_message = {
#                 "role": "assistant",
#                 "content": ai_response,
#                 "timestamp": datetime.now(),
#                 "is_error": "technical difficulties" in ai_response.lower() or "connection" in ai_response.lower()
#             }
#             st.session_state.messages.append(ai_message)
            
#         except Exception as e:
#             # Add error message
#             error_message = {
#                 "role": "assistant",
#                 "content": "I'm sorry, I encountered an unexpected issue. Please try again or contact support if this continues.",
#                 "timestamp": datetime.now(),
#                 "is_error": True
#             }
#             st.session_state.messages.append(error_message)
        
#         finally:
#             st.session_state.is_loading = False
#             st.rerun()
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     # Input section
#     st.markdown('<div class="input-section">', unsafe_allow_html=True)
    
#     # Create columns for input and button
#     col1, col2 = st.columns([5, 1])
    
#     with col1:
#         user_input = st.text_area(
#             "Message",
#             placeholder="Share what's on your mind... I'm here to listen and support you 💙",
#             height=80,
#             key="chat_input",
#             label_visibility="collapsed",
#             disabled=st.session_state.is_loading or not connection_ok
#         )
    
#     with col2:
#         st.write("")  # Spacing
#         send_clicked = st.button(
#             "Send 💬", 
#             type="primary", 
#             use_container_width=True,
#             disabled=st.session_state.is_loading or not connection_ok,
#             on_click=send_message
#         )
    
#     # Handle Enter key submission
#     if user_input and user_input != st.session_state.get("last_input", ""):
#         if user_input.endswith('\n') and not st.session_state.is_loading and connection_ok:
#             st.session_state.chat_input = user_input.strip()
#             send_message()
#         st.session_state.last_input = user_input
    
#     # Privacy and tips
#     st.markdown("""
#     <div style="margin-top: 1rem; text-align: center; color: #64748b; font-size: 0.875rem;">
#         🔒 <strong>Completely confidential</strong> • Press Enter to send • Shift+Enter for new line
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # Enhanced Sidebar
# with st.sidebar:
#     st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
#     st.markdown("### 🎛️ Chat Controls")
    
#     if st.button("🔄 Start New Conversation", use_container_width=True):
#         st.session_state.messages = [
#             {
#                 "role": "assistant",
#                 "content": "Hello! I'm here to provide a safe space for you to share your thoughts and feelings. How are you doing today? 😊",
#                 "timestamp": datetime.now()
#             }
#         ]
#         st.session_state.session_id = str(int(time.time()))
#         st.success("New conversation started!")
#         time.sleep(1)
#         st.rerun()
    
#     st.markdown("---")
    
#     # Session info
#     st.markdown("### 📊 Session Info")
#     st.info(f"**Messages:** {len(st.session_state.messages)}")
#     st.info(f"**Session ID:** {st.session_state.session_id[-8:]}")
    
#     st.markdown("---")
    
#     # Tips section
#     st.markdown("### 💡 Tips for Better Support")
#     st.markdown("""
#     - **Be honest** about your feelings
#     - **Take your time** to express yourself
#     - **Ask specific questions** for targeted help
#     - **Share context** about your situation
#     - **Remember**: Seeking help shows strength 💪
#     """)
    
#     st.markdown("---")
    
#     # Quick topics
#     st.markdown("### 🏷️ Common Topics")
#     topics = [
#         "Academic stress", "Anxiety management", "Sleep issues",
#         "Relationship concerns", "Time management", "Self-care tips"
#     ]
    
#     for topic in topics:
#         if st.button(f"💬 {topic}", use_container_width=True, key=f"topic_{topic}"):
#             st.session_state.chat_input = f"I'd like to talk about {topic.lower()}. Can you help me?"
#             send_message()
    
#     st.markdown('</div>', unsafe_allow_html=True)

# # Crisis resources footer
# st.markdown("""
# <div class="crisis-footer">
#     <div class="crisis-title">
#         🚨 Crisis Resources
#     </div>
#     <div class="crisis-content">
#         <strong>If you're experiencing a mental health emergency:</strong><br>
#         • Campus Counseling Services: <strong>[Your Campus Number]</strong><br>
#         • National Suicide Prevention Lifeline: <strong>988</strong><br>
#         • Crisis Text Line: Text <strong>HOME</strong> to <strong>741741</strong><br>
#         • Emergency Services: <strong>911</strong>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # Auto-scroll to bottom script
# st.markdown("""
# <script>
# function scrollToBottom() {
#     const chatMessages = document.querySelector('.chat-messages');
#     if (chatMessages) {
#         chatMessages.scrollTop = chatMessages.scrollHeight;
#     }
# }

# // Scroll on page load
# window.addEventListener('load', scrollToBottom);

# // Scroll when new content is added
# const observer = new MutationObserver(scrollToBottom);
# const chatContainer = document.querySelector('.chat-messages');
# if (chatContainer) {
#     observer.observe(chatContainer, { childList: true, subtree: true });
# }
# </script>
# """, unsafe_allow_html=True)




























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

# # Styling with light blue-purplish gradient theme
# st.markdown("""
#     <style>
#     body {
#         background: linear-gradient(135deg, #d1e6ff, #e6d1ff);
#         color: #2d2d5e;
#     }
#     .main-header {
#         text-align: center;
#         padding: 2rem;
#         color: #2d2d5e;
#     }
#     .chat-bubble {
#         border-radius: 1rem;
#         padding: 1rem;
#         margin-bottom: 1rem;
#         width: fit-content;
#         max-width: 70%;
#     }
#     .user-bubble {
#         background-color: #a3bffa; /* Light blue for user */
#         color: #2d2d5e;
#         margin-left: auto;
#         text-align: right;
#     }
#     .bot-bubble {
#         background-color: #b1a3fa; /* Light purple for bot */
#         color: #2d2d5e;
#         margin-right: auto;
#     }
#     .quote-box {
#         font-style: italic;
#         color: #4a4e69;
#         text-align: center;
#         margin-top: 1rem;
#     }
#     .stSidebar {
#         background: linear-gradient(135deg, #c6d9ff, #d9c6ff); /* Sidebar gradient */
#     }
#     .stButton>button {
#         background-color: #7f9cf5; /* Button color */
#         color: #ffffff;
#         border-radius: 0.5rem;
#     }
#     .stButton>button:hover {
#         background-color: #9f7aea; /* Hover color */
#     }
#     .stTextInput>div>input {
#         background-color: #e6e6ff;
#         color: #2d2d5e;
#         border-radius: 0.5rem;
#     }
#     .stSelectbox>div>div {
#         background-color: #e6e6ff;
#         color: #2d2d5e;
#         border-radius: 0.5rem;
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
from datetime import datetime
import random
from rag_query_system import generate_response

# # Page setup
# st.set_page_config(
#     page_title="MindMatters - Your AI Therapist",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
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