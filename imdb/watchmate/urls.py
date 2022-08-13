from django.urls import path
from .views import movie_list, individual_movie

urlpatterns = [
        path('list/', movie_list, name='movie_list'),
        path('details/<int:pk>/', individual_movie, name='single_movie')
]