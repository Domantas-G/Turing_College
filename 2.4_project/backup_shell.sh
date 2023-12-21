#!/bin/bash

# Import database settings
source /Users/wxo508/scripts_testing/crontab_trial/config/settings.sh

# Variables for Path and File name:
BACKUP_PATH="USER/db_backups/"
BACKUP_NAME="db_backup_$(date +\%Y\%m\%d\%H).sql"

# Create a database backup
mysqldump -u"$DATABASE_USERNAME" -p"$DATABASE_PASSWORD" -h"$DATABASE_HOST" -P"$DATABASE_PORT" "$DATABASE_NAME" > "$BACKUP_PATH/$BACKUP_NAME"

echo "Backup $BACKUP_NAME created successfully at: $(date '+%Y-%m-%d %H:%M')"

# Check the number of backups in the directory. Important to keep only backups in this directory.
# List all SQL files, -1 ensures each file gets a new line, and count the lines from `ls -1`. 
backup_count=$(ls -1 "$BACKUP_PATH"/*.sql | wc -l)

# If there are more than 20 backups, delete the oldest ones
if [ "$backup_count" -gt 20 ]; then
    # List backups, sort them, delete all except the newest 20.
    # -t to sort by modification time, newest first. -r to reverse --> oldest first.
    # -n -$20 to exclude newest 20 backups.  
    backups_to_delete=$(ls -1tr "$BACKUP_PATH"/db_backup_*.sql | head -n -$20)

    for file in $backups_to_delete; do
        echo "Deleting old backup: $file"
        rm "$file"
    done
fi


