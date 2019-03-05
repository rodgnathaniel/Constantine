from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game, Mode

import json



# def boat_view(request):

#     return render(request, "boat/boat.html", {})
    

# def level_2_view(request):

#     return render(request, "boat/boat_level_2.html", {})


def home_view(request):
    modes = Mode.objects.all()
    return render(request, "boat/home.html", {'modes': modes})


def iguana_game_view(request):
    if 'game_mode' in request.GET:
        game_mode_id = request.GET['game_mode']
        game_mode = Mode.objects.get(id=game_mode_id)
    else:
        game_mode = Mode.objects.all()[0]
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
        if average_time != 0:
            average_time /= game_count
    context = {'average_time':average_time, 'gold':gold, 'mode': game_mode}
    return render(request, "boat/iguana_game.html", context)


def instructions_view(request):

    return render(request, "boat/instructions.html", {})


def scores_view(request):
    all_scores = []
    high_score = 0
    top_3 = Game.objects.order_by('-score')[:3]
    # for game in games:
    #     all_scores.append(game.score)
    # all_scores.sort()
    # high_score = all_scores[]

    context = {'top_3':top_3}

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


