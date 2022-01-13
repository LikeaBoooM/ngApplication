
from django import forms
from . models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Movie
        fields = ['title']
