from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from pprint import pprint

from pydantic import BaseModel

class TopicInfo(BaseModel):
    description: str
    pros: str
    cons: str

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()
token_limit = int(input("Enter token limit (e.g., 50)\n").strip())

system_prompt = """
You are a helpful expert who explain in crisp manner one positive and one negative and consume less than 100 token.
topic vehicle:
    vehicle used to drive to reach destination.
    vehicle maintenance cost money
topic owning cat:
    cat is playful reduces stress and have happy environment watching them play.
    taking care of cat is costly and not recommended for busy people
topic summer:
    in summer day starts early and enough of vitamin D
    summer is very hot which forces us to stay indoor 
"""
# f"You are a helpful {domain} expert who explain in crisp manner and consume less than 100 token."
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=system_prompt),
    HumanMessage(content=f"Explain {topic}.")
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
