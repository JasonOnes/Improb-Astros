from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import date
import re 

#from django.contrib.auth.models import EmailField
from .models import Movie, User, Review, MovieGenre


class UserModelTests(TestCase):
   
    def setup(self):
        self.user_1 = User.objects.create(username='Timmy', email='lkasjdflkasjdfljaslkdj')
        self.user_2 = User.objects.create(username='Tracey', email='tracey@flowers.com')

    def test_email_not_valid_form(self):
        user_1 = User.objects.create(username='Timmy', email='lkasjdflkasjdfljaslkdj')
        #user_2 = User.objects.create(name='Tracey', email='tracey@flowers.com')
        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', user_1.email)
        self.assertEqual(match, None, msg="Email not valid")
    
    def test_email_valid(self):
        #user_1 = User.objects.create(name='Timmy', email='lkasjdflkasjdfljaslkdj')
        user_2 = User.objects.create(username='Tracey', email='tracey@flowers.com')
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
    '''
    def setUp(self):

        self.user_X = User.objects.create(name='Steve', email='gg@allen.edu')
        self.user_Y = User.objects.create(name='Jill', email='humble@pie.com')
        self.user_Y_Not = User.objects.create(name='Jack', email='stupid@does.org')


        self.movie_X = Movie.objects.create(
            title="Police Academy IX",
            seen_on="1987-03-16",
            rating=4,
            category='C',
            comments='I laughed, I cried',
            reviewer=user_X
        )
        self.movie_Y = Movie.objects.create(
            title="Something Wicked This Way Comes",
            rating=7,
            category='H',
            reviewer='user_Y'
        )

    def test_movie_list_view(self):
        response = self.client.get(reverse('movies:movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.movie_X, response.context['movies'])
        self.assertIn(self.movie_Y, response.context['moives'])
        self.assertTemplateUsed(response, 'movies/movie_list.html')
        self.assertContains(response, self.movie.title)#test that the title is somewhere on page


    def test_movie_details_view(self):
        response = self.client.get(reverse('movies:movie_detail', kwargs={'pk':self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.movie, response.context['movie'])
        pass

    def test_movie_list_by_user_view(self):
        response = self.client.get(reverse('movies:movie_detail', kwargs={'user_pk':self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        pass
'''
class UserViewTests(TestCase):
    pass




    

