FROM python:3.6-alpine

WORKDIR /src

COPY send_to_datadog.py /src

RUN pip3 install datadog

COPY . /src

CMD python send_to_datadog.py
