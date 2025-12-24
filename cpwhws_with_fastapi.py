# Single-file integration of Streamlit + FastAPI + LangChain

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import streamlit as st
import requests
from threading import Thread
import time
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# ==================== FASTAPI BACKEND ====================

app1 = FastAPI()

# LangChain setup
llm = ChatOllama(model="tinyllama", temperature=0.0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Make sure your answer is correct and provide the answer in a simple way and in one line."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

# Store for sessions
session_store = {}

def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

chain = prompt | llm
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str

# API Endpoints
@app1.get("/")
def root():
    return {"status": "FastAPI + LangChain is running!"}

@app1.post("/chat")
def chat(request: ChatRequest):
    config = {"configurable": {"session_id": request.session_id}}
    response = chain_with_history.invoke({"input": request.message}, config=config)
    return ChatResponse(response=response.content)

# ==================== STREAMLIT FRONTEND ====================

def run_fastapi():
    """Run FastAPI in background thread"""
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

# Start FastAPI in background when Streamlit starts
if "fastapi_started" not in st.session_state:
    st.session_state.fastapi_started = True
    thread = Thread(target=run_fastapi, daemon=True)
    thread.start()
    time.sleep(2)  # Give FastAPI time to start

# Streamlit UI
st.title("🤖 Chat with TinyLlama")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = "user-1"

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt_input := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.write(prompt_input)
    
    # Get AI response via FastAPI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call FastAPI endpoint
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "message": prompt_input,
                        "session_id": st.session_state.session_id
                    },
                    timeout=30
                )
                
                if response.status_code == 200:
                    ai_response = response.json()["response"]
                    st.write(ai_response)
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                else:
                    st.error(f"API Error: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to FastAPI. Please refresh the page.")
            except Exception as e:
                st.error(f"Error: {str(e)}")