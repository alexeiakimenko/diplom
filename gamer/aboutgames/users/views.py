from django.contrib import messages
from .forms import UserRegisterForm, FullForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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

            login(request, user)
            return render(request, 'users/full-form.html',
                          {'form': FullForm(instance=request.user.profile),
                           'message': 'Регистрация прошла успешно!Вы можете добавить данные,по желанию.'})
        else:
            return render(request, 'users/register.html',
                          {'form': UserRegisterForm(request.POST)})

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
            messages.error(request, 'Неверный логин или пароль!')
            return render(request, 'users/login.html', {'form': AuthenticationForm()})
        else:
            login(request, user)
            messages.info(request, 'Вы успешно вошли в свой профиль')
            return redirect('index')


@login_required(login_url='register')
def profile(request):
    prof = request.user.profile
    context = {
        'profile': prof
    }
    return render(request, 'users/profile.html', context)


def full_form(request):
    user = User.objects.get(username=request.user.profile.username)
    prof = request.user.profile
    form = FullForm(instance=prof)
    if request.method == 'POST':
        form = FullForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            user.username = request.user.profile.username
            user.first_name = request.user.profile.name
            user.email = request.user.profile.email
            user.save()
            form.save()
            messages.success(request, "Профиль успешно внесён! ")
            return redirect('profile')
        else:
            context = {'form': FullForm(request.POST, request.FILES, instance=prof), 'message': 'Изменение данных'}
            return render(request, 'users/full-form.html', context)

    context = {'form': form, 'message': 'Изменение данных', 'profile': prof}
    return render(request, 'users/full-form.html', context)

