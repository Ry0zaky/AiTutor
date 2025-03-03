from django.urls import path
from .views import ask_ai  # Import the placeholder view

urlpatterns = [
    path('ask-ai/', ask_ai, name='ask_ai'),
]
