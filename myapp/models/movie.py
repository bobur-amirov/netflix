from django.db import models
from .actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    imdb = models.FloatField()
    genre = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actor, related_name='actors')

    def __str__(self):
        return self.name
