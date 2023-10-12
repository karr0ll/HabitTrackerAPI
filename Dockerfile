FROM python:3.11 AS builder

# для корректного вывода логов
ENV PYTHONDONTWRITEBYCODE 1

# для удаления из образа runtime кэша
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.6.1
RUN poetry install

COPY . .


