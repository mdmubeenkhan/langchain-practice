from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from pprint import pprint

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()
token_limit = int(input("Enter token limit (e.g., 50)\n").strip())

chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=f"You are a helpful {domain} expert who explain in crisp manner and consume less than 100 token."),
    HumanMessage(content=f"Explain in simple terms, the concept of {topic} in 2 points.")
])

prompt = chat_template.format_prompt(domain=domain, topic=topic)
print(prompt.to_string())
print(f"\n[Token limit set to: {token_limit}]")
print("[Press Ctrl+C to interrupt streaming]\n")

model = ChatOllama(
    model="llama3.2",
    num_predict=token_limit
)

try:
    for chunk in model.stream(prompt.to_messages()):
        print(chunk.content, end="", flush=True)
except KeyboardInterrupt:
    print("\n[Interrupted by user]")

print("\n\n========")
result = model.invoke(prompt.to_messages())
print("======RESP METADATA=======")
pprint(result.response_metadata)
pprint(f"Tokens generated: {result.response_metadata.get('eval_count')}")
