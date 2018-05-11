FROM python:3.6-alpine

WORKDIR /envcat

ENTRYPOINT ["envcat"]

COPY . /app

RUN cd /app && pip3 install datadog
