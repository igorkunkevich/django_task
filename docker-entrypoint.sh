#!/bin/bash

# Make migrations
echo "Collect static files"
python manage.py makemigrations company

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000