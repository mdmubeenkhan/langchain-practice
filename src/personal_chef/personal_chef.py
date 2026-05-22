from agent_tools import web_search_tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from pprint import pprint


checkpointer = InMemorySaver()

system_prompt="""
you are a personal chef. user will give you a list of ingredients they have.
using the web search tool, search the web for recipes that can be made with the ingredients they have.
return recipe suggestions and eventually the recipe instruction to user, if requested.
"""

question = HumanMessage(content="I have chicken and rice. what can i make?")
config = {"configurable": {"thread_id": "user_session_1"}}

agent = create_agent(
    model="openai:gpt-5.4-mini",
    tools=[web_search_tool],
    system_prompt=system_prompt,
    checkpointer=checkpointer
    
)

response = agent.invoke(
    {"messages": [question]},
    config
)

pprint(response)

