from django.urls import path
from .views import HomeView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/home', permanent=False), name='home'),
    path('home', HomeView.as_view(), name='home'),
]
