import requests

API_KEY = "802248b8a798a6e1e59be31a4560e2ec"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

# Here's a response object example, seperated by key: 

#{'coord': {'lon': -84.388, 'lat': 33.749}, 
# 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
# 'base': 'stations',
# 'main': {'temp': 297.34, 'feels_like': 296.28, 'temp_min': 296.07, 'temp_max': 298.79, 'pressure': 1018, 'humidity': 18}, 
# 'visibility': 10000, 
# 'wind': {'speed': 2.68, 'deg': 322, 'gust': 6.71}, 
# 'clouds': {'all': 0}, 'dt': 1646254801, 
# 'sys': {'type': 2, 'id': 2006620, 
# 'country': 'US', 
# 'sunrise': 1646222700, 
# 'sunset': 1646264082}, 
# 'timezone': -18000, 
# 'id': 4180439, 
# 'name': 'Atlanta', 
# 'cod': 200}



if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    # round to 2 decimal places
    # temperature = round((data['main']['temp'] -273.15) * 9/5 + 32, 2)
    # round to no decimal places
    temperature = round((data['main']['temp'] -273.15) * 9/5 + 32)
    print(f"The weather in {city} : {weather}. The temperature in {city} is : {temperature}f.")
else:
    print("Sorry, no weather for you.  Have you considered staying inside today?  Maybe just read a book.")