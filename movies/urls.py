from django.urls import path
from django.conf.urls import url 
from . import views 

urlpatterns = [

    url(r'(?P<pk>\d+)/$', views.movie_detail),
    #path('movies_seen', views.movies_seen),
]
