from django.urls import path
from watchmate.api.views import WatchListView, WatchDetailsView, StreamPlatformListView, StreamPlatformDetailView
# from watchmate.api.views import movie_list, movie_details

urlpatterns = [
        path('watchlist/', WatchListView.as_view(), name='watchlist'),
        path('watchdetails/<int:pk>/', WatchDetailsView.as_view(), name='single_watchlist'),
        path('streamplatform/list', StreamPlatformListView.as_view(), name='streamplatform_list'),
        path('streamplatform/details/<int:pk>',StreamPlatformDetailView.as_view(), name='single_streamplatform' )
]