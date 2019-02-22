from django.db import models

from django.contrib.auth.models import User

class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    won = models.BooleanField()
    time = models.IntegerField() # the duration of the game in seconds
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.player