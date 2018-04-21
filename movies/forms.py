from django import forms

from .models import Movie, User, Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('movie', 'rating', 'comment')


