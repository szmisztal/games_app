from django.urls import path
from .views import homepage, games_list, single_game

urlpatterns = [
    path("", homepage, name = "homepage"),
    path("games_list/", games_list, name = "games_list"),
    path("single_game/<int:game_id>/", single_game, name = "single_game")
]
