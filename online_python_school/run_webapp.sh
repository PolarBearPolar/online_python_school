#!/bin/bash
# wait until database is initialized
connection_status=1
while [ $connection_status -ne 0 ]
do
	echo "Connecting to database"
	psql --command="SELECT NOW();" postgresql://$PG_USER:$PG_PASSWORD@$PG_HOST:$PG_PORT/$PG_DB
	connection_status=$?
	sleep 5
done
echo "Connected"
echo "=================================="
# initialize Django
echo "Create Django migrations"
python manage.py makemigrations
echo "=================================="
echo "Migrate"
python manage.py migrate
echo "=================================="
echo "Start server"
python manage.py runserver 0.0.0.0:8000
echo "=================================="