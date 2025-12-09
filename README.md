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

Script 1 ~ Not Working
```bash
python ./OllamaAgent.py
```

Script 2 ~ Working
```bash
python ./RAG_LangChainMemory.py
```

NOTE - The script is slow, so wait for a minute to get the whole output.