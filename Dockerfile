FROM python:3.11 AS builder

# для корректного вывода логов
ENV PYTHONDONTWRITEBYCODE 1

# для удаления из образа runtime кэша
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./poetry.lock ./pyproject.toml ${APP_HOME}/

RUN pip install poetry==1.6.1
RUN poetry install --no-root

EXPOSE 8000

COPY . ${APP_HOME}/



