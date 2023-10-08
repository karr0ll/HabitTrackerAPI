from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from users.apps import UsersConfig

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="HabitTracker API Docs",
      default_version='v1',
      description="API methods documentation",
      license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

app_name = UsersConfig.name

urlpatterns = [
    path('api/v1/docs/swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0
    ), name='schema-swagger-ui'
         ),
    path('api/v1/docs/redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0
    ), name='schema-redoc'
         ),
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls', namespace='users')),
    path('api/v1/habit/', include('habits.urls', namespace='habit')),

]
