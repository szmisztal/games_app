from django.shortcuts import render, get_object_or_404
from .models import Game
from .forms import NewGameForm
from django.views import generic

class HomepageView(generic.TemplateView):
    template_name = "home.html"

class GamesListView(generic.ListView):
    template_name = "games_list.html"
    context_object_name = "games"

    def get_queryset(self):
        return Game.objects.order_by("developer", "title")

class SingleGameView(generic.DetailView):
    model = Game
    context_object_name = "game"
    template_name = "single_game.html"

class AddNewGame(generic.CreateView):
    model = Game
    form_class = NewGameForm
    template_name = "add_game.html"
    success_url = "/games_app/games_list/"






