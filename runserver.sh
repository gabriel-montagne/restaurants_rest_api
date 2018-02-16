#!/usr/bin/env bash

cd src/restaurants_project/
export PYTHONPATH=restaurants_project;$PYTHONPATH

python manage.py migrate
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000