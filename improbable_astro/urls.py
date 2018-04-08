"""improbable_astro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #won't be needed when deployed via PaaS
from django.urls import include, path, re_path
# from django.conf.urls import url => url soon to be deprecated
from . import views 
import movies



urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.hello_world),
    path('all_movies', movies.views.all_movies),
    re_path(r'\S*/all_movies', movies.views.all_movies),
    re_path(r'\S*/home', views.hello_world),
    path('', views.hello_world),
    re_path(r'^$', views.hello_world),
    #url(r'', views.hello_world).
    #path('movies_seen_by_user', movies.views.movies_seen_by_user),
    
    re_path(r'movies_seen_by_user/(?P<user_pk>\d+)/$', movies.views.movies_seen_by_user),
    re_path(r'(?P<pk>\d+)/$', movies.views.movie_detail),
   
    
    #url(r'(?P<user_pk>\d+)/$', movies.views.movies_seen_by_user),
]
""" below for treehouse demo version 1.8 """
    #url(r'^$', views.hello_world),

urlpatterns += staticfiles_urlpatterns() # only used for local development to locate static


