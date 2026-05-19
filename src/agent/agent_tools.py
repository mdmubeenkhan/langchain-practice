import urllib.error
import urllib.request
import meteostat as ms

from langchain.tools import tool
from datetime import datetime

# # simple function
# def mubeen_details() -> str:
#     """This function returns mubeen details"""
#     with open("/Users/mubeen/lc/practice/src/agent/mubeen.txt", "r") as f:
#         data = f.readlines()
#     return "".join(data)  # Return as string, not list


@tool
def fetch_hyderabad_weather_details() -> str:
    """Fetch hyderabad current weather details including temperature."""
    
    POINT = ms.Point(17.3850, 78.4867, 505)
    stations = ms.stations.nearby(POINT, limit=1)
    
    start = datetime.now().date()
    end = datetime.now().date()
    
    if not stations.empty:
        station_id = stations.index[0]
        data = ms.hourly(station_id, start, end)
        data = data.fetch()
        
        temperature = data['temp'].values[0]
        result = f"Temperature in Hyderabad: {temperature}°C"
        print(result)
        return result  # Fixed: was missing 'f' prefix before the string
    
    return "Unable to fetch temperature data"


@tool
def mubeen_details() -> str:
    """Get details about Mubeen including his work and education."""
    with open("/Users/mubeen/lc/practice/src/agent/mubeen.txt", "r") as f:
        data = f.readlines()
    return "".join(data)
