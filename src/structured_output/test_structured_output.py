from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import json

class TopicInfo(BaseModel):
    description: str
    pros: str
    cons: str

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()
token_limit = int(input("Enter token limit (e.g., 50)\n").strip())

system_prompt = """
You are a helpful expert who explains in a crisp manner with one positive and one negative aspect.
Keep response under 100 tokens.

Examples:
topic vehicle:
    description: vehicle used to drive to reach destination.
    pros: enables transportation and mobility
    cons: vehicle maintenance costs money

topic owning cat:
    description: a domesticated feline pet
    pros: cat is playful, reduces stress, and creates a happy environment
    cons: taking care of a cat is costly and not recommended for busy people

topic summer:
    description: the warmest season of the year
    pros: day starts early and provides vitamin D from sunlight
    cons: summer is very hot which forces us to stay indoors
"""

chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=system_prompt),
    HumanMessage(content=f"Explain {topic} in the specified JSON format with description, pros, and cons fields.")
])

prompt = chat_template.format_prompt(domain=domain, topic=topic)
print(prompt.to_string())
print(f"\n[Token limit set to: {token_limit}]")
print("[Generating structured output...]\n")

model = ChatOllama(
    model="llama3.2",
    num_predict=token_limit
)

# Add structured output enforcement
structured_model = model.with_structured_output(TopicInfo)

try:
    result = structured_model.invoke(prompt.to_messages())
    
    print("========")
    print("STRUCTURED OUTPUT:")
    print(f"Description: {result.description}")
    print(f"Pros: {result.pros}")
    print(f"Cons: {result.cons}")
    
except KeyboardInterrupt:
    print("\n[Interrupted by user]")
except Exception as e:
    print(f"Error: {e}")
