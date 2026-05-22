from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


@tool
def web_search_tool(query):
    """Search the web for information"""
    print()
    print("=========")
    print(f"query for web search = {query}")
    tavily_client = TavilyClient()
    return tavily_client.search(query)



