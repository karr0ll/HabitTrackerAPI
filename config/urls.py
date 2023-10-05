from django.contrib import admin
from django.urls import path, include

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls', namespace='users')),
    path('api/v1/habit/', include('habits.urls', namespace='habit')),

]
