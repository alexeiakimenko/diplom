from django.shortcuts import render
from .models import NewGame


def new_games(request):
    new_game = NewGame.objects.all()
    context = {
        'new_games': new_game
    }
    return render(request, 'new_games/new_games.html', context)


def single_new_game(request, pk):
    new_game = NewGame.objects.get(id=pk)
    context = {
        'new_game': new_game,
    }
    return render(request, 'new_games/single_new_game.html', context)


def new_games_genre(request, pk):
    genre = pk
    new_game = NewGame.objects.filter(genre=pk)
    context = {
        'new_games': new_game,
        'genre': genre
    }
    return render(request, 'new_games/new_games_genre.html', context)
