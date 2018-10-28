from django.urls import path

from .views import health, trip

urlpatterns = [
    path('/health', health, name='health'),
    path('/trip', trip, name='trip')
]