import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File paths
daily_data_file = "weather_data.csv"
hottest_capitals_file = "hottest_capitals.csv"
coldest_capitals_file = "coldest_capitals.csv"

# Load data
daily_data = pd.read_csv(daily_data_file)
hottest_capitals = pd.read_csv(hottest_capitals_file)
coldest_capitals = pd.read_csv(coldest_capitals_file)

# Streamlit App
st.title("Global Capitals Weather Dashboard")

# Display daily weather data
st.subheader("Weather Data for All Capitals")
st.dataframe(daily_data)

# Display hottest capitals
st.subheader("Top 5 Hottest Capitals Today")
st.dataframe(hottest_capitals)

# Display coldest capitals
st.subheader("Top 5 Coldest Capitals Today")
st.dataframe(coldest_capitals)

# Visualisation for hottest capitals
st.subheader("Top 5 Hottest Capitals - Temperature Visualization")
plt.figure(figsize=(10, 5))
plt.bar(hottest_capitals['City'], hottest_capitals['Temperature'], color='orange')
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Top 5 Hottest Capitals")
st.pyplot(plt)

# Visualisation for coldest capitals
st.subheader("Top 5 Coldest Capitals - Temperature Visualization")
plt.figure(figsize=(10, 5))
plt.bar(coldest_capitals['City'], coldest_capitals['Temperature'], color='blue')
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Top 5 Coldest Capitals")
st.pyplot(plt)
