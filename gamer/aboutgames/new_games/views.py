from django.shortcuts import render, redirect
from .models import *
from users.models import *
from transliterate import translit, detect_language
from django.db.models import Q
from .utils import page_list, calculate_rating

search = ''
page = 1


def new_games(request):
    global page
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    new_game = NewGame.objects.all()
    new_game_list = page_list(request, new_game, page)
    new_game = new_game_list[0].page(new_game_list[1])
    context = {
        'new_games': new_game
    }
    return render(request, 'new_games/new_games.html', context)


def single_new_game(request, pk):
    new_game = NewGame.objects.get(id=pk)
    comments = Comments.objects.filter(game_commented=pk)
    try:
        user_eval = NewVoteUser.objects.distinct().filter(game_evaluation_id=int(pk),
                                                          user_evaluation_id=request.user.profile.id).values(
            'evaluation')
        ev = user_eval[0]['evaluation']

    except:
        ev = 'Вашей оценки нет'

    context = {
        'new_game': new_game,
        'comments': comments,
        'ev': ev,
    }
    return render(request, 'new_games/single_new_game.html', context)


def new_games_genre(request, pk):
    page = 1
    sort_genre = pk
    new_game = NewGame.objects.distinct().filter(Q(genre=pk) | Q(genre2=pk) | Q(genre3=pk))
    new_game_list = page_list(request, new_game, page)
    new_game = new_game_list[0].page(new_game_list[1])

    context = {
        'new_games': new_game,
        'sort_genre': sort_genre
    }
    return render(request, 'new_games/new_games_genre.html', context)


def comment_new_games(request, pk):
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
        try:
            user_eval = NewVoteUser.objects.distinct().filter(game_evaluation_id=int(pk),
                                                              user_evaluation_id=request.user.profile.id).values(
                'evaluation')
            ev = user_eval[0]['evaluation']

        except:
            ev = 'Вашей оценки нет'
        return render(request, 'new_games/single_new_game.html',
                      {'new_game': game_commented,
                       'comments': Comments.objects.filter(game_commented=game_commented), 'ev': ev,
                       'user_eval': request.user.profile})
    game_id = pk
    game = NewGame.objects.get(id=pk)
    context = {'name': name,
               'avatar': avatar,
               'favourite_game': favourite_game,
               'favourite_genre': favourite_genre,
               'new_game': game,
               }
    return render(request, 'new_games/comment_new_games.html', context)


def profile_view(request, name):
    profile_view = Profile.objects.get(name=name)
    return render(request, 'users/profile_view.html', {'profile_view': profile_view})


def search_new_game(request):
    global search
    page = 1
    if 'search' in request.GET:
        search = request.GET.get('search')

    search1 = translit(search, 'ru')
    if detect_language(search) == 'ru':
        search2 = translit(search, reversed=True)
        new_game = NewGame.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search2))
    else:
        new_game = NewGame.objects.distinct().filter(Q(title__icontains=search1) | Q(title__icontains=search))
    new_game_list = page_list(request, new_game, page)
    new_game = new_game_list[0].page(new_game_list[1])
    context = {
        'new_games': new_game
    }

    return render(request, 'new_games/search_new_game.html', context)


def new_game_evaluation(request, pk):
    new_game = NewGame.objects.get(id=pk)
    if request.method == 'POST':
        NewVoteUser.objects.create(
            evaluation=request.POST['eval'],
            user_evaluation=request.user.profile,
            game_evaluation_id=new_game.id
        )
        game_evaluations = NewVoteUser.objects.filter(game_evaluation_id=pk).values('evaluation')
        evaluations = []
        for i in range(len(game_evaluations)):
            evaluations.append(game_evaluations[i]['evaluation'])
        length_evaluations = len(evaluations)
        sum_evaluations = sum(evaluations)

        rating = calculate_rating(sum_evaluations, length_evaluations)
        new_game.rating_site = rating
        new_game.save()

        comments = Comments.objects.filter(game_commented=pk)
        context = {
            'new_game': new_game,
            'comments': comments,
            'ev': request.POST['eval'],
            'user_eval': request.user.profile
        }
        return render(request, 'new_games/single_new_game.html', context)
    context = {
        'new_game': new_game
    }
    return render(request, 'new_games/new_game_evaluation.html', context)


def new_other_evaluations(request, pk):
    game_evaluations = NewVoteUser.objects.filter(game_evaluation_id=pk).order_by('-evaluation')

    length = len(game_evaluations)
    context = {
        'evaluations': game_evaluations,
        'length': length

    }
    return render(request, 'new_games/new_other_evaluations.html', context)
