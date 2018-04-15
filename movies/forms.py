from django import forms

from .models import Movie, User

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'seen_on', 'rating', 'category', 'comments')