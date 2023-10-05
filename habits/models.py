from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    place = models.TextField(verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    nice_habit = models.BooleanField(
        default=True,
        verbose_name='Приятная привычка'
    )
    habit_related_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        blank=True,
        null=True
    )
    periodicity_in_days = models.PositiveIntegerField(
        default=1,
        verbose_name='Периодичность в днях'
    )
    reward = models.CharField(
        max_length=255,
        verbose_name='Вознаграждение',
        blank=True,
        null=True
    )
    completion_time_in_minutes = models.PositiveIntegerField(
        verbose_name='Время на выполнение в минутах'
    )
    is_public = models.BooleanField(default=False, verbose_name='Публичность')

    def __str__(self):
        return (
            f'{self.pk}, '
            f'{self.place}, '
            f'{self.time}, '
            f'{self.action}'
        )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
