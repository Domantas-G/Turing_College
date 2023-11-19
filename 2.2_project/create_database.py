"""
This script is designed for setting up and managing a database for weather data collection. 
"""
import os
import pandas as pd

from setup.database_loader import DatabaseLoader

# Importing a list of cities that will be fed to a database.
from src.top_20_europe_cities import cities_20

"""Create database connection and database."""
db_loader = DatabaseLoader()
db_loader.create_engine()

"""Delete old and create new database, to ensure a fresh setup. 
Then update engine to include newly created database for storing weather data."""
db_loader.create_database()

"""Create all tables in MySQL database with required PK/FK/Constraints."""
db_loader.create_tables()

"""Add initial cities to the database of the top 20 European cities.
This list is imported from `src.top_20_europe_cities`."""
db_loader.add_cities(cities_20)

"""Extended city management through adding/removing cities to/from the database."""
db_loader.add_cities(["Vilnius", "Kaunas"])
db_loader.remove_cities(["Kaunas"])

"""Load historical data into a database."""
OUTPUT_TABLE = "weather_data"
current_path = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(current_path, "src", "weather_data_results_2.csv")
weather_data = pd.read_csv(csv_file_path)

db_loader.send_data(weather_data, OUTPUT_TABLE)
