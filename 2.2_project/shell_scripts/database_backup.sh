#!/bin/bash

# Import database settings
source /Users/wxo508/scripts_testing/crontab_trial/config/settings.sh

# Variables for Path and File name:
BACKUP_PATH="/Users/wxo508/scripts_testing/crontab_trial/db_backups/"
# BACKUP_NAME="weather_db_backup_$(date +\%Y\%m\%d\%H\%M\%S).sql"
BACKUP_NAME="weather_db_backup_$(date +\%Y\%m\%d\%H).sql"

# Create a database backup
mysqldump -u"$DATABASE_USERNAME" -p"$DATABASE_PASSWORD" -h"$DATABASE_HOST" -P"$DATABASE_PORT" "$DATABASE_NAME" > "$BACKUP_PATH/$BACKUP_NAME"

echo "Backup $BACKUP_NAME created successfully."


# Deleting old backups
# find "$BACKUP_PATH" -name 'weather_db_backup_*.sql' -mtime +1 -exec rm {} \;

# Current date in the format matching the filename
# current_date=$(date +%Y%m%d)

# Get the date from which all files should be deleted
deletion_date=$(date -v-24H +%Y%m%d%H)



# Loop over backup files
# "$file": This is the variable that contains the name of the file you're checking.
# loop processes only existing files. It helps to avoid errors when the pattern weather_db_backup_*.sql doesn't match any files and does not process non-existent files
for file in "$BACKUP_PATH"/weather_db_backup_*.sql; do
    if [ -f "$file" ]; then
        # Extract the date from the filename
        # awk -F'[_.]' '{print $(NF-1)}': This uses awk, a powerful text processing tool, to split the filename and extract a specific part.
        # '{print $(NF-1)}': This instructs awk to print the second-to-last field. 
        file_date_hour=$(echo "$file" | awk -F'[_.]' '{print $(NF-1)}')

        # Compare the file date to the current date
        if [[ "$file_date_hour" -lt "$deletion_date" ]]; then
            echo "Deleting old backup: $file"
            rm "$file"
        fi
    fi
done
