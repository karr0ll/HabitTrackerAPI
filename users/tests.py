from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class TestHabitCRUD(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = User.objects.create(
            email='test_user@test.tst',
            password='test_password'
        )

    def test_validate_non_unique_user_create(self):
        user_data = {
            'email': self.user_data.email,
            'password': self.user_data.password
        }
        response = self.client.post(
            path=reverse('users:register_user'),
            data=user_data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_validate_email(self):
        user_data = {
            'email': 'test_user2test.tst',
            'password': 'test_password2'
        }

        response = self.client.post(
            path=reverse('users:register_user'),
            data=user_data
        )
        self.assertEqual(
            response.json(),
            {'email': ['Enter a valid email address.']}
        )

    def test_user_create(self):
        user_data = {
            'email': 'test_user3@test.tst',
            'first_name': 'test_first_name',
            'password': 'test_password2'
        }
        response = self.client.post(
            path=reverse('users:register_user'),
            data=user_data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        user = User.objects.filter(email='test_user3@test.tst')
        for item in user:
            self.assertEqual(
                item.first_name,
                user_data['first_name']
            )
