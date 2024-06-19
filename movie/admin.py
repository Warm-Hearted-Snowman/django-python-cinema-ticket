from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'rating')
