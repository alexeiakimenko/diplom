from django.shortcuts import render
from .models import NewGame


def new_games(request):
    new_game = NewGame.objects.all()
    context = {
        'new_games': new_game
    }
    return render(request, 'new_games/new_games.html', context)
