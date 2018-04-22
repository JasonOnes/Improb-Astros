from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import date
import re 

#from django.contrib.auth.models import EmailField
from .models import Movie, User


class UserModelTests(TestCase):

    def setUp(self):

        User.objects.create(name='Timmy', email='lkasjdflkasjdfljaslkdj')
        User.objects.create(name='Tracey', email='tracey@flowers.com')

    def test_email_not_valid_form(self):
        ''' checks to see if the match between email and a valid email form is None, ie no match'''
        user_1 = User.objects.get(name='Timmy')
        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', user_1.email)
        self.assertEqual(match, None, msg="Email not valid")
    
    def test_email_valid(self):
        ''' checks to see if there is a match between a valid email regex, ie match != None '''
        user_2 = User.objects.get(name='Tracey')
        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', user_2.email)
        #self.assertEqual(match, user_2.email, msg="Email
        self.assertNotEqual(match, None, 'there\'s and email match "somewhere" in the string')
        

class MovieModelTests(TestCase):

    def setUp(self):

        user = User.objects.create(
        name='Timmy',
        email='alskdjfalskdfjlaskdjf'
    )
    

        self.movie_X = Movie.objects.create(
            title="Police Academy IX",
            genre='C',
            rotten_tomatoes_score=4,
            imdb_score=3.1,

        )

        self.movie_Y = Movie.objects.create(
            title="Chung_King Express TEST",
            # seen_on="2014-06-16",
            # rating=16,
            genre='D',
            rotten_tomatoes_score=90,
            imdb_score=8.1,
            #imdb_url=www.imdb.com/title/tt0109424/?ref_=nv_sr_1,
        )

    # def test_movie_seen_on_date(self):
    #     ''' tests to see if movie isn't listed as being seen today'''
    #     movie = Movie.objects.get(title="Police Academy IX")
    #     today = date.today
    #     self.assertNotEqual(movie.seen_on, today)
    #
    # def test_movie_rating_between_1and10(self):
    #     ''' tests whether the rating is between 1 and 10, no need to check if int '''
    #     movie_with_good = Movie.objects.get(title="Police Academy IX")
    #     movie_with_bad = Movie.objects.get(title="Dumb")
    #     self.assertLessEqual(movie_with_good.rating, 10) and self.assertGreaterEqual(movie_with_good, 1)
    #     self.assertGreater(movie_with_bad.rating, 10, msg="Not a valid rating, too high")
    #
class ReviewModelTest(TestCase):
    pass

class MovieViewsTests(TestCase):

    def setUp(self):

        user = User.objects.create(name="Hula", email="hoop@hop.edu")
        self.movie = Movie.objects.create(
            title="Something Wicked",
            genre='H',
            rotten_tomatoes_score=88,
            imdb_score=5.6,

        )
        self.movie = Movie.objects.create(
            title="It",

            genre='H',

        )

    def test_movie_list_view(self):
        ''' checks various aspects of the movie_list view '''
        
        movie_X = Movie.objects.get(title="Something Wicked")
        movie_Y = Movie.objects.get(title="It")
        
        response = self.client.get(reverse('movies:all_movies'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(movie_X, response.context['movies'])
        self.assertIn(movie_Y, response.context['movies'])
        self.assertTemplateUsed(response, 'movies/movie_list.html')
        self.assertContains(response, self.movie.title)#test that the title is somewhere on page


    def test_movie_details_view(self):
        movie_X = Movie.objects.get(title="Something Wicked")
        response = self.client.get(reverse('movies:movie_detail', kwargs={'pk':movie_X.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.movie, response.context['movie'])
        pass
'''
    def test_movie_list_by_user_view(self):
        response = self.client.get(reverse('movies:movie_detail', kwargs={'user_pk':self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        pass

'''
class UserViewTests(TestCase):
    pass

class ReviewViewTests(TestCase):
    pass





