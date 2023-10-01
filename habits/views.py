from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)
from rest_framework.permissions import IsAuthenticated

from config.pagination import ListPagination
from habits.models import Habit
from habits.serializers import HabitSerializer


class PublicHabitListView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class UserHabitListView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitCreateView(CreateAPIView):
    """Контроллер саздания урока"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод создания урока и его привязки к создавшему пользователю"""
        user = self.request.user
        serializer.save(user=user)


class HabitUpdateView(UpdateAPIView):
    """Контроллер обновления урока"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteView(DestroyAPIView):
    """Контроллер обновления урока"""
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
