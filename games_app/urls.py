from django.urls import path
from .views import HomepageView, GamesListView, DevStudioListView, SingleGameView, SingleDevView, AddNewGame, AddDev

urlpatterns = [
    path("", HomepageView.as_view(), name = "homepage"),
    path("games_list/", GamesListView.as_view(), name = "games_list"),
    path("dev_studios/", DevStudioListView.as_view(), name = "devs_list"),
    path("single_game/<int:pk>/", SingleGameView.as_view(), name = "single_game"),
    path("single_dev/<int:pk>/", SingleDevView.as_view(), name = "single_dev"),
    path("add_game/", AddNewGame.as_view(), name = "add_game"),
    path("add_dev/", AddDev.as_view(), name = "add_dev")
]
