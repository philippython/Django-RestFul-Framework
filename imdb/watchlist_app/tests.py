from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse

class RegistrationTest(APITestCase):

    """test registration route"""

    def test_register_user(self):

        url = reverse('register')
        data = {
                "username": "testcase",
                "email": "testcase@example.com",
                "password": "NewPassword@123",
                "password2": "NewPassword@123"
                }

        response = self.client.post(url, data,'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, "testcase")
        self.assertEqual(User.objects.count(), 1)
        

class LoginLogoutTest(APITestCase):

    """tests Login and Logout"""
    def setup(self):
        data = {
                "email": "testcase",
                "password": "NewPassword@123",
                }
