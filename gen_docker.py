"""Generate Dockerfile, docker-compose, run scripts."""
from helpers import put

def generate_docker(report, root, A, T):
    put(root, "Dockerfile", DOCKERFILE.replace("__A__", A).replace("__P__", "portalproj"))
    put(root, "docker-compose.yml", COMPOSE.replace("__T__", T.lower().replace(" ", "-")))
    put(root, "run.sh", RUNSH.replace("__P__", "portalproj").replace("__A__", A))
    put(root, "run.bat", RUNBAT.replace("__P__", "portalproj").replace("__A__", A))
    put(root, "gunicorn.conf.py", GUNICORN)
    put(root, ".env.example", ENV.replace("__T__", T))
    put(root, "Makefile", MAKEFILE)
    print("  Docker: Dockerfile, docker-compose, run scripts, Makefile")

DOCKERFILE = """FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p logs staticfiles media
RUN python manage.py collectstatic --noinput 2>/dev/null || true
EXPOSE 8000
CMD ["gunicorn", "__P__.wsgi:application", "-c", "gunicorn.conf.py"]
"""

COMPOSE = """version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./db.sqlite3:/app/db.sqlite3
      - ./logs:/app/logs
      - ./media:/app/media
      - ./staticfiles:/app/staticfiles
    env_file:
      - .env
    command: gunicorn __P__.wsgi:application -c gunicorn.conf.py
    restart: unless-stopped
"""

RUNSH = """#!/bin/bash
set -e
echo "=== __P__ Portal ==="
pip install -r requirements.txt
python manage.py makemigrations __A__
python manage.py migrate
python manage.py collectstatic --noinput 2>/dev/null
if [ ! -f db.sqlite3 ]; then
  echo "Create superuser:"
  python manage.py createsuperuser
fi
echo "Starting server at http://0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000
"""

RUNBAT = """@echo off
echo === __P__ Portal ===
pip install -r requirements.txt
python manage.py makemigrations __A__
python manage.py migrate
python manage.py collectstatic --noinput 2>nul
if not exist db.sqlite3 (
  echo Create superuser:
  python manage.py createsuperuser
)
echo Starting server at http://0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
"""

GUNICORN = """bind = "0.0.0.0:8000"
workers = 4
worker_class = "sync"
worker_timeout = 120
max_requests = 1000
max_requests_jitter = 50
accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"
"""

ENV = """SECRET_KEY=change-this-in-production
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
"""

MAKEFILE = """.PHONY: setup migrate run test lint docker

setup:
\tpip install -r requirements.txt

migrate:
\tpython manage.py makemigrations __A__
\tpython manage.py migrate

createsuperuser:
\tpython manage.py createsuperuser

run:
\tpython manage.py runserver 0.0.0.0:8000

test:
\tpython manage.py test

lint:
\tpython -m py_compile __P__/settings.py __P__/urls.py __A__/models.py __A__/views.py __A__/api.py

docker:
\tdocker compose up --build

docker-down:
\tdocker compose down

clean:
\trm -rf __pycache__ */__pycache__ */*/__pycache__ logs/*.log
"""
