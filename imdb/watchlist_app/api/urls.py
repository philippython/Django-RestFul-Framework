from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view

url_patterns = [
    path('login', obtain_auth_token, name='login'),
    path('register', registration_view, name='register')
]
