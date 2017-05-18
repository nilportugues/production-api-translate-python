FROM python:2.7

RUN apt-get update
RUN apt-get install -y supervisor

COPY ./wsgi.py /var/www/

# Copying the requirements for installation to take advantage of the caching.
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

# Supervisor to keep it running forever
#ADD ./data/supervisor/flask_app.conf /etc/supervisor/conf.d/flask_app.conf
EXPOSE 5000

## Copy over the entrypoint
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

RUN mkdir -p /var/www
WORKDIR /var/www
RUN export PYTHONPATH=/var/www
ENTRYPOINT ["entrypoint.sh"]