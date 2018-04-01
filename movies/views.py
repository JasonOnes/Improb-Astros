from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie 

# Create your views here.
def movies_seen(request):
    movies = Movie.objects.all()
    output = ','.join([str(movie) for movie in movies])
    html_response = """
        <h1>Here's a list of those that you have seen</h1>
        <ul>for movie in movies
        <li>movie</li>
        </ul>
        
        """

    #return HttpResponse(html_response)
    return HttpResponse(output)
