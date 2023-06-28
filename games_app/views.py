from django.shortcuts import render, get_object_or_404
from .models import Game, DevelopmentStudio
from .forms import NewGameForm, NewDevForm
from django.views import generic
from django.contrib import messages

class HomepageView(generic.TemplateView):
    template_name = "home.html"

class GamesListView(generic.ListView):
    template_name = "games_list.html"
    context_object_name = "games"

    def get_queryset(self):
        return Game.objects.order_by("developer", "title")

class DevStudioListView(generic.ListView):
    template_name = "devs_list.html"
    context_object_name = "dev_studios"

    def get_queryset(self):
        return DevelopmentStudio.objects.order_by("name")

class SingleGameView(generic.DetailView):
    model = Game
    context_object_name = "single_game"
    template_name = "single_game.html"

class SingleDevView(generic.DetailView):
    model = DevelopmentStudio
    template_name = "single_dev.html"
    context_object_name = "single_dev"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_dev = self.get_object()
        games = single_dev.games.all().order_by("title")
        context["games"] = games
        return context

class AddNewGame(generic.CreateView):
    model = Game
    form_class = NewGameForm
    template_name = "add_game.html"
    success_url = "/games_app/games_list/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Game was created successfully")
        return response

class AddDev(generic.CreateView):
    model = DevelopmentStudio
    form_class = NewDevForm
    template_name = "add_dev.html"
    success_url = "/games_app/games_list/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Development studio was created successfully")
        return response

# class EditGame(generic.UpdateView):
#     model





