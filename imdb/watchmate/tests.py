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

		self.token_key = Token.objects.get(user__username="testcase1").key
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
		self.watchlist = WatchList.objects.create(title="Iwaju and Gwaju", description="A futuridtic lagos movie by Disney",
											      active=False, stream_platform=1)
		def test_watchlist_create(self):
			data = {
					"title":"Iwaju and Gwaju", 
					"description" : "A futuridtic lagos movie by Disney",
					"active":False,
					"stream_platform":1
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
	def setUP(self):
		self.user = User.objects.create_user(username="testcase1", password="testcase@123")

		self.token_key = Token.objects.get(user__username="testcase1").key
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
		self.stream = StreamPlatform.objects.create(name="TestPlatform", about="A testing streaming platform", website= "www.testplatform.com") 
		self.watchlist = WatchList.objects.create(title="Iwaju and Gwaju", description="A futuridtic lagos movie by Disney",
											      active=False, stream_platform=1)


	def 



















"""
class Property:
    def __init__(self) -> None:
        self.__name = "chris"
        self.__exp = None
        

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if exp > 100:
            raise ValueError("Exp too high!!")
        self.__exp = exp

    @exp.deleter
    def exp(self):
        del self.__exp

    def __str__(self) -> str:
        return self.__name

chris = Property()
chris.exp = 20
print(chris.exp)

# chris.set_name("diva")
# print(chris.get_name())

unordered_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]

def find_word(arr):    
    before = []
    after = []
    word = []

    # seperating last characters from first letters
    for i in arr:
        before.append(i[0])
        after.append(i[2])
    
    # getting first character in word
    for char in before:
        if char not in after:
            word.append(char)

    # commenting Code for better understanding
    for i  in range(0, len(arr) + 1):
        letter = word[i]
        nextLetter = ""
        newIndex = ""
        # getting next letter using index
        if letter in before:
            newIndex = before.index(letter)
            nextLetter = after[newIndex]
            word.append(nextLetter)
        
    return "".join(word)

print(find_word(unordered_list))
print(find_word(["P>E","E>R","R>U"]))
print(find_word(["I>N","A>I","P>A","S>P"]))
print(find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))
print(find_word(["I>F", "W>I", "S>W", "F>T"]))

function find_word(arr) {
  let before = []
  let after = []
  let word = []

  //get all the before and after
  for (let i of arr) {
    before.push(i[0])
    after.push(i[2])
  }

  //find first word
  let firstLetter;
  let i = 0;

  while (i < before.length) {
    if (!after.includes(before[i])) {
      firstLetter = before[i]
      word.push(firstLetter)
    }
    i++
  }

  //get other letters
  for (let i = 0; i < arr.length; i++) {
    let letter = word[i]
    let nextLetter;
    let newIndex;
    if (before.includes(letter)) {
      newIndex = before.indexOf(letter)
      nextLetter = after[newIndex]
      word.push(nextLetter)
    }
  }

  return word.join("")
}

print(find_word(["I>E", "M>I", "A>M", "D>A", "E>N"]));
print(find_word(["P>E","E>R","R>U"]));
console.log(find_word(["I>N","A>I","P>A","S>P"]));
console.log(find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]));
console.log(find_word(["I>F", "W>I", "S>W", "F>T"]));
"""