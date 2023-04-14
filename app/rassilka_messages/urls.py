from django.urls import path
from .views import send_message, writer

urlpatterns = [
    path('', send_message),
    path('', writer)
]