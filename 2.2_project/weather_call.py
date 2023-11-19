#!/Volumes/Workspace/Anaconda/anaconda3/bin/python

import concurrent.futures
import pandas as pd
import time
from datetime import datetime


from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from setup.database_loader import DatabaseLoader
from setup.weather_api import get_weather_data

"""Variables:"""
OUTPUT_TABLE = "weather_data"
NUM_THREADS = 3

"""Starting timer"""
start_time = time.time()


"""Instantiating Database connection."""
db_loader = DatabaseLoader()
db_loader.create_engine_with_db()


"""Initialize an empty DataFrame to store all results"""
all_weather_data = pd.DataFrame()

"""Retrieving up-to-date cities from MySQL database for querying."""
Session = sessionmaker(bind=db_loader.engine)

with Session() as session:
    result = session.execute(text("SELECT city_name FROM cities ORDER BY city_id ASC"))
    # Extract city names into a list
    lookup_cities = [row[0] for row in result]

print(lookup_cities)
# cities = ["London", "Berlin"]  # Example list of cities

# """Linear"""
# all_weather_data = pd.DataFrame()

# # Loop through each city and append the data
# for city in lookup_cities:
#     # Fetch weather data for the city
#     # city_weather_data = get_weather_data(city, API_KEY)
#     city_weather_data = get_weather_data(city)

#     # Check if DataFrame is not empty (i.e., successful data fetch).
#     if not city_weather_data.empty:
#         # Send the DataFrame to the 'cities' table in the database.
#         db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
#         print(f"Weather data for {city} sent to database.")
#     else:
#         print(f"Failed to fetch or send data for {city}.")

#     # Add all to the DataFrame.
#     all_weather_data = pd.concat([all_weather_data, city_weather_data], ignore_index=True)

# all_weather_data

"""Threaded model, with 3 threads."""
# Initialize an empty DataFrame to store all weather data
all_weather_data = pd.DataFrame()

# Use ThreadPoolExecutor to fetch weather data concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    # Create a future to city mapping
    # future_to_city = {executor.submit(get_weather_data, city, API_KEY): city for city in cities}
    future_to_city = {
        executor.submit(get_weather_data, city): city
        for city in lookup_cities[
            :3
        ]  ## CHANGE HERE!!! !!!!!!!!!!!! !!!!!! !!!!!! !!!!!! !!!!!! !!!!!! !!!!!!
    }

    # loop iterates over the Future objects as they are completed. as_completed yields futures as they complete (either successfully or with an exception).
    # A Future object is a representation of an eventual result of an asynchronous operation. When submit is called, it immediately returns a Future, even though the associated function might not have completed yet.
    # as_completed yields futures as they complete, regardless of the order in which they were submitted.
    for future in concurrent.futures.as_completed(future_to_city):
        city = future_to_city[future]
        # future.result() retrieves the result of the completed task. It's wrapped in a try block to handle potential exceptions.
        try:
            city_weather_data = future.result()
            # Check and Process the Result
            # If the result (data for a city) is not empty, it is sent to a database using db_loader
            if not city_weather_data.empty:
                # Send the DataFrame to the 'cities' table in the database
                db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
                print(f"Weather data for {city} sent to database.")
            else:
                print(f"Failed to fetch or send data for {city}.")
        except Exception as exc:
            print(f"{city} generated an exception: {exc}")

        # Add all to the DataFrame
        all_weather_data = pd.concat(
            [all_weather_data, city_weather_data], ignore_index=True
        )

"""End the timer and print the elapsed time"""
end_time = time.time()
elapsed_time = end_time - start_time
timestamp = datetime.now()

"""Formatting for readability:"""
minutes, seconds = divmod(elapsed_time, 60)
formatted_elapsed_time = f"{int(minutes)} minutes, {int(seconds)} seconds"

# Print the formatted output
print("=" * 30)
print("Execution Summary")
print("=" * 30)
print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Total elapsed time: {formatted_elapsed_time}")
print("=" * 30)
