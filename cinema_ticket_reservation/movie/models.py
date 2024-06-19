from django.db import models


# Create your models here.

class Movie(models.Model):
    Movie_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.FloatField()
    description = models.TextField()
    length = models.IntegerField()
    image = models.ImageField(upload_to="movies/images/", null=True, blank=True)
    banner = models.ImageField(upload_to="movies/banners/", null=True, blank=True)
    ticket_office = models.IntegerField()

    def __str__(self):
        return self.title
