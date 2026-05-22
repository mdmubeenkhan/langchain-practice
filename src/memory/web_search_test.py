from agent_tools import web_search_for_latest_information
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from pprint import pprint

from pydantic import BaseModel

class InfoFormat(BaseModel):
    name: str

checkpointer = InMemorySaver()

system_prompt="you search web and answer the user, search tool you have is web_search_for_latest_information."

question = HumanMessage(content="name the person who is current chief minister of west bengal in india may 2026.")

agent = create_agent(
    model="ollama:llama3.2",
    tools=[web_search_for_latest_information],
    system_prompt=system_prompt
    # response_format=InfoFormat
)

response = agent.invoke(
    {"messages": [question]}
)

pprint(response)
