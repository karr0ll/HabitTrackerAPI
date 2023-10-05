from rest_framework import serializers

from config.validators import (
    RelatedHabitAndRewardValidator,
    CompletionTimeValidator,
    NiceHabitValidator,
    HabitPeriodicityValidator, RewardAndRelatedHabitValidator
)
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit

        fields = (
            'pk',
            'user',
            'place',
            'time',
            'action',
            'nice_habit',
            'habit_related_to',
            'periodicity_in_days',
            'reward',
            'completion_time_in_minutes',
            'is_public',
        )

        validators = [
            RelatedHabitAndRewardValidator(
                fields=[
                    'habit_related_to',
                    'reward'
                ]
            ),
            CompletionTimeValidator(
                field='completion_time_in_minutes'
            ),
            NiceHabitValidator(
                fields=[
                    'nice_habit',
                    'habit_related_to',
                    'reward'
                ]
            ),
            RewardAndRelatedHabitValidator(
                fields=[
                    'nice_habit',
                    'habit_related_to',
                    'reward'
                ]
            ),
            HabitPeriodicityValidator(
                field='periodicity_in_days'
            )
        ]
