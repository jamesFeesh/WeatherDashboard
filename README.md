# Weather Dashboard Project

## Overview

This project is a weather dashboard that fetches and displays live weather data for global capitals. It identifies the hottest and coldest capitals for the day and allows users to manually refresh the data. The dashboard is built using Python for backend processing and Streamlit for a user-friendly front-end interface.

## Features

- **Fetch Live Weather Data**: Uses the OpenWeather API to gather real-time weather data for global capitals.
- **Top 5 Hottest and Coldest Capitals**: Highlights the extreme temperatures in an easy-to-read format.
- **Interactive Dashboard**: Built with Streamlit for an intuitive and responsive user interface.
- **Daily and On-Demand Refresh**: Automatically refreshes daily but allows users to manually refresh (limited to once every 30 minutes).

## Project Structure

- `fetch_weather.py`: The Python script that handles data fetching, processing, and saving results.
- `dashboard.py`: The Streamlit app script that displays the dashboard.
- `capitals.csv`: A CSV file containing the list of world capitals.
- `city.list.json`: A JSON file mapping city names to their respective OpenWeather city IDs.
- `requirements.txt`: Contains the dependencies required to run the project.

## Setup Instructions

### Prerequisites

1. Install Python (preferably 3.9 or later).
2. Create and activate a virtual environment.
3. Install Streamlit and other dependencies.

### Installation

1. Clone this repository:
   git clone https://github.com/your-username/weather-dashboard.git cd weather-dashboard

2. Install dependencies:
   pip install -r requirements.txt

3. Set up OpenWeather API:

- Obtain an API key from [OpenWeather](https://openweathermap.org/).
- Add your API key to the `fetch_weather.py` file (`API_KEY` variable).

### Usage

1. **Fetch Weather Data**:
   python fetch_weather.py

This will save the data to `weather_data.csv`.

2. **Run the Dashboard**:
   streamlit run dashboard.py

Open the URL provided in your terminal to access the dashboard.

### File Outputs

- `weather_data.csv`: Contains the full weather data for all capitals.
- `hottest_capitals.csv`: Contains the top 5 hottest capitals.
- `coldest_capitals.csv`: Contains the top 5 coldest capitals.

## Deployment

To deploy the dashboard online, you can use [Streamlit Community Cloud](https://streamlit.io/cloud) or similar hosting platforms:

1. Upload your project files.
2. Configure the dashboard as the main entry point.
3. Ensure API credentials are secure and accessible.

## Future Improvements

- Add search functionality for user-specified cities.
- Integrate additional weather metrics (e.g., wind speed, humidity).
- Enable user authentication for personalised dashboards.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Developed by James Fish. For inquiries, contact [jamesrobfish@gmail.com].
