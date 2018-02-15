#!/usr/bin/env bash
set -e

echo "Waiting for postgres..."

while ! nc -z amity-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started kyakabi nnyo mwana!!!"


python manage.py db init
python manage.py db migrate
python manage.py db upgrade

python run.py






