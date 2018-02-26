#!/usr/bin/env bash
set -e

echo "Waiting for postgres..."

while ! nc -z amity-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

python run.py

# this bash script checks port number 5432 of container named amity-db
# to ascertain that it is open. this means that the postgres server is up and running
# amity-db is what i named the postgres database container.
# when the port is open, then the script run all other subsequent commands following
# which commands are essentially running migrations on the database in that said container
# and then start the flask API application.






