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
        'games': game,
    }
    return render(request, 'help_games/help_games.html', context)


def single_game(request, pk):
    game = Game.objects.get(id=pk)
    hints = Hint.objects.filter(hint_game=pk)
    videos = VideoView.objects.filter(video_game=pk)
    comment = GameComment.objects.filter(comment_game=pk)
    try:
        user_eval = VoteUser.objects.distinct().filter(game_evaluation_id=int(pk),
                                                       user_evaluation_id=request.user.profile.id).values(
            'evaluation')
        ev = user_eval[0]['evaluation']

    except:
        ev = 'Вашей оценки нет'
    context = {
        'game': game,
        'hints': hints,
        'videos': videos,
        'comment': comment,
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
    if request.method == 'POST':
        try:
            user_eval = VoteUser.objects.distinct().filter(game_evaluation_id=int(pk),
                                                           user_evaluation_id=request.user.profile.id).values(
                'evaluation')
            ev = user_eval[0]['evaluation']

        except:
            ev = 'Вашей оценки нет'
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
                       'comment': GameComment.objects.filter(comment_game=game_commented), 'ev': ev,
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
    sort_genre = title
    help_game = Game.objects.distinct().filter(Q(genre=title) | Q(genre2=title) | Q(genre3=title))
    game_list = page_list(request, help_game, page)
    game = game_list[0].page(game_list[1])
    context = {
        'help_games': game,
        'sort_genre': sort_genre
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
        game_evaluations = VoteUser.objects.filter(game_evaluation_id=pk).values('evaluation')
        evaluations = []
        for i in range(len(game_evaluations)):
            evaluations.append(game_evaluations[i]['evaluation'])
        length_evaluations = len(evaluations)
        sum_evaluations = sum(evaluations)

        rating = calculate_rating(sum_evaluations, length_evaluations)
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


def other_evaluations(request, pk):
    prof = None
    game_evaluations = VoteUser.objects.filter(game_evaluation_id=int(pk)).order_by('-evaluation')
    length = len(game_evaluations)
    context = {
        'evaluations': game_evaluations,
        'length': length

    }
    return render(request, 'help_games/other_evaluations.html', context)
