# tinyllama with nomic-embed-text

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOllama(model="tinyllama", temperature=0.0)

prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
            ("human", "{input}")
])

chain = prompt | llm

res = chain.invoke({"input": "What is the famous food?"})
print(res)

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ollama serve
ollama pull tinyllama

python ./chatprompt.py

"""