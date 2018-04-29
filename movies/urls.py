from django.urls import path, re_path
from django.conf.urls import url
from . import views 


app_name = 'movies'

urlpatterns = [
    #path('all_movies/', views.all_movies, name='all_movies'),
    path('login/', views.login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('movie_search/', views.movie_search, name='movie_search'),
    path('omdb_movie_data/', views.movie_search, name='omdb_data'),

    path('movies_list/', views.all_movies, name='all_movies'),

    re_path(r'movies_seen_by_user/(?P<user_pk>\d+)/$', views.movies_seen_by_user, name="movies_by_user"),
    re_path(r'(?P<pk>\d+)/$', views.movie_detail, name='movie_detes'),
    re_path(r'^new_movie_review/$', views.movie_review, name='movie_review'),


    #url(r'(?P<pk>\d+)/$', views.movie_detail),
    #url(r'movies_seen_by_user/(?P<user_pk>\d+)/$', views.movies_seen_by_user),
    
    #url(r'(?P<user_pk>\d+)/$', views.movies_seen_by_user)
    # path('movies_seen_by_user', views.movies_seen_by_user),
    #path('home', improbable_astro.views.hello_world),
]
