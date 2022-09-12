from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse

class RegistrationTestCase(APITestCase):

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
        

class LoginLogoutTestCase(APITestCase):

    """tests Login and Logout"""
    def setUp(self):

        self.user = User.objects.create_user(username="testcase", password ="NewPassword@123",)
       

    def test_login_user(self):
        data = {
                "username": "testcase",
                "password": "NewPassword@123",
                }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_user(self):

        self.token_key = Token.objects.get(user__username="testcase").key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

