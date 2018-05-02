FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive

RUN pip install datadog

CMD python send_to_datadog.py

RUN netstat | grep "8125"
