from django.db import models
from datetime import date

from django.contrib.auth.models import AbstractBaseUser# django default, since no custom user fields
from django.core.validators import MinValueValidator, MaxValueValidator


 # may notice no id key, not necessary with django auto pk set 

class User(AbstractBaseUser): # just named CustomUser for now
    # Let's see how the default behaves for now, based on our schema I don't see any custom fields
    first_name = None # for some anonymity, is_anonymous or AnonymousUser doesn't set id
    last_name = None # can change these later if desired (obvs)
    following = models.ManyToManyField("self", symmetrical=False) # self allows reference to same model 
    '''symmetrical keeps the relationship unilateral, we don't want that, Jane following Sue doesn't 
    automatically mean Sue is following Jane'''


    def __str__(self):
        return self.username

# TODO look into User Groups (models.Group) where we can set permissions
# Below doesn't work well https://stackoverflow.com/questions/41595364/fields-e304-reverse-accessor-clashes-in-django
# restructuring with Many-toMany
'''
class FollowPairs(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE) 
    followed_reviewer = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return "{} is following {}".format(self.follower, self.followed_reviewer)

'''

class Movie(models.Model):
    title = models.CharField(max_length=500)
    length = models.PositiveSmallIntegerField(default=0)
    genre = models.ForeignKey('MovieGenre',null=True, on_delete=models.SET_NULL) # not sure why a genre would be deleted but . . .
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
    reviewer = models.ForeignKey(User,null=True, on_delete=models.SET_NULL) # Keeps the reviews of people who are no longer users sets user to null
    # Is this what we want or do we want to delete the Review
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    last_reviewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} gives {} a {}.".format(self.reviewer, self.movie, self.rating)

class MovieGenre(models.Model):
    # TODO look into Enum classing/choices, match to omdb genres, but can't find complete list 
   
    movie_with_genre = models.ForeignKey(Movie, on_delete=models.CASCADE) # wonky column name but can't have it clash with movie
    genre = models.CharField(max_length=50)

    def __str__(self):
        return "{} is a(n) {} movie.".format(self.movie_with_genre, self.genre)





# from django.db import models
# from datetime import date

# from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import UserManager  # django default manager, since no custom user fields
# from django.core.validators import MinValueValidator, MaxValueValidator

# class User(models.Model):
#     # id
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     # TODO look inManyToManyField
#     followed_users = ArrayField(models.IntegerField(), blank=True, null=True)#blank allows form fields to be left empty
#     friends_list = ArrayField(models.IntegerField(), blank=True, null=True)
#     movies_wanting_to_see = ArrayField(models.IntegerField(), blank=True,  null=True)

#     def __str__(self):
#         return self.name

#     def getMoviesReviewed():
#         pass


# class Movie(models.Model):
#     #all movies (?) will be populated through api, not manually entered with form
#     MOVIE_CATEGORIES = (
#         ('C', 'Comedy'),
#         ('D', 'Documentary'),
#         ('H', 'Horror'),
#         ('RC', 'Romantic Comedy'),
#         ('SF', 'Sci-Fi'),
#         ('D', 'Drama'),
#         ('Cl', 'Classic'),
#         ('CC', 'Cult Classic'),
#     )

#     added = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=200)
#     year = models.PositiveSmallIntegerField(null=True)
#     length = models.CharField(max_length=20, default="90 min")
#     #genre = models.CharField(choices=MOVIE_CATEGORIES, max_length=2, default='D')
#     rated = models.CharField(max_length=10, null=True)
#     rotten_tomatoes_score = models.PositiveSmallIntegerField(null=True)  # TODO max=100)
#     imdb_score = models.PositiveSmallIntegerField(default=0, null=True)
#     imdb_url = models.URLField(null=True)

#     def __str__(self):
#         return self.title

#     def getUsersAverageRating(self):
#         pass


# class Review(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
#     # different default methods have different meanings for textFields
#     # Nullable if no value db stored as Null, blank=True allows form fields to be blank, and default=""
#     comment = models.TextField(blank=True, default='', max_length=1000)
#     reviewed_on = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return "{} was given a {} by {}.".format(self.movie, self.rating, self.reviewer)

