from django.shortcuts import render, get_object_or_404
from .models import Movie
from cinema.models import Hall, Cinema


def movies_list(request):
    movies = Movie.objects.all()
    comedy_movies = Movie.objects.filter(genre='کمدی')[:3]
    best_movies = movies.order_by('-rating')[:3]
    box_office = movies.order_by('-ticket_office')[:5]
    return render(request, 'home.html', {'movies': movies, 'best_movies': best_movies, 'box_office': box_office, 'comedy_movies': comedy_movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    # Fetch halls showing the movie
    halls = Hall.objects.filter(movie=movie).select_related('cinema')

    # Fetch related cinemas
    related_cinemas = Cinema.objects.filter(halls__in=halls).distinct().order_by('-rating')

    # Organize halls by cinema
    cinema_halls = {}
    for hall in halls:
        if hall.cinema_id not in cinema_halls:
            cinema_halls[hall.cinema_id] = []
        cinema_halls[hall.cinema_id].append(hall)

    similar_movies = Movie.objects.filter(genre=movie.genre).exclude(pk=movie_id).order_by('-rating')[:5]

    return render(request, 'Movie_Detail_tmp.html', {
        'similar_movies': similar_movies,
        'movie': movie,
        'related_cinemas': related_cinemas,
        'cinema_halls': cinema_halls
    })

