import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# -------------------------------
# Initialize LLM (Ollama)
# -------------------------------
llm = ChatOllama(model="llama3.2:1b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

chain = prompt | llm

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🔗 Streamlit + Ollama Connected App")

# -------------------------------
# Form 1: User Registration
# -------------------------------
with st.form("user_form"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Admin", "User", "Guest"])
    agree = st.checkbox("I agree to terms")
    register = st.form_submit_button("Register")

if register:
    if not agree:
        st.error("You must agree to terms")
    else:
        st.success(f"Registered successfully as {role}")

st.divider()

# -------------------------------
# Form 2: Chat with Ollama
# -------------------------------

if "text" not in st.session_state:
    st.session_state.text = ""

with st.form("text_form"):
    st.session_state.text = st.text_input("Enter message for AI")
    submit_chat = st.form_submit_button("Ask AI")

if submit_chat:
    with st.spinner("Thinking..."):
        response = chain.invoke({"input": st.session_state.text})
        st.success("AI Response:")
        st.write(response.content)
        st.session_state.text = ""

# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

# ollama serve
# ollama pull llama3.2:1b

# streamlit run ./app.py