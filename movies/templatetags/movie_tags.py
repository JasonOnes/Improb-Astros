from django import template

from movies.models import Review, Movie

'''
Remember to load tags in appropriate templates as needed
{% load movie_tags %}
in this case
'''

register = template.Library()

@register.simple_tag
def newest_reviewed():
    ''' Gets the most recent reviews'''
    return Review.object.latest('reviewed_on')
# will be rendered with {% newest_reviewed %}

def highest_rated():
    ''' Gets the top ten movies by rating'''
    pass

def  newest_movies():
    ''' GEts the newest movies'''
    pass

def freshest():
    ''' Highest 10 rotten tomatoes rated'''
    pass

#TODO look into inclustion tags
@register.inclusion_tag('path_to/something.html')
def whatever():
    pass

'''Custom Filters'''

@register.filter('fresh')
def fresh():
    ''' filters movies based on rotten or fresh tomato rating'''
    fresh = Movie.rotten_tomatoes_score > 50
    pass
