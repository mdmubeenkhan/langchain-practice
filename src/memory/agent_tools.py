import urllib.error
import urllib.request
import meteostat as ms
from langchain.tools import tool
from datetime import datetime
from typing import Dict, Any
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

@tool
def mubeen_details() -> str:
    """Get detailed information about Mubeen. 
    Call this tool when asked 'who is mubeen', 'tell me about mubeen', 
    'what does mubeen do', or any questions about Mubeen's background, 
    education, work, or hobbies."""
    try:
        with open("/Users/mubeen/lc/practice/src/agent/mubeen.txt", "r") as f:
            data = f.read()
        return data if data.strip() else "No Mubeen details found in file."
    except FileNotFoundError:
        return "Mubeen details file not found."


@tool
def fetch_hyderabad_weather_details() -> str:
    """Fetch the current temperature in Hyderabad, India. 
    Call this tool when asked about weather, temperature, or climate in Hyderabad."""
    
    POINT = ms.Point(17.3850, 78.4867, 505)
    stations = ms.stations.nearby(POINT, limit=1)
    
    start = datetime.now().date()
    end = datetime.now().date()
    
    if not stations.empty:
        station_id = stations.index[0]
        data = ms.hourly(station_id, start, end)
        data = data.fetch()
        
        temperature = data['temp'].values[0]
        result = f"Current temperature in Hyderabad: {temperature}°C"
        return result
    
    return "Unable to fetch temperature data for Hyderabad"

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information"""
    tavily_client = TavilyClient()
    return tavily_client.search(query)


