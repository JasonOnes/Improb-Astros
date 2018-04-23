from django import forms

from .models import Movie, User, Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('movie', 'rating', 'comment',)


class SearchForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title',)

#
# class ReviewForm(forms.Form):
#     #rating = forms.IntegerField(choices=list(range(10)), widget=forms.ChoiceField)
#     comment = forms.CharField(widget=forms.Textarea)