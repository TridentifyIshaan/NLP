from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Initialize LLM
llm = ChatOllama(model="llama3.2:1b")

# Create chain
chain = prompt | llm

# Invoke chain
res = chain.invoke({"input": "Hello, how are you?"})

print(res)

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ollama serve
ollama pull llama3.2:1b

python ./runnable.py

"""