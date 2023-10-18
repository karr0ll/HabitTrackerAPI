from datetime import datetime

import telebot
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_notification():
    bot = telebot.TeleBot(settings.TG_TOKEN)
    current_time_str = f'{datetime.now().time(): %H:%M}'
    habits = Habit.objects.all()

    for item in habits:
        habit_time_str = f'{item.time: %H:%M}'
        if habit_time_str == current_time_str:
            if not item.reward:
                message_text = (
                    f'Напоминание: '
                    f'{item.action}.\n'
                    f'Вознаграждение {item.reward}'
                )
            else:
                message_text = (
                    f'Напоминание: {item.action}.\n'
                    f'После этого надо сделать: '
                    f'{item.habit_related_to.action}'
                                )
            try:
                bot.send_message(
                    chat_id=item.user.tg_chat_id,
                    text=message_text
                )
            except telebot.apihelper.ApiTelegramException:
                print('у пользователя нет tg_chat_id')
                pass
