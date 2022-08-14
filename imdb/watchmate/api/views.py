from .serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchmate.models import Movie

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    all_movies = MovieSerializers(movies)
    print(id(all_movies))
    return Response(all_movies.data)


@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_exact = MovieSerializers(movie)
    return Response(movie_exact.data)