from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
            'tg_chat_id'
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    """Контроллер регистрации пользователя"""
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all()
            )
        ]
    )
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        try:
            first_name = validated_data['first_name']
        except KeyError:
            first_name = None
        try:
            last_name = validated_data['last_name']
        except KeyError:
            last_name = None

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'password',
            'first_name',
            'last_name',
        )
