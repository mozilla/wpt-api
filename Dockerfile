FROM python:3.6

WORKDIR /src

COPY Pipfile Pipfile.lock pipenv.txt send_to_datadog.py /src/

RUN pip install -r pipenv.txt && \
  pipenv install --dev --system

COPY . /src

CMD python send_to_datadog.py
