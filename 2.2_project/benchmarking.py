# #!/Volumes/Workspace/Anaconda/anaconda3/bin/python

# import concurrent.futures
# import logging
# import time
# from datetime import datetime

# import pandas as pd
# from sqlalchemy import text
# from sqlalchemy.orm import sessionmaker

# from setup.database_loader import DatabaseLoader
# from setup.weather_api import get_weather_data

# # Logs for benchmarking
# logging.basicConfig(
#     filename="/Users/wxo508/scripts_testing/crontab_trial/logs/benchmarking.log",
#     filemode="a",
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# """Variables:"""
# OUTPUT_TABLE = "weather_data"
# NUM_THREADS = 3

# """Starting timer and retrieval process."""
# start_time = time.time()


# """Instantiating Database connection."""
# db_loader = DatabaseLoader()
# db_loader.create_engine_with_db()


# """Initialize an empty DataFrame to store all results"""
# all_weather_data = pd.DataFrame()

# """Retrieving up-to-date cities from MySQL database for querying."""
# Session = sessionmaker(bind=db_loader.engine)

# with Session() as session:
#     result = session.execute(text("SELECT city_name FROM cities ORDER BY city_id ASC"))
#     lookup_cities = [row[0] for row in result]

# # Decrease the number of calls.
# lookup_cities = lookup_cities[:5]

# """Benchmarking Theards and Processes."""


# def benchmark(executor_type):
#     start_time = time.time()

#     if executor_type == "threads":
#         with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
#             future_to_city = {
#                 executor.submit(get_weather_data, city): city for city in lookup_cities
#             }
#             for future in concurrent.futures.as_completed(future_to_city):
#                 city = future_to_city[future]
#                 try:
#                     city_weather_data = future.result()
#                     if not city_weather_data.empty:
#                         db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
#                         logging.info(f"Weather data for {city} sent to database.")
#                     else:
#                         logging.warning(f"Failed to fetch data for {city}.")
#                 except Exception as exc:
#                     logging.error(f"{city} generated an exception: {exc}")

#     elif executor_type == "processes":
#         with concurrent.futures.ProcessPoolExecutor(
#             max_workers=NUM_THREADS
#         ) as executor:
#             future_to_city = {
#                 executor.submit(get_weather_data, city): city for city in lookup_cities
#             }
#             for future in concurrent.futures.as_completed(future_to_city):
#                 city = future_to_city[future]
#                 try:
#                     city_weather_data = future.result()
#                     if not city_weather_data.empty:
#                         db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
#                         logging.info(f"Weather data for {city} sent to database.")
#                     else:
#                         logging.warning(f"Failed to fetch data for {city}.")
#                 except Exception as exc:
#                     logging.error(f"{city} generated an exception: {exc}")

#     end_time = time.time()
#     return end_time - start_time


# # Benchmarking
# NUM_THREADS = 3
# num_trials = 4
# executor_types = ["threads", "processes"]

# for executor_type in executor_types:
#     times = [benchmark(executor_type) for _ in range(num_trials)]
#     avg_time = sum(times) / num_trials
#     outcome = f"Average execution time using {executor_type}: {avg_time} seconds"
#     print(outcome)
#     logging.info(outcome)


#!/Volumes/Workspace/Anaconda/anaconda3/bin/python

import concurrent.futures
import pandas as pd
import time
from datetime import datetime
import logging
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from setup.database_loader import DatabaseLoader
from setup.weather_api import get_weather_data

# Setup logging for information during execution and debugging
logging.basicConfig(
    filename="/Users/wxo508/scripts_testing/crontab_trial/logs/benchmarking.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Variables
OUTPUT_TABLE = "weather_data"
NUM_THREADS = 3


# Abstract a function for benchmarking to call it into main() for processes to work properly.
def benchmark(executor_type):
    start_time = time.time()

    if executor_type == "threads":
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            future_to_city = {
                executor.submit(get_weather_data, city): city for city in lookup_cities
            }
            for future in concurrent.futures.as_completed(future_to_city):
                city = future_to_city[future]
                try:
                    city_weather_data = future.result()
                    if not city_weather_data.empty:
                        db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
                except Exception as exc:
                    logging.error(f"{city} generated an exception: {exc}")
    elif executor_type == "processes":
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=NUM_THREADS
        ) as executor:
            future_to_city = {
                executor.submit(get_weather_data, city): city for city in lookup_cities
            }
            for future in concurrent.futures.as_completed(future_to_city):
                city = future_to_city[future]
                try:
                    city_weather_data = future.result()
                    if not city_weather_data.empty:
                        db_loader.send_data(df=city_weather_data, db_table=OUTPUT_TABLE)
                except Exception as exc:
                    logging.error(f"{city} generated an exception: {exc}")

    end_time = time.time()
    return end_time - start_time


# Benchmarking performance:
if __name__ == "__main__":
    db_loader = DatabaseLoader()
    db_loader.create_engine_with_db()

    Session = sessionmaker(bind=db_loader.engine)
    with Session() as session:
        result = session.execute(
            text("SELECT city_name FROM cities ORDER BY city_id ASC")
        )
        lookup_cities = [row[0] for row in result]

    # Limit the number of cities for benchmarking
    lookup_cities = lookup_cities[:5]

    num_trials = 4
    executor_types = ["threads", "processes"]

    for executor_type in executor_types:
        times = [benchmark(executor_type) for _ in range(num_trials)]
        avg_time = round(sum(times) / num_trials, 2)
        log_message = (
            f"Average execution time using {executor_type}: {avg_time} seconds"
        )
        print(log_message)
        logging.info(log_message)
