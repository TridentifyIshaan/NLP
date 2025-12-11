"""

# Ollama RAG with Chat History

A LangChain-based Retrieval-Augmented Generation (RAG) application using Ollama for local LLM inference with conversation history tracking.

## Prerequisites

- Python 3.12+
- Ollama installed and running

## Installation

### 1. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, restart your shell or source your bashrc:
```bash
source ~/.bashrc
```

### 2. Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Start Ollama Server

Start the Ollama service:
```bash
ollama serve
```

### 4. Pull Required Ollama Models

NOTE- Open a new terminal and don't close the previous terminal. Now run the following:-

```bash
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

### 5. Run the RAG Script

```bash
python ./RAG_LangChainMemory.py
```

NOTE - The script is slow, so wait for a minute to get the whole output.

"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.runnables import RunnablePassthrough
llm = ChatOllama(model="llama3.2:1b")
texts = [
    "LangChain helps developers build LLM applications.",
    "FAISS is used for vector similarity search.",
    "Chat history must be manually maintained in LangChain 1.1.",
    "Retrievers are used in RAG pipelines.",
    "OpenAI embeddings create vector representations."
]
embeddings = OllamaEmbeddings(model="nomic-embed-text")
db = FAISS.from_texts(texts, embeddings)
retriever = db.as_retriever()
# 1. Define a store for chat session
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
 
# 2. New prompt with history placeholder
# This prompt now explicitly expects the chat history as part of its messages.
rag_prompt_with_history = ChatPromptTemplate.from_messages([
    ("system", "Use the retrieved context to answer the user."),
    MessagesPlaceholder("history"), # This is where the history will be injected
    ("human", "{question}\n\nContext:\n{context}")
])

# 3. Define a processing step to get context from the retriever
def get_context_from_retriever(question_dict):
    # The input to this function will be a dictionary, e.g., {'question': '...'}
    docs = retriever.invoke(question_dict["question"])
    return "\n".join([d.page_content for d in docs])
# 4. Create the RAG chain with context retrieval and history handling
# RunnablePassthrough.assign is used to add 'context' to the input dictionary before passing it to the prompt.
runnable = RunnablePassthrough.assign(context=get_context_from_retriever)
rag_chain_with_context = (
    runnable | rag_prompt_with_history | llm
)

# 5. Wrap this chain with RunnableWithMessageHistory
# This runnable automatically manages adding messages to history and retrieving them based on the session_id.
conversational_rag_chain_with_history = RunnableWithMessageHistory(
    rag_chain_with_context,
    get_session_history,
    input_messages_key="question", # Key in the input dict for the user's question
    history_messages_key="history", # Key in the prompt for the chat history
)

# Example usage function with managed history
def ask_with_managed_history(question: str, session_id: str = "default_session"):
    response = conversational_rag_chain_with_history.invoke(
        {"question": question}, # Input only needs the question now
        config={
            "configurable": {"session_id": session_id}
        }
    )
    return response.content
store.clear()
print("User (session1): What is FAISS?")
print("AI (session1):", ask_with_managed_history("What is FAISS?", session_id="session1"))

print("\nUser (session1): What did I ask earlier?")
print("AI (session1):", ask_with_managed_history("What did I ask earlier?", session_id="session1"))

print("\nUser (session2): How does LangChain handle memory?")
print("AI (session2):", ask_with_managed_history("How does LangChain handle memory?", session_id="session2"))

print("\nUser (session1): And what about LangChain's memory?")
print("AI (session1):", ask_with_managed_history("And what about LangChain's memory?", session_id="session1"))