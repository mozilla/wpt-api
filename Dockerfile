FROM python:2-alpine3.7

RUN pip install pipenv
RUN pipenv install datadog

RUN pipenv shell

CMD python send_to_datadog.py
