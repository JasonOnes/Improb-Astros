from django import forms
from django.core import validators
from .models import Movie, User, Review

''' 3 different ways to validate honeypots haven't caught a bot '''
def must_be_empty(value):
    ''' checks validator to see if honeypot filled in '''
    if value:
        raise forms.ValidationError("NOT EMPTY")


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('movie', 'rating', 'comments',)
        honeypot = forms.CharField(required=False, 
                                    widget=forms.HiddenInput, 
                                    label="Leave blank",
                                    validators=[must_be_empty] #see above no.1
                                    )

class SearchForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title',)
        # below
        honeypot = forms.CharField(required=False, 
                                    widget=forms.HiddenInput, 
                                    label="Leave blank")

    # example no.2 of clean fields for security and validation (not sure how honeypots catched bots)
    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("honeypot should be empty nice try robot!")
        return honeypot

class LoginForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm_pass = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'password',)

    def clean(self):
        cleaned_data = super().clean()
        # cleaned data => dict
        password = cleaned_data.get('password')
        verify = cleaned_data.get('confirm_pass')

        if password != verify:
            raise forms.ValidationError("passwords don't match")


class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)
        honeypot = forms.CharField(required=False, widget=forms.HiddenInput,
                                    label="Leave alone",
                                    validators=[validators.MaxLengthValidator(0)]
                                    ) #no. 3 honeypot check if filled in

#
# class ReviewForm(forms.Form):
#     #rating = forms.IntegerField(choices=list(range(10)), widget=forms.ChoiceField)
#     comment = forms.CharField(widget=forms.Textarea)