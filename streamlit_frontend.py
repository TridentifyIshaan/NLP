"""
Streamlit Frontend for FastAPI + LangChain Integration
This file provides a user interface that communicates with the FastAPI backend
"""

import streamlit as st
import requests
from datetime import datetime
import json

# Configuration
API_BASE_URL = "http://localhost:8000"

# Page configuration
st.set_page_config(
    page_title="Chat with AI",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .user-message {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .ai-message {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = f"user-{datetime.now().strftime('%Y%m%d%H%M%S')}"

# Helper function to check API health
def check_api_health():
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

# Helper function to send chat message
def send_message(message: str, session_id: str):
    try:
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json={"message": message, "session_id": session_id},
            timeout=30
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API error: {response.status_code}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timeout. The AI is taking too long to respond."}
    except Exception as e:
        return {"error": f"Connection error: {str(e)}"}

# Helper function to get all sessions
def get_sessions():
    try:
        response = requests.get(f"{API_BASE_URL}/sessions", timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

# Helper function to clear session
def clear_session(session_id: str):
    try:
        response = requests.delete(f"{API_BASE_URL}/sessions/{session_id}", timeout=5)
        return response.status_code == 200
    except:
        return False

# Main UI
st.title("🤖 AI Chat Assistant")
st.markdown("*Powered by FastAPI + LangChain + Ollama*")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # API status
    api_status = check_api_health()
    if api_status:
        st.success("✅ API Connected")
    else:
        st.error("❌ API Not Connected")
        st.warning("Please start the FastAPI backend:\n```bash\npython cpwhws_with_fastapi.py\n```")
    
    st.divider()
    
    # Session management
    st.subheader("Session Management")
    st.text(f"Current Session:\n{st.session_state.session_id}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆕 New Session"):
            st.session_state.session_id = f"user-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear Chat"):
            if clear_session(st.session_state.session_id):
                st.session_state.messages = []
                st.success("Chat cleared!")
                st.rerun()
    
    st.divider()
    
    # Active sessions
    st.subheader("📊 Active Sessions")
    sessions_data = get_sessions()
    if sessions_data:
        st.metric("Total Sessions", sessions_data.get("total", 0))
        with st.expander("View All Sessions"):
            for session in sessions_data.get("sessions", []):
                st.text(f"ID: {session['session_id']}")
                st.caption(f"Messages: {session['message_count']}")
                st.divider()

# Main chat area
st.divider()

# Display chat messages
chat_container = st.container()
with chat_container:
    for idx, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f"""
                <div class="user-message">
                    <b>👤 You:</b> {msg["content"]}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="ai-message">
                    <b>🤖 AI:</b> {msg["content"]}
                </div>
            """, unsafe_allow_html=True)

# Chat input
if api_status:
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input(
                "Message",
                placeholder="Type your message here...",
                label_visibility="collapsed"
            )
        with col2:
            submit_button = st.form_submit_button("Send 📤", use_container_width=True)
    
    if submit_button and user_input:
        # Add user message to chat
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Show spinner while waiting for response
        with st.spinner("AI is thinking..."):
            # Send to API
            result = send_message(user_input, st.session_state.session_id)
            
            if "error" in result:
                st.error(result["error"])
            else:
                # Add AI response to chat
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result.get("response", "No response")
                })
        
        # Rerun to update chat display
        st.rerun()
else:
    st.warning("⚠️ Please start the FastAPI backend to begin chatting")
    st.code("""
    # In a terminal, run:
    python cpwhws_with_fastapi.py
    
    # Or:
    uvicorn cpwhws_with_fastapi:app --reload --host 0.0.0.0 --port 8000
    """, language="bash")

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit, FastAPI, and LangChain")

"""
HOW TO RUN:

1. Start Ollama server (in terminal 1):
   ollama serve

2. Pull required model (if not already done):
   ollama pull tinyllama

3. Start FastAPI backend (in terminal 2):
   python cpwhws_with_fastapi.py
   
   Or:
   uvicorn cpwhws_with_fastapi:app --reload --host 0.0.0.0 --port 8000

4. Start Streamlit frontend (in terminal 3):
   streamlit run streamlit_frontend.py

5. Open browser to the Streamlit URL (typically http://localhost:8501)

FEATURES:
- Real-time chat with AI
- Session management
- Conversation history
- Multiple sessions support
- Clear chat functionality
- API health monitoring
- Beautiful UI with custom styling
"""
