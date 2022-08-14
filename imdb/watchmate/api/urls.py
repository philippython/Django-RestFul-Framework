from django.urls import path
from watchmate.api.views import movie_list, movie_details

urlpatterns = [
        path('list/', movie_list, name='movie_list'),
        path('details/<int:pk>/', movie_details, name='single_movie')
]