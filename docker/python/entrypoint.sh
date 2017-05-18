#!/bin/bash

cd /var/www/
export PYTHONPATH=/var/www/
gunicorn wsgi:application -b :5000
