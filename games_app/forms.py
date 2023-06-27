from django import forms
from .models import Game

class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'short_description', 'premiere', 'developer', 'completed']
