# pip install -qU langchain langchain-ollama
from langchain.agents import create_agent
from agent_tools import mubeen_details
from agent_tools import fetch_hyderabad_weather_details

# calling tools individually
# PROBLEM without CHECK Pointing
def main():
    agent = create_agent(
        model="ollama:llama3.2",
        tools=[mubeen_details, fetch_hyderabad_weather_details],
        system_prompt="You are a helpful assistant who summarizes info and present neatly in few points",
    )

    print("=== Query 1: Who is Mubeen? ===")
    result1 = agent.invoke(
        {"messages": [{"role": "user", "content": "who is mubeen?"}]}
    )
    print(result1["messages"][-1].content_blocks)

    print("\n=== Query 2: Random question (Agent forgets Mubeen) ===")
    result3 = agent.invoke(
        {"messages": [{"role": "user", "content": "tesla ev"}]}
    )
    print(result3["messages"][-1].content_blocks)

    print("\n=== Query 3: What's Mubeen's city temperature? ===")
    print("PROBLEM: Agent doesn't remember Mubeen from Query 1!")
    result2 = agent.invoke(
        {"messages": [{"role": "user", "content": "mubeen's city's current temperature"}]}
    )
    print(result2["messages"][-1].content_blocks)   

    print("\n=== Query 4: Who is Mubeen again? ===")
    print("PROBLEM: Agent has to fetch Mubeen info AGAIN (redundant)!")
    result4 = agent.invoke(
        {"messages": [{"role": "user", "content": "who is mubeen?"}]}
    )
    print(result4["messages"][-1].content_blocks)



if __name__ == "__main__":
    main()
