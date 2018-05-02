FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y  python 3.6 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install datadog

iptables -t nat -A DOCKER -p udp --dport 8125 -j DNAT --to-destination 34.197.24.237:8125

CMD python send_to_datadog.py
