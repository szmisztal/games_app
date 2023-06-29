from django.urls import path
from .views import HomepageView, GamesListView, DevStudioListView, SingleGameView, SingleDevView, AddNewGame, AddNewDev, EditGame, EditDev, DeleteGame, DeleteDev

urlpatterns = [
    path("", HomepageView.as_view(), name = "homepage"),
    path("games_list/", GamesListView.as_view(), name = "games_list"),
    path("dev_studios/", DevStudioListView.as_view(), name = "devs_list"),
    path("single_game/<int:pk>/", SingleGameView.as_view(), name = "single_game"),
    path("single_dev/<int:pk>/", SingleDevView.as_view(), name = "single_dev"),
    path("add_game/", AddNewGame.as_view(), name = "add_game"),
    path("add_dev/", AddNewDev.as_view(), name = "add_dev"),
    path("edit_game/<int:pk>/", EditGame.as_view(), name = "edit_game"),
    path("edit_dev/<int:pk>/", EditDev.as_view(), name = "edit_dev"),
    path("delete_game/<int:pk>/", DeleteGame.as_view(), name = "delete_game"),
    path("delete_dev/<int:pk>/", DeleteDev.as_view(), name = "delete_dev")
]
