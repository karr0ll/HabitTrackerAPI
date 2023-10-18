from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class TestHabitCRUD(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test_user@test.tst',
            password='test_password'
        )
        self.client.force_authenticate(user=self.user)

        self.habit_data = Habit.objects.create(
            user=self.user,
            place='test_place',
            time='10:00:00',
            action='test_action',
            nice_habit='False',
            habit_related_to=None,
            periodicity_in_days=2,
            reward='test_reward',
            completion_time_in_minutes=2,
            is_public=False
        )

    def test_habit_create(self):
        habit_data = {
            'place': self.habit_data.place,
            'time': self.habit_data.time,
            'action': self.habit_data.action,
            'nice_habit': self.habit_data.nice_habit,
            'periodicity_in_days': self.habit_data.periodicity_in_days,
            'reward': self.habit_data.reward,
            'completion_time_in_minutes':
                self.habit_data.completion_time_in_minutes,
            'is_public': self.habit_data.is_public
        }
        response = self.client.post(
            path=reverse('habits:create'),
            data=habit_data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            {
                'place': 'test_place',
                'time': '10:00:00',
                'action': 'test_action',
                'nice_habit': 'False',
                'periodicity_in_days': 2,
                'reward': 'test_reward',
                'completion_time_in_minutes': 2,
                'is_public': False
            },
            habit_data
        )

    def test_habit_list(self):
        response = self.client.get(
            reverse('habit:list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 1)

    def test_habit_update(self):
        response = self.client.patch(
            reverse('habit:update', kwargs={'pk': self.habit_data.pk}),
            data={
                'place': 'new_test_place',
                'completion_time_in_minutes': 1,
                'periodicity_in_days': 3,
                'is_public': True
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], 'new_test_place')

    def test_lesson_destroy(self):
        response = self.client.delete(
            reverse('habit:delete', kwargs={'pk': self.habit_data.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
