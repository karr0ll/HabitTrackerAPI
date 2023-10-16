FROM python:3.11 AS builder

# для корректного вывода логов
ENV PYTHONUNBUFFERED 1

# для удаления из образа runtime кэша
ENV PYTHONDONTWRITEBYTECODE 1
ARG APP_HOME=/app

WORKDIR ${APP_HOME}

RUN pip install poetry==1.6.1

COPY ./poetry.lock ./pyproject.toml ${APP_HOME}/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

EXPOSE 8000

COPY . ${APP_HOME}/



