from django.contrib import admin

from .models import Movie, User
'''
class StepInline(admin.StackedInline):
    model = User

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]
    '''

admin.site.register(Movie)
admin.site.register(User)