from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie, User

# Create your views here.

#below placed in improbable views
'''
def movies_seen(request):
    movies = Movie.objects.all()
    output = ','.join([str(movie) for movie in movies])
    html_response = """
        <h1>Here's a list of those that you have seen</h1>
        <ul>for movie in movies
        <li>movie</li>
        </ul>
        
        """

    return HttpResponse(html_response)
    #return HttpResponse(output)
'''
def all_movies(request):
    ''' renders a page with ALL the movies by all users '''
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies':movies})


def movies_seen_by_user(request, user_pk):
    ''' renders a page with a list of all the movies that user has seen'''
    #user = User.objects.get(pk=user_pk)
    #or
    user = get_object_or_404(User, pk=user_pk)
    # gets a query set of all the movies of that user
    movies = Movie.objects.filter(reviewer=user).order_by('-rating') # - before rating reverses order!
    return render(request, 'movies/movie_list.html', {'movies': movies}, {'reviewer':user.name})

def movie_detail(request, pk):
    ''' renders a page with all the movies attributes, friendly (readable) format '''
    #movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk) # 404 page not found if some idiot types in bad query param
    #user = User.objects.get(pk=movie.reviewer)
    user = movie.reviewer
    return render(request, 'movies/movie_detail.html', {'movie':movie, 'user':user})
    
   
