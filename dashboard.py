import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# File paths
daily_data_file = "weather_data.csv"
API_KEY = "e1bb8904f6fa68631705320c11e0b77b"
BASE_URL = "http://api.openweathermap.org/data/2.5/group"

# Load daily data
daily_data = pd.read_csv(daily_data_file)

# Page title
st.title("Global Capitals Weather Dashboard")

# Show last update time
last_update = dt.datetime.now()
st.text(f"Last updated: {last_update.strftime('%Y-%m-%d %H:%M:%S')}")

# Top 5 Hottest and Coldest Capitals
st.subheader("Top 5 Hottest Capitals")
hottest = daily_data.sort_values("Temperature", ascending=False).head(5)
st.bar_chart(hottest[["City", "Temperature"]].set_index("City"))

st.subheader("Top 5 Coldest Capitals")
coldest = daily_data.sort_values("Temperature").head(5)
st.bar_chart(coldest[["City", "Temperature"]].set_index("City"))

# Live Weather Refresh (Button with a Limit)
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = None

def fetch_live_weather():
    global daily_data
    # Replace with your weather fetching logic
    # For simplicity, we use the same daily_data here
    daily_data = pd.read_csv(daily_data_file)
    st.session_state.last_refresh = dt.datetime.now()

refresh_button = st.button("Refresh Live Weather")
if refresh_button:
    now = dt.datetime.now()
    if st.session_state.last_refresh is None or (now - st.session_state.last_refresh).seconds > 1800:
        fetch_live_weather()
        st.success("Weather updated!")
    else:
        st.error("You can only refresh once every 30 minutes.")

# Select a city to view live weather
city = st.selectbox("Select a capital to view live weather", daily_data["City"].unique())
selected_city_data = daily_data[daily_data["City"] == city].iloc[0]
st.subheader(f"Live Weather for {city}")
st.write(f"**Temperature**: {selected_city_data['Temperature']}°C")
st.write(f"**Weather**: {selected_city_data['Weather']}")
st.write(f"**Country**: {selected_city_data['Country']}")

# Footer
st.text("Data powered by OpenWeather API")
