from turtle import title
from urllib import response
from watchmate.models import StreamPlatform, Review, WatchList
from watchmate.api.serializers import StreamPlatformSerializers, WatchListSerializers, Reviewserializers
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse



# Create your tests here.
class StreamPlatformTestCase(APITestCase):

  """Tests StreamPlatform"""

  def setUp(self):
      self.user = User.objects.create_user(username="testcase1", password="testcase@123")

      self.token_key = Token.objects.get(user__username="testcase1").key
      self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
      self.stream = StreamPlatform.objects.create(name="TestPlatform", about="A testing streaming platform", website= "www.testplatform.com") 

  def test_streamplatform_create(self):

      data = {
        "name": "TestPlatform",
        "about" : "A testing streaming platform",
        "website": "www.testplatform.com"
      }
      response = self.client.post(reverse('streamplatform_list'), data, "json")
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_streamplatform_list(self):
      response = self.client.get(reverse('streamplatform_list'))
      self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_streamplatform_ind(self):
      response = self.client.get(reverse('single_streamplatform', kwargs={"pk": self.stream.id}))
      self.assertEqual(response.status_code, status.HTTP_200_OK)

class watchListTestCase(APITestCase):
	
	"""test watchlist route """
	def setUp(self):
		self.user = User.objects.create_user(username="testcase1", password="testcase@123")
		self.stream = StreamPlatform.objects.create(name="TestPlatform", about="A testing streaming platform", website= "www.testplatform.com") 

		self.token_key = Token.objects.get(user__username="testcase1").key
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
		self.watchlist = WatchList.objects.create(title="Iwaju and Gwaju", description="A futuridtic lagos movie by Disney",
											      active=False, stream_platform=self.stream)
	def test_watchlist_create(self):
			data = {
					"title":"Iwaju and Gwaju", 
					"description" : "A futuridtic lagos movie by Disney",
					"active":False,
					"stream_platform": StreamPlatform.objects.get(id=1)
					}
			response = self.client.post(reverse('watchlist'), data)
			self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_watchlist_list(self):
			response = self.client.get(reverse('watchlist'))
			self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_watchlist_ind(self):
			response = self.client.get(reverse('single_watchlist', kwargs={"pk": self.watchlist.id}))
			self.assertEqual(response.status_code, status.HTTP_200_OK)
			self.assertEqual(WatchList.objects.get().title, 'Iwaju and Gwaju')
			self.assertEqual(WatchList.objects.count(), 1)

class ReviewTestCase(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="testcase1", password="testcase@123")

		self.token_key = Token.objects.get(user__username="testcase1").key
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
		self.stream = StreamPlatform.objects.create(name="TestPlatform", about="A testing streaming platform", website= "www.testplatform.com") 
		self.watchlist = WatchList.objects.create(title="Iwaju and Gwaju", description="A futuristic lagos movie by Disney",
											      active=False, stream_platform=self.stream)
		self.review = Review.objects.create(username=self.user, rating=5.0, description="Amazing sci-fi movie", active=False, watchlist=self.watchlist)

	def test_review_create(self):
		data = {
			"username" : self.user,
			"rating" : 5.0,
			"description": "Amazing sci-fi movie-- Updated",
			"active": True,
			"watchlist": self.watchlist
		}

		response = self.client.post(reverse('create_review', kwargs={"pk": 1}), data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Review.objects.get().rating, 5)
		self.assertEqual(Review.objects.count(), 1)

		response = self.client.post(reverse('create_review', kwargs={"pk": 1}), data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_review_unauth(self):
		data = {
			"username" : self.user,
			"rating" : 5.0,
			"description": "Amazing sci-fi movie",
			"active": True,
			"watchlist": self.watchlist
		}

		self.client.force_authenticate(user=None)
		response = self.client.post(reverse('create_review', kwargs={"pk": 1}), data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_review_update(self):
		data = {
			"username" : self.user,
			"rating" : 4.0,
			"description": "Amazing sci-fi movie",
			"active": False,
			"watchlist": self.watchlist
		}

		response = self.client.put(reverse('review_detail', kwargs={"pk": 1}), data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

