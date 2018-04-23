from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date

import omdb

from .models import Movie, User, Review
from .forms import ReviewForm, SearchForm



def all_movies(request):
    ''' renders a page with ALL the movies by all users '''
    movies = Movie.objects.all().order_by('title')
    # return the average ranking as additional paramater 
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

    movie = get_object_or_404(Movie, pk=pk) # 404 page not found if some idiot types in bad query param

    return render(request, 'movies/movie_detail.html', {'movie':movie})
    
   
def movie_review(request):#, movie_pk, user_pk):
    ''' form to submit a movie review, pk should be User.pk '''
    if request.method == "POST":
        form = ReviewForm(request.POST)
        T#TODO get User instance (ie logged in session user, not superuser admin
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.added = date.today()
            movie = review.title

            try:
                review.save()
                return render(request, 'movies/movie_detail.html', {'movie':movie})
            except:
                print("Probably no User instance")
                pass
            return redirect('movie_detail', pk=movie_pk)
    else:
        form = ReviewForm()
    return render(request, 'movies/movie_review.html', {'form':  form})

def movie_search(request):
    '''form for looking up movie and hit omdb api'''
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            #movie.title = request.title
            print("##")
            print(movie.title)
            sucker = request.user
            print(sucker)
            #movie.save()
            #title = request.title
            movie = form.save(commit=False)
            #returned_values = omdb.request(t=form)# json should be default, r='json')
            returned_values = omdb.get(title=movie.title)

            #movie.rotten_tomatoes_score = returned_values.ratings[]
            # TODO add movie attributes from omdb to model
            # movie.imdb_score = returned_values.imdb_rating
            # movie.rating = returned_values.rated
            # movie.length = returned_values.runtime
            try:

                movie.save()
                print("Movie saved")
            except:
                print("Unable to Save")

            return render(request, 'movies/omdb_movie_data.html', {'details': returned_values})
    else:
        form = SearchForm()
    return render(request, 'movies/movie_search.html', {'form': form})

