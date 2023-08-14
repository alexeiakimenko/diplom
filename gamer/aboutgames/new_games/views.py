from django.shortcuts import render, redirect
from .models import *


def new_games(request):
    new_game = NewGame.objects.all()
    context = {
        'new_games': new_game
    }
    return render(request, 'new_games/new_games.html', context)


def single_new_game(request, pk):
    new_game = NewGame.objects.get(id=pk)
    comments = Comments.objects.filter(game_commented=pk)
    context = {
        'new_game': new_game,
        'comments': comments
    }
    return render(request, 'new_games/single_new_game.html', context)


def new_games_genre(request, pk):
    genre = pk
    new_game = NewGame.objects.filter(genre=pk)
    context = {
        'new_games': new_game,
        'genre': genre
    }
    return render(request, 'new_games/new_games_genre.html', )


def comment_new_games(request, pk):
    if request.user.is_authenticated:
        name = request.user.profile.name
    else:
        name = 'Гость'
    game_commented = NewGame.objects.get(id=pk)
    if request.method == 'POST':
        comment = request.POST['comment']
        Comments.objects.create(
            name=name,
            comment=comment,
            game_commented=game_commented

        )
        return render(request, 'new_games/single_new_game.html',
                      {'new_game': game_commented, 'comments': Comments.objects.filter(game_commented=game_commented)})

    context = {'name': name,}
    return render(request, 'new_games/comment_new_games.html', context)
