FROM python:3.7-alpine

LABEL maintainer="me@aurelienhugues.com"
LABEL description="Heimdall monitoring center full application"
LABEL version="0.0.0"

RUN apk update && apk add --no-cache nginx supervisor

WORKDIR /usr/app
COPY monitoring-center-backend/app.py monitoring-center-backend/README.md monitoring-center-backend/requirements.txt monitoring-center-backend/wsgi.py ./
COPY monitoring-center-backend/monitoring_center ./monitoring_center

RUN rm /etc/nginx/conf.d/default.conf
COPY monitoring-center-frontend/docker/*.conf /etc/nginx/conf.d/
COPY monitoring-center-frontend/dist/ /www/

COPY docker/supervisor/* /etc/supervisor.d/
COPY docker/supervisord.conf /etc/supervisord.conf

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN mkdir /config
RUN mkdir /run/nginx

VOLUME /config

EXPOSE 80
EXPOSE 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]