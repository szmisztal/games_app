from django.shortcuts import render, get_object_or_404
from .models import Game, DevelopmentStudio
from .forms import GameForm, DevForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

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
    form_class = GameForm
    template_name = "game_form.html"
    success_url = "/games_app/games_list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new"] = True
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Game was created successfully")
        return response

class AddNewDev(generic.CreateView):
    model = DevelopmentStudio
    form_class = DevForm
    template_name = "dev_form.html"
    success_url = "/games_app/dev_studios/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Development studio was created successfully")
        return response

class EditGame(generic.UpdateView):
    model = Game
    form_class = GameForm
    template_name = "game_form.html"

    def get_success_url(self):
        return reverse_lazy("single_game", kwargs = {"pk": self.object.pk})
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Game was edited successfully")
        return response

class EditDev(generic.UpdateView):
    model = DevelopmentStudio
    form_class = DevForm
    template_name = "dev_form.html"

    def get_success_url(self):
        return reverse_lazy("single_dev", kwargs = {"pk": self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Developer was edited successfully")
        return response





