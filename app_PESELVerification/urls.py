from django.urls import path
from .views import verify_pesel_view

urlpatterns = [
    path('verification', verify_pesel_view, name='PESEL verification'),
]