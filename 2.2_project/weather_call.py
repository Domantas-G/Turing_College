#!/Volumes/Workspace/Anaconda/anaconda3/bin/python

import concurrent.futures
import logging
import time
from datetime import datetime

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from setup.database_loader import DatabaseLoader
from setup.weather_api import get_weather_data


"""Variables:"""
OUTPUT_TABLE = "weather_data"
NUM_THREADS = 3

"""Starting timer and retrieval process."""
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


"""
Concurrent threading model, with 3 threads.
Alternatively, use ProcessPoolExecutor to fetch weather data concurrently with 3 Processors.
"""

if __name__ == "__main__":
    """Setup logging for information during execution and debugging."""
    logging.basicConfig(
        filename="/Users/wxo508/scripts_testing/crontab_trial/logs/weather_call_python.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.info("Started weather data retrieval.")

    # Print out which cities the data is being retrieved for.
    logging.info(f"Cities for weather retrieval: {lookup_cities}")

    """Choose a line for Threading or Processes. Both cases default to 3 workers."""
    # with concurrent.futures.ProcessPoolExecutor(max_workers=NUM_THREADS) as executor:
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        # Create a future to city mapping. Submit immediately returns a future regardless of functions' completion state.
        future_to_city = {
            executor.submit(get_weather_data, city): city for city in lookup_cities
        }
        # Loop over future objects as they are retrieved, yield futures as they are completed.
        for future in concurrent.futures.as_completed(future_to_city):
            city = future_to_city[future]
            try:
                # Retrieve results of completed tasks from futures.
                city_weather_data = future.result()
                # If there is a result returned then send it to a database table using db_loader.
                if not city_weather_data.empty:
                    db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
                    logging.info(f"Weather data for {city} sent to database.")
                else:
                    logging.warning(f"Failed to fetch data for {city}.")
            except Exception as exc:
                logging.error(f"{city} generated an exception: {exc}")

            # Add all results into a single dataframe for easy viewing and debugging.
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

"""Output the logging information."""
logging.info("Execution Summary")
logging.info(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
logging.info(f"Total elapsed time: {formatted_elapsed_time}")
