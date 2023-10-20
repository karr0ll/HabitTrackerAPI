FROM python:3.11 AS builder

# для корректного вывода логов
ENV PYTHONUNBUFFERED 1

# для удаления из образа runtime кэша
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./requirements.txt ${APP_HOME}/

RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP_HOME}/



