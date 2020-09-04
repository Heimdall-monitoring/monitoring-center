FROM python:3.7-alpine

LABEL maintainer="me@aurelienhugues.com"
LABEL description="Heimdall monitoring center backend"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY app.py README.md requirements.txt wsgi.py ./
COPY monitoring_center ./monitoring_center

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN mkdir /config

VOLUME /config

ENTRYPOINT [ "gunicorn" ]
CMD ["wsgi:app", "-b", "0.0.0.0:8000"]
