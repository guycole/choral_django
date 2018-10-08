from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    mb_id = models.CharField(max_length=64)

    def __repr__(self):
        return "%d %s %s" % (id, first_name, last_name)

    def __str__(self):
        return "%d %s %s" % (id, first_name, last_name)

class Album(models.Model):
    asin = models.CharField(max_length=32)
    disc_count = models.IntegerField()
    duration = models.IntegerField()
    file_name = models.CharField(max_length=64)
    format = models.CharField(max_length=16)
    genre = models.CharField(max_length=16)
    mb_id = models.CharField(max_length=64)
    note = models.CharField(max_length=128)
    release = models.DateField()
    track_count = models.IntegerField()
    title = models.CharField(max_length=128)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __repr__(self):
        return "%d %s" % (id, title)

    def __str__(self):
        return "%d %s" % (id, title)

class Track(models.Model):
    disc = models.CharField(max_length=64)
    duration = models.CharField(max_length=64)
    file_name = models.CharField(max_length=64)
    mb_id = models.CharField(max_length=64)
    note = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    track = models.CharField(max_length=64)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __repr__(self):
        return "%d %s" % (id, title)

    def __str__(self):
        return "%d %s" % (id, title)
