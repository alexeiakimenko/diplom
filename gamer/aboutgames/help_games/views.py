from django.shortcuts import render
from .models import *
from users.models import *
from new_games.utils import page_list, calculate_rating
from transliterate import translit, detect_language
from django.db.models import Q

search = ''
page = 1


def help_games(request):
    global page
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    game = Game.objects.all()
    game_list = page_list(request, game, page)
    game = game_list[0].page(game_list[1])
    context = {
        'games': game
    }
    return render(request, 'help_games/help_games.html', context)


def single_game(request, pk):
    game = Game.objects.get(id=pk)
    hints = Hint.objects.filter(hint_game=pk)
    videos = VideoView.objects.filter(video_game=pk)
    comment = GameComment.objects.filter(comment_game=pk)
    try:
        user_eval = VoteUser.objects.filter(user_evaluation=request.user.profile.id)
        flag = 1
        for e in user_eval:
            if int(e.game_evaluation_id) == int(pk):
                ev = e.evaluation
                flag = 0

        if flag == 0:
            user_eval = request.user.profile
        else:
            user_eval = None
            ev = None
    except:
        user_eval = None
        ev = None

    context = {
        'game': game,
        'hints': hints,
        'videos': videos,
        'comment': comment,
        'user_eval': user_eval,
        'ev': ev
    }
    return render(request, 'help_games/single_game.html', context)


def profile_view(request, name):
    profile_view = Profile.objects.get(name=name)
    return render(request, 'users/profile_view.html', {'profile_view': profile_view})


def hint_game(request, title):
    hint = Hint.objects.get(hint_title=title)
    game = Game.objects.get(id=hint.hint_game_id)
    context = {
        'hint': hint,
        'game': game,
    }
    return render(request, 'help_games/hint_game.html', context)


def video_view_game(request, title):
    video = VideoView.objects.get(video_title=title)
    game = Game.objects.get(id=video.video_game_id)
    context = {
        'video': video,
        'game': game,
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
    ev2 = None
    if request.method == 'POST':
        ev = VoteUser.objects.filter(user_evaluation_id=request.user.profile.id)
        for e in ev:
            if e.game_evaluation_id == int(pk):
                ev2 = e.evaluation

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
                       'comment': GameComment.objects.filter(comment_game=game_commented), 'ev': ev2,
                       'user_eval': request.user.profile})
    game = Game.objects.get(id=pk)
    context = {'name': name,
               'avatar': avatar,
               'favourite_game': favourite_game,
               'favourite_genre': favourite_genre,
               'game': game,
               }

    return render(request, 'help_games/comment_games.html', context)


def help_games_genre(request, title):
    page = 1
    genre = title
    help_game = Game.objects.filter(genre=title)
    game_list = page_list(request, help_game, page)
    game = game_list[0].page(game_list[1])
    context = {
        'help_games': game,
        'genre': genre
    }
    return render(request, 'help_games/help_games_genre.html', context)


def search_game(request):
    global search
    page = 1
    if 'search' in request.GET:
        search = request.GET.get('search')

    search1 = translit(search, 'ru')
    if detect_language(search) == 'ru':
        search2 = translit(search, reversed=True)
        game = Game.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search2))
    else:
        game = Game.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search))
    game_list = page_list(request, game, page)
    game = game_list[0].page(game_list[1])
    context = {
        'games': game
    }

    return render(request, 'help_games/search_game.html', context)


def game_evaluation(request, pk):
    game = Game.objects.get(id=pk)
    game_commented = GameComment.objects.filter(comment_game=pk)
    hints = Hint.objects.filter(hint_game=pk)
    videos = VideoView.objects.filter(video_game=pk)
    if request.method == 'POST':
        VoteUser.objects.create(
            evaluation=request.POST['eval'],
            user_evaluation=request.user.profile,
            game_evaluation_id=game.id
        )
        game_evaluation = VoteUser.objects.filter(game_evaluation_id=pk)
        s = 0
        l = 0
        for e in game_evaluation:
            s += e.evaluation
            l += 1
        rating = calculate_rating(s, l)
        game.rating_site = rating
        game.save()
        context = {
            'game': game,
            'comment': game_commented,
            'hints': hints,
            'videos': videos,
            'ev': request.POST['eval'],
            'user_eval': request.user.profile
        }
        return render(request, 'help_games/single_game.html', context)
    return render(request, 'help_games/game_evaluation.html', {'game': game})
