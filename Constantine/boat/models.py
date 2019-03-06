from django.db import models

from django.contrib.auth.models import User

class Title(models.Model):
    name = models.CharField(max_length=200)

class Game(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField() # the duration of the game in seconds
    level = models.IntegerField()
    gold = models.IntegerField()
    score = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.player

class Mode(models.Model):
    name = models.CharField(max_length=100)
    snowman_delay = models.IntegerField()
    avocado_delay = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name

