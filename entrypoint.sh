#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Craete database migrations
echo "Creating database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

#Load dummy data
echo 'creating dummy data'
python manage.py loaddata db.json

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

