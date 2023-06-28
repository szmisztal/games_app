from django import forms
from .models import Game, DevelopmentStudio

class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'short_description', 'premiere', 'developer', 'completed']

class NewDevForm(forms.ModelForm):
    class Meta:
        model = DevelopmentStudio
        fields = ['name']
