import meteostat as ms
from datetime import datetime


POINT = ms.Point(17.3850, 78.4867, 505)  # Try with your location

# Get nearby weather stations
stations = ms.stations.nearby(POINT, limit=1)

# print(stations)

# Get current weather data
# You can fetch historical or current data
start = datetime.now().date()
end = datetime.now().date()

# Fetch data from the closest station
if not stations.empty:
    station_id = stations.index[0]
    data = ms.hourly(station_id, start, end)
    data = data.fetch()
    
    # Get only temperature
    temperature = data['temp'].values[0]
    print()
    print(f"Temperature in Hyderabad: {temperature}°C")
