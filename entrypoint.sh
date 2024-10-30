#!/bin/sh

gunicorn gitpractice.wsgi:application --bind 0.0.0.0:8000