FROM python:3.7-alpine

LABEL maintainer="your email here"
LABEL description="You description here"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY app.py README.md requirements.txt ./
COPY monitoring_center ./monitoring_center

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN mkdir /config

VOLUME /config

ENTRYPOINT [ "gunicorn" ]
CMD ["wsgi:app"]
