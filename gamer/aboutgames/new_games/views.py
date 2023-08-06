from django.shortcuts import render


def new_games(request):
    context = {
        'video': 'valhalla.mp4'
    }
    return render(request, 'new_games/new_games.html', context)
