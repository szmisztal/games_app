from django.urls import path
from .views import HomepageView, GamesListView, SingleGameView, AddNewGame

urlpatterns = [
    path("", HomepageView.as_view(), name = "homepage"),
    path("games_list/", GamesListView.as_view(), name = "games_list"),
    path("single_game/<int:pk>/", SingleGameView.as_view(), name = "single_game"),
    path("add_game/", AddNewGame.as_view(), name = "add_game")
]
