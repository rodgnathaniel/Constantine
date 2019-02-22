from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game

import json



def boat_view(request):

    return render(request, "boat/boat.html", {})


def save_game(request):
    
    data = json.loads(request.body)
    game_time = data['game_time']
    won = data['won']
    player = request.user
    game = Game(time=game_time, won=won, player=player)
    game.save()
    return HttpResponse('ok')



