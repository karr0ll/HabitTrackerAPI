# HabitTrackerAPI

Маленький API для приложения - трекера полезных привычек.  
Поддерживает отправку уведомлений через telegram(pytelegrambotapi 4.14.0) и работу с периодическими задачами(redis 5.0.1).

****

>#### Документация: 
>
>#### Swagger:  
>api/v1/docs/swagger/  
>
>#### Redoc:
>api/v1/docs/redoc/

Библиотеки, используемые в проекте:
>python 3.11  
>django 4.2.5  
>django-rest-framework 0.1.0  
>psycopg2 2.9.7  
>python-dotenv 1.0.0  
>django-filter 23.3  
>djangorestframework-simplejwt 5.3.0  
>drf-yasg 1.21.7  
>django-celery-beat 2.5.0  
>celery 5.3.4  
>django-cors-headers 4.2.0  
>pytelegrambotapi 4.14.0  
>redis 5.0.1  

### Установка:
1. Установите зависимости проекта
>  poetry install

2. Добавьте переменные окружения, описанные в файле .env_sample в файл .env, созданный в корневой директории вашего проекта
3. Создайте миграции
> python3 manage.py migrate 
4. Запустите телеграм-бота командой
> python3 manage.py tg_bot
5. Запустите Celery worker
> celery -A config  worker -l info
6. Запустите Celery beat
> celery beat python -m celery -A config beat -l info



### Создание Docker-образа приложения: 
1. Скачайте Docker по инструкции из документации:
https://docs.docker.com/desktop/

2. Клонируйте Dockerfile
3. В терминале выполните команду 
>docker build -t habit_tracker_app .

### Запуск контейнера:  

Выполните команды в терминале:

1. Сборка образа
>docker-compose build

2. Запуск контейнеров
>docker-compose up

3. Применение миграций
>docker-compose exec app python manage.py migrate





