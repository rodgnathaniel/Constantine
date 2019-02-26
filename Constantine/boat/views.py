from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game

import json



def boat_view(request):

    return render(request, "boat/boat.html", {})
    

def level_2_view(request):

    return render(request, "boat/boat_level_2.html", {})




def scores_view(request):
    games = request.user.game_set.all()
    context = {'games':games}
    return render(request, "boat/scores.html", context)


def instructions_view(request):

    return render(request, "boat/instructions.html", {})


def save_game(request):
    
    data = json.loads(request.body)
    game_time = data['game_time']
    won = data['won']
    player = request.user
    game = Game(time=game_time, won=won, player=player)
    game.save()
    return HttpResponse('ok')



# use .count with the django orm to count the number of wins and losses
# calculate average play time?
