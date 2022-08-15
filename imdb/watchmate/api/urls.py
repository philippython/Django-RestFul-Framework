from django.urls import path
from watchmate.api.views import MovieListView, MovieDetailsView
# from watchmate.api.views import movie_list, movie_details

urlpatterns = [
        path('list/', MovieListView.as_view(), name='movie_list'),
        path('details/<int:pk>/', MovieDetailsView.as_view(), name='single_movie')
]