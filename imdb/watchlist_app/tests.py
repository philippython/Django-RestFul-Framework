from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    """test registration route"""

    def test_register_user(self):

        url = reverse('register')
