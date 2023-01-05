"""Url patterns for blog."""

from django.urls import path

from blog.views import *
from users.views import messages, delete_msg, new_message

app_name = 'blog'


urlpatterns = [
    # Inicio
    path('', inicio, name='Inicio'),
    # Posts
    path('pages/', posts, name='Posts'),
    path('pages/new_post/', agregar_post, name='NewPost'),
    path('pages/delete_post/<int:pk>', DeletePost.as_view(), name='DeletePost'),
    path('pages/edit_post/<post_id>/', edit_post, name='EditPost'),
    path('pages/<post_id>/', post_detail, name='PostDetail'),
    # About
    path('about/', about, name='About'),
    # Messages
    path('messages/', messages, name='Messages'),
    path('messages/delete/<msg_id>/', delete_msg, name='DeleteMsg'),
    path('messages/new_msg/', new_message, name='NewMsg'),
]