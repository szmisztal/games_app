from django.shortcuts import render, get_object_or_404
from .models import Game

def homepage(request):
    return render(request, "home.html")

def games_list(request):
    games = Game.objects.all()
    return render(request, "games_list.html", {"games": games})

def single_game(request, game_id):
    game = get_object_or_404(Game, pk = game_id)
    return render(request, "single_game.html", {"game": game})

