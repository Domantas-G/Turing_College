Plan

1. Data Acquisition:
   Select a weather API (e.g., OpenWeatherMap) to retrieve hourly weather data.
   Use Python to periodically query the API for the 20 largest cities in Europe.
   Since the API calls need to be made concurrently, we can use asyncio (co-routines) to fetch data for multiple cities simultaneously.
2. Database Setup:
   Choose an RDBMS (e.g., PostgreSQL) for storing the weather data.
   Design a schema to store the city, country, timestamp, temperature, and weather condition.
3. Data Insertion:
   Use Python to insert the fetched data into the database.
4. Data Analysis:
   Create SQL views or queries to:
   Compute max, min, and standard deviation of temperatures per country and city for today, yesterday, current week, and last seven days.
   Identify the cities with the highest or lowest temperature for each hour, day, and week.
   Count the number of times it rained in the last day and week.
5. Scheduling:
   Set up cron jobs to:
   Periodically fetch and store data from the weather API.
   Run the analysis queries as required.
6. Scalability:
   Ensure that the code and database schema are designed in a way that they can easily accommodate an increasing number of cities.
7. Validation:
   Compare the fetched data with the simulator's predictions for validation.
8. Improvements and Insights:
   Provide insights on potential improvements in data acquisition, storage, and analysis.
   Implementation Details
9. Data Acquisition:
   Use Python's asyncio library to make concurrent API calls to fetch data for multiple cities.
   Justification: Asyncio is lightweight, efficient, and suitable for IO-bound tasks like API calls.

10. Edit the Crontab:
    Open the crontab file for editing using the crontab -e command. Once inside, you can add your tasks.

11. Setup Cron Jobs:
    a. Fetch and Store Data:
    Let's assume you have a Python script named fetch_and_store_data.py that fetches the weather data and stores it in the database. To run this script every hour, add the following line to your crontab file:
    0 \* \* \* \* /path/to/python3 /path/to/fetch_and_store_data.py

This means: at minute 0 of every hour of every day of every month, execute the Python script.

b. Run Analysis Queries:
Suppose you have another Python script run_analysis.py that executes the SQL queries for the data analysis. Depending on the frequency you want to run the analysis, you can add a corresponding line in the crontab file.

Every Hour:
0 \* \* \* _ /path/to/python3 /path/to/run_analysis.py
Every Day at Midnight:
0 0 _ \* \* /path/to/python3 /path/to/run_analysis.py

Every Week on Sunday at Midnight:
0 0 \* \* 0 /path/to/python3 /path/to/run_analysis.py

5. Logging (Optional):
   To keep track of the cron jobs, you can redirect the output (stdout and stderr) to log files:
   0 \* \* \* _ /path/to/python3 /path/to/fetch_and_store_data.py >> /path/to/log/fetch_data.log 2>&1
   0 0 _ \* \* /path/to/python3 /path/to/run_analysis.py >> /path/to/log/analysis.log 2>&1

Views:
Temperature Statistics Views:

Purpose: These views provide statistical analysis of temperatures, including maximum, minimum, and standard deviation, for different timeframes: today, yesterday, the current week, and the last seven days.
Views: city_temperature_stats_today, city_temperature_stats_yesterday, city_temperature_stats_current_week, city_temperature_stats_last_seven_days.
Functionality: Each view groups data by city and calculates the mentioned temperature statistics. These views help in understanding daily and weekly temperature fluctuations and identifying anomalies or trends.
Extreme Temperature Views:

Purpose: To identify cities experiencing the highest and lowest temperatures for each hour, day, and week.
Views: min_max_temp_hourly, min_max_temp_daily, min_max_temp_weekly.
Functionality: These views rank cities based on their temperatures and extract the city with the highest and the lowest temperature for each time period. They are instrumental in pinpointing extreme weather conditions and their geographic distribution.
Rainfall Frequency Views:

Purpose: To count the number of hours it rained in each city during the last day and week.
Views: city_rain_stats.
Functionality: These views calculate the count of distinct hours with rainfall for each city, giving an insight into the frequency of rainy conditions. They are crucial for understanding the rainfall patterns and planning activities that depend on weather conditions.
Applications:
Weather Forecasting and Analysis: These views are invaluable for meteorologists and researchers in analyzing weather patterns and forecasting.
Urban Planning and Agriculture: Understanding temperature trends and rainfall patterns aids in urban development and agricultural planning.
Public Awareness and Safety: These views can inform the public about extreme weather conditions, aiding in preparation and safety measures.
Notes:
The data is aggregated based on timestamps and city names.
Temperature data is rounded to two decimal places where applicable for clarity.
The views are designed for efficient querying and can be easily integrated into reporting tools or dashboards for real-time weather analytics.

Ideally split out cronjobs by timeframes - i.e. 7 day window analytical / reporting functions all move to that job to recalculate only once a day. I opted to keep jobs running by type of functions they perform rather than by frequency that they need to run. But once the table would get bigger, this would need to change.
