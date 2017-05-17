#!/usr/bin/env bash

pyvenv venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=.:$PYTHONPATH
python translate_api/app.py