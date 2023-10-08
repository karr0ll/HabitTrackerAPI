from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)
from rest_framework.permissions import IsAuthenticated

from config.pagination import ListPagination
from config.permissions import HabitUserPermissions
from habits.models import Habit
from habits.serializers import HabitSerializer


class PublicHabitListView(ListAPIView):
    """
    Контроллер отображения списка всех публичных привычек
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class UserHabitListView(ListAPIView):
    """
    Контроллер отображения списка всех привычек пользователя
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitCreateView(CreateAPIView):
    """Контроллер саздания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод создания привычки и ее привязки к создавшему пользователю"""
        user = self.request.user
        serializer.save(user=user)


class HabitUpdateView(UpdateAPIView):
    """Контроллер обновления привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, HabitUserPermissions]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDeleteView(DestroyAPIView):
    """Контроллер удаления привычки"""
    permission_classes = [IsAuthenticated, HabitUserPermissions]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
