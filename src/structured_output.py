from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()

# create template from message objects
chat_template = ChatPromptTemplate([
    ('system', 'you are very knoledgeable assistant'),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", '{query}')
])

#load chat history
chat_history=[]
with open


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


