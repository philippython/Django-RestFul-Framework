from http import client
from rest_framework.test import APITestCase
import rest_framework
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    """test registration route"""

    def test_register_user(self):

        url = reverse('register')
        data = {"name": "philip"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, "philip")



if __name__ == '__main__':
    rest_framework.test.main()