from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()

# create template from message objects
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=f"You are a helpful {domain} expert."),
    HumanMessage(content=f"Explain in simple terms, the concept of {topic} in 5 points.")
])

# format the prompt
prompt = chat_template.format_prompt(domain=domain, topic=topic)
print(prompt.to_string())   # verify it shows your domain/topic


# instantiate model and call
model = ChatOllama(model="llama3.2")
result = model.invoke(prompt.to_messages())

  # or prompt.to_messages() if invoke accepts messages

print()
print("========")
print(result.content)
