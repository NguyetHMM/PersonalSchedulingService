FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get clean

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]