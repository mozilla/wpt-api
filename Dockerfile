FROM python:3

ADD send_to_datadog.py /

RUN pip3 install datadog

CMD [ "python", "./send_to_datadog.py" ]
