import os

from translate_api.application import create_app

"""
WSGI config for this project.

It exposes the WSGI callable as a module-level variable named ``application.py``.
"""

application = create_app()

if __name__ == '__main__':
    application.run()