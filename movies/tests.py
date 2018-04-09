from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import reverse
from datetime import date
import re 

#from django.contrib.auth.models import EmailField
from .models import Movie, User


class UserModelTests(TestCase):

    user_1 = User.objects.create(name='Timmy', email='lkasjdflkasjdfljaslkdj')
    user_2 = User.objects.create(name='Tracey', email='tracey@flowers.com')

    def test_email_not_valid_form(self):
        user_1 = User.objects.create(name='Timmy', email='lkasjdflkasjdfljaslkdj')
        #user_2 = User.objects.create(name='Tracey', email='tracey@flowers.com')
        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', user_1.email)
        self.assertEqual(match, None, msg="Email not valid")
    
    def test_email_valid(self):
        #user_1 = User.objects.create(name='Timmy', email='lkasjdflkasjdfljaslkdj')
        user_2 = User.objects.create(name='Tracey', email='tracey@flowers.com')
        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', user_2.email)
        #self.assertEqual(match, user_2.email, msg="Email
        self.assertNotEqual(match, None, 'there\'s and email match "somewhere" in the string')
        self.assertIn

class MovieModelTests(TestCase):
    pass



class MovieViewsTests(TestCase):
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

class UserViewTests(TestCase):
    pass




    '''
    def test_email_not_valid_style(self):
        user = User.objects.create(
            name='Timmy',
            email='alskdjfalskdfjlaskdjf'
        )

        match=re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', str(user.email))
        #self.assertNotEqual(user.email, 'jasonr.jones14@gmail.com')
        #self.assertEqual(user.email, 'alskdjfalskdfjlaskdjf')
        #self.assertTrue(match(self.email))
        self.assertNotEqual(match, None, msg='Email doesn\'t match pattern')
        self.assertEqual(match, self.email, msg='Email does match')
        #self.assertFormError(user.email, EmailField)
    '''    

# class MovieModelTests(TestCase):

#     def test_moive_seen_on_date(self):
#         movie = Movie.objects.create(
#             title="Some Piece of Crap", 
#             rating=2,
#             category='Cl',
#             reviewer= 'Timmy'
#         )

#         today = date.today
#         self.assertEqual(movie.seen_on, today)

    
