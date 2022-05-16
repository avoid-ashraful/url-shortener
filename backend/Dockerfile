FROM python:3.8.4-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ADD backend/requirements.txt /app/backend/requirements.txt
RUN apt-get update && apt-get install git iputils-ping gcc -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt --no-cache-dir

COPY . /app/backend
RUN useradd backend
RUN chown -R backend:backend /app
USER backend

ENV DATABASE_URL=postgres://kpler:kpler@db:5432/kpler
ENV DEBUG=false