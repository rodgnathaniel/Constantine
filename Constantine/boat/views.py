from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game

import json



def boat_view(request):
    wins = 0
    losses = 0
    average_time = 0
    game_count = 0
    if request.user.is_authenticated:
        games = request.user.game_set.all()
        for game in games:
            game_count += 1
            average_time += game.time
            if game.won:
                wins += 1
            else:
                losses +=1
        average_time /= game_count
    context = {'wins':wins, 'losses':losses, 'average_time':average_time}
    return render(request, "boat/boat.html", context)
    

def level_2_view(request):

    return render(request, "boat/boat_level_2.html", {})
    

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
