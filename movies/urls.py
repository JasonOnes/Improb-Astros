from django.urls import path, re_path
from django.conf.urls import url
from . import views 

urlpatterns = [
    path('all_movies/', views.all_movies, name='all_movies'),


    re_path(r'movies_seen_by_user/(?P<user_pk>\d+)/$', views.movies_seen_by_user, name="movies_by_user"),
    re_path(r'(?P<pk>\d+)/$', views.movie_detail, name='movie_detes'),
   
    #url(r'(?P<pk>\d+)/$', views.movie_detail),
    #url(r'movies_seen_by_user/(?P<user_pk>\d+)/$', views.movies_seen_by_user),
    
    #url(r'(?P<user_pk>\d+)/$', views.movies_seen_by_user)
    # path('movies_seen_by_user', views.movies_seen_by_user),
    #path('home', improbable_astro.views.hello_world),
]
