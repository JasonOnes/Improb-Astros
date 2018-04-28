from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import date
import re 

#from django.contrib.auth.models import EmailField
from .models import Movie, User, Review, MovieGenre


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

    #movie_1 = Movie.objects.create("Princess Bride", 120, 'Dramedy', 'PG')
    pass

class ReviewModelTest(TestCase):
    pass

class MovieGenreModelTest(TestCase):
    pass


    
class MovieViewsTests(TestCase):
    pass
   
class UserViewTests(TestCase):
    pass

class ReviewViewTests(TestCase):
    pass



    

