FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y  python 3.6 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install datadog

CMD python send_to_datadog.py

RUN netstat | grep "8125"
