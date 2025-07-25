import streamlit as st
import requests
import json
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="AI Therapist Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #2E86AB;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        max-width: 80%;
    }
    
    .user-message {
        background-color: #E3F2FD;
        margin-left: auto;
        border-left: 4px solid #2196F3;
    }
    
    .assistant-message {
        background-color: #F1F8E9;
        margin-right: auto;
        border-left: 4px solid #4CAF50;
    }
    
    .sidebar-info {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .welcome-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'api_base_url' not in st.session_state:
    st.session_state.api_base_url = "http://localhost:8000"  # Default local URL

def make_api_request(endpoint, data=None, method="POST"):
    """Make API request to backend"""
    try:
        url = f"{st.session_state.api_base_url}/api/{endpoint}"
        if method == "POST":
            response = requests.post(url, json=data, timeout=30)
        else:
            response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"detail": f"Error {response.status_code}: {response.text}"}
    except requests.exceptions.RequestException as e:
        return False, {"detail": f"Connection error: {str(e)}"}

def login_page():
    """Display login/registration page"""
    st.markdown('<h1 class="main-header">🧠 AI Therapist Assistant</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="welcome-message">
        <h2>Welcome to Your Personal Mental Health Support</h2>
        <p>A safe space to talk, reflect, and receive supportive guidance tailored for students.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # API Configuration
    with st.expander("🔧 API Configuration", expanded=False):
        new_url = st.text_input(
            "Backend API URL", 
            value=st.session_state.api_base_url,
            help="Enter your backend API URL (e.g., http://localhost:8000 for local or your deployed URL)"
        )
        if st.button("Update API URL"):
            st.session_state.api_base_url = new_url
            st.success(f"API URL updated to: {new_url}")
    
    # Login/Register tabs
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login to Your Account")
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="your.email@example.com")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login", use_container_width=True)
            
            if submitted:
                if email and password:
                    with st.spinner("Logging in..."):
                        success, response = make_api_request("login", {
                            "email": email,
                            "password": password
                        })
                    
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.user_info = response
                        st.success(f"Welcome back, {response['name']}!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(f"Login failed: {response.get('detail', 'Unknown error')}")
                else:
                    st.error("Please fill in all fields")
    
    with tab2:
        st.subheader("Create New Account")
        with st.form("register_form"):
            name = st.text_input("Full Name", placeholder="Your Name")
            email = st.text_input("Email", placeholder="your.email@example.com")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Register", use_container_width=True)
            
            if submitted:
                if name and email and password and confirm_password:
                    if password != confirm_password:
                        st.error("Passwords don't match!")
                    else:
                        with st.spinner("Creating account..."):
                            success, response = make_api_request("register", {
                                "name": name,
                                "email": email,
                                "password": password
                            })
                        
                        if success:
                            st.success("Account created successfully! Please login.")
                        else:
                            st.error(f"Registration failed: {response.get('detail', 'Unknown error')}")
                else:
                    st.error("Please fill in all fields")

def chat_interface():
    """Main chat interface"""
    # Header
    st.markdown('<h1 class="main-header">🧠 AI Therapist Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.user_info.get('name', 'User')}! 👋")
        
        st.markdown("""
        <div class="sidebar-info">
        <h4>💡 How to get the best help:</h4>
        <ul>
        <li>Be honest about your feelings</li>
        <li>Ask specific questions</li>
        <li>Share what's on your mind</li>
        <li>Take your time to reflect</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 New Conversation", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.user_info = {}
            st.session_state.chat_history = []
            st.rerun()
        
        # Chat history summary
        if st.session_state.chat_history:
            st.markdown("### 📝 Chat Summary")
            st.markdown(f"**Messages:** {len(st.session_state.chat_history)}")
            if len(st.session_state.chat_history) > 0:
                last_msg_time = st.session_state.chat_history[-1].get('timestamp', '')
                st.markdown(f"**Last message:** {last_msg_time}")
        
        # Quick suggestions
        st.markdown("### 💭 Need inspiration?")
        suggestions = [
            "I'm feeling stressed about exams",
            "How can I manage anxiety?",
            "I'm having trouble sleeping",
            "I feel overwhelmed with coursework",
            "How to deal with social anxiety?"
        ]
        
        for suggestion in suggestions:
            if st.button(f"💬 {suggestion}", key=f"suggestion_{suggestion}", use_container_width=True):
                # Add suggestion to chat
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": suggestion,
                    "timestamp": datetime.now().strftime("%H:%M")
                })
                # Process the suggestion
                process_user_message(suggestion)
                st.rerun()
    
    # Main chat area
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        if not st.session_state.chat_history:
            st.markdown("""
            <div class="welcome-message">
                <h3>Hello! I'm here to support you. 🌟</h3>
                <p>Feel free to share what's on your mind, ask questions about mental health, 
                or just have a conversation. I'm here to listen and help.</p>
                <p><em>This is a safe, confidential space for you.</em></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You ({message['timestamp']}):</strong><br>
                        {message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message assistant-message">
                        <strong>AI Therapist ({message['timestamp']}):</strong><br>
                        {message['content']}
                    </div>
                    """, unsafe_allow_html=True)
    
    # Chat input
    st.markdown("---")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your message here...", 
            placeholder="Share what's on your mind, ask a question, or just say hello!",
            key="user_input"
        )
    
    with col2:
        send_button = st.button("Send 📤", use_container_width=True)
    
    # Process message
    if (send_button or st.session_state.get('user_input_submitted', False)) and user_input:
        st.session_state['user_input_submitted'] = False
        process_user_message(user_input)
        st.rerun()

def process_user_message(user_input):
    """Process user message and get AI response"""
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().strftime("%H:%M")
    })
    
    # Get AI response
    with st.spinner("🤔 Thinking..."):
        success, response = make_api_request("chat", {"query": user_input})
    
    if success:
        ai_response = response.get("answer", "I'm sorry, I couldn't generate a response.")
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": datetime.now().strftime("%H:%M")
        })
    else:
        error_msg = f"❌ Sorry, I encountered an error: {response.get('detail', 'Unknown error')}"
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": error_msg,
            "timestamp": datetime.now().strftime("%H:%M")
        })

# Handle enter key submission
if st.session_state.get('user_input', ''):
    st.session_state['user_input_submitted'] = True

# Main app logic
def main():
    if not st.session_state.authenticated:
        login_page()
    else:
        chat_interface()

if __name__ == "__main__":
    main()