from django.urls import path
from . import views
from .views import get_context_data

urlpatterns = [
    path('', get_context_data )

]