from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchmate.models import Movie

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
