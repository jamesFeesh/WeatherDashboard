import os
import subprocess
import pandas as pd
import streamlit as st

# File paths
daily_data_file = "weather_data.csv"

# Check if the file exists
if not os.path.exists(daily_data_file):
    # Run fetch_weather.py to generate the data
    try:
        st.write("Generating weather data file...")
        subprocess.run(["python", "fetch_weather.py"], check=True)
        st.write("Weather data file generated successfully.")
    except subprocess.CalledProcessError as e:
        st.error("Failed to generate weather data. Please check fetch_weather.py.")
        st.stop()

# Load the weather data
try:
    daily_data = pd.read_csv(daily_data_file)
except Exception as e:
    st.error(f"Error reading weather data: {e}")
    st.stop()

# Dashboard Title
st.title("Weather Dashboard")

# Hottest Capitals
st.subheader("Top 5 Hottest Capitals")
try:
    hottest = daily_data.sort_values("Temperature", ascending=False).head(5)
    st.write(hottest)
except Exception as e:
    st.error(f"Error processing hottest capitals: {e}")

# Coldest Capitals
st.subheader("Top 5 Coldest Capitals")
try:
    coldest = daily_data.sort_values("Temperature", ascending=True).head(5)
    st.write(coldest)
except Exception as e:
    st.error(f"Error processing coldest capitals: {e}")
