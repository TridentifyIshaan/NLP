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
pip install --break-system-packages langchain-core langchain-text-splitters langchain-community langchain-ollama faiss-cpu ollama lshw
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
python ./rag.py
```

NOTE - The script is slow, so wait for a minute to get the whole output.

## What It Does

The script demonstrates:
- **Vector Search**: Creates a FAISS index from sample texts using Ollama embeddings
- **Chat History**: Maintains conversation context across multiple turns
- **Session Management**: Tracks separate conversation sessions
- **RAG Pipeline**: Retrieves relevant context and uses it to answer questions

## Expected Output

The script will run 4 Q&A interactions demonstrating:
- Basic retrieval (asking about FAISS)
- Memory recall within a session
- Independent session tracking
- Context switching between sessions

## Troubleshooting

**Error: "model not found"**
- Run `ollama pull <model-name>` for the missing model

**Error: "connection refused"**
- Ensure `ollama serve` is running in a separate terminal

**Import errors**
- Verify all dependencies are installed with `pip list | grep langchain`