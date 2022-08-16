from .serializers import WatchListSerializers, StreamPlatformSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from watchmate.models import WatchList, StreamPlatform


class WatchListView(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializers(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailsView(APIView):
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

    def get(self, request):
        stream_platforms = StreamPlatform.objects.all(many=True)
        serializer = StreamPlatformSerializers(stream_platforms)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)  
        return Response(serializer.error, status=400)     

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