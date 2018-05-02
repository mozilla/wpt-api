FROM python:2-alpine3.7

RUN pip install datadog

CMD python send_to_datadog.py
