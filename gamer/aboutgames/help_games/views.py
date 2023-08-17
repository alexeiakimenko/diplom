from django.shortcuts import render
from .models import *


def help_games(request):
    game = Game.objects.all()
    context = {
        'games': game
    }
    return render(request, 'help_games/help_games.html',context)
