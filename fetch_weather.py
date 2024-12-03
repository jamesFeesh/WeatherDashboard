import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

# File paths
capitals_file = "capitals.csv"
city_data_file = "city.list.json"

# API Key and Base URL
API_KEY = "e1bb8904f6fa68631705320c11e0b77b"
BASE_URL = "http://api.openweathermap.org/data/2.5/group"

# Load the capitals.csv file
capitals_df = pd.read_csv(capitals_file)

# Load the city.list.json file
with open(city_data_file, "r", encoding="utf-8") as f:
    city_data = json.load(f)

# Create a mapping of capital names to city IDs
city_id_mapping = {}
for city in city_data:
    if city.get("name") in capitals_df["capital"].values:
        city_id_mapping[city["name"]] = city["id"]

# Prepare a list of city IDs for capitals
city_ids = list(city_id_mapping.values())

# Split city IDs into batches (OpenWeather API allows up to 20 IDs per request)
batch_size = 20
batches = [city_ids[i:i + batch_size] for i in range(0, len(city_ids), batch_size)]

# Fetch weather data for all batches
weather_data = []
for batch in batches:
    response = requests.get(
        BASE_URL,
        params={"id": ",".join(map(str, batch)), "units": "metric", "appid": API_KEY},
    )
    if response.status_code == 200:
        weather_data.extend(response.json()["list"])
    else:
        print(f"Error fetching data for batch {batch}: {response.status_code}")

# Process the weather data into a DataFrame
if weather_data:
    weather_df = pd.DataFrame([{
        "City": city["name"],
        "Temperature": city["main"]["temp"],
        "Weather": city["weather"][0]["description"],
        "Country": city["sys"]["country"]
    } for city in weather_data])

    # Identify the top 5 hottest capitals
    hottest = weather_df.sort_values("Temperature", ascending=False).head(5)
    print("\nTop 5 Hottest Capitals:")
    print(hottest)
    hottest.to_csv("hottest_capitals.csv", index=False)
    print("\nTop 5 hottest capitals saved to hottest_capitals.csv.")

    # Identify the top 5 coldest capitals
    coldest = weather_df.sort_values("Temperature", ascending=True).head(5)
    print("\nTop 5 Coldest Capitals:")
    print(coldest)
    coldest.to_csv("coldest_capitals.csv", index=False)
    print("\nTop 5 coldest capitals saved to coldest_capitals.csv.")

    # Plot hottest capitals
    plt.bar(hottest['City'], hottest['Temperature'], color='orange')
    plt.title("Top 5 Hottest Capitals")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("hottest_capitals.png")
    print("\nBar chart for hottest capitals saved as hottest_capitals.png.")

    # Plot coldest capitals
    plt.figure()
    plt.bar(coldest['City'], coldest['Temperature'], color='blue')
    plt.title("Top 5 Coldest Capitals")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("coldest_capitals.png")
    print("\nBar chart for coldest capitals saved as coldest_capitals.png.")
else:
    print("No valid weather data found.")
