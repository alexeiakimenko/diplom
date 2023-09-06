from django.shortcuts import render, redirect
from .models import *
from users.models import *


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
    return render(request, 'new_games/new_games_genre.html', context)


def comment_new_games(request, pk):
    global avatar

    if request.user.is_authenticated:
        name = request.user.profile.name
        avatar = request.user.profile.avatar
        favourite_game = request.user.profile.favorite_game
        favourite_genre = request.user.profile.favorite_genre
    else:
        name = 'Гость'
        favourite_game = 'Нет данных'
        favourite_genre = 'Нет данных'
    game_commented = NewGame.objects.get(id=pk)
    if request.method == 'POST':
        game_id = pk
        print(game_id)
        comment = request.POST['comment']
        Comments.objects.create(
            name=name,
            avatar=avatar,
            comment=comment,
            game_commented=game_commented,
            favourite_game=favourite_game,
            favourite_genre=favourite_genre,

        )
        return render(request, 'new_games/single_new_game.html',
                      {'new_game': game_commented,
                       'comments': Comments.objects.filter(game_commented=game_commented)})
    game_id = pk
    context = {'name': name,
               'avatar': avatar,
               'favourite_game': favourite_game,
               'favourite_genre': favourite_genre,
               }
    return render(request, 'new_games/comment_new_games.html', context)


def profile_view(request, name):
    profile_view = Profile.objects.get(name=name)
    return render(request, 'users/profile_view.html', {'profile_view': profile_view})
