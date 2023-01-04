"""Url patterns for blog."""

from django.urls import path

from blog.views import *
from users.views import messages, delete_msg, new_message

app_name = 'blogapp'


urlpatterns = [
    # Inicio
    path('', inicio, name='Inicio'),
  
]