from django.contrib import admin

from .models import Movie, User, Review, MovieGenre

'''
class StepInline(admin.StackedInline):
    model = User

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]
    '''

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Review)
#admin.site.register(FollowPairs)
admin.site.register(MovieGenre)