from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin,
                                   DestroyModelMixin)
from .serializers import (WatchListSerializers, StreamPlatformSerializers,
                          Reviewserializers)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from watchmate.models import WatchList, StreamPlatform, Review
from watchmate.api.permission import AdminOrReadOnly, ReviewUserOrReadOnly
from watchmate.api.throttling import ReviewCreateThrottle, ReviewListThrottle
from watchmate.api.pagination import ViewPaginator, WatchListPaginatorLO

class UserReviewList(ListAPIView):
    serializer_class = Reviewserializers
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(username__username=username)


class ReviewList(ListAPIView):
    serializer_class = Reviewserializers
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    pagination_class = ViewPaginator
    filterset_fields = ['active', 'username__username']

    def get_queryset(self):
        pk = self.kwargs['pk']
        review = Review.objects.filter(watchlist=pk)
        return review

class ReviewCreate(CreateAPIView):
    serializer_class = Reviewserializers
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]


    def perform_create(self, serializer):
        watchlist = WatchList.objects.get(pk=self.kwargs['pk'])

        review_queryset = Review.objects.filter(watchlist=watchlist, username=self.request.user)

        if review_queryset.exists():
            raise ValidationError({'error': 'you already added a review for this movie'})

        if watchlist.total_rating > 1 :
            watchlist.avg_rating = (watchlist.total_rating + serializer.validated_data['rating']) / watchlist.total_rating
        else:
            watchlist.avg_rating = serializer.validated_data['rating']

        watchlist.total_rating += 1

        watchlist.save()

        serializer.save(watchlist=watchlist, username=self.request.user)

class ReviewDetail(RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = Reviewserializers
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = [ReviewUserOrReadOnly]


class WatchListView(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializers
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    pagination_class = WatchListPaginatorLO


class WatchDetailsView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = WatchListSerializers(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        try:    
            movie = WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
                serializer = WatchListSerializers(movie, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            movie.delete()
            return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

class StreamPlatformListView(APIView):
    permission_classes = [AdminOrReadOnly]
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(stream_platforms, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class StreamPlatformDetailView(APIView):

    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream Platform does not exist'}, status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = StreamPlatformSerializers(stream_platform)
            return Response(serializer.data, status=200)

    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.error, status=400)

    def delete(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Response({'error': 'Stream Platform does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            stream_platform.delete()
            return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)







"""
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = WatchListSerializers(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)
"""
