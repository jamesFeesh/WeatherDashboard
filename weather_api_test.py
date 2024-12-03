import requests

# Your actual API key
API_KEY = "e1bb8904f6fa68631705320c11e0b77b"
CITY = "Amsterdam"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch the weather data
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error:", response.status_code)
