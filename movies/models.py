from django.db import models
from datetime import date 
from django.contrib.auth.models import UserManager # django default manager, since no custom user fields

class User(models.Model):
    name =  models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return self.name




class Movie(models.Model):
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

    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    seen_on = models.DateField(default=date.today)
    rating = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(choices=MOVIE_CATEGORIES, max_length=2, default='D')
    comments = models.TextField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE) #many to one, if user is deleted all movies attributed will also be removed

    def __str__(self):
        return self.title
    