from django.db import models
from datetime import date

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import UserManager  # django default manager, since no custom user fields


class User(models.Model):
    # id
    name = models.CharField(max_length=200)
    email = models.EmailField()
    # TODO look inManyToManyField
    followed_users = ArrayField(models.IntegerField(), null=True)
    friends_list = ArrayField(models.IntegerField(), null=True)
    movies_wanting_to_see = ArrayField(models.IntegerField(), null=True)

    def __str__(self):
        return self.name

    def getMoviesReviewed():
        pass


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
    genre = models.CharField(choices=MOVIE_CATEGORIES, max_length=2, default='D')

    rotten_tomatoes_score = models.PositiveSmallIntegerField(null=True)  # TODO max=100)
    imdb_score = models.PositiveSmallIntegerField(default=0, null=True)
    imdb_url = models.URLField(null=True)

    def __str__(self):
        return self.title

    def getUsersAverageRating(self):
        pass


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    # different default methods have different meanings for textFields
    # Nullable if no value db stored as Null, blank=True allows form fields to be blank, and default=""
    comment = models.TextField(blank=True, default='', max_length=1000)
    reviewed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} was given a {} by {}.".format(self.movie, self.rating, self.reviewer)
