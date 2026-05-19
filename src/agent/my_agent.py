# pip install -qU langchain langchain-ollama
from langchain.agents import create_agent
from agent_tools import mubeen_details
from agent_tools import fetch_hyderabad_weather_details


def main():
    agent = create_agent(
        model="ollama:llama3.2",
        tools=[mubeen_details, fetch_hyderabad_weather_details],
        system_prompt="You are a helpful assistant who summarizes info and present neately in few points",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "who is mubeen and what work he does also fetch his city's current temperature"}]}
    )
    print()
    print("=========")
    print(result["messages"][-1].content_blocks)

if __name__ == "__main__":
    main()
