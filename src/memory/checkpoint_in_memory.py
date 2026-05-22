from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from agent_tools import mubeen_details, fetch_hyderabad_weather_details

from dotenv import load_dotenv

load_dotenv()

# langgraph = A library for building stateful, multi-step workflows
# checkpoint = A snapshot of the agent's state at a point in time
# memory = Stores checkpoints in RAM (not in a database)
# InMemorySaver = The tool that saves and retrieves these snapshots

# checkpointer = InMemorySaver()
# Explanation: Creates an instance of InMemorySaver. This object will:

# Store the agent's state after each message
# Retrieve the state when the same thread_id is used again
# Keep everything in memory (lost when program ends)
# Think of it as a conversation memory manager.




def main():
    # Create checkpointer
    checkpointer = InMemorySaver()
    
    # checkpointer=checkpointer  # Add this!
    # Explanation: This is the key line! Gives the agent access to the checkpointer. Now the agent will:

    # Save its state after each invoke
    # Load previous state when you call it again with the same thread_id
        
    agent = create_agent(
        model="ollama:llama3.2",
        tools=[mubeen_details, fetch_hyderabad_weather_details],
        system_prompt="You are a helpful assistant who summarizes info and present neatly in few points",
        checkpointer=checkpointer  # Add this!
        # response_format=
        
    )

    # Use same thread_id for all queries
    # Create Configuration with Thread ID

    # Use same thread_id for all queries
    # config = {"configurable": {"thread_id": "user_session_1"}}
    # Explanation: Creates a configuration dictionary that tells the agent:

    # configurable = Configuration settings for this session
    # thread_id = Unique identifier for this conversation thread
    # "user_session_1" = All messages with this ID are part of the same conversation
    # Different thread_id = Different conversation (separate history)
    # Think of thread_id as a session ID or conversation room number.
    config = {"configurable": {"thread_id": "user_session_1"}}

    print("=== Query 1: Who is Mubeen? ===")
    result1 = agent.invoke(
        {"messages": [{"role": "user", "content": "who is mubeen?"}]},
        config  # Pass config
    )
    print(result1["messages"][-1].content_blocks)

    print("\n=== Query 2: Random question ===")
    result3 = agent.invoke(
        {"messages": [{"role": "user", "content": "tesla ev"}]},
        config  # Same thread_id
    )
    print(result3["messages"][-1].content_blocks)

    print("\n=== Query 3: What's Mubeen's city temperature? ===")
    print("SOLUTION: Agent REMEMBERS Mubeen from Query 1!")
    result2 = agent.invoke(
        {"messages": [{"role": "user", "content": "mubeen's city's current temperature"}]},
        config  # Same thread_id - agent has full history
    )
    print(result2["messages"][-1].content_blocks)

    print("\n=== Query 4: Who is Mubeen again? ===")
    print("BONUS: Agent remembers from Query 1 (no redundant tool calls)!")
    result4 = agent.invoke(
        {"messages": [{"role": "user", "content": "who is mubeen?"}]},
        config  # Same thread_id
    )
    print(result4["messages"][-1].content_blocks)

    # VIEW FULL CONVERSATION HISTORY
    print("\n=== Full Conversation History ===")
    state = agent.get_state(config)
    print(f"Total messages: {len(state.values['messages'])}")
    for i, msg in enumerate(state.values['messages']):
        print(f"\nMessage {i}:")
        print(msg)

if __name__ == "__main__":
    main()
