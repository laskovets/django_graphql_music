from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Album(models.Model):
    name = models.CharField(max_length=100, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    downloaded = models.BooleanField(null=False, default=False)


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    tags = ArrayField(
        models.CharField(max_length=100, null=False)
    )
    listeners = models.IntegerField(null=False, default=0)
    play_counts = models.IntegerField(null=False, default=0)

    class Meta:
        unique_together = ('name', 'artist')
