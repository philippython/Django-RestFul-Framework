from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from watchmate.models import Movie


class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = MovieSerializers(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
                serializer = MovieSerializers(movie, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            movie.delete()
            return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

"""
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
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