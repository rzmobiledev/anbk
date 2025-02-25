#!/bin/bash

set -e

python manage.py checkdb --settings=core.settings
python manage.py makemigrations --settings=core.settings
python manage.py migrate --settings=core.settings
python manage.py collectstatic --no-input --settings=core.settings
python manage.py createuser --settings=core.settings

echo "========================================="
echo "ANBK, YOUR PROJECT IS UP AND RUNNING NOW"
echo "========================================="

export DJANGO_SETTINGS_MODULE=core.settings

daphne core.asgi:application -p 3001 -b 0.0.0.0