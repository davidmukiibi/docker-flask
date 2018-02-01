#!/usr/bin/env bash
set -e

python manage.py db migrate
python manage.py db upgrade