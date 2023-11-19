#!/bin/bash

# Import database settings
source /Users/wxo508/scripts_testing/crontab_trial/config/settings.sh

# Execute the SQL script
mysql -u"$DATABASE_USERNAME" -p"$DATABASE_PASSWORD" -h"$DATABASE_HOST" -P"$DATABASE_PORT" "$DATABASE_NAME" -e "OPTIMIZE TABLE weather_data;"

echo "Weather_data reindexed successfully."