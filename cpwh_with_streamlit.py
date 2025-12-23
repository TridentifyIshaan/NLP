# tinyllama with nomic-embed-text

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import streamlit as st

st.title("Chat with TinyLlama")

llm = ChatOllama(model="tinyllama", temperature=0.0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Make sure your answer is correct and provide the answer in a simple way and in one line."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = InMemoryChatMessageHistory()

history = st.session_state.history

chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "user-1"}}

# Streamlit UI
user_input = st.text_input("Ask a question:")

if user_input:
    response = chain_with_history.invoke({"input": user_input}, config=config)
    st.write("**Assistant:**", response.content)

# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

# ollama serve
# ollama pull llama3.2:1b

# streamlit run ./cpwh_with_streamlit.py


# Include RAG and Multimodal in next class - 24/12/2025 because that is required in the final project