
from langchain_ollama import ChatOllama




def main():
    llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
    )

    messages = [
        (
            "system",
            "You are a helpful assistant who is knowledgeable and answers user question",
        ),
        ("human", "do you remember my name"
        ""),
    ]
    ai_msg = llm.invoke(messages)
    print()
    print("=============")
    print(ai_msg.content)


if __name__ == "__main__":
    main()
