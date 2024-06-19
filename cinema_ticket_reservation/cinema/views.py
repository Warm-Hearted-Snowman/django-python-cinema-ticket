from django.shortcuts import render
from .models import Cinema
from movie.models import Movie


# Create your views here.

def cinemas_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas_home.html', {'cinemas': cinemas})


def cinema_detail(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    movies = Movie.objects.filter(hall__cinema=cinema).distinct()
    return render(request, 'cinema_detail.html', {'cinema': cinema, 'movies': movies})
