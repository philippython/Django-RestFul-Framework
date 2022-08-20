from django.urls import path
from rest_framework.routers import DefaultRouter
from watchmate.api.views import ( WatchListView, WatchDetailsView,
                                  StreamPlatformListView,StreamPlatformDetailView,
                                  ReviewList, ReviewDetail, ReviewCreate)
# from watchmate.api.views import movie_list, movie_details
router = DefaultRouter()
# router.register('stream', StreamPlatform)
urlpatterns = [
        path('watchlist/', WatchListView.as_view(), name='watchlist'),
        path('watchdetails/<int:pk>/', WatchDetailsView.as_view(), name='single_watchlist'),
        path('streamplatform/list', StreamPlatformListView.as_view(), name='streamplatform_list'),
        path('streamplatform/details/<int:pk>',StreamPlatformDetailView.as_view(), name='single_streamplatform'),
        path('watchlist/<int:pk>/reviews', ReviewList.as_view(), name='review_list'),
        path('watchlist/<int:pk>/review-create', ReviewCreate.as_view(), name='create_review'),
        path('watchlist/detail-review/<int:pk>', ReviewDetail.as_view(), name='review_detail')
]
