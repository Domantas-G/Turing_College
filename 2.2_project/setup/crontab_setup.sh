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