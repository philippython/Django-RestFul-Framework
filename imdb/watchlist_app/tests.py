from rest_framework.test import APITestCase
from rest_framework.response import Response
import rest_framework
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    """test registration route"""

    def test_register_user(self):

        url = reverse('register')

        self.assertEqual(url.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "hp")



if __name__ == '__main__':
    rest_framework.test.main()