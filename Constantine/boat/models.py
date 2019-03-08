from django.db import models

from django.contrib.auth.models import User

class State(models.Model):
    player              = models.ForeignKey(User, on_delete=models.CASCADE)
    duskball_is         = models.BooleanField(default=False)
    haunted_painting_is = models.BooleanField(default=False)
    lucario_is          = models.BooleanField(default=False)
    computer_on         = models.BooleanField(default=False)
    stair_collision     = models.IntegerField()
    cabnet_collision    = models.IntegerField()
    rail2_collision     = models.IntegerField()  
    duskball_collision  = models.IntegerField()
    painting_collision  = models.IntegerField()
    haunted_collision   = models.IntegerField()
    lucario_collision   = models.IntegerField()


class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    time   = models.IntegerField() # the duration of the game in seconds
    level  = models.IntegerField()
    gold   = models.IntegerField()
    score  = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.player

class Mode(models.Model):
    name          = models.CharField(max_length=100)
    snowman_delay = models.IntegerField()
    avocado_delay = models.IntegerField()
    speed         = models.IntegerField()

    def __str__(self):
        return self.name

