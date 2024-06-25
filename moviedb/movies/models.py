from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

