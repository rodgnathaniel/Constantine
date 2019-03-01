from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game

import json



# def boat_view(request):

#     return render(request, "boat/boat.html", {})
    

# def level_2_view(request):

#     return render(request, "boat/boat_level_2.html", {})


# def level_3_view(request):

#     return render(request, "boat/boat_level_3.html", {})


def boating_game_view(request):
        # wins = 0
    # losses = 0
    average_time = 0
    gold = 0
    game_count = 0
    high_score = 0 
    if request.user.is_authenticated:
        games = request.user.game_set.all()
        for game in games:
            game_count += 1
            average_time += game.time
            gold += game.gold
            # if game.won:
            #     wins += 1
            # else:
            #     losses += 1
        if average_time != 0:
            average_time /= game_count
    context = {'average_time':average_time, 'gold':gold}
    return render(request, "boat/boating_game.html", context)


def instructions_view(request):

    return render(request, "boat/instructions.html", {})


def scores_view(request):
    game_times = []
    games = Game.objects.all()
    for game in games:
        game_times.append(game.time)
    game_times = sorted(game_times)
    fastest_game = game_times[8000]

    context = {'fastest_game':fastest_game}

    return render(request, "boat/scores.html", context)
            

def save_game(request):
    
    data = json.loads(request.body)
    game_time = data['game_time']
    game_level = data['game_level']
    game_score = data['game_score']
    gold_collected = data['gold_collected']
    player = request.user
    game = Game(score=game_score, level=game_level, gold=gold_collected, time=game_time, player=player)
    game.save()
    return HttpResponse('ok')


