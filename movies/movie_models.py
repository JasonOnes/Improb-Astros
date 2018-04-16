import datetime

from django.db import models
from django.utils import timezone

# -----------------------
# User-related Classes
# -----------------------


class User(models.Model):
    """ Defines a class for Users. """

    # user_id
    # username - CharField
    # email - CharField
    # password - CharField

    def __str__(self):
        return self.username


class Friendship(models.Model):
    """ Defines a friendship relationship between 2 users. """

    # friendship_id
    # user_id - FK
    # friend_id - FK (user ID)
    # is_mutual - Boolean - default is false, check before adding

    def __str__(self):
        return self.user.username, self.friend.username


class Review(models.Model):
    """ Defines a class for Review objects. """

    # review_id
    # movie_id - FK
    # user_id - FK
    # user_score - Int
    # review_text - TextField
    # pub_date - DateTime.now()

    def __str__(self):
        return (self.user.username, self.movie.title, self.user_score)

# ------------------------
# Movie-related Classes
# ------------------------


class Movie(models.Model):
    """ Defines a class for Movie objects. """

    # movie_id
    # title - CharField
    # release_year - Int
    # rated - ENUM? (G, PG, PG-13, R, NC-17, NR)
    # release_date - datetime
    # runtime - Int
    # production_co - CharField
    # plot_summary - TextField
    # poster_url - TextField
    # imdb_id - Int - can create a link to IMDB for each movie with this
    # imdb_rating - Float
    # rotten_tomatoes_rating - Int
    # metacritic_rating - Int

    def __str__(self):
        return (self.title, self.release_year)


class Genre(models.Model):
    """ Defines a class for Genre objects. """

    # genre_id
    # genre_name - CharField

    def __str__(self):
        return self.genre_name


class MovieGenre(models.Model):
    """ Defines an association table for movies with multiple genres. """

    # movie_genre_id
    # genre_id - FK
    # movie_id - FK

    def __str__(self):
        return (self.movie.title, self.genre.genre_name)


class CastCrewMember(models.Model):
    """ Defines a class of objects to represent a movie's cast/crew. """

    # cast_crew_id
    # name - CharField

    def __str__(self):
        return self.name


class MovieCast(models.Model):
    """ Defines an association table of cast and crew members on a particular movie. """

    # movie_cast_id
    # movie_id - FK
    # cast_crew_id - FK
    # role - ENUM? (ex, Director, Writer, Actor)

    def __str__(self):
        return (self.movie.title, self.cast_member.name)

# ----------------------------
# Movie Lists - save for V2?
# ----------------------------


class UserList(models.Model):
    """ Defines a class for a UserList object. """

    # user_list_id
    # user_id - FK
    # list_name - CharField

    def __str__(self):
        return self.name


class UserMovieList(models.Model):
    """ Association table for movies on a UserList. """

    # user_movie_list_id
    # user_list_id - FK
    # movie_id - FK

    def __str__(self):
        return (self.user_list.list_name, self.user.username)
