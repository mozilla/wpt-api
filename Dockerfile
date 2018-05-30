FROM python:3.6

WORKDIR /src

COPY Pipfile pipenv.txt send_to_datadog.py /src/

RUN pip install -r pipenv.txt && \
  pipenv install --dev

COPY . /src

CMD python send_to_datadog.py
