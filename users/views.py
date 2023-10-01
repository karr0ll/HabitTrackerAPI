from rest_framework import generics

from users.models import User
from users.serializers import UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    """Generic контроллер для регистрации пользователя"""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
