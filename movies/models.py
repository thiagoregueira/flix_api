from django.db import models

from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.release_date.year})'
