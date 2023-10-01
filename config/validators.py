from rest_framework.serializers import ValidationError


class RelatedHabitAndRewardValidator:

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

    def __init__(self, field):
        self.field = field

    def __call__(self, request_data):
        completion_time: str = dict(request_data).get(self.field)
        if int(completion_time) > 2:
            raise ValidationError("Время выполнения не может быть больше 2х минут")


class NiceHabitValidator:
    def __init__(self, fields):
        self.nice_habit = fields[0]
        self.habit_related_to = fields[1]
        self.reward = fields[2]

    def __call__(self, request_data):
        request_data_dict: dict = dict(request_data)
        try:
            if all(
                    [
                        (request_data_dict[self.nice_habit] is False),
                        (request_data_dict[self.habit_related_to] is not None)
                    ]
            ):
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки.')

            if request_data_dict[self.nice_habit] is True:
                if all(
                        [
                            (request_data_dict[self.reward] is not None),
                            (request_data_dict[self.habit_related_to] is not None)
                        ]
                ):
                    raise ValidationError(
                        'У приятной привычки не может быть вознаграждения или связанной привычки.'
                    )
        except KeyError:
            pass


class HabitPeriodicityValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, request_data):
        periodicity_in_days: str = dict(request_data).get(self.field)
        if int(periodicity_in_days) > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
