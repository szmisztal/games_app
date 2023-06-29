from django.db import models

class Genre(models.TextChoices):
    ANOTHER = 'Another', "Another"
    SHOOTER = 'Shooter', "Shooter"
    STRATEGY = 'Strategy', "Strategy"
    RPG = 'RPG', "RPG"
    HORROR = 'Horror', "Horror"
    RACING = 'Racing', "Racing"
    ACTION = 'Action', "Action"
    ADVENTURE = 'Adventure', "Adventure"
    SPORTS = 'Sports', "Sports"

class DevelopmentStudio(models.Model):
    name = models.CharField(max_length = 50, blank = False, unique = True)

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    title = models.CharField(max_length = 50, blank = False)
    genre = models.CharField(max_length = 20, choices = Genre.choices, default = Genre.ANOTHER)
    short_description = models.TextField(max_length = 200, blank = True)
    premiere = models.PositiveSmallIntegerField(blank = True, null = True)
    developer = models.ForeignKey(DevelopmentStudio, on_delete = models.CASCADE, related_name = "games")
    completed = models.BooleanField(default = False)

    def lower_str(self):
        if self.genre != "RPG":
            return self.genre.lower()
        else:
            return self.genre

    def __str__(self):
        genre = self.lower_str()
        return f"{self.title} is {genre} genre game, published in {self.premiere} year by {self.developer}. Description: {self.short_description}"
