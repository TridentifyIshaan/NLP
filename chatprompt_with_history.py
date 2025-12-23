# tinyllama with nomic-embed-text

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOllama(model="tinyllama", temperature=0.0)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("human", "{input}")
# ])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "Make sure your answer is correct and provide the answer in a simple way and in one line."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

history = InMemoryChatMessageHistory()

chain = prompt2 | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="history",
)

config={"configurable": {"session_id": "user-3"}}

res = chain_with_history.invoke({"input": "What is the famous food in India?"}, config=config)
print(res.content)
print()

config={"configurable": {"session_id": "user-4"}}

res = chain_with_history.invoke({"input": "What is the famous food in France?"}, config=config)
print(res.content)

"""
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ollama serve
ollama pull tinyllama

python ./chatprompt_with_history.py

"""