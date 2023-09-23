from django.shortcuts import render
from .models import *
from users.models import *
from transliterate import translit, detect_language
from django.db.models import Q


def help_games(request):
    if request.method == 'POST':
        search = request.POST['search']
        search1 = translit(search, 'ru')
        if detect_language(search) == 'ru':
            search2 = translit(search, reversed=True)
            game = Game.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search2))
        else:
            game = Game.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search))
        context = {
            'games': game
        }
        return render(request, 'help_games/help_games.html', context)
    else:
        game = Game.objects.all()
        context = {
            'games': game
        }
        return render(request, 'help_games/help_games.html', context)


def single_game(request, pk):
    game = Game.objects.get(id=pk)
    hints = Hint.objects.filter(hint_game=pk)
    videos = VideoView.objects.filter(video_game=pk)
    comment = GameComment.objects.filter(comment_game=pk)
    context = {
        'game': game,
        'hints': hints,
        'videos': videos,
        'comment': comment,
    }
    return render(request, 'help_games/single_game.html', context)


def profile_view(request, name):
    profile_view = Profile.objects.get(name=name)
    return render(request, 'users/profile_view.html', {'profile_view': profile_view})


def hint_game(request, title):
    hint = Hint.objects.get(hint_title=title)
    context = {
        'hint': hint,
    }
    return render(request, 'help_games/hint_game.html', context)


def video_view_game(request, title):
    video = VideoView.objects.get(video_title=title)
    context = {
        'video': video,
    }
    return render(request, 'help_games/video_view_game.html', context)


def comment_games(request, pk):
    if request.user.is_authenticated:
        name = request.user.profile.name
        avatar = request.user.profile.avatar
        favourite_game = request.user.profile.favorite_game
        favourite_genre = request.user.profile.favorite_genre
    else:
        name = 'Гость'
        avatar = ''
        favourite_game = 'Нет данных'
        favourite_genre = 'Нет данных'
    game_commented = Game.objects.get(id=pk)
    hints = Hint.objects.filter(hint_game=pk)
    videos = VideoView.objects.filter(video_game=pk)
    if request.method == 'POST':
        comment = request.POST['comment']
        GameComment.objects.create(
            name=name,
            avatar=avatar,
            comment=comment,
            comment_game=game_commented,
            favourite_game=favourite_game,
            favourite_genre=favourite_genre,

        )
        return render(request, 'help_games/single_game.html',
                      {'game': game_commented, 'hints': hints, 'videos': videos,
                       'comment': GameComment.objects.filter(comment_game=game_commented)})

    context = {'name': name,
               'avatar': avatar,
               'favourite_game': favourite_game,
               'favourite_genre': favourite_genre,
               }

    return render(request, 'help_games/comment_games.html', context)


def help_games_genre(request, title):
    genre = title
    help_game = Game.objects.filter(genre=title)
    context = {
        'help_games': help_game,
        'genre': genre
    }
    return render(request, 'help_games/help_games_genre.html', context)
