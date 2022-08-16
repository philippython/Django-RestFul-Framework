from django.urls import path
from watchmate.api.views import WatchListView, WatchDetailsView, StreamPlatformListView
# from watchmate.api.views import movie_list, movie_details

urlpatterns = [
        path('watchlist/', WatchListView.as_view(), name='movie_list'),
        path('watchdetails/<int:pk>/', WatchDetailsView.as_view(), name='single_watchlist'),
        path('streamplatform/list', StreamPlatformListView.as_view(), name='streamplatform_list'),
        path('streamplatform/details/<int:pk>', )
]