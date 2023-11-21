# dgervi-DE2.2

# Author: Domantas Gervinskas

![crontab](res.crontab.png)

## Contents

- [Project Introduction](#project-introduction)
- [Prerequisites](#prerequisites)
- [Key Features](#key-features)
- [Setup & Usage](#setup-&-usage)
- [Concurrency Threading choice](#concurrency-threading-choice)
- [Future Improvements](#future-improvements)

# Project Introduction

**Weather Data Collection API and Database Reporting**

This projects setups a database, creates an API for weather data collection using OpenWeatherMap API, then stores and analyzes weather data the top 20 European cities, with functionalities to add more.
The project sets up MySQL database, creates tables, retrieves weather data from the OpenWeatherMap API, and stores the data in a MySQL database, and then analysis and reporting is performed through SQL View creation.
Data is collected, and analyses refreshed automatically through a Crontab shell and python scripts execution, mostly hourly.
Additionally there are scripts for database re-indexing and backup tasks.

The projects intention is to be used by data scientists to validate their weather data predictions.

## Prerequisites

- Python 3.11
- MySQL database
- 2+ CPU cores

## Key Features

- Data models and schemas defined in SQLAlchemy.
- Create, configure and setup a MySQL database from Python (`database_loader.py`) using ORM classes (`models.py`).
  - Schema for city information, weather data including timestamps.
  - Constraints and default values for field validation.
- Database creation and pre-population with historical data from Python script.
- Scalable and dynamic city list management stored in MySQL database.
- Most scripts use context manager for database connections and API calls to free-up resources upon completion.
- Hourly weather data collection from the top 20 European cities, from OpenWeatherMap API.
  - Parsed APIs JSON responses into DataFrame and inserted data into the database.
  - Aggregated data into a single DataFrame for analysis.
- Storage of weather data in a SQL database for simulation and analysis.
  - Creating SQL views and scripts for automated weather data analysis.
  - Scheduling daily and weekly analytical reports with cron.
- Concurrent API data fetching with rate-limiting to prevent server overload.
  - Implemented concurrent data fetching using `concurrent.futures`.
  - Flexible switching between threads and processes.
  - Benchmarked concurrent methods for performance.
- Comprehensive analysis and reporting for acquired weather data.
- Automated tasks with cron for hourly data collection, analysis and reporting, and database maintenance.
- Implemented monitoring & logging at two levels - crontab and python.

## Concurrency Threading choice

Decision to proceed with threads concurrency is simple - Threads are simpler, require less CPU, don't separate memory, and web I/O is not CPU intensive thus making Threads preferred option. Big plus is that the method is easily switchable with a more complicated and sophisticated Processing methods for multi-core options, but is also capable of running on old and slow servers. Threading is unlikely to use up all resources on an outdated device, while processing might. ThreadPoolExecutor and ProcessPoolExecutor are interchangeable because they are both implemented by the same `concurrent.futures` module.
Threading is simple to implement and execute, while Processing requires additional guards to be put in place (i.e. need for entry point protection with `if __name__ == "__main__"` when multiprocessing with `ProcessPoolExecutor` otherwise multiple processes would be created before finishing the previous one, thus causing multiple errors).

Processes have a higher CPU and processing needs than Threads because they create separate Python interpreters.
For I/O (web API calls/requests) threads are more than sufficient because there are often wait times for I/O operations to complete, during which other threads can use the CPU and thus can efficiently perform I/O operations.

# Setup & Usage

1. Clone the repository.

```
git clone https://github.com/TuringCollegeSubmissions/dgervi-DE2.2.git
cd dgervi-DE2.2/
```

2. Update demo settings file with database connection details and API key in `config` directory.
   This is then used by `database_loader`, crontab and shell scrips when creating a database, tables, calling API, uploading data to the MySQL database, performing monitoring and administrations tasks.

All sripts have shebang line for easy execution. You might need to update it with your Python and Shell paths.

3. Navigate to the project directory:
   `cd dgervi-DE2.2`

4. Install the prerequisite Python libraries from the provided `requirements.txt` file:
   `pip install -r requirements.txt`

5. Setup the database, create necessary tables.
   This script also loads the database with historical data.
   `python create_database.py`

6. Database schema and constraints are defines in the `setup.models.py` file, while `database_loader.py` manages database connections and operations.
   ![ERD_Diagram](res.ERD_img.png)

7. Retrieve weather data and send it to the database. `setup.weather_api.py` handles API calls functions to OpenWeatherMap, while `weather_call.py` implements the function calls concurrently. This script includes Python logging, written into `logs/weather_call_python.log`:
   `python weather_call.py`

8. Currently `python weather_call.py` implements 2 concurrent programming with 3 threads, and supports flexible switching to concurrent processes. Interchange between the threads and processes by changing one line of code from/to:

```
FROM: with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
TO:   with concurrent.futures.ProcessPoolExecutor(max_workers=NUM_THREADS) as executor:
```

9. Reporting and Analysis views in MySQL database:
   Run SQL scripts in the `reporting` directory by executing the following scripts from `shell_scripts` directory:

```
<your_directory>/dgervi-de2.2/shell_scripts/extreme_temperatures.sh
<your_directory>/dgervi-de2.2/shell_scripts/raininess.sh
<your_directory>/dgervi-de2.2/shell_scripts/statistics_per_city.sh
```

10. Run Database Maintenance script for re-indexing weather data, for improved database performance:
    `<your_directory>/dgervi-de2.2/shell_scripts/index_weather_data.sh`

11. Run Database Backup script:
    `<your_directory>/dgervi-de2.2/shell_scripts/database_backup.sh`

12. Create a Crontab through Terminal/CLI:

```
crontab -e
```

13. Add required configurations for scripts to run automatically and save. These scripts include logging (copy-paste from `setup/crontab_setup.sh`).
    There's 2 readability additions here: MySQL path being set at the beginning for easy MySQL scripts execution, and Scripts path for all scripts. You need to update these according to your MySQL and this repository's locations'.

```
# Setting variable for common path, for readability.
# Define the common path
SCRIPTS_PATH=/Users/wxo508/scripts_testing/crontab_trial

# Setting MySQL path
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/mysql-8.1.0-macos13-arm64/bin

# Weather API call to OpenWeatherMap and storage to MySQL database, Hourly
0 * * * * $SCRIPTS_PATH/weather_call.py >> $SCRIPTS_PATH/logs/weather_call.log 2>&1

# Report and Analytical views refresh based on newly ingested data, Hourly
0 * * * * $SCRIPTS_PATH/shell_scripts/extreme_temperatures.sh >> $SCRIPTS_PATH/logs/extreme_temperatures.log 2>&1
0 * * * * $SCRIPTS_PATH/shell_scripts/raininess.sh >> $SCRIPTS_PATH/logs/raininess.log 2>&1
0 * * * * $SCRIPTS_PATH/shell_scripts/statistics_per_city.sh >> $SCRIPTS_PATH/logs/statistics_per_city.log 2>&1

# Weather data database backup and 24h+ age backup deletion, Hourly
0 * * * * $SCRIPTS_PATH/shell_scripts/database_backup.sh >> $SCRIPTS_PATH/logs/database_backup.log 2>&1

# Database reindexation for performance, Daily at 1pm
0 13 * * * $SCRIPTS_PATH/shell_scripts/index_weather_data.sh >> $SCRIPTS_PATH/logs/index_weather_data.log 2>&1
```

14. Compare performance between Threads and Process by running:
    `benchmarking.py`
    Output is saved into `logs/benchmarking.log`. Example output (actual):

```
Average execution time using threads: 2.358593165874481 seconds
Average execution time using processes: 1.795440673828125 seconds
```

You're done - scripts will now execute automatically every hours, thus calling a Weather API, storing the weather data in MySQL database, refreshing analytical and reporting views to be up to date, reindexing main database table, creating a backup and deleting old backups, as long as you keep the server/computer active.

**Note on logging:**
There is Python-level logging implemented with logging that controls what gets logged, while cron logs serve as a catch-all that is not captured by the Python logging (unhandled exceptions, system print statements, etc).

## Future Improvements

- Add Pydantic for data validation when it's being sent to MySQL database.
- Ideally split out cronjobs by timeframes - i.e. 7 day window analytical / reporting functions all move to that job to recalculate only once a day. I opted to keep jobs running by type of functions they perform rather than by frequency that they need to run. But once the table would get bigger, this would need to change.
- Process pool executor logging solution is not completely functioning, and while all processes share same logging configuration, there can be file access conflights because each process have their own Python interpreter running, and child processes do not share the logging configuration from the main process. Therefore to handle concurrent processing accurately there should be a QueueHandler applied.
