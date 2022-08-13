from math import fabs
from django.shortcuts import render
import pkg_resources
from .models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies' : list(movies.values())
    }
    return JsonResponse(data)

def individual_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name' : movie.name,
        'description' : movie.description,
        'active' : movie.active
    }
    return JsonResponse(data)
