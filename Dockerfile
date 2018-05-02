FROM python:3

ADD send_to_datadog.py /

RUN pip3 install datadog

# RUN iptables -t nat -A DOCKER -p udp --dport 8125 -j DNAT --to-destination 34.197.24.237:8125

CMD [ "python", "./send_to_datadog.py" ]
