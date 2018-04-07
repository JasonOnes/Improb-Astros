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

def movies_seen(request):
    movies = Movie.objects.all().order_by('-rating') # - before rating reverses order!
    #return HttpResponse(html_response)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    #movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk)
    print(movie.reviewer)
    #user = User.objects.get(pk=movie.reviewer)
    user = movie.reviewer
    return render(request, 'movies/movie_detail.html', {'movie':movie, 'user':user})
    
   
