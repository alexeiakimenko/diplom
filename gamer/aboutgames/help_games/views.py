from django.shortcuts import render
from .models import *
from users.models import *


def help_games(request):
    game = Game.objects.all()
    context = {
        'games': game
    }
    return render(request, 'help_games/help_games.html', context)


def profile_view(request, name):
    profile_view = Profile.objects.get(name=name)
    return render(request, 'users/profile_view.html', {'profile_view': profile_view})
