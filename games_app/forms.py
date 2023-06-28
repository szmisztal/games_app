from django import forms
from .models import Game, DevelopmentStudio

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'short_description', 'premiere', 'developer', 'completed']

class DevForm(forms.ModelForm):
    class Meta:
        model = DevelopmentStudio
        fields = ['name']
