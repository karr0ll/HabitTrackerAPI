from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateView,
    HabitUpdateView,
    HabitDeleteView,
    UserHabitListView,
    PublicHabitListView
)

app_name = HabitsConfig.name

urlpatterns = [
    path('public/list/', PublicHabitListView.as_view(), name='habit_list'),
    path('list/', UserHabitListView.as_view(), name='habit_list'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_delete'),
]
