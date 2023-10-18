from rest_framework.serializers import ValidationError


class RelatedHabitAndRewardValidator:
    """
    Исключает одновременный выбор связанной привычки и указания вознаграждения
    """

    def __init__(self, fields):
        self.habit_related_to = fields[0]
        self.reward = fields[1]

    def __call__(self, request_data):
        if all(
                [
                    (self.habit_related_to in request_data.keys()),
                    (self.reward in request_data.keys())
                ]
        ):
            raise ValidationError(
                "Можно указать либо связанную привычку, либо награду"
            )


class CompletionTimeValidator:
    """
    Исключает указание времени выполнения привычки > 2 минут
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, request_data):
        completion_time: str = dict(request_data).get(self.field)
        if int(completion_time) > 2:
            raise ValidationError(
                "Время выполнения не может быть больше 2х минут"
            )


class NiceHabitValidator:
    """
    Проверяет попадние в связанные привычки
    только привычек с признаком приятной привычки.
    """
    def __init__(self, fields):
        self.nice_habit = fields[0]
        self.habit_related_to = fields[1]
        self.reward = fields[2]

    def __call__(self, request_data):
        request_data_dict: dict = dict(request_data)
        try:
            related_habit = request_data_dict['habit_related_to']

            if related_habit.nice_habit is False:
                raise ValidationError(
                        'В связанные привычки могут попадать '
                        'только привычки с признаком приятной привычки.'
                )
        except KeyError:
            pass


class RewardAndRelatedHabitValidator(NiceHabitValidator):
    """
    Проверяет наличие вознаграждения или
    связанной привычки у приятной привычки.
    """
    def __init__(self, fields):
        super().__init__(fields)

    def __call__(self, request_data):
        request_data_dict: dict = dict(request_data)
        try:
            if request_data_dict[self.nice_habit] is True:
                if (
                        request_data_dict[self.reward] is not None
                        or request_data_dict[
                            self.habit_related_to
                        ] is not None
                ):
                    raise ValidationError(
                        'У приятной привычки не может быть '
                        'вознаграждения или связанной привычки.'
                    )
        except KeyError:
            pass


class HabitPeriodicityValidator:
    """
    Проверяет периодичность выполнения привычки не реже раза в 7 дней
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, request_data):
        periodicity_in_days: str = dict(request_data).get(self.field)
        if int(periodicity_in_days) > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )
