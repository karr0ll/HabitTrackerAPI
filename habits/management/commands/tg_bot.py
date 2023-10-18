import telebot
from django.conf import settings
from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Команда отправки напоминаний в telegram'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TG_TOKEN)

        @bot.message_handler(commands=["start"])
        def say_hello(message):
            bot.send_message(
                message.from_user.id,
                "Привет, это бот для напоминания об привычках.\n"
                "Отправьте свой email для запуска бота\n"

            )

        @bot.message_handler(
            regexp='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]'
                   '+@[A-Za-z0-9-]+'
                   '.[A-Z|a-z]{2,})+',
            content_types=['text']
        )
        def get_user_chat_id(message):
            received_email = message.text
            tg_chat_id = message.chat.id
            user_data = User.objects.filter(email=received_email)
            if user_data.exists():
                for item in user_data:
                    item.tg_chat_id = tg_chat_id
                    item.save()

                    bot.send_message(
                        message.from_user.id,
                        f'Ваш email: {message.text}\n'
                        f'Ваш id чата: {tg_chat_id}\n'
                        f'Ваш id в сервисе: {item.pk}'
                    )
            else:
                bot.send_message(
                    message.from_user.id,
                    f'Пользователь с email {message.text} не найден'
                )

        bot.infinity_polling()
