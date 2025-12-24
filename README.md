# NLP & LLM Learning Project

A comprehensive workspace for exploring Natural Language Processing, Large Language Models, RAG (Retrieval-Augmented Generation), and web application development using modern AI frameworks.

## 📋 Table of Contents

- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [Usage Examples](#usage-examples)
- [Learning Path](#learning-path)

## 🎯 Overview

This workspace demonstrates a progression from basic NLP concepts to advanced LLM applications, including:
- Retrieval-Augmented Generation (RAG) with conversation history
- RESTful API development with FastAPI
- Database integrations (SQLite and MongoDB)
- Interactive chat interfaces using Streamlit
- Natural Language Processing with NLTK
- LangChain integration with local Ollama models

## 🛠 Technology Stack

### AI/ML Frameworks
- **LangChain**: Framework for developing LLM applications
- **Ollama**: Local LLM inference (llama3.2:1b, tinyllama)
- **NLTK**: Natural Language Toolkit for text processing
- **FAISS**: Vector similarity search for RAG

### Web Frameworks
- **FastAPI**: Modern, fast web framework for building APIs
- **Streamlit**: Interactive web apps for ML/AI projects
- **Uvicorn**: ASGI server

### Databases
- **SQLite**: Lightweight relational database
- **MongoDB**: NoSQL document database (with Motor async driver)

### Embeddings & Vector Stores
- **Nomic Embed Text**: Text embedding model
- **FAISS CPU**: Efficient similarity search

## 📦 Prerequisites

- Python 3.12+
- Ollama installed and running
- MongoDB Atlas account (for MongoDB examples)
- Virtual environment support

## 🚀 Installation

### 1. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
source ~/.bashrc
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Pull Ollama Models

Open a new terminal (keep Ollama server running):

```bash
# Start Ollama server (in one terminal)
ollama serve

# Pull required models (in another terminal)
ollama pull llama3.2:1b
ollama pull nomic-embed-text
ollama pull tinyllama
```

### 4. Environment Configuration (Optional)

For MongoDB examples, create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
DB_NAME=your_database_name
```

## 📁 Project Structure

```
/workspaces/Ollama/
├── RAG_LangChainMemory.py          # RAG with chat history
├── requirements.txt                # Python dependencies
├── fast.py                        # FastAPI learning examples
├── nltk.ipynb                     # NLP with NLTK notebook
├── newdpost.py                    # FastAPI + SQLite setup
├── dbpase.py                      # SQLite POST endpoint
├── mongo.py                       # FastAPI + MongoDB
├── app.py                         # Streamlit multi-form app
├── runnable.py                    # Basic LangChain runnable
├── Modelfile                      # Custom Ollama model config
├── chatprompt.py                  # Simple chat without history
├── chatprompt_with_history.py     # Chat with memory
├── cpwh_with_streamlit.py         # Streamlit chat with history
└── README.md                      # This file
```

## 📚 File Descriptions

### 🔍 **RAG_LangChainMemory.py** (Dec 6)
**Advanced RAG implementation with multi-session conversation history**

- Implements FAISS vector store for document retrieval
- Manages isolated conversation sessions
- Demonstrates context-aware responses using retrieved documents
- Uses `RunnableWithMessageHistory` for automatic memory management

**Run:**
```bash
python ./RAG_LangChainMemory.py
```

---

### 📦 **requirements.txt** (Dec 6)
**Complete dependency list for the project**

Includes all necessary packages for:
- LangChain ecosystem
- Vector databases
- Web frameworks (FastAPI, Streamlit)
- Database drivers
- NLP tools

---

### 🌐 **fast.py** (Dec 9)
**FastAPI endpoint patterns and REST API examples**

Demonstrates:
- Path parameters (`/hello/{name}`)
- Query parameters (`/info?age=19&city=ghaziabad`)
- Form data handling
- JSON body processing with Pydantic
- Multilingual responses

**Run:**
```bash
uvicorn fast:appn --reload --host 0.0.0.0
```

**Access:** `http://localhost:8000`

---

### 📓 **nltk.ipynb** (Dec 11)
**Interactive NLP preprocessing notebook**

Features:
- Text tokenization
- Stopword removal
- Frequency distribution analysis
- Hands-on NLTK learning

**Run:** Open in Jupyter or VS Code notebook editor

---

### 💾 **newdpost.py + dbpase.py** (Dec 11)
**FastAPI + SQLite customer management system**

- Database initialization on startup
- Customer table with auto-increment ID
- POST endpoint for adding customers
- SQL injection protection with parameterized queries

**Run:**
```bash
uvicorn newdpost:app --reload
```

---

### 🍃 **mongo.py** (Dec 12)
**Async FastAPI with MongoDB integration**

- Motor async driver for non-blocking operations
- Environment-based configuration
- User management endpoints
- Cloud database (MongoDB Atlas) support

**Run:**
```bash
uvicorn mongo:app --reload --log-level debug
```

**Test:**
```bash
curl -X POST http://localhost:8000/add_user \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

---

### 🎨 **app.py** (Dec 23)
**Streamlit dual-form application with AI chat**

Features:
1. **User Registration Form**: Email, password, role selection
2. **AI Chat Interface**: Real-time responses from Ollama LLM
3. Session state management
4. Loading indicators and validation

**Run:**
```bash
streamlit run ./app.py
```

---

### ⚡ **runnable.py** (Dec 23)
**Introduction to LangChain runnables and LCEL**

- Basic chain composition using pipe operator
- Simple prompt template structure
- Foundation for understanding LangChain chains

**Run:**
```bash
python ./runnable.py
```

---

### 🔧 **Modelfile** (Dec 23)
**Custom Ollama model configuration**

Configures TinyLlama with:
- Reduced context window (30 tokens)
- Custom parameters for testing

**Build custom model:**
```bash
ollama create my-custom-model -f Modelfile
```

---

### 💬 **chatprompt.py** (Dec 23)
**Basic stateless chat implementation**

- Single query-response pattern
- No conversation history
- Deterministic responses (temperature=0.0)
- TinyLlama model usage

**Run:**
```bash
python ./chatprompt.py
```

---

### 🧠 **chatprompt_with_history.py** (Dec 23)
**Multi-turn conversations with memory**

- In-memory chat history
- Session-based isolation
- Context retention across queries
- Demonstrates conversation continuity

**Run:**
```bash
python ./chatprompt_with_history.py
```

---

### 🖥️ **cpwh_with_streamlit.py** (Dec 23)
**Interactive web-based chat with persistent memory**

- Streamlit UI for chat interface
- Session state for history persistence
- Real-time AI responses
- User-friendly conversation experience

**Run:**
```bash
streamlit run ./cpwh_with_streamlit.py
```

**Future Plans:** RAG and Multimodal features integration

---

## 🎓 Usage Examples

### Example 1: RAG with Chat History

```python
# RAG_LangChainMemory.py demonstrates:
# Session 1
User: "What is FAISS?"
AI: "FAISS is used for vector similarity search."

User: "What did I ask earlier?"
AI: "You asked about FAISS."

# Session 2 (separate memory)
User: "How does LangChain handle memory?"
AI: "Chat history must be manually maintained in LangChain 1.1."
```

### Example 2: FastAPI Endpoints

```bash
# Test various endpoints
curl http://localhost:8000/
curl http://localhost:8000/hello/Ishaan
curl "http://localhost:8000/info?age=19&city=ghaziabad"
```

### Example 3: NLP Text Processing

```python
# In nltk.ipynb
text = "Natural language processing is amazing and powerful!"
# Output: ['natural', 'language', 'processing', 'amazing', 'powerful']
```

### Example 4: Streamlit Chat

```python
# cpwh_with_streamlit.py
# User types: "What is Python?"
# AI responds with context from previous messages in the session
```

## 📈 Learning Path

The project follows a structured learning progression:

1. **Week 1 (Dec 6)**: RAG fundamentals and dependency management
2. **Week 2 (Dec 9-11)**: Web APIs, NLP, and database integrations
3. **Week 3 (Dec 12)**: NoSQL databases and async operations
4. **Week 4 (Dec 23)**: Chat applications with increasing complexity

### Progression:
```
Basic Concepts → API Development → Database Integration → Chat Applications → Advanced RAG
```

## 🔮 Future Enhancements

Based on project comments and structure:
- [ ] Multimodal AI integration
- [ ] Advanced RAG techniques
- [ ] Production-ready deployment configurations
- [ ] Authentication and authorization
- [ ] Vector store optimization
- [ ] Long-term memory solutions

## 🤝 Contributing

This is a personal learning workspace. Feel free to fork and experiment!

## 📄 License

Educational and experimental use.

## 🙏 Acknowledgments

- **LangChain** for the amazing LLM framework
- **Ollama** for local model inference
- **FastAPI** and **Streamlit** for rapid development
- Open-source AI/ML community

---

**Last Updated:** December 24, 2025  
**Repository:** TridentifyIshaan/NLP  
**Branch:** mainstream