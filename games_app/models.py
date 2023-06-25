from django.db import models

class Genre(models.IntegerChoices):
    ANOTHER = 0, "Another"
    SHOOTER = 1, "Shooter"
    STRATEGY = 2, "Strategy"
    RPG = 3, "RPG"
    HORROR = 4, "Horror"
    RACING = 5, "Racing"
    ACTION = 6, "Action"
    ADVENTURE = 7, "Adventure"
    SPORTS = 8, "Sports"
class DevelopmentStudio(models.Model):
    name = models.CharField(max_length = 50, blank = False, unique = True)

    def __str__(self):
        return f"{self.name}"
class Game(models.Model):
    title = models.CharField(max_length = 50, blank = False)
    genre = models.PositiveSmallIntegerField(choices = Genre.choices, default = 0)
    premiere = models.PositiveSmallIntegerField(blank = True, null = True)
    developer = models.ForeignKey(DevelopmentStudio, on_delete = models.CASCADE, related_name = "games")
    completed = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.title}"
