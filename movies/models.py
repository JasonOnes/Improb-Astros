from django.db import models
from datetime import date 

MOVIE_CATEGORIES = (
    ('C', 'Comedy'),
    ('D', 'Documentary'),
    ('H', 'Horror'),
    ('RC', 'Romantic Comedy'),
    ('SF', 'Sci-Fi'),
    ('D', 'Drama'),
    ('Cl', 'Classic'),
    ('CC', 'Cult Classic'),

)
class Movie(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    seen_on = models.DateField(default=date.today)
    rating = models.PositiveSmallIntegerField()
    category = models.CharField(choices=MOVIE_CATEGORIES, max_length=2, default='D')
    comments = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.title
        