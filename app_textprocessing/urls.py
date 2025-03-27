from django.urls import path
from .views import upload_text_view

urlpatterns = [
    path('textprocessing', upload_text_view, name='Text Processing'),
]