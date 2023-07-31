from django.contrib import messages
from .forms import UserRegisterForm, FullForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.create(
                username=user.username,
                name=user.first_name,
                email=user.email,
                user_id=user.id
            )

            messages.success(request, "Вы зарегистрированы! ")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        user_form = UserRegisterForm()

        context = {'form': user_form}
        return render(request, 'users/register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из профиля')
    return redirect('index')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {'form': AuthenticationForm()})
        else:
            login(request, user)
            return redirect('index')


def profile(request,):
    prof = request.user.profile
    context = {
        'profile': prof
    }
    return render(request, 'users/profile.html', context)
