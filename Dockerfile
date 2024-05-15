# Dockerfile
FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/