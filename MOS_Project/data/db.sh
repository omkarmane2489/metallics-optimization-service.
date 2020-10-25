#!/bin/bash
#################
# Change these values
#################


psqluser="omkar_mane"   # Database username
psqlpass="password"  # Database password
psqldb="MOS"   # Database name

#################
# Database
#################
printf "CREATE USER $psqluser WITH PASSWORD '$psqlpass';\nCREATE DATABASE $psqldb WITH OWNER $psqluser;" > script.sql

psql -f script.sql

echo "Finished Database section"

echo "End of the script"

exit