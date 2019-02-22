from django.db import models
from django.contrib.auth.models import User

# class PlayerStat(models.Model):
#     games_lost = models.IntegerField(blank=True, null=True)
#     games_won = models.IntegerField(blank=True, null=True)
#     game_times = models.CharField(max_length=120)


class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    won = models.BooleanField()
    time = models.IntegerField() # the duration of the game in seconds
    timestamp = models.DateTimeField(auto_now_add=True)
