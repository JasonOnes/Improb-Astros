from django.db import models
from datetime import date

from django.contrib.auth.models import User # django default, since no custom user fields
from django.core.validators import MinValueValidator, MaxValueValidator


 # may notice no id key, not necessary with django auto pk set 

class CustomUser(User):
    # Let's see how the default behaves for now, based on our schema I don't see any custom fields
    first_name = None # for some anonymity, is_anonymous or AnonymousUser doesn't set id
    last_name = None # can change these later if desired (obvs)

    def __str__(self):
        return self.username

# TODO look into User Groups (models.Group) where we can set permissions
class FollowPairs(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE) 
    followed_reviewer = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return "{} is following {}".format(self.follower, self.followed_reviewer)



class Movie(models.Model):
    title = models.CharField(max_length=500)
    length = models.PositiveSmallIntegerField(default=0)
    genre = models.ForeignKey('MovieGenre', on_delete=models.SET_NULL) # not sure why a genre would be deleted but . . .
    rated = models.CharField(max_length=10)
    rot_toms_score = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    imdb_score = models.PositiveSmallIntegerField(default=0, null=True)
    imdb_url = models.URLField(null=True)
    # null must be true for initial movie details, not in db no reviewers yet
    num_of_reviewers = models.PositiveIntegerField(null=True)
    user_ratings_average = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.title

    def get_num_of_reviewers(self):
        # try:
        #     num_reviews = Review.objects.filter(movie=self).all()
        # except NoneTypeError:

        # return num_reviews
        pass

    def update_movie_num_reviewers(self):
        new_number_of_reviewers = self.get_num_of_reviewers
        self.num_of_reviewers = new_number_of_reviewers
        pass
    
    def get_average_user_rating(self):
        # num = self.get_num_of_reviewers
        # # get list of all the ratings and add
        # reviews = Review.objects.filter(movie=self)
        # ratings_list = [rating for review.rating in reviews]

        # rating_sum = sum(ratings_list)
        # return rating_sum//num
        pass
        
    
    def update_user_ratings(self):
        new_rating = self.get_average_user_rating
        self.user_ratings_average = new_rating
        pass


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, default='')
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL) # Keeps the reviews of people who are no longer users sets user to null
    # Is this what we want or do we want to delete the Review
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    last_reviewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} gives {} a {}.".format(self.reviewer, self.movie, self.rating)

class MovieGenre(models.Model):
    # TODO look into Enum classing/choices, match to omdb genres, but can't find complete list 
   
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return "{} is a(n) {} movie.".format(self.movie, self.genre)