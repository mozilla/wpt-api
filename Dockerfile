FROM python:3.7.2-alpine

WORKDIR /src

COPY Pipfile Pipfile.lock pipenv.txt send_to_datadog.py send_to_telemetry.py /src/

RUN pip install -r pipenv.txt --upgrade pip && \
  pipenv install --dev --system

COPY . /src

CMD python send_to_datadog.py
