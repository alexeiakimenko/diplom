from django.contrib import messages
from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def index(request):
    return render(request, 'users/index.html')



def register(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Вы зарегистрированы! ")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    context = {'form': form}
    return render(request, 'users/register.html', context)
