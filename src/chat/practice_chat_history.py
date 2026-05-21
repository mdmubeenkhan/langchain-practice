
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



model = ChatOllama(model="llama3.2")
chat_history = [
    SystemMessage(content="You are a helpful assistant who is knowledgeable and answers user question")
]

while True:
    user_input=input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower()=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print()
    print("=================")
    print(f"Bot = {result.content}")

print(f"chat history = {chat_history}")


