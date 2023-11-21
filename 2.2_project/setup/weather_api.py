import os
import sys
import time
import requests
from datetime import datetime

"""Adding absolute path for to be able to import config"""
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


import pandas as pd

from config.settings import API_KEY

"""API call function to OpenWeatherMap to get weather data for a specific city. """


def get_weather_data(city):
    # Simulating a network request delay to prevent a block from server.
    time.sleep(0.1)

    try:
        # The API request URL
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        # Performing the request
        response = requests.get(url)

        # Ensure action on successful responses
        if response.status_code == 200:
            data = response.json()

            # Extract relevant data from the response
            weather_data = {
                "city_name": city,
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["main"],
                "conditions_description": data["weather"][0]["description"],
                # Add a current timestamp to know what time the weather was recorded.
                "timestamp": datetime.now(),
            }
            # Return a DataFrame
            return pd.DataFrame([weather_data])
        else:
            # Handling unsuccessful calls
            print(f"Failed to retrieve data for {city}, status: {response.status_code}")

    # Handling any other exceptions.
    except Exception as e:
        print(f"Exception occurred while fetching data for {city}: {str(e)}")
