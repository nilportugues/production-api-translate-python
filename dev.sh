#!/usr/bin/env bash

pip install virtualenv


pyvenv venv
source venv/bin/activate
pip install -r translate_api/translate_api/requirements.txt
export PYTHONPATH=.:$PYTHONPATH
python translate_api/translate_api/application_dev.py