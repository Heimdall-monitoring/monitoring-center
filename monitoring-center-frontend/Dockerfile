FROM nginx:1.19-alpine

RUN mkdir /config

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/*.conf /etc/nginx/conf.d/
COPY docker_healthcheck .

VOLUME /config
VOLUME /var/log/nginx

RUN rm -rf /docker-entrypoint*
ENTRYPOINT []

CMD ["nginx", "-g", "daemon off;"]
HEALTHCHECK --interval=120s --timeout=5s \
    CMD /docker_healthcheck || exit 1

COPY dist/ /www/
