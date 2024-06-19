from django.urls import path
from .views import movies_list, movie_detail

app_name = 'movie'

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movies/', movies_list, name='movies_list'),
    path('detail/<int:movie_id>/', movie_detail, name='movie_detail'),
]
