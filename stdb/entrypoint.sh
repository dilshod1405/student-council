#!/usr/bin/env bash

sleep 5
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

